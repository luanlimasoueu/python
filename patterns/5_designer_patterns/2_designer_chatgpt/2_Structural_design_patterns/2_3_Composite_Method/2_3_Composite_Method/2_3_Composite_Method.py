from abc import ABC, abstractmethod
from typing import List


# ===== Component =====
class EmployeeComponent(ABC):
    @abstractmethod
    def show_details(self, indent: int = 0) -> None:
        ...


# ===== Leaf =====
class Employee(EmployeeComponent):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def show_details(self, indent: int = 0) -> None:
        print(" " * indent + f"👤 {self.name} - {self.role}")


# ===== Composite =====
class Department(EmployeeComponent):
    def __init__(self, name: str):
        self.name = name
        self.members: List[EmployeeComponent] = []

    def add(self, component: EmployeeComponent) -> None:
        self.members.append(component)

    def show_details(self, indent: int = 0) -> None:
        print(" " * indent + f"🏢 Departamento: {self.name}")
        for member in self.members:
            member.show_details(indent + 2)


# ===== Client =====
def main():
    # Funcionários (Leaf)
    emp1 = Employee("Alice", "Analista de Dados")
    emp2 = Employee("Bob", "Desenvolvedor Backend")
    emp3 = Employee("Carla", "Designer UI/UX")

    # Departamentos (Composite)
    depto_ti = Department("Tecnologia")
    depto_ti.add(emp1)
    depto_ti.add(emp2)

    depto_design = Department("Design")
    depto_design.add(emp3)

    empresa = Department("Empresa")
    empresa.add(depto_ti)
    empresa.add(depto_design)

    # Mostrar hierarquia
    empresa.show_details()


if __name__ == "__main__":
    main()
