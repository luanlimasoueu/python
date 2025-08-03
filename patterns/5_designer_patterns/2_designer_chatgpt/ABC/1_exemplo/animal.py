from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def jump(self):
        return f"{self.__class__.__name__} is jumping"