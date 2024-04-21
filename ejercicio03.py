class Vehiculo():

    def __init__(self, placa, color, ruedas):
        self.placa = placa
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Placa: {}, Color: {}, Ruedas: {} ".format(self.placa, self.color, self.ruedas)

class Auto(Vehiculo):

    def __init__(self, placa, color, ruedas, velocidad, cilindrada):
        self.placa = placa
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "Placa {}, color {}, {} km/h, {} ruedas, {} cc".format(self.placa, self.color, self.velocidad, self.ruedas, self.cilindrada )

class Motocicleta(Vehiculo):
    def __init__(self, placa, color,ruedas,tipo):
        self.placa = placa
        self.color = color
        self.ruedas = ruedas
        self.tipo = tipo
    def __str__(self):
        return "Placa {}, color {}, {} ruedas, tipo {} ".format(self.placa, self.color, self.ruedas, self.tipo)


auto1 = Auto("AZ123","azul", 4, 150, 1200)
print(auto1)
motocicleta1 = Motocicleta("W233","Rojo",2,"Urbana")
print(motocicleta1)
