from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p1 = Person("Luiz", 25)
print(p1)  # Person(name='Luan', age=25)

