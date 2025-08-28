from typing import Dict


# ===== Flyweight =====
class TreeType:
    def __init__(self, name: str, color: str, texture: str):
        self.name = name
        self.color = color
        self.texture = texture  # Estado intrínseco (compartilhado)

    def draw(self, x: int, y: int) -> None:
        # Estado extrínseco vem do cliente
        print(f"🌳 Desenhando '{self.name}' ({self.color}, {self.texture}) em ({x},{y})")


# ===== Flyweight Factory =====
class TreeFactory:
    _tree_types: Dict[str, TreeType] = {}

    @classmethod
    def get_tree_type(cls, name: str, color: str, texture: str) -> TreeType:
        key = (name, color, texture)
        if key not in cls._tree_types:
            print(f"✨ Criando novo tipo de árvore: {key}")
            cls._tree_types[key] = TreeType(name, color, texture)
        return cls._tree_types[key]


# ===== Client (usando Flyweight) =====
class Tree:
    def __init__(self, x: int, y: int, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        self.tree_type.draw(self.x, self.y)


# ===== Client Code =====
def main():
    forest = []

    # Criando várias árvores reutilizando tipos
    tree_type1 = TreeFactory.get_tree_type("Carvalho", "Verde", "Rugosa")
    tree_type2 = TreeFactory.get_tree_type("Pinheiro", "Verde Escuro", "Lisa")

    # Árvores em posições diferentes, mas compartilhando tipo
    forest.append(Tree(10, 20, tree_type1))
    forest.append(Tree(15, 25, tree_type1))  # Reusa o mesmo tipo
    forest.append(Tree(50, 60, tree_type2))

    for tree in forest:
        tree.draw()


if __name__ == "__main__":
    main()
