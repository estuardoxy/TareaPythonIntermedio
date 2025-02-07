#Esta es mi clase base, es decir que es la base de todas las demas
class Persona:
    def __init__(self, nombre, edad, trabajo):
        self.nombre = nombre
        self.edad = edad
        self.trabajo = trabajo

    """
    def dormir(self):
        print("Durmiendo...")
    
    def comer(self):
        print("Comiendo...")
    """
        
    def __str__(self):
        return f'''
        La persona se llama {self.nombre}, 
        tiene {self.edad} años 
        y es {self.trabajo}
        '''