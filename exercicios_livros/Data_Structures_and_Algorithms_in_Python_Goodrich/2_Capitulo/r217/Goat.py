class Goat:

    def __init__(self, tail):
        self._tail = tail

    def milk(self):
        print("Milk")

    def jump(self):
        print("Jump")


goat = Goat(True)

goat.milk()

goat.jump()