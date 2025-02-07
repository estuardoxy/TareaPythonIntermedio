from ClasePersona import Persona

#Clase heredada de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, trabajo="Estudiante"):
        super().__init__(nombre, edad, trabajo) #Lo que hace es llamar al constructor de la clase padre
    
    def estudiar(self):
        print("Estudiando...")