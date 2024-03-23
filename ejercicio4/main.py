from perros import Perros
from vida import Vida

#a las variables ponerles los nombres de los perros 

if __name__ == "__main__":

    jorge = Perros()
    
    jorge.nombre =  "Jorge" 
    jorge.color = "Café"
    jorge.raza = "Quiltro"
    jorge.edad = 13
#   HOMBRE = H     MUJER = M
    jorge.sexo = "H"
    jorge.b_vida = 4
    jorge.b_hambre = 5

    vale = Perros()
    vale.nombre =  "pedro" 
    vale.color = "negro"
    vale.raza = "rotweailler"
    vale.edad = 2
#   hombre = H     MUJER = M
    vale.sexo = "H"
    vale.b_vida = 2
    vale.b_hambre = 3

    interaccion = Vida()

    interaccion.iniciar_perros(jorge,vale)

    interaccion.pelea_territorio("2")

    interaccion.mostrar_vida_hambre()

    interaccion.jugar()

    interaccion.mostrar_vida_hambre()







