class Botao:
    def desenhar(self):
        raise NotImplementedError

class CaixaTexto:
    def desenhar(self):
        raise NotImplementedError

class BotaoWindows(Botao):
    def desenhar(self):
        return "Botão estilo Windows"

class CaixaTextoWindows(CaixaTexto):
    def desenhar(self):
        return "Caixa de texto estilo Windows"

class BotaoMac(Botao):
    def desenhar(self):
        return "Botão estilo Mac"

class CaixaTextoMac(CaixaTexto):
    def desenhar(self):
        return "Caixa de texto estilo Mac"

class UIFactory:
    def criar_botao(self) -> Botao:
        raise NotImplementedError

    def criar_caixa_texto(self) -> CaixaTexto:
        raise NotImplementedError

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
def renderizar_ui(factory: UIFactory):
    botao = factory.criar_botao()
    caixa = factory.criar_caixa_texto()
    print(botao.desenhar())
    print(caixa.desenhar())
