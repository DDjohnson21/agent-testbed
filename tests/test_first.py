"""Smoke-test bounty: a `first.py` script at repo root that prints hello world.

This test exercises the agent's ability to CREATE A NEW FILE from scratch
(not just edit an existing one). The fix is one new file with one line.
"""
import pathlib
import subprocess
import sys


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
FIRST_PY = REPO_ROOT / "first.py"


def test_first_py_exists():
    # Issue: first.py doesn't exist yet — create it at the repo root.
    assert FIRST_PY.exists(), f"expected {FIRST_PY} to exist"


def test_first_py_prints_hello_world():
    # Issue: running `python first.py` should print "hello world" (any case).
    if not FIRST_PY.exists():
        # Surfaced by the previous test; don't double-report.
        return
    result = subprocess.run(
        [sys.executable, str(FIRST_PY)],
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0, (
        f"first.py exited non-zero: code={result.returncode}, stderr={result.stderr!r}"
    )
    assert "hello world" in result.stdout.lower(), (
        f"expected 'hello world' in stdout, got: {result.stdout!r}"
    )
