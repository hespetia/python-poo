class Alumno:
    # Constructor
    def __init__(self, codigo, nombres, apellidos, nota):
        self.codigo = codigo
        self.nombres = nombres
        self.apellidos = apellidos
        self.nota = nota
    # función para imprimir los datos
    def imprimir(self):
        print("Codigo: ", self.codigo)
        print("Nombres: ", self.nombres)
        print("Apellidos: ", self.apellidos)
        print("Nota: ", self.nota)
    # función para obtener el resultado
    def condicion(self):
        if self.nota < 14:
            print("El alumno esta desaprobado")
        else:
            print("El alumno ha aprobado")

# bloque principal
# creamos los nuevos objetos
alumno1 = Alumno("01","Apaza","Juan",12)
alumno2 = Alumno("02","Flores","Smith",15)

# imprimimos los datos y resultados de cada alumno
alumno1.imprimir()
alumno1.condicion()
alumno2.imprimir()
alumno2.condicion()
