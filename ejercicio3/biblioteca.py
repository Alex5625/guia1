from libro import Libro

class Biblioteca():
    def __unit__(self):
        self.encargado = None
        self.externo = None
        self.nombre = ""
        

    def llegada_trabajador(self,nombre):

        self.encargado = nombre
        print(f"Bienvenido a Le Octopus, le atenderá {self.encargado}.")

    def agregar_libro(self,libro):
        if isinstance(libro,Libro):
            self.externo = libro

    def prestar_libro(self):

        if self.externo.n_disponibles == 0:
            print("losiento no quedan mas copias")
        else:
            self.nombre = str(input("¿A que nombre asignamos este prestamo?\n"))
            print(f"Bien {self.nombre} quedan copias, toma uno")

            self.externo.n_disponibles = self.externo.n_disponibles - 1
            self.externo.n_prestados = self.externo.n_prestados + 1

    def devolver_libro(self):
        if self.externo.n_prestados == 0:
            print("no se ha prestado ningun libro xdd")
            
            self.mostrar_disponibles()

        else:
            print("okis, gracias por devolverlo")
            self.externo.n_disponibles = self.externo.n_disponibles + 1
            self.externo.n_prestados = self.externo.n_prestados - 1

    def mostrar_disponibles(self):
        print(f"Hay {self.externo.n_disponibles} libro(s) disponible(s) =)")


