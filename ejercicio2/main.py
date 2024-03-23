from persona import Persona
from tarjeta import Tarjeta

if __name__ == "__main__":
    
    emilio = Persona()
    emilio.nombre = "Eimlio"
    emilio.apellido_paterno = "jozque"
    emilio.apellido_materno = "fogeUX"
    emilio.telefono = "133"

    masterplop = Tarjeta()
    masterplop.numero_tarjeta = "123456789"
    masterplop.asocia_persona(emilio)

    print(masterplop.titular.nombre)
    print(masterplop.titular.apellido_paterno)
    print(masterplop.titular.apellido_materno)
    # print(masterplop.titular.mostrar_titular())

    masterplop.abona_plata(1000)

    masterplop.cargo_tarjeta(500)

    masterplop.muestra_saldo()

    masterplop.asocia_persona(emilio)