from persona import Persona

class Tarjeta():
    def __init__(self):
        self.saldo = 0
        self.titular = None
        self.numero_tarjeta = None

    def asocia_persona(self,persona):
        if isinstance(persona,Persona):
            if not self.titular:
                self.titular = persona
            else:
                print("esta vinculada a otra persona peldom")
        else:
            print("error no se vinculo a na")

    def abona_plata(self,monto):
        if isinstance(monto,int):
            self.saldo = self.saldo + monto
        else:
            print("error")

    def cargo_tarjeta(self,monto):
        if isinstance(monto, int):
            if self.monto >= monto:
                self.saldo = self.saldo- monto
            else:
                print("no te alcanza unu")
                self.muestra_saldo()

        

    def muestra_saldo(self):
        print(f"Su saldo es: {self.saldo}")