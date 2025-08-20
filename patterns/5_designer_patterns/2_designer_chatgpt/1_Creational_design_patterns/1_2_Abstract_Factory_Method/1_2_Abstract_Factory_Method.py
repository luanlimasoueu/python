# Produtos abstratos
class Botao:
    def desenhar(self):
        raise NotImplementedError

class CaixaTexto:
    def desenhar(self):
        raise NotImplementedError

# Produtos concretos - Windows
class BotaoWindows(Botao):
    def desenhar(self):
        return "Botão estilo Windows"

class CaixaTextoWindows(CaixaTexto):
    def desenhar(self):
        return "Caixa de texto estilo Windows"

# Produtos concretos - Mac
class BotaoMac(Botao):
    def desenhar(self):
        return "Botão estilo Mac"

class CaixaTextoMac(CaixaTexto):
    def desenhar(self):
        return "Caixa de texto estilo Mac"

# Fábrica abstrata
class UIFactory:
    def criar_botao(self) -> Botao:
        raise NotImplementedError

    def criar_caixa_texto(self) -> CaixaTexto:
        raise NotImplementedError

# Fábricas concretas
class WindowsFactory(UIFactory):
    def criar_botao(self):
        return BotaoWindows()

    def criar_caixa_texto(self):
        return CaixaTextoWindows()

class MacFactory(UIFactory):
    def criar_botao(self):
        return BotaoMac()

    def criar_caixa_texto(self):
        return CaixaTextoMac()

# Código cliente
def renderizar_ui(factory: UIFactory):
    botao = factory.criar_botao()
    caixa = factory.criar_caixa_texto()
    print(botao.desenhar())
    print(caixa.desenhar())

# Escolha da fábrica com base no sistema
sistema = input("Qual sistema? (windows/mac): ").lower()

if sistema == "windows":
    factory = WindowsFactory()
elif sistema == "mac":
    factory = MacFactory()
else:
    raise ValueError("Sistema inválido!")

# Executa a interface
renderizar_ui(factory)
