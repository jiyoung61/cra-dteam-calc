import pytest
from calc import Calc


def test_sample():
    pass

def test_division():
    sut = Calc()
    ret = sut.get_divide(4, 2)
    assert ret == 2

from calc import Calc
def test_get_sum_1():
    # arrange
    calc = Calc()

    # act
    actual = calc.get_sum(1, 2)

    # assert
    assert actual == 3

