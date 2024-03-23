from perros import Perros


#aki realizaremos los metodos de las acciones del dia a dia
class Vida():
    
    def __init__(self):

        self.perro1 = None
        self.perro2 = None

# CREAR METODOS PARA: INICIALZAR PERROS | PELEAR | JUGAR | COMER 
    def iniciar_perros(self,perro_1,perro_2):
                       
        if isinstance(perro_1,Perros) and isinstance(perro_2,Perros):
            
            self.perro1 = perro_1
            self.perro2 = perro_2


#  PELEAR = EL QUE PIERDA -1 DE VIDA Y -1 DE HAMBRE
# al llamar a la funcion, podemos entregarle el vencedor: 1 gana el perro1 y 2 gana el perro2
    def pelea_territorio(self,ganador):
        ganador = int(ganador)

        if self.perro1.sexo == "H" and self.perro2.sexo == "H":
            if ganador == 1:
                self.perro2.b_vida -= 1
                self.perro2.b_hambre -= 1
                print(f"\nGanó {self.perro1.nombre}, ahora el es el dueño del territorio\n")
            elif ganador == 2:
                self.perro1.b_vida -= 1
                self.perro1.b_hambre -= 1

                print(f"\nGanó {self.perro2.nombre}, ahora el es el dueño del territorio\n")
            else:
                print("La pelea es solo de dos perros >:(")
            
        else:
            
            print("Se sintió el ambiente tenso pero no llego a ocurrir nada\n")

# JUGAR = +1 DE VIDA Y -1 DE HAMBRE
    def jugar(self):
        print("ambos perros estan jugando, se notan muy contentos :)\n")
        self.perro1.b_vida += 1
        self.perro1.b_hambre -= 1

        self.perro2.b_vida += 1
        self.perro2.b_hambre -= 1


# #Darle cariños, +1 de vida solo
        
#     def mimos(self):

#         self.perro1.b_vida += 1

#         self.perro2.b_vida += 1

#         print("Le encantaron demasiado los cariños, tanto asi que recuperaron vida")


#MOSTRAR VIDA DE AMBOS 
            
    def mostrar_vida_hambre(self):
        
        print(f"{self.perro1.nombre} tiene {self.perro1.b_vida} de vida, y {self.perro1.b_hambre} de hambre!\n")
        

        if self.perro1.b_vida == 0:
            print(f"OH no! {self.perro1.nombre} esta por debilitarse, hay que darle cariño para que se recupere\n")
            self.perro1.b_vida += 1
            print("Le encantaron demasiado los cariños, tanto asi que recuperaron vida")

        if self.perro1.b_hambre == 0:
            print(f"{self.perro1.nombre} está hambriento, le voy a dar de comer\n")
            self.perro1.b_hambre += 1


        print(f"{self.perro2.nombre} tiene {self.perro2.b_vida} de vida, y {self.perro2.b_hambre} de hambre!")

        if self.perro2.b_vida == 0:
            print(f"OH no! {self.perro2.nombre} esta por debilitarse, hay que darle cariño para que se recupere\n")
            self.perro2.b_vida += 1
            print("Le encantaron demasiado los cariños, tanto asi que recuperaron vida")

        if self.perro2.b_hambre == 0:
            print(f"{self.perro2.nombre} está hambriento, le voy a dar de comer")
            self.perro2.b_hambre += 1