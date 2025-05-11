class Projetil(object):
    def __init__(self, alcance, tempo):
        self.alcance = alcance
        self.tempo = tempo

    # Calcula a velocidade
    def getv(self):
        return self.alcance / self.tempo
    # Calcula o tempo
    def setv(self, v):
        self.tempo = self.alcance / v
        # Define a propriedade
    velocidade = property(getv, setv)

moab = Projetil(alcance=10000, tempo=60)
print (moab.velocidade)
# Muda a velocidade
moab.velocidade = 350
print (moab.tempo)
