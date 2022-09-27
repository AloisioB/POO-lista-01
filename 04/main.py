class Shapes:
    def __init__(self):
        self.quantity = int(input("Enter the number of shapes: "))
        self.totalshapes = []

    def calcular(self):
        for i in range(0, self.quantity):
            shape = input("R/C ")
            if shape == "R" or shape == "r":
                largura = float(input("Type the width: "))
                altura = float(input("Type the height: "))
                area = largura * altura
                self.totalshapes.append(area)
            elif shape == "C" or shape == "c":
                raio = float(input("Type the radio: "))
                area = ((raio * 2) * 3.1415)
                self.totalshapes.append(area)

        print("SHAPES AREAS: \n")
        for i in self.totalshapes:
            print(i)

S = Shapes()
S.calcular()

