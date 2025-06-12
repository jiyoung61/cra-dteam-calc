import pytest
from calc import Calc

def test_sample():
    pass

def test_division():
    sut = Calc()
    ret = sut.get_divide(4, 2)
    assert ret == 2