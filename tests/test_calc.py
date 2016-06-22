import pytest

from calc import calc


@pytest.mark.parametrize('expression, expected', [
    ('2+2', 4),
    ('2+4.5', 6.5),
    ('11', 11),
    ('', None),
    ('+15', None),
    ('fgjkfdljgk', None),
])
def test_addition(expression, expected):
    result = calc(expression)
    assert result == expected
