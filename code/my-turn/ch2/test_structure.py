from cards import Card


# AAA -> Arrange, Act, Assert
# or (choose any one `same thing`)
# GWT -> Give, When, Then
def test_to_dict_aaa():
    # Arrange
    c1 = Card("something", "Jude", "todo", 123)
    # Act
    c2 = c1.to_dict()
    # Assert
    c2_expected = {
        "summary": "something",
        "owner": "Jude",
        "state": "todo",
        "id": 123,
    }
    assert c2 == c2_expected


def test_to_dict_gwt():
    # Given a card with known value
    c1 = Card("something", "Jude", "todo", 123)
    # When we call to_dict() on card
    c2 = c1.to_dict()
    # Then we egt the expected dictionary
    c2_expected = {
        "summary": "something",
        "owner": "Jude",
        "state": "todo",
        "id": 123,
    }
    assert c2 == c2_expected
