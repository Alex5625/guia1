
class Calculadora():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        try:
            return self.num1 + self.num2

        except TypeError:
            return "Error"
        
    def restar (self):

        try:
            return self.num1 - self.num2

        except TypeError:
            return "Error"

    def multiplicar(self):

        try:
            return self.num1 * self.num2

        except TypeError:
            return "Error"

    def dividir(self):

        try:
            return self.num1 / self.num2

        except TypeError:
            return "Error"
        
        except ZeroDivisionError:
            return "No se puee dividir por cero"