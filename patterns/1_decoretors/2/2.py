class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    @property
    def area(self):
        return self.largura * self.altura

retangulo = Retangulo(5, 3)
print(retangulo.area)  # Saída: 15
