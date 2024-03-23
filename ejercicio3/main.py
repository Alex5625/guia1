from libro import Libro
from biblioteca import Biblioteca

if __name__ == "__main__":

    alexis = Libro()
    alexis.titulo = "Las seis"
    alexis.autor = "joe vasconsellos"
    alexis.n_disponibles = 2
    alexis.n_prestados = 0

    # print(f"{alexis.autor} {alexis.titulo}")
    le_octopus = Biblioteca()
    le_octopus.llegada_trabajador("Loquito")

    le_octopus.agregar_libro(alexis)

    le_octopus.mostrar_disponibles()

    desicion = input("Digita 1 si deseas pedir un libro \nDigita un 2 si deseas devolver el libro\n")

    if int(desicion) == 1:
        le_octopus.prestar_libro()
        le_octopus.mostrar_disponibles()
    
    if int(desicion) == 2:
        le_octopus.devolver_libro()






