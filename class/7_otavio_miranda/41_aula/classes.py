class Escritor :
    def __init__( self, nome):
        self.__nome = nome
        self.__ferramenta

    @property
    def nome(self):
        return self.__nome

class Caneta:

    def __init__( self, marca):
        self.__marca = marca

    @property
    def marca (self):
        return self.__marca
    
class MaquinaDeEscrever:
    pass
