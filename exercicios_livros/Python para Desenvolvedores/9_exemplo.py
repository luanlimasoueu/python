# -*- coding: latin1 -*-
import time
def logger(cls):
    """
    Função decoradora de classes
    """
    class Logged(cls):
        """
        Classe derivada que mostra os parâmetros de inicialização
        """
        def __init__(self, *args, **kargs):
            print ('Hora:', time.asctime())
            print ('Classe:', repr(cls))
            print ('args:', args)
            print ('kargs:', kargs)
# Executa a inicialização da classe antiga
            cls.__init__(self, *args, **kargs)
# Retorna a nova classe
    return Logged

@logger
class Musica(object):
    def __init__(self, nome, artista, album):
        self.nome = nome
        self.artista = artista
        self.album = album
        
m = Musica('Hand of Doom', 'Black Sabbath', album='Paranoid')