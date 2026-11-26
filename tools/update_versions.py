#!/usr/bin/env python3
"""Actualiza los números de versión de la página de programación.

Lee la última versión publicada de cada programa (las versiones de GitHub
y de Codeberg, y el Visual Studio Marketplace para la extensión Schematron
Validator) y la escribe en los tres idiomas del sitio:

- la línea de cada entrada (`<p class="project-role">2026 · vX.Y · …`) en
  coding.md, es/programacion.md y la/programmata.md;
- el recuadro de datos de las páginas de detalle (coding/*.md y sus pares
  en es/ y la/), con la fecha de la versión;
- las menciones «(version X)», «(versión X)», «(editio X)» que siguen a un
  enlace a un repositorio en esas páginas.

No escribe prosa: si a la historia de una página de detalle le falta la
versión nueva, o si la descripción de una entrada puede haber quedado
atrás, lo avisa para que se corrija a mano. Tampoco hace commit ni push.
"""

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path

if sys.version_info < (3, 14):
    sys.exit("update_versions.py needs Python 3.14 or later.")

HELP = """\
Update the version numbers of the Coding page and its detail pages, in
English, Spanish and Latin, from the latest releases on GitHub and
Codeberg (and the Visual Studio Marketplace for Schematron Validator).
Nothing is committed: check the result with `git diff`.

--add-repo and --remove-repo change which repositories are checked (kept
in tools/update_versions.json) and do nothing else."""

ROOT = Path(__file__).resolve().parent.parent
# Repos added to or removed from the check by hand (--add-repo, --remove-repo).
REPO_LIST = ROOT / "tools" / "update_versions.json"
LIST_PAGES = ["coding.md", "es/programacion.md", "la/programmata.md"]
DETAIL_DIRS = {"en": "coding", "es": "es/programacion", "la": "la/programmata"}

MARKETPLACE_ITEM = "NicolasVaughan.validate-schematron"
MARKETPLACE_QUERY = "https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery"
VSPACKAGE = ("https://marketplace.visualstudio.com/_apis/public/gallery/publishers/"
             "NicolasVaughan/vsextensions/validate-schematron/{}/vspackage")
USER_AGENT = "site-version-updater"

# El enlace a un repositorio, tal como se escribe en las páginas (con las
# variables de Liquid del sitio).
REPO_LINK = (r"https://(?:github\.com/\{\{ site\.github_username \}\}"
             r"|codeberg\.org/\{\{ site\.codeberg_username \}\})/([A-Za-z0-9._-]+?)")
ROLE_LINE = re.compile(r'(<p class="project-role">[^<]*?· v)([0-9][0-9.]*)( ·.*?</p>)')
FACTS = re.compile(r"(<dt>(?:Version|Versión|Editio)</dt><dd>)(.*?)(</dd>)")
FACT_PART = re.compile(r"^(?P<label>.*?)(?P<ver>\d+(?:\.\d+)+)(?P<rest>\s*\((?P<date>[^)]*)\))$")
PROSE = re.compile(r"(\[(?P<name>[^\]]+)\]\(" + REPO_LINK + r"\)\s*\((?:version|versión|editio) )"
                   r"(?P<ver>\d+(?:\.\d+)+)(\))")
LINK_TEXT = re.compile(r"\[([^\]]+)\]\(" + REPO_LINK + r"[/)]")
WHEN = re.compile(r'<span class="when">(.*?)(?:<br>.*?)?</span>')

