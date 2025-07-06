class Animal:
    def __init__(self, especie, idade):
        self._especie = especie
        self._idade = idade

    @property
    def especie(self):
        return self._especie

    @especie.setter
    def especie(self, valor):
        if isinstance(valor, str):
            self._especie = valor
        else:
            raise ValueError("Espécie deve ser uma string.")

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if isinstance(valor, int) and valor >= 0:
            self._idade = valor
        else:
            raise ValueError("Idade deve ser um número inteiro positivo.")

class Cachorro(Animal):
    def __init__(self, nome, especie, idade):
        super().__init__(especie, idade)
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str):
            self._nome = valor
        else:
            raise ValueError("Nome deve ser uma string.")

cachorro = Cachorro("Rex", "Canino", 5)
print(cachorro.nome) # Output: Rex
print(cachorro.especie) # Output: Rex
cachorro.nome = "Max"
print(cachorro.nome) # Output: Max