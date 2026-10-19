"""Offline, read-only checks for the source-grounded Marp lecture deck.

Does NOT export/render the slides. It checks local media/link presence, the
built-in math directive, YAML markers, and self-contained SVG XML structure.
Use before Marp CLI; manual PDF/HTML visual inspection is still required.
"""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", choices=("v1", "v2"), default="v1")
    args = parser.parse_args()
    deck = here / ("001_process_diversity_lecture.md" if args.version == "v1"
                   else "002_process_diversity_lecture_v2.md")
    errors: list[str] = []
    if not deck.is_file():
        raise SystemExit(f"Missing deck: {deck}")
    text = deck.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not text.startswith("---\nmarp: true\n"):
        errors.append("Missing Marp frontmatter")
    if "math: katex" not in text:
        errors.append("Missing explicit KaTeX directive")
    if text.count("$$") % 2:
        errors.append("Unpaired $$ display math delimiter")
    slides = len(re.findall(r"(?m)^---\s*$", text)) - 1
    min_slides = 150 if args.version == "v2" else 60
    if slides < min_slides:
        errors.append(f"Unexpectedly short lecture: {slides} slides")
    images = re.findall(r"!\[[^\]]*]\(([^)]+)\)", text)
    if len(images) < (35 if args.version == "v2" else 20):
        errors.append(f"Expected gallery and new figure images, got {len(images)}")
    checks = set()
    for media in images:
        if "://" in media or media.startswith("#"):
            errors.append(f"Unexpected external/anchor slide asset: {media}")
            continue
        p = (here / media).resolve()
        if not p.is_file():
            errors.append(f"Missing local asset: {media}")
        elif not p.stat().st_size:
            errors.append(f"Empty local asset: {media}")
        if p.suffix.lower() == ".svg" and p not in checks and p.is_file():
            try:
                if not ET.parse(p).getroot().tag.endswith("svg"):
                    errors.append(f"Wrong vector root: {p}")
            except ET.ParseError as exc:
                errors.append(f"Invalid SVG/XML {media}: {exc}")
            checks.add(p)
    svg_assets = sorted((here / "assets").glob("*.svg"))
    expected_min = 23 if args.version == "v2" else 12
    if len(svg_assets) < expected_min:
        errors.append(f"Expected at least {expected_min} lecture SVGs, found {len(svg_assets)}")
    for p in svg_assets:
        if p not in checks:
            try:
                ET.parse(p)
            except ET.ParseError as exc:
                errors.append(f"Invalid unused vector asset {p.name}: {exc}")
    print(
        f"Marp static check: {slides} slide separators, {len(images)} "
        f"image mentions, {len(set(images))} distinct linked paths, "
        f"{len(svg_assets)} generated SVGs"
    )
    if errors:
        for error in errors:
            print("ERROR:", error, file=sys.stderr)
        return 1
    print("PASS — all referenced local assets exist, SVGs parse, and math is delimited.")
    print("NOTE — Marp CLI render/slide-clipping validation still required separately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
