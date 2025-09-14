from dataclasses import dataclass, field

@dataclass
class Order:
    product: str
    quantity: int
    total: float = field(init=False)

    def __post_init__(self):
        self.total = self.quantity * 10.0


t = Order("Carro", 1)
print(t.total)