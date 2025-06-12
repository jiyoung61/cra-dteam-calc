import pytest
from calc import Calc


def test_sample():
    pass

def test_division():
    sut = Calc()
    ret = sut.get_divide(4, 2)
    assert ret == 2


def test_get_nzegop():
    result1 = Calc().get_nzegop(2, 3)
    result2 = Calc().get_nzegop(3, 2)
    result3 = Calc().get_nzegop(4, 3)
    assert result1 == 8
    assert result2 == 9
    assert result3 == 64


def test_get_sum_1():
    # arrange
    calc = Calc()

    # act
    actual = calc.get_sum(1, 2)

    # assert
    assert actual == 3

