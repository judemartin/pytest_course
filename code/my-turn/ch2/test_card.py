from cards import Card


def test_field_access():
    c = Card("something", "jude", "todo", 12)
    print(c)
    assert c.summary == "something"
    assert c.owner == "jude"
    assert c.state == "todo"
    assert c.id == 12


def test_defaults():
    c = Card()
    print(c)
    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None
