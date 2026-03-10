from src.logic import is_anagram


def test_positive_anagram():
    assert is_anagram("listen", "silent") is True


def test_negative_anagram():
    assert is_anagram("hello", "world") is False


def test_empty_strings():
    assert is_anagram("", "") is True
