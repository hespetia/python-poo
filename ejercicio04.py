class Persona(object):
    """Clase que representa una Persona"""

    def __init__(self, dni, nombre, apellido, sexo):
        # Constructor de la clase persona
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo

    def __str__(self):
        """Devuelve una cadena representativa de Persona"""
        return "DNI: %s, Nombres: %s, Apellidos: %s, Genero: %s" % (
            str(self.dni), self.nombre,
            self.apellido, self.getGenero(self.sexo))

    def trabajar(self, mensaje):
        """Mostrar mensaje de saludo de Persona"""
        return mensaje

    def getGenero(self, sexo):
        """Mostrar el genero de la Persona"""
        genero = ('Masculino','Femenino')
        if sexo == "M":
            return genero[0]
        elif sexo == "F":
            return genero[1]
        else:
            return "Desconocido"

persona1 = Persona("23983323", "Leonardo", "Quispe", "M")
persona2 = Persona("34324223", "Ana", "Polanco", "F")

print(persona1.dni, persona1.nombre, persona1.apellido)
print(persona1.getGenero(persona1.sexo))
print(persona2.dni, persona2.nombre, persona2.apellido)
print(persona2.getGenero(persona2.sexo))

print(str(persona1) + "\n")
print(str(persona2) + "\n")

# Docente
class Docente(Persona):
    """Clase que representa a un Docente"""

    def __init__(self, dni, nombre, apellido, sexo, especialidad):
        """Constructor de clase Docente"""

        # Invoca al constructor de clase Persona
        Persona.__init__(self, dni, nombre, apellido, sexo)

        # Nuevos atributos
        self.especialidad = especialidad
        self.cursos = ['Algo II','SW I','SW II','SW III']

    def __str__(self):
        """Devuelve una cadena representativa al Docente"""
        return "%s %s, especialidad: '%s', sus cursos: %s." % (
            self.nombre, self.apellido,
            self.especialidad, self.consulta_cursos())

    def consulta_cursos(self):
        """Mostrar las tareas del Docente"""
        return ', '.join(self.cursos)

docente1 = Docente("45645456", "Lornel", "Rivas", "M", "Sistemas")
print(str(docente1))
