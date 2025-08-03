# animal.py

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def make_sound(self):
        pass

# animal.py 

class Bird(Animal):
    
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def make_sound(self):
        return "Chirp chirp!"
    
# animal.py

animals = [Bird("Tweety")]

for animal in animals:
    print(animal.get_name(), animal.make_sound())