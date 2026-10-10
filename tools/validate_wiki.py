"""Validate the Trend Estimation mathematical Obsidian wiki.

This script intentionally uses only Python's standard library. Wiki cards use
a constrained YAML frontmatter subset: one JSON-compatible scalar/array per
line, also valid YAML. The script validates graph *integrity*, not proofs.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"

FRONT_LINE = re.compile(r"^([a-z][a-z0-9_]*):\s*(.+)$")
FENCE = re.compile(r"^ {0,3}([\x60]{3,}|~{3,})")
WIKILINK = re.compile(r"!?\[\[([^\]]+)\]\]")
SINGLE_DOLLAR = re.compile(r"^\s*\$\s*$")
DOUBLE_DOLLAR = re.compile(r"^\s*\$\$\s*$")
LEGACY_MATH = re.compile(r"\\(?:\(|\)|\[|\])")
CARD_FOLDERS = {
    "definiciones": ("DEF-", "definicion"),
    "resultados": ("RES-", "resultado"),
    "demostraciones": ("DEM-", "demostracion"),
    "literatura": ("LIT-", "literatura"),
}


def _frontmatter(path: Path, errors: list[str]) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        errors.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return {}, text
    try:
        end = lines.index("---", 1)
    except ValueError:
        errors.append(f"{path.relative_to(ROOT)}: unterminated frontmatter")
        return {}, text
    meta = {}
    for line_no, line in enumerate(lines[1:end], 2):
        match = FRONT_LINE.fullmatch(line)
        if match is None:
            errors.append(f"{path.relative_to(ROOT)}:{line_no}: expected key: JSON-compatible YAML value")
            continue
        key, value = match.groups()
        if key in meta:
            errors.append(f"{path.relative_to(ROOT)}:{line_no}: duplicate field {key}")
            continue
        try:
            meta[key] = json.loads(value)
        except json.JSONDecodeError:
            errors.append(f"{path.relative_to(ROOT)}:{line_no}: invalid JSON-compatible field {key}")
    return meta, "\n".join(lines[end + 1:])


def _markdown_lines(content: str):
    """Yield lines outside fenced code; strip inline code before checking."""
    fence_char = None
    fence_size = 0
    for number, line in enumerate(content.splitlines(), 1):
        marker = FENCE.match(line)
        if marker:
            chunk = marker.group(1)
            if fence_char is None:
                fence_char, fence_size = chunk[0], len(chunk)
            elif chunk[0] == fence_char and len(chunk) >= fence_size:
                fence_char, fence_size = None, 0
            continue
        if fence_char is not None:
            continue
        yield number, re.sub(r"[\x60][^\x60]*[\x60]", "", line)


def _target(value: str) -> str:
    return value.split("|", 1)[0].split("#", 1)[0].strip()


def _neighbors(value) -> list[str] | None:
    if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
        return None
    return [_target(x[2:-2]) if x.startswith("[[") and x.endswith("]]") else "" for x in value]


def validate(root: Path = ROOT) -> list[str]:
    wiki = root / "wiki"
    errors: list[str] = []
    if not wiki.is_dir():
        return [f"Missing vault {wiki}"]

    files = sorted(wiki.rglob("*.md"))
    cards: dict[str, tuple[Path, dict]] = {}
    name_to_path: dict[str, Path] = {}
    targets: set[str] = set()

    for path in list(files) + sorted(wiki.rglob("*.base")):
        rel = path.relative_to(wiki).as_posix()
        targets.add(rel)
        if path.suffix == ".md":
            name_to_path.setdefault(path.stem, path)

    for path in files:
        folder = path.relative_to(wiki).parts[0]
        if folder not in CARD_FOLDERS:
            continue  # Maps/templates are narrative rather than proof-graph nodes.
        prefix, expected_type = CARD_FOLDERS[folder]
        meta, _ = _frontmatter(path, errors)
        if not meta:
            continue
        id_ = meta.get("id")
        if not isinstance(id_, str) or not id_.startswith(prefix):
            errors.append(f"{path.relative_to(root)}: invalid ID prefix")
            continue
        if id_ != path.stem:
            errors.append(f"{path.relative_to(root)}: filename and ID disagree")
        if id_ in cards:
            errors.append(f"{id_}: duplicate ID")
        else:
            cards[id_] = (path, meta)
        if meta.get("tipo") != expected_type:
            errors.append(f"{id_}: wrong 'tipo'")
        if not isinstance(meta.get("titulo"), str) or not meta["titulo"]:
            errors.append(f"{id_}: empty 'titulo'")
        if meta.get("estado") not in {"definido", "documentado", "demostrado", "pendiente"}:
            errors.append(f"{id_}: invalid estado")
        if _neighbors(meta.get("up")) is None:
            errors.append(f"{id_}: 'up' must be a list of quoted wikilinks")
        if _neighbors(meta.get("fuentes")) is None:
            errors.append(f"{id_}: 'fuentes' must be a list of quoted wikilinks")

    adjacency = {}
    for id_, (path, meta) in cards.items():
        deps = _neighbors(meta.get("up")) or []
        adjacency[id_] = deps if id_.startswith(("DEF-", "RES-")) else []

        for target in deps:
            if target not in cards:
                errors.append(f"{id_}: nonexistent dependency {target!r}")
            elif not target.startswith(("DEF-", "RES-")):
                errors.append(f"{id_}: dependencies must target definitions/results, not {target}")
            elif cards[target][1].get("estado") not in {"definido", "demostrado"}:
                errors.append(f"{id_}: prerequisite {target} not established")

        for ref in _neighbors(meta.get("fuentes")) or []:
            if ref not in cards or cards[ref][1].get("tipo") != "literatura":
                errors.append(f"{id_}: missing literature card {ref!r}")

        if meta.get("tipo") == "resultado" and meta.get("estado") == "demostrado":
            proof = _target(str(meta.get("prueba", "")).strip("[]"))
            if proof not in cards or cards[proof][1].get("tipo") != "demostracion":
                errors.append(f"{id_}: missing proof {proof!r}")
            elif _target(str(cards[proof][1].get("resultado", "")).strip("[]")) != id_:
                errors.append(f"{id_}: non-reciprocal proof link from {proof}")

        if meta.get("tipo") == "demostracion":
            result = _target(str(meta.get("resultado", "")).strip("[]"))
            if result not in cards or cards[result][1].get("tipo") != "resultado":
                errors.append(f"{id_}: missing result {result!r}")
            elif _target(str(cards[result][1].get("prueba", "")).strip("[]")) != id_:
                errors.append(f"{id_}: non-reciprocal result link from {result}")
            if result in deps:
                errors.append(f"{id_}: proof depends on its own conclusion {result}")

        if meta.get("tipo") == "literatura":
            for key in ("origen_repo", "extraccion_repo"):
                value = meta.get(key)
                if not isinstance(value, str) or not value.startswith("literature/"):
                    errors.append(f"{id_}: missing or invalid {key}")
                elif not (root / value).is_file():
                    errors.append(f"{id_}: source file does not exist: {value}")
            if not isinstance(meta.get("doi"), str) or not meta.get("doi"):
                errors.append(f"{id_}: DOI unavailable; provide explicit provenance if truly missing")

    # Dependencies are directed FROM a result TO its prerequisites.
    active: set[str] = set()
    finished: set[str] = set()

    def visit(node: str, stack: list[str]) -> None:
        if node in finished:
            return
        if node in active:
            errors.append("Dependency cycle: " + " -> ".join(stack + [node]))
            return
        active.add(node)
        for nxt in adjacency.get(node, []):
            if nxt in adjacency:
                visit(nxt, stack + [node])
        active.remove(node)
        finished.add(node)

    for node in sorted(adjacency):
        visit(node, [])

    # Check internal Obsidian links and multiline LaTeX blocks in every wiki page.
    for path in files:
        text = path.read_text(encoding="utf-8")
        _, body = _frontmatter(path, []) if path.relative_to(wiki).parts[0] in CARD_FOLDERS else ({}, text)
        math_markers = 0
        for number, line in _markdown_lines(body):
            if SINGLE_DOLLAR.fullmatch(line):
                errors.append(f"{path.relative_to(root)}:{number}: use '$$' for display math")
            if DOUBLE_DOLLAR.fullmatch(line):
                math_markers += 1
            if LEGACY_MATH.search(line):
                errors.append(f"{path.relative_to(root)}:{number}: use $ or $$, not old LaTeX delimiters")
            for match in WIKILINK.finditer(line) if path.relative_to(wiki).parts[0] != "_plantillas" else []:
                target = _target(match.group(1))
                if not target:
                    continue
                if target in name_to_path:
                    continue
                if target in targets or (target + ".md") in targets:
                    continue
                errors.append(f"{path.relative_to(root)}:{number}: broken Obsidian link {target!r}")
        if math_markers % 2:
            errors.append(f"{path.relative_to(root)}: unmatched standalone '$$' marker")

    for base in sorted(wiki.rglob("*.base")):
        raw = base.read_text(encoding="utf-8")
        if not all(key in raw for key in ("filters:", "views:", "- type: table")):
            errors.append(f"{base.relative_to(root)}: incomplete Obsidian Bases configuration")

    return sorted(set(errors))


def main() -> int:
    errors = validate()
    if errors:
        print("Wiki validation failed:")
        for issue in errors:
            print(" -", issue)
        return 1
    print("Wiki validation passed: links, sources, DAG, proofs, metadata, math delimiters, catalog files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
