from dataclasses import dataclass

@dataclass(order=True)
class Point:
    x: int
    y: int

p1 = Point(1, 5)
p2 = Point(2, 3)
print(p1 < p2)  # True (compara primeiro x, depois y)

