import pytest

from calc import calc


@pytest.mark.parametrize('expression, expected', [
    ('2+2', 4),
    # ('2+4', 6),
])
def test_addition(expression, expected):
    result = calc.calc(expression)
    assert result == expected
