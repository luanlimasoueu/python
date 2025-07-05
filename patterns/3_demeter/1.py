class Endereco:
    def __init__(self, rua):
        self.rua = rua

    def get_rua(self):
        return self.rua

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco

    def get_rua(self):
        # Aplica a Lei de Demeter: não expõe o objeto interno
        return self.endereco.get_rua()

# Uso
endereco = Endereco("Rua das Flores")
cliente = Cliente(endereco)

print(cliente.get_rua())  # Correto