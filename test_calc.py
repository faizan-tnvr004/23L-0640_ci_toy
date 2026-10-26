from calc import add, is_ai


def test_add():
    assert add(2, 3) == 5


def test_threshold():
    assert is_ai(0.6) is True
    assert is_ai(0.4) is False
