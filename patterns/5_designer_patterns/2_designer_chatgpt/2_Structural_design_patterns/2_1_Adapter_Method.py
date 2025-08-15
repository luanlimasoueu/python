# Classe existente (alvo esperado)
class Tomada3Pinos:
    def conectar(self):
        print("🔌 Conectado na tomada de 3 pinos")


# Classe incompatível que queremos usar
class Tomada2Pinos:
    def ligar(self):
        print("🔌 Conectado na tomada de 2 pinos")


# Adapter que faz a Tomada2Pinos funcionar como Tomada3Pinos
class AdaptadorTomada(Tomada3Pinos):
    def __init__(self, tomada2):
        self.tomada2 = tomada2

    def conectar(self):
        # Adapta o método "ligar" para o esperado "conectar"
        print("🛠 Usando adaptador...")
        self.tomada2.ligar()


# Código cliente
if __name__ == "__main__":
    # Sem adaptador
    t3 = Tomada3Pinos()
    t3.conectar()

    # Com adaptador
    t2 = Tomada2Pinos()
    adaptador = AdaptadorTomada(t2)
    adaptador.conectar()

