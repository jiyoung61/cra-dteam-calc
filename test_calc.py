import pytest

from calc import Calc


def test_get_sum_1():
    # arrange
    calc = Calc()

    # act
    actual = calc.get_sum(1, 2)

    # assert
    assert actual == 3
