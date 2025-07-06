class Forma:
    @property
    def tipo(self):
        return "Forma"

class Circulo(Forma):
    @property
    def tipo(self):
        return "Círculo"
    
    @staticmethod
    def tipo_1():
        print('Teste')

forma = Forma()
circulo = Circulo()
print(forma.tipo)  # Output: Forma
print(circulo.tipo)  # Output: Círculo
circulo.tipo_1()