class Pig:

    def __init__(self, food):
        self._food = food


    def eat(self):
        print(self._food)

    def wallow(self):
        print("Chafurdando")

pig = Pig( "Milho")

pig.eat()

pig.wallow()