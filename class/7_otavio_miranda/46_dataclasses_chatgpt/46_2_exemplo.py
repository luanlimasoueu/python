from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float = 0.0  # valor padrão

p = Product(1, "Caneta")
print(p)  # Product(id=1, name='Caneta', price=0.0)


