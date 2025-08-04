class Sanduiche:
    def __init__(self):
        self.pao = None
        self.carne = None
        self.saladas = []
        self.molhos = []

    def __str__(self):
        return (
            f"Pão: {self.pao}\n"
            f"Carne: {self.carne}\n"
            f"Saladas: {', '.join(self.saladas)}\n"
            f"Molhos: {', '.join(self.molhos)}"
        )

from abc import ABC, abstractmethod

class SanduicheBuilder(ABC):
    def __init__(self):
        self.sanduiche = Sanduiche()

    @abstractmethod
    def escolher_pao(self):
        pass

    @abstractmethod
    def escolher_carne(self):
        pass

    @abstractmethod
    def adicionar_saladas(self):
        pass

    @abstractmethod
    def adicionar_molhos(self):
        pass

    def get_sanduiche(self):
        return self.sanduiche

class SanduicheSimplesBuilder(SanduicheBuilder):
    def escolher_pao(self):
        self.sanduiche.pao = "Pão francês"

    def escolher_carne(self):
        self.sanduiche.carne = "Frango grelhado"

    def adicionar_saladas(self):
        self.sanduiche.saladas = ["Alface", "Tomate"]

    def adicionar_molhos(self):
        self.sanduiche.molhos = ["Maionese"]

class SanduicheVeganoBuilder(SanduicheBuilder):
    def escolher_pao(self):
        self.sanduiche.pao = "Pão integral"

    def escolher_carne(self):
        self.sanduiche.carne = "Tofu grelhado"

    def adicionar_saladas(self):
        self.sanduiche.saladas = ["Alface", "Cenoura", "Tomate"]

    def adicionar_molhos(self):
        self.sanduiche.molhos = ["Mostarda", "Molho tahine"]


class Cozinheiro:
    def construir_sanduiche(self, builder: SanduicheBuilder):
        builder.escolher_pao()
        builder.escolher_carne()
        builder.adicionar_saladas()
        builder.adicionar_molhos()
        return builder.get_sanduiche()

def main():
    builder = SanduicheVeganoBuilder()  # Ou SanduicheSimplesBuilder()
    cozinheiro = Cozinheiro()
    sanduiche = cozinheiro.construir_sanduiche(builder)
    print("Sanduíche pronto:")
    print(sanduiche)

if __name__ == "__main__":
    main()
