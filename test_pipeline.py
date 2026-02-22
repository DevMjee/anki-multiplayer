from pipeline import extract, transform, load
import pytest


def test_extract_1():
    """Is the source empty? - keep this way for the future update from files to imports"""
    src = ''
    with pytest.raises(ValueError):
        extract(src)


def test_extract_2(empty_deck):
    """Is the deck empty?"""
    with pytest.raises(ValueError):
        extract(empty_deck)


def test_extract_3():
    ...


def test_transform_1():
    ...


def test_load_1():
    ...
