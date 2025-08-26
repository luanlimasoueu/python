# Target: interface esperada pelo cliente
class Target:
    def request(self):
        return "Requisição padrão de Target"


# Adaptee: possui uma interface diferente (incompatível com Target)
class Adaptee:
    def specific_request(self):
        return "Resposta especial do Adaptee"


# Adapter: traduz a interface do Adaptee para o Target
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        # Faz a ponte entre Client e Adaptee
        return f"Adapter traduz -> {self.adaptee.specific_request()}"


# -------- Exemplo de uso (Client) ----------
if __name__ == "__main__":
    client_target = Target()
    print("Cliente usa Target:", client_target.request())

    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    print("Cliente usa Adaptee via Adapter:", adapter.request())
