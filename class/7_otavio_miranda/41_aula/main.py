from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
print( escritor.nome)
print(caneta.marca)
maquina.escrever()
#print(caneta.marca)
#print(caneta.escrever())

print()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
