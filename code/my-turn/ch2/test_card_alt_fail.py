from cards import Card


def test_equality_fail():
    c1 = Card("something", "Jude")
    c2 = Card("something", "Jude")
    assert c1 == c2