MONTHS_EN = ["January", "February", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December"]
MONTHS_ES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
             "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
MONTHS_LA = ["Ianuarii", "Februarii", "Martii", "Aprilis", "Maii", "Iunii", "Iulii",
             "Augusti", "Septembris", "Octobris", "Novembris", "Decembris"]


def vtuple(v: str) -> tuple[int, ...]:
    return tuple(int(n) for n in v.split("."))


def clean_tag(tag: str) -> str | None:
    """'v1.4.0' -> '1.4.0'; None si la etiqueta no lleva número."""
    m = re.search(r"\d+(?:\.\d+)+|\d+$", tag)
    return m.group(0) if m else None


def roman(n: int) -> str:
    out = ""
    for value, sym in [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
                       (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
                       (5, "V"), (4, "IV"), (1, "I")]:
        while n >= value:
            out += sym
            n -= value
    return out


def format_date(d: date, lang: str) -> str:
    """The date as the facts boxes write it in each language."""
    match lang:
        case "es":
            return f"{d.day} de {MONTHS_ES[d.month - 1]} de {d.year}"
        case "la":
            return f"die {roman(d.day)} mensis {MONTHS_LA[d.month - 1]} anni {roman(d.year)}"
        case _:
            return f"{d.day} {MONTHS_EN[d.month - 1]} {d.year}"


# --- Consultas a los servidores -------------------------------------------

@dataclass
class Latest:
    repo: str
    version: str | None = None
    released: date | None = None
    source: str = ""
    notes: list[str] = field(default_factory=list)


def http_json(url: str, data: bytes | None = None, headers: dict | None = None):
    req = urllib.request.Request(url, data=data, headers={"User-Agent": USER_AGENT, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def gh_json(path: str):
    # gh usa la sesión del usuario, así que también ve los repositorios privados.
    p = subprocess.run(["gh", "api", path], capture_output=True, text=True)
    if p.returncode != 0:
        if "404" in p.stderr or "Not Found" in p.stderr:
            return None
        raise RuntimeError(f"gh api {path}: {p.stderr.strip()}")
    return json.loads(p.stdout)


def to_date(stamp: str | None) -> date | None:
    # Las fechas vienen en UTC (GitHub) o con su huso (Codeberg): se pasan a la hora local.
    if not stamp:
        return None
    return datetime.fromisoformat(stamp.replace("Z", "+00:00")).astimezone().date()


def fetch_latest(repo: str, owner_gh: str, owner_cb: str) -> Latest:
    """La versión publicada más reciente en cualquiera de los dos servidores.

    Manda la última *release*: una etiqueta puede ser más vieja que la
    última versión publicada. Solo si no hay ninguna release se toma la
    etiqueta más alta.
    """
    res = Latest(repo)
    releases: list[tuple[tuple[int, ...], str, date | None, str]] = []
    tags: list[tuple[tuple[int, ...], str, str]] = []

    gh_rel = gh_json(f"repos/{owner_gh}/{repo}/releases?per_page=10") or []
    for r in gh_rel:
        if not r["draft"] and not r["prerelease"] and (v := clean_tag(r["tag_name"])):
            releases.append((vtuple(v), v, to_date(r["published_at"]), "GitHub"))
            break
    cb_base = f"https://codeberg.org/api/v1/repos/{owner_cb}/{repo}"
    cb_rel = http_json(f"{cb_base}/releases?limit=10") or []
    for r in cb_rel:
        if not r["draft"] and not r["prerelease"] and (v := clean_tag(r["tag_name"])):
            releases.append((vtuple(v), v, to_date(r["published_at"]), "Codeberg"))
            break

    for t in gh_json(f"repos/{owner_gh}/{repo}/tags?per_page=100") or []:
        if v := clean_tag(t["name"]):
            tags.append((vtuple(v), v, "GitHub tag"))
    for t in http_json(f"{cb_base}/tags?limit=50") or []:
        if v := clean_tag(t["name"]):
            tags.append((vtuple(v), v, "Codeberg tag"))

    if releases:
        best = max(releases, key=lambda r: r[0])
        res.version, res.released = best[1], best[2]
        hosts = [r[3] for r in releases if r[0] == best[0]]
        res.source = " and ".join(hosts)
        # Si la misma versión está en los dos, vale la fecha más temprana.
        dates = [r[2] for r in releases if r[0] == best[0] and r[2]]
        res.released = min(dates) if dates else None
        if len({r[0] for r in releases}) > 1:
            lag = [f"{r[3]} has {r[1]}" for r in releases if r[0] != best[0]]
            res.notes.append("hosts differ: " + ", ".join(lag))
        if tags and max(tags)[0] > best[0]:
            res.notes.append(f"a newer tag exists without a release: {max(tags)[1]}")
    elif tags:
        best = max(tags)
        res.version, res.source = best[1], best[2] + " (no release)"
        res.notes.append("no release on either host; version taken from the tag, date unknown")
    else:
        res.notes.append("no release or tag found")
    return res


def fetch_marketplace(repo_latest: Latest) -> Latest:
    """La versión del Marketplace, o la del repositorio si ya se puede descargar."""
    body = json.dumps({"filters": [{"criteria": [{"filterType": 7, "value": MARKETPLACE_ITEM}]}],
                       "flags": 914}).encode()
    data = http_json(MARKETPLACE_QUERY, body, {"Content-Type": "application/json",
                                                "Accept": "application/json;api-version=3.0-preview.1"})
    ver = data["results"][0]["extensions"][0]["versions"][0]
    res = Latest(repo_latest.repo, clean_tag(ver["version"]), to_date(ver.get("lastUpdated")),
                 "Marketplace")
    rv = repo_latest.version
    if rv and vtuple(rv) > vtuple(res.version):
        # Una subida reciente puede descargarse antes de que el listado se actualice.
        try:
            req = urllib.request.Request(VSPACKAGE.format(rv), method="HEAD",
                                         headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=30):
                pass
            res.notes.append(f"listing says {res.version}, but {rv} is downloadable: taking {rv}")
            res.version, res.released, res.source = rv, repo_latest.released, "Marketplace (vspackage)"
        except urllib.error.HTTPError:
            res.notes.append(f"repo is at {rv}, Marketplace still serves {res.version} (kept)")
    return res


# --- La lista de repositorios añadidos y quitados ---------------------------

def load_repo_list() -> dict[str, list[str]]:
    try:
        data = json.loads(REPO_LIST.read_text(encoding="utf-8"))
    except FileNotFoundError:
        data = {}
    return {"added": data.get("added", []), "removed": data.get("removed", [])}


def save_repo_list(lst: dict[str, list[str]]) -> None:
    lst = {k: sorted(set(v)) for k, v in lst.items()}
    REPO_LIST.write_text(json.dumps(lst, indent=2) + "\n", encoding="utf-8")


def repo_hosts(repo: str, owner_gh: str, owner_cb: str) -> list[str]:
    """Where the repository exists: GitHub, Codeberg, both or neither."""
    hosts = []
    if gh_json(f"repos/{owner_gh}/{repo}"):
        hosts.append("GitHub")
    if http_json(f"https://codeberg.org/api/v1/repos/{owner_cb}/{repo}"):
        hosts.append("Codeberg")
    return hosts


def edit_repo_list(add: list[str], remove: list[str], on_pages: set[str],
                   owner_gh: str, owner_cb: str) -> int:
    lst = load_repo_list()
    status = 0
    for repo in add:
        hosts = repo_hosts(repo, owner_gh, owner_cb)
        if not hosts:
            print(f"{repo}: not found on GitHub ({owner_gh}) or Codeberg ({owner_cb}); not added",
                  file=sys.stderr)
            status = 1
            continue
        # Si estaba quitado, basta con volver a ponerlo.
        if repo in lst["removed"]:
            lst["removed"].remove(repo)
            print(f"{repo}: checked again")
            continue
        elif repo in on_pages or repo in lst["added"]:
            print(f"{repo}: already checked")
            continue
        else:
            lst["added"].append(repo)
        missing = {"GitHub", "Codeberg"} - set(hosts)
        print(f"{repo}: added (on {' and '.join(hosts)})"
              + (f"; not on {missing.pop()}" if missing else ""))
    for repo in remove:
        if repo in lst["added"]:
            lst["added"].remove(repo)
        elif repo in on_pages and repo not in lst["removed"]:
            lst["removed"].append(repo)
        else:
            print(f"{repo}: not checked now; nothing to remove", file=sys.stderr)
            status = 1
            continue
        print(f"{repo}: removed from the check")
    save_repo_list(lst)
    return status


# --- Lectura y escritura de las páginas --------------------------------------

def site_config() -> tuple[str, str]:
    text = (ROOT / "_config.yml").read_text(encoding="utf-8")
    gh = re.search(r"^github_username:\s*(\S+)", text, re.M).group(1)
    cb = re.search(r"^codeberg_username:\s*(\S+)", text, re.M).group(1)
    return gh, cb


def role_repo(line: str) -> str | None:
    # Se prefiere el enlace a GitHub; si no lo hay, el de Codeberg.
    repos = re.findall(r"github\.com/\{\{ site\.github_username \}\}/([A-Za-z0-9._-]+)", line)
    repos = repos or re.findall(r"codeberg\.org/\{\{ site\.codeberg_username \}\}/([A-Za-z0-9._-]+)", line)
    return repos[0] if repos else None


def entry_names(text: str) -> dict[str, str]:
    """Repo -> nombre mostrado, tomado del título de cada entrada (antes de los dos puntos)."""
    names = {}
    for block in re.findall(r'<li class="project.*?</li>', text, re.S):
        title = re.search(r"<h2><a [^>]*>(.*?)</a></h2>", block, re.S)
        role = re.search(r'<p class="project-role">.*?</p>', block, re.S)
        if title and role and (repo := role_repo(role.group(0))):
            names[repo] = re.sub(r"<[^>]+>", "", title.group(1)).split(":")[0].strip()
    return names


def front_matter(text: str, key: str) -> str | None:
    m = re.search(rf"^{key}:\s*(.+)$", text.split("---", 2)[1] if text.startswith("---") else "", re.M)
    return m.group(1).strip() if m else None


def detail_pages() -> dict[str, dict[str, Path]]:
    """ref -> {idioma: archivo}, para cada página de detalle."""
    pages: dict[str, dict[str, Path]] = {}
    for lang, d in DETAIL_DIRS.items():
        for p in sorted((ROOT / d).glob("*.md")):
            if ref := front_matter(p.read_text(encoding="utf-8"), "ref"):
                pages.setdefault(ref, {})[lang] = p
    return pages


def covered_by_history(text: str, version: str) -> bool:
    """¿Nombra la historia de la página esta versión, sola o dentro de un intervalo?"""
    v = vtuple(version)
    for when in WHEN.findall(text):
        for part in re.split(r",\s*", when):
            nums = re.findall(r"\d+(?:\.\d+)+", part)
            if len(nums) == 1 and vtuple(nums[0]) == v:
                return True
            if len(nums) == 2 and "–" in part and vtuple(nums[0]) <= v <= vtuple(nums[1]):
                return True
    return False


@dataclass
class Change:
    name: str
    old: str
    new: str


def main() -> int:
    ap = argparse.ArgumentParser(description=HELP, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-n", "--dry-run", action="store_true",
                    help="only report what would change; write nothing")
    ap.add_argument("--add-repo", action="append", default=[], metavar="REPO",
                    help="also check REPO (on GitHub and Codeberg); can be repeated")
    ap.add_argument("--remove-repo", action="append", default=[], metavar="REPO",
                    help="stop checking REPO; can be repeated")
    ap.add_argument("repos", nargs="*", metavar="REPO",
                    help="check only these repositories (default: every one on the pages)")
    args = ap.parse_args()

    owner_gh, owner_cb = site_config()
    files = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in LIST_PAGES}
    details = detail_pages()
    for langs in details.values():
        for p in langs.values():
            files[str(p.relative_to(ROOT))] = p.read_text(encoding="utf-8")
    original = dict(files)

    # Todos los repositorios que nombran las páginas, con su nombre visible.
    names = entry_names(files["coding.md"])
    marketplace_repo = None
    for line in ROLE_LINE.finditer(files["coding.md"]):
        if "marketplace.visualstudio.com" in line.group(0):
            marketplace_repo = role_repo(line.group(0))
    for ref, langs in details.items():
        text = files[str(langs["en"].relative_to(ROOT))] if "en" in langs else ""
        names.setdefault(ref, ref)
        for m in PROSE.finditer(text):
            names.setdefault(m.group(3), m.group("name"))
        for txt, repo in LINK_TEXT.findall(text):
            if FACTS.search(text) and txt in FACTS.search(text).group(2):
                names.setdefault(repo, txt)
    on_pages = set(names)
    if args.add_repo or args.remove_repo:
        return edit_repo_list(args.add_repo, args.remove_repo, on_pages, owner_gh, owner_cb)

    # Lo añadido se comprueba aunque no esté en las páginas; lo quitado, nunca.
    lst = load_repo_list()
    repos = sorted((on_pages | set(lst["added"])) - set(lst["removed"]))
    if lst["removed"]:
        print("Not checked (removed): " + ", ".join(sorted(lst["removed"])), file=sys.stderr)
    if args.repos:
        unknown = set(args.repos) - set(repos)
        if unknown:
            print("Not checked: " + ", ".join(sorted(unknown)), file=sys.stderr)
            return 2
        repos = [r for r in repos if r in args.repos]

    print(f"Checking {len(repos)} repositor{'y' if len(repos) == 1 else 'ies'}…", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=8) as pool:
        latest = dict(zip(repos, pool.map(lambda r: fetch_latest(r, owner_gh, owner_cb), repos)))
    if marketplace_repo in latest:
        latest[marketplace_repo] = fetch_marketplace(latest[marketplace_repo])

    changes: dict[str, Change] = {}
    warnings: list[str] = []

    def bump(repo: str, old: str) -> str:
        lt = latest.get(repo)
        if not lt or not lt.version or vtuple(lt.version) <= vtuple(old):
            if lt and lt.version and vtuple(lt.version) < vtuple(old):
                warnings.append(f"{repo}: page says {old}, newest release is {lt.version} (kept)")
            return old
        changes.setdefault(repo, Change(names.get(repo, repo), old, lt.version))
        return lt.version

    # 1. La línea de cada entrada de la lista.
    for rel in LIST_PAGES:
        files[rel] = ROLE_LINE.sub(
            lambda m: m.group(1) + (bump(r, m.group(2)) if (r := role_repo(m.group(0))) else m.group(2))
                      + m.group(3), files[rel])

    # 2. El recuadro de datos y las menciones en prosa de las páginas de detalle.
    for ref, langs in details.items():
        en_text = files[str(langs["en"].relative_to(ROOT))] if "en" in langs else ""
        # Las partes del recuadro, en el orden de la página en inglés: la
        # primera es el programa de la página; las demás se reconocen por el
        # texto de los enlaces (p. ej. «Slowdown for Android»).
        links = {txt: repo for txt, repo in LINK_TEXT.findall(en_text)}
        facts = FACTS.search(en_text)
        part_repos = []
        if facts:
            for i, part in enumerate(facts.group(2).split("; ")):
                label = FACT_PART.match(part).group("label").strip() if FACT_PART.match(part) else ""
                part_repos.append(ref if i == 0 else links.get(label))

        for lang, path in langs.items():
            rel = str(path.relative_to(ROOT))
            text = files[rel]

            def new_facts(m: re.Match) -> str:
                parts = m.group(2).split("; ")
                for i, part in enumerate(parts):
                    pm = FACT_PART.match(part)
                    repo = part_repos[i] if i < len(part_repos) else None
                    if not pm or not repo:
                        continue
                    new = bump(repo, pm.group("ver"))
                    if new != pm.group("ver"):
                        d = latest[repo].released
                        when = format_date(d, lang) if d else pm.group("date")
                        if not d:
                            warnings.append(f"{rel}: no release date for {repo} {new}; old date kept")
                        parts[i] = f"{pm.group('label')}{new} ({when})"
                return m.group(1) + "; ".join(parts) + m.group(3)

            text = FACTS.sub(new_facts, text)
            text = PROSE.sub(lambda m: m.group(1) + bump(m.group(3), m.group("ver")) + m.group(5), text)
            files[rel] = text

            # La historia es prosa: solo se avisa.
            main = latest.get(ref)
            if main and main.version and ref in changes and not covered_by_history(text, main.version):
                warnings.append(f"{rel}: the history has no line for {main.version}; add it by hand")

    # --- Informe ---
    width = max((len(names.get(r, r)) for r in repos), default=10)
    for r in repos:
        lt = latest[r]
        if r in changes:
            shown = f"{changes[r].old} → {changes[r].new}"
        elif r in on_pages:
            shown = f"{lt.version or '?'}  ok"
        else:
            # Repos added by hand: nothing on the pages to update.
            shown = f"{lt.version or '?'}  (not on the pages)"
        print(f"{names.get(r, r):<{width}}  {shown:<21} {lt.source}")
        for note in lt.notes:
            print(f"{'':<{width}}    note: {note}")
    for w in warnings:
        print("warning: " + w)
    # Las descripciones de las entradas tampoco se tocan: se recuerda revisarlas.
    listed = {role_repo(m.group(0)) for m in ROLE_LINE.finditer(original["coding.md"])}
    for r, c in changes.items():
        if r in listed:
            print(f"check:   {c.name}: does its description on the Coding page still fit {c.new}?")

    changed = [rel for rel in files if files[rel] != original[rel]]
    if not changed:
        print("\nEverything is up to date.")
        return 0
    if args.dry_run:
        print("\nWould change: " + ", ".join(changed))
    else:
        for rel in changed:
            (ROOT / rel).write_text(files[rel], encoding="utf-8")
        print("\nChanged: " + ", ".join(changed))
    summary = ", ".join(f"{c.name} {c.new}" for c in changes.values())
    print(f"\nSuggested commit message:\n  Coding page: update versions ({summary})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
