from Horse import Horse

class Racer(Horse):

    def __init__(self, height):
        super().__init__( height)

    def race(self):
        print("A raça é Alazão")

Racer(123).race()
Racer(123).jump()