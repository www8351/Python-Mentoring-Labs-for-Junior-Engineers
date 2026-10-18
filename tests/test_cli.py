"""Tests for labs.cli."""

from __future__ import annotations

from typer.testing import CliRunner

from labs import __version__
from labs.cli import app

runner = CliRunner()


def test_version_flag_prints_version_and_exits() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert result.output.strip() == f"labs {__version__}"
