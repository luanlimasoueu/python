from abc import ABC, abstractmethod

# ----------------------------
# Abstract Products
# ----------------------------
class Chair(ABC):
    @abstractmethod
    def sit(self):
        pass

class Sofa(ABC):
    @abstractmethod
    def lie_down(self):
        pass

# ----------------------------
# Concrete Products
# ----------------------------
class ModernChair(Chair):
    def sit(self):
        print("🪑 Sentando em uma cadeira moderna!")

class VictorianChair(Chair):
    def sit(self):
        print("🪑 Sentando em uma cadeira vitoriana elegante!")

class ModernSofa(Sofa):
    def lie_down(self):
        print("🛋️ Deitando em um sofá moderno minimalista!")

class VictorianSofa(Sofa):
    def lie_down(self):
        print("🛋️ Deitando em um sofá vitoriano luxuoso!")

# ----------------------------
# Abstract Factory
# ----------------------------
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

# ----------------------------
# Concrete Factories
# ----------------------------
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()
    
    def create_sofa(self) -> Sofa:
        return ModernSofa()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()
    
    def create_sofa(self) -> Sofa:
        return VictorianSofa()

# ----------------------------
# Client
# ----------------------------
def client_code(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()

    chair.sit()
    sofa.lie_down()

if __name__ == "__main__":
    print("🏢 Cliente pediu móveis modernos:")
    client_code(ModernFurnitureFactory())

    print("\n🏛️ Cliente pediu móveis vitorianos:")
    client_code(VictorianFurnitureFactory())
