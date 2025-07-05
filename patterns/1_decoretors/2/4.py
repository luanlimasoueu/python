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
    
    @largura.deleter
    def largura(self):
        del self._largura
    
    @property
    def area(self):
        return self.largura * self.altura
    
retangulo = Retangulo(5, 3)
print(retangulo.largura)  # Saída: 5

del retangulo.largura

print(retangulo.largura)    