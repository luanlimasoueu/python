class Retangulo:
    def __init__(self, largura, altura):
        self._largura = largura
        self.altura = altura
    
    @property
    def largura(self):
        return self._largura
    
    @largura.setter
    def largura(self, nova_largura):
        if nova_largura > 0:
            self._largura = nova_largura
        else:
            raise ValueError("A largura deve ser maior que 0.")
    
    @property
    def area(self):
        return self.largura * self.altura
    
retangulo = Retangulo(5, 3)
print(retangulo.largura)  # Saída: 5

retangulo.largura = 7
print(retangulo.largura)  # Saída: 7

retangulo.largura = -1  # Lança uma exceção ValueError
