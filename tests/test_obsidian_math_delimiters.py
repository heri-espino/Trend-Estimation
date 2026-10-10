"""Regression check for Obsidian display-math delimiter syntax in notes/."""

from pathlib import Path
import re


NOTES = Path(__file__).resolve().parents[1] / "notes"
FENCE = re.compile(r"^ {0,3}([\x60]{3,}|~{3,})")
SINGLE_DOLLAR = re.compile(r"^\s*\$\s*$")
DOUBLE_DOLLAR = re.compile(r"^\s*\$\$\s*$")


def _delimiter_issues(path: Path) -> list[str]:
    """Inspect Markdown outside fenced code; no changes to the note itself."""
    issues: list[str] = []
    fence_char = None
    fence_width = 0
    block_markers = 0

    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        marker = FENCE.match(line)

        if marker and fence_char is None:
            fence_char, fence_width = marker.group(1)[0], len(marker.group(1))
            continue

        if marker and marker.group(1)[0] == fence_char and len(marker.group(1)) >= fence_width:
            fence_char, fence_width = None, 0
            continue

        if fence_char is not None:
            continue

        if SINGLE_DOLLAR.fullmatch(line):
            issues.append(f"{path.relative_to(NOTES)}:{number}: multiline math must use '$$' (not '$')")
        elif DOUBLE_DOLLAR.fullmatch(line):
            block_markers += 1

    if block_markers % 2 != 0:
        issues.append(f"{path.relative_to(NOTES)}: unmatched display-math '$$' marker")

    return issues


def test_obsidian_display_math_delimiters():
    notes = list(NOTES.rglob("*.md"))
    assert notes, "No Markdown notes found to validate."
    issues = [issue for path in notes for issue in _delimiter_issues(path)]
    assert not issues, "\n".join(issues)
