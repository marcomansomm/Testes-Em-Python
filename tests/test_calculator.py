import pytest

from Calculator import Calculator
from Calculator import CalcError

@pytest.mark.parametrize("a, b, res",
                         [(5, 2, 7),
                          (3, 6, 9)])
def test_soma(a, b, res):
    calculadora = Calculator()
    res_calc = calculadora.soma(a, b)
    assert res == res_calc

@pytest.mark.parametrize("a, b, res",
                         [("5", 2, 7),
                          (5, "2", 7),
                          ("5", "2", "7")])

def test_soma_tipos(a, b, res):
    calculadora = Calculator()
    with pytest.raises(CalcError):
        res_cal = calculadora.soma(a, b)
    assert res == res_cal