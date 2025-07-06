class Retangulo:
    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, valor):
        if valor > 0:
            self._largura = valor
        else:
            raise ValueError("Largura deve ser positiva.")

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self._altura = valor
        else:
            raise ValueError("Altura deve ser positiva.")

    @property
    def area(self):
        return self._largura * self._altura

retangulo = Retangulo(4, 5)
print(retangulo.area) # Output: 20