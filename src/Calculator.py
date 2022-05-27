import numbers

class CalcError(Exception):
    pass

class Calculator(object):
    def soma(self, a, b):

        self.check_type(a)
        self.check_number_natural(a)
        self.check_numbers_negativos(a)
        self.check_type(b)
        self.check_number_natural(b)
        self.check_numbers_negativos(b)

        return a+b

    def check_type(self, op):

        if not isinstance(op, numbers.Number):
            raise CalcError(f" {op} não é um número!")

    def check_number_natural(self, op):

        if not isinstance(op, numbers.Rational):
            raise CalcError(f" {op} não é um número natural!")

    def division_zero(self, dividendo):
        if dividendo == 0:
            raise CalcError(f"O dividendo {dividendo}, é igual a zero! ")

    def check_res_natural(self, res):

        if not isinstance(res, numbers.Rational):
            raise CalcError(f"A resposta foi {res} e não é um número natural!")

    def check_numbers_negativos(self, op):

        if op < 0:
            raise CalcError(f"{op} é menor que 0!")

    def check_result_negativos(self, res):
        if res < 0:
            raise CalcError(f"{res} é menor que 0!")



    def subtracao(self, a, b):

        self.check_type(a)
        self.check_number_natural(a)
        self.check_numbers_negativos(a)
        self.check_type(b)
        self.check_number_natural(b)
        self.check_numbers_negativos(b)
        res = b-a
        self.check_result_negativos(res)

        return res

    def potencia(self, a, b):

        self.check_type(a) #base
        self.check_number_natural(a)
        self.check_numbers_negativos(a)
        self.check_type(b) #expoente
        self.check_number_natural(b)
        self.check_numbers_negativos(b)

        return a**b

    def divisao(self, a, b, res):

        self.check_type(a)
        self.check_number_natural(a)
        self.check_numbers_negativos(a)
        self.check_type(b)
        self.chek_number_natural(b)
        self.division_zero(b)
        self.check_numbers_negativos(b)
        res = a/b
        self.check_res_natural(res)

        return res