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

@pytest.mark.parametrize("a, b, res",
                         [(5, 2, 3),
                          (3, 6, 3),
                          (3, -5, 8)])


def test_sub(a, b, res):
    calculadora = Calculator()
    res_calc = calculadora.subtracao(a, b)
    assert res == res_calc

@pytest.mark.parametrize("a, b, res",
                         [("5", 2, 3),
                          (5, "2", 3),
                          ("5", "2", "3")])

def test_sub_tipos(a, b, res):
    calculadora = Calculator()
    with pytest.raises(CalcError):
        res_cal = calculadora.subtracao(a, b)
    assert res == res_cal

@pytest.mark.parametrize("a, b, res",
                         [(5, 2, 2.5),
                          (3, 6, 0.5)])

def test_divisao(a, b, res):
    calculadora = Calculator()
    res_calc = calculadora.divisao(a, b)
    assert res == res_calc


@pytest.mark.parametrize("a, b, res",
                         [("5", 2, 2.5),
                          (5, "2", 2.5),
                          ("5", "2", "2.5")])

def test_divisao_tipos(a, b, res):
    calculadora = Calculator()
    with pytest.raises(CalcError):
        res_cal = calculadora.divisao(a, b)
    assert res == res_cal

@pytest.mark.parametrize("a, b, res",
                         [(5, 2, 25),
                          (3, 6, 729)])

def test_potencia(a, b, res):
    calculadora = Calculator()
    res_calc = calculadora.potencia(a, b)
    assert res == res_calc

@pytest.mark.parametrize("a, b, res",
                         [("5", 2, 25),
                          (5, "2", 25),
                          ("5", "2", "25")])


def test_potencia_tipos(a, b, res):
    calculadora = Calculator()
    with pytest.raises(CalcError):
        res_cal = calculadora.potencia(a, b)
    assert res == res_cal