from abc import ABC, abstractmethod


# ===== Component =====
class Beverage(ABC):
    @abstractmethod
    def cost(self) -> float: ...
    @abstractmethod
    def description(self) -> str: ...


# ===== Concrete Component =====
class Espresso(Beverage):
    def cost(self) -> float:
        return 5.0
    def description(self) -> str:
        return "Espresso"


# ===== Decorator =====
class BeverageDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage


# ===== Concrete Decorators =====
class Milk(BeverageDecorator):
    def cost(self) -> float:
        return self._beverage.cost() + 1.5
    def description(self) -> str:
        return self._beverage.description() + ", Milk"


class WhippedCream(BeverageDecorator):
    def cost(self) -> float:
        return self._beverage.cost() + 2.0
    def description(self) -> str:
        return self._beverage.description() + ", Whipped Cream"


# ===== Client =====
def main():
    # Bebida simples
    order1 = Espresso()
    print(f"{order1.description()} -> ${order1.cost():.2f}")

    # Bebida decorada
    order2 = Milk(Espresso())
    print(f"{order2.description()} -> ${order2.cost():.2f}")

    # Bebida com múltiplos decoradores
    order3 = WhippedCream(Milk(Espresso()))
    print(f"{order3.description()} -> ${order3.cost():.2f}")


if __name__ == "__main__":
    main()
