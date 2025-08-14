class MethodTypes:

    name = "Ragnar"

    def instanceMethod(self):
        # Creates an instance atribute through keyword self
        self.lastname = "Lothbrock"
        print(self.name)
        print(self.lastname)
        print()

    @classmethod
    def classMethod(cls):
        # Access a class atribute through keyword cls
        cls.name = "Lagertha"
        print(cls.name)
        print()

    @staticmethod
    def staticMethod():
        print("This is a static method")
        print()

# Creates an instance of the class
m = MethodTypes()
# Calls instance method
m.instanceMethod()


MethodTypes.classMethod()
MethodTypes.staticMethod()