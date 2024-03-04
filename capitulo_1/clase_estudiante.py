class Estudiante(object):
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def hola(self):
        return "Mi nombre es %s y mi edad es %i"%(self.nombre, self.edad)
    
e = Estudiante('Henry', 25)

print(e.hola())