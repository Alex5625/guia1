from calculadora import Calculadora

if __name__ == "__main__":
    obj_calculos = Calculadora(2,0)

    print(obj_calculos.num1, obj_calculos.num2)

    print(obj_calculos.sumar())

    print(obj_calculos.restar())

    print(obj_calculos.multiplicar())

    print(obj_calculos.dividir())
