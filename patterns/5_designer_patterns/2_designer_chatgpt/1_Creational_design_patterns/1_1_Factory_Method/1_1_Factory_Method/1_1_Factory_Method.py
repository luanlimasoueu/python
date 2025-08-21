from abc import ABC, abstractmethod

# ----------------------------
# Product Interface
# ----------------------------
class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

# ----------------------------
# Concrete Products
# ----------------------------
class MargheritaPizza(Pizza):
    def prepare(self):
        print("🍕 Preparando pizza Margherita!")

class PepperoniPizza(Pizza):
    def prepare(self):
        print("🍕 Preparando pizza Pepperoni!")

# ----------------------------
# Creator Interface
# ----------------------------
class PizzaFactory(ABC):
    @abstractmethod
    def create_pizza(self) -> Pizza:
        pass

# ----------------------------
# Concrete Creators
# ----------------------------
class MargheritaPizzaFactory(PizzaFactory):
    def create_pizza(self) -> Pizza:
        return MargheritaPizza()

class PepperoniPizzaFactory(PizzaFactory):
    def create_pizza(self) -> Pizza:
        return PepperoniPizza()

# ----------------------------
# Client
# ----------------------------
if __name__ == "__main__":
    # Cliente quer uma Margherita
    factory = MargheritaPizzaFactory()
    pizza = factory.create_pizza()
    pizza.prepare()  # 🍕 Preparando pizza Margherita!

    # Cliente quer uma Pepperoni
    factory = PepperoniPizzaFactory()
    pizza = factory.create_pizza()
    pizza.prepare()  # 🍕 Pre