class DadosPessoais:
    def __init__(self, dados):
        self.dados = dados

class Validador(DadosPessoais):
    def validadorcpf(self):
        if len(self.dados) == 14 and self.dados[3] == self.dados[7] == "." and self.dados[11] == "-":
            print("O CPF " + self.dados + " está valido!\n")
            return True
        else:
            print("O CPF " + self.dados + " está invalido!\n")
            return False

    def validadorcnpj(self):
        if len(self.dados) == 18 and self.dados[2] == self.dados[6] and self.dados[10] == "/" and self.dados[15] == "-":
            print("O CNPJ " + self.dados + " está valido!\n")
            return True
        else:
            print("O CNPJ " + self.dados + " está invalido!\n")
            return False

print("digite o cpf/cnpj com pontos, traços e/ou barras")

V = Validador("715.147.159-250")
V.validadorcpf()

W = Validador("14.147.159/0001-10")
W.validadorcnpj()

