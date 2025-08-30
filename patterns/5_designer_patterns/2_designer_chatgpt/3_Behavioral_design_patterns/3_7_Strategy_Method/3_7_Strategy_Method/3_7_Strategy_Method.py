from abc import ABC, abstractmethod

# ----------------------------
# Strategy Interface
# ----------------------------
class FreteStrategy(ABC):
    @abstractmethod
    def calcular(self, distancia):
        pass


# ----------------------------
# Concrete Strategies
# ----------------------------
class CorreiosStrategy(FreteStrategy):
    def calcular(self, distancia):
        return distancia * 1.20  # R$1,20 por km


class TransportadoraStrategy(FreteStrategy):
    def calcular(self, distancia):
        return distancia * 0.90 + 15  # taxa fixa + km


class MotoboyStrategy(FreteStrategy):
    def calcular(self, distancia):
        return distancia * 2.00  # mais caro, mas mais rápido


# ----------------------------
# Context
# ----------------------------
class FreteCalculator:
    def __init__(self, strategy: FreteStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: FreteStrategy):
        self._strategy = strategy

    def calcular_frete(self, distancia):
        return self._strategy.calcular(distancia)


# ----------------------------
# Exemplo de uso
# ----------------------------
if __name__ == "__main__":
    distancia = 10  # km

    # Cliente pode trocar estratégia a qualquer momento
    frete = FreteCalculator(CorreiosStrategy())
    print("Correios:", frete.calcular_frete(distancia))

    frete.set_strategy(TransportadoraStrategy())
    print("Transportadora:", frete.calcular_frete(distancia))

    frete.set_strategy(MotoboyStrategy())
    print("Motoboy:", frete.calcular_frete(distancia))
