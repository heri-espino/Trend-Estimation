from pathlib import Path


def test_experiment_scripts_compile():
    root = Path(__file__).resolve().parents[1]
    scripts = sorted((root / "experiments").rglob("*.py"))

    assert scripts, "Expected at least one experiment script."

    for path in scripts:
        source = path.read_text(encoding="utf-8")
        compile(source, str(path), "exec")
