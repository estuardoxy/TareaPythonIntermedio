from ClasePersona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, trabajo = "Profesor"):
        super().__init__(nombre, edad, trabajo)

    def darClases(self):
        print("Dando clases...")
