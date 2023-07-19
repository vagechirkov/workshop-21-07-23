import pytest

from factorial import factorial


@pytest.mark.parametrize("x, expected", [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120)])
def test_factorial(x, expected):
    assert factorial(x) == expected
