import pytest
from cards import Card


def test_equality_fail():
    c1 = Card("something", "Jude")
    c2 = Card("something", "Jude!")
    if c1 != c2:
        pytest.fail("They are not equal")


def test_equality_fail_2():
    c1 = Card("something", "Jude")
    c2 = Card("something", "Jude!")
    if c1 != c2:
        raise Exception("They are not equal")
