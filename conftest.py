"""Primarily for reusable fixtures to use in testing"""
import pytest


@pytest.fixture()
def empty_deck(tmp_path):
    filename = 'empty.txt'
    contents = ''
    # creating directory and path
    dir = tmp_path / "tmp"
    dir.mkdir()
    path = dir / filename
    path.write_text(contents, encoding="utf-8")
    return path
