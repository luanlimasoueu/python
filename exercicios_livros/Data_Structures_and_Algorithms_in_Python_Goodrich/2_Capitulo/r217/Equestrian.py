from Horse import Horse

class Equestrian(Horse):

    def __init__(self,  _height, weight):
        super().__init__( _height)
        self._weight =  weight

    def peso(self):
        print(self._weight)

eques =Equestrian(12, 23)

eques.peso()
eques.altura()
eques.jump()