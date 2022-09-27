class Funcionario:
    def __init__(self, nome, salariobruto, taxas):
        self.nome = nome
        self.salariobruto = salariobruto
        self.taxas = taxas
        self.salarioliquido = None
        self.porcetagem = None

    def printout(self):
        self.salarioliquido = self.salariobruto - self.taxas
        print("Nome do funcionario:", self.nome, "|", "Salario Liquido:", self.salarioliquido)

        self.porcetagem = int(input("Qual a porcetagem de aumento do salario? "))
        self.salariobruto = self.salariobruto + (self.salariobruto * self.porcetagem) / 100
        print("Update data:", "Nome:", self.nome, "|", "Salario", self.salariobruto)


F = Funcionario("Pedro", 6500, 15)
F.printout()