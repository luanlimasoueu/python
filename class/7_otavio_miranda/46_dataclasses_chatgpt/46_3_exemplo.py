from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float = 0.0  # valor padrão

p1 = Product(1, "Caneta")
p2 = Product(1, "Caneta")
print(p1 == p2)  # True


