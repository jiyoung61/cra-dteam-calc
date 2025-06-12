import pytest
from calc import Calc
def test_sample():
    pass

@pytest.fixture
def calc():
    calc = Calc()
    return calc

def test_get_minus(calc):
    assert calc.get_minus(2, 1) == 2 - 1
    assert calc.get_minus(3, 1) == 3 - 1
    assert calc.get_minus(1, 3) == 1 - 3

def test_get_minus_typeerror(calc):
    assert calc.get_minus("2", "1") == 1
    assert calc.get_minus(2, "1") == 1
    assert calc.get_minus("2", 1) == 1

def test_get_minus_valueerror(calc):
    with pytest.raises(ValueError):
        assert calc.get_minus("2ta", "1")