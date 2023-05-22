def test_pass():
    a = (1, 2, 3)
    assert a == (1, 2, 3)


def test_fail():
    a = (1, 2, 3)
    assert a == (1, 2, 3, 4)
