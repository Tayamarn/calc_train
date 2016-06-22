import pytest

import calc


@pytest.mark.parametrize('expression, expected', [
    ('2+2', 4),
    ('2+4.5', 6.5),
    ('11', 11),
])
def test_addition(expression, expected):
    result = calc.calc(expression)
    assert result == expected


# @pytest.mark.parametrize('expression, expected', [
#     ('2-2', 0),
#     ('5-1', 4),
#     ('2-7', -5),
#     ('3.2-3.1', .1),
# ])
# def test_substration(expression, expected):
#     result = calc.calc(expression)
#     assert result == expected


@pytest.mark.parametrize('expression', [
    (''),
    ('+15'),
    ('fgjkfdljgk'),
])
def test_errors(expression):
    with pytest.raises(ValueError):
        calc.calc(expression)
