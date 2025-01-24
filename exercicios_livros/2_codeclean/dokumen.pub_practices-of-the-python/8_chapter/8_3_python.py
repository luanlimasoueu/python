class BigCat:
    def eats(self):
        return ['rodents']
class Lion(BigCat):
    def eats(self):
        return ['wildebeest']
class Tiger(BigCat):
    def eats(self):
        return ['water buffalo']
class Liger(Lion, Tiger):
    def eats(self):
        return super().eats() + ['rabbit', 'cow', 'pig', 'chicken']
if __name__ == '__main__':
    lion = Lion()
    print('The lion eats', lion.eats())
    tiger = Tiger()
    print('The tiger eats', tiger.eats())
    liger = Liger()
    print('The liger eats', liger.eats())