
class Calculadora():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

#lo ideal es que por una mejor manera de expresar una cosa, el return si es un numero, debe retornar siempre un numero
        

    def sumar(self):
        try:
            return self.num1 + self.num2

        except TypeError:
            #con un raise en vez de retornar un string
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