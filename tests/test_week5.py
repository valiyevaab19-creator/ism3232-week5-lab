import math


def test_tax_at_seven_percent():
    subtotal = 200.00
    tax = subtotal * 0.07
    assert math.isclose(tax, 14.0)


def test_over_limit_true():
    amount = 1500
    limit = 1000
    assert (amount > limit) is True


def test_over_limit_false():
    amount = 500
    limit = 1000
    assert (amount > limit) is False


def test_type_of_string():
    name = "ISM3232"
    assert type(name) == str


def test_type_coversion():
    s = "42"
    assert int(s) == 42
