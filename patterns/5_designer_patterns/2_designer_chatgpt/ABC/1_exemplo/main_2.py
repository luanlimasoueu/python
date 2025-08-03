from animal import Animal

class Dog(Animal):
    def speak(self):
        return "Woof Woof"


dog = Dog()
print(dog.speak())


print(dog.jump())


