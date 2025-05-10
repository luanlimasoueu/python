class Terrestre(object):
    """
    Classe de veículos terrestres
    """
    se_move_em_terra = True
    def __init__(self, velocidade=100):
        """
        Inicializa o objeto
        """
        self.velocidade_em_terra = velocidade

class Aquatico(object):
    """
    Classe de veículos aquaticos
    """
    se_move_na_agua = True
    def __init__(self, velocidade=5):
        """
        Inicializa o objeto
        """
        self.velocidade_agua = velocidade

class Carro(Terrestre):
    """
    Classe de carros
    """
    rodas = 4
    def __init__(self, velocidade=120, pistoes=4):
        """ Inicializa o objeto
        """
        self.pistoes = pistoes
        Terrestre.__init__(self, velocidade=velocidade)

class Barco(Aquatico):
    """
    Classe de barcos
    """
    def __init__(self, velocidade=6, helices=1):
        """
        Inicializa o objeto
        """
        self.helices = helices
        Aquatico.__init__(self, velocidade=velocidade)

class Anfibio(Carro, Barco):
    """
    Classe de anfíbios
    """
    def __init__(self, velocidade_em_terra=80,
    velocidade_na_agua=4, pistoes=6, helices=2):
    """
    Inicializa o objeto
    """
# É preciso evocar o __init__ de cada classe pai
Carro.__init__(self, velocidade=velocidade_em_terra,
pistoes=pistoes)
Barco.__init__(self, velocidade=velocidade_na_agua,
helices=helices)
novo_anfibio = Anfibio()
for atr in dir(novo_anfibio):
# Se não for método especial:
if not atr.startswith('__'):
print atr, '=', getattr(novo_anfibio, atr)