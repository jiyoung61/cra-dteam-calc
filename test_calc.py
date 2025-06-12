import pytest

from calc import Calc


@pytest.mark.parametrize("a, expected", [
    (0, 0),
    (1, 1),
    (-1, 1),
    (2, 4),
    (-3, 9),
    (1.5, 2.25),
    (-2.5, 6.25),
    (1e3, 1e6),
])
def test_get_zegop(a, expected):
    assert Calc.get_zegop(a) == expected
