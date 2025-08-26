import copy

# Classe que será clonada
class Biscoito:
    def __init__(self, formato, cobertura):
        self.formato = formato
        self.cobertura = cobertura

    # Método de clonagem
    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Biscoito {self.formato} com cobertura de {self.cobertura}"


# Exemplo de uso
if __name__ == "__main__":
    # Criamos um biscoito modelo (protótipo)
    biscoito_estrela = Biscoito("estrela", "chocolate")

    # Clonamos para fazer vários iguais
    copia1 = biscoito_estrela.clone()
    copia2 = biscoito_estrela.clone()

    # Personalizamos alguns clones
    copia2.cobertura = "morango"

    print("Protótipo:", biscoito_estrela)
    print("Clone 1 :", copia1)
    print("Clone 2 :", copia2)
