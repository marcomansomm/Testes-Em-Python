import numbers

class CalcError(Exception):
    pass

class Calculator(object):
    def soma(self, a, b):

        self._check_type(a)
        self._check_type(b)

        return a+b

    def _check_type(self, op):

        if not isinstance(op, numbers.Number):
            raise CalcError(f" {op} não é um número")

