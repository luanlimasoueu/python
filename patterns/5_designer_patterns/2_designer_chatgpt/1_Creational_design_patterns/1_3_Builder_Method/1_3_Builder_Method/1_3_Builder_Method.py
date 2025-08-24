from abc import ABC, abstractmethod

# ----------------------------
# Produto
# ----------------------------
class Pizza:
    def __init__(self):
        self.parts = []

    def add(self, part: str):
        self.parts.append(part)

    def show(self):
        print("🍕 Pizza contém:", ", ".join(self.parts))


# ----------------------------
# Builder abstrato
# ----------------------------
class PizzaBuilder(ABC):
    @abstractmethod
    def add_base(self): pass

    @abstractmethod
    def add_sauce(self): pass

    @abstractmethod
    def add_topping(self): pass

    @abstractmethod
    def get_result(self) -> Pizza: pass


# ----------------------------
# Builders concretos
# ----------------------------
class VegPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def add_base(self):
        self.pizza.add("Massa Integral")

    def add_sauce(self):
        self.pizza.add("Molho de Tomate")

    def add_topping(self):
        self.pizza.add("Vegetais Frescos")

    def get_result(self):
        return self.pizza


class PepperoniPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def add_base(self):
        self.pizza.add("Massa Tradicional")

    def add_sauce(self):
        self.pizza.add("Molho de Tomate Especial")

    def add_topping(self):
        self.pizza.add("Queijo + Pepperoni")

    def get_result(self):
        return self.pizza


# ----------------------------
# Diretor
# ----------------------------
class Director:
    def construct(self, builder: PizzaBuilder):
        builder.add_base()
        builder.add_sauce()
        builder.add_topping()


# ----------------------------
# Cliente
# ----------------------------
if __name__ == "__main__":
    director = Director()

    print("🥦 Montando Pizza Vegetariana:")
    veg_builder = VegPizzaBuilder()
    director.construct(veg_builder)
    veg_pizza = veg_builder.get_result()
    veg_pizza.show()

    print("\n🍕 Montando Pizza de Pepperoni:")
    pep_builder = PepperoniPizzaBuilder()
    director.construct(pep_builder)
    pep_pizza = pep_builder.get_result()
    pep_pizza.show()
