from ClasePersona import Persona

class Secretaria(Persona):
    def __init__(self, nombre, edad, trabajo = "Secretaria"):
        super().__init__(nombre, edad, trabajo)

    def atenderLlamadas(self):
        print("Atendiendo llamadas...")