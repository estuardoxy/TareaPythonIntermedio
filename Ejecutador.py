from ClaseEstudiante import Estudiante
from ClaseProfesor import Profesor
from ClaseSecretaria import Secretaria

#Asigno datos a cada uno
estudiante = Estudiante("Juan", 20,)
profesor = Profesor("Pedro", 30, "Profesor de Matematicas") #Ejemplo por si quiero cambiar el trabajo
secretaria = Secretaria("Maria", 25)

#Quien es cada uno?
print(estudiante)
print(profesor)
print(secretaria)

#Que esta haciendo cada uno?
estudiante.estudiar()
profesor.darClases()
secretaria.atenderLlamadas()
