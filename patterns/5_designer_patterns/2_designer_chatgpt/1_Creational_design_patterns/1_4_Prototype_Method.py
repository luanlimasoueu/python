from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class EnemyPrototype(Prototype):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Enemy(name={self.name}, health={self.health}, attack_power={self.attack_power})"

def client_code(prototype: Prototype):
    prototype_clone = prototype.clone()
    print("Cloned enemy:", prototype_clone)
    # Customizing the cloned enemy
    prototype_clone.health += 10
    prototype_clone.attack_power += 5
    print("Customized cloned enemy:", prototype_clone)

if __name__ == "__main__":
    # Creating a prototype for a basic enemy
    basic_enemy_prototype = EnemyPrototype("Goblin", 100, 15)
    print("Original enemy:", basic_enemy_prototype)
    
    # Using the prototype to create and customize new enemies
    client_code(basic_enemy_prototype)