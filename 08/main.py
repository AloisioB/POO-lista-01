class Alunos:
    def __init__(self, nome, matricula, notas, assunto):
        self.notasemestral = None
        self.notafinal = None
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
        self.assunto = assunto
        self.erro = False

    def check(self):
        i = j = 0
        for k in self.nome:
            if k == " ":
                i += 1
            j += 1

        if i < 1 or j > 50 or len(self.matricula) != 8 or self.matricula[0:3] != "201" or len(self.notas) != 5 \
                or self.assunto is None:
            print("Há um erro com as informações fornecidas.\n")
            self.erro = True

        for i in self.notas:
            if (i > 10 or i < 0) and self.erro is False:
                print("Há um erro com as informações fornecidas.\n")
                self.erro = True

    def math(self):
        self.notas = sorted(self.notas)
        del self.notas[0]
        self.notasemestral = sum(self.notas) / 4
        if self.notasemestral < 6:
            self.notafinal = self.notafinal * 0.85
        elif 6 <= self.notasemestral < 7:
            self.notafinal = 7
        elif 7 <= self.notasemestral < 8:
            self.notafinal = 8
        else:
            self.notafinal = 10

    def printout(self):
        if not self.erro:
            print("Matricula:", self.matricula)
            print("None:", self.nome)
            print("Notas:", *self.notas)
            print("Assunto:", self.assunto)
            print("Nota semestral:", self.notasemestral)
            print("Nota final", self.notafinal, "\n")





A = Alunos("Ana Maria", "20101578", [10, 5, 4, 8, 10], "POO")
A.check()
A.math()
A.printout()

C = Alunos("Leticia Santos", "20102578", [10, 5, 4, 8, 10], "POO")
C.check()
C.math()
C.printout()

B = Alunos("João", "20102578", [12, 5, 4, 8, 15], "POO")
B.check()
B.math()
B.printout()

D = Alunos("João Paulo", "20102578", [8, 5, 4, 8, 1], "POO")
D.check()
D.math()
D.printout()



