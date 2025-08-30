from abc import ABC, abstractmethod

# ----------------------------
# Classe Abstrata (Template)
# ----------------------------
class BebidaQuente(ABC):
    def preparar(self):
        """Método Template que define o fluxo fixo"""
        self.ferver_agua()
        self.colocar_ingrediente()
        self.servir()
        self.adicionar_extras()

    def ferver_agua(self):
        print("Fervendo a água...")

    def servir(self):
        print("Servindo na xícara...")

    @abstractmethod
    def colocar_ingrediente(self):
        pass

    # Hook (opcional - pode ser sobrescrito ou não)
    def adicionar_extras(self):
        pass


# ----------------------------
# Subclasses concretas
# ----------------------------
class Cafe(BebidaQuente):
    def colocar_ingrediente(self):
        print("Colocando pó de café no filtro...")

    def adicionar_extras(self):
        print("Adicionando açúcar e leite.")


class Cha(BebidaQuente):
    def colocar_ingrediente(self):
        print("Colocando o saquinho de chá...")

    def adicionar_extras(self):
        print("Adicionando mel.")


# ----------------------------
# Exemplo de uso
# ----------------------------
if __name__ == "__main__":
    print("== Preparando Café ==")
    bebida = Cafe()
    bebida.preparar()

    print("\n== Preparando Chá ==")
    bebida = Cha()
    bebida.preparar()
