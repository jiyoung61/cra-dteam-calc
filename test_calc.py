import pytest
from calc import Calc

def test_sample():
    calc = Calc()
    assert calc.get_sumsum(1, 2, 3) == 6
    assert calc.get_sumsum(5, -1, 2.0) == 6.0
