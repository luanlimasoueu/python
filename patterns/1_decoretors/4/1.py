class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and valor:
            self._nome = valor
        else:
            raise ValueError("Nome deve ser uma string não vazia.")

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if isinstance(valor, int) and valor >= 0:
            self._idade = valor
        else:
            raise ValueError("Idade deve ser um número inteiro positivo.")

# Usando a nossa classe
pessoa = Pessoa("Ana", 30)
print(pessoa.nome)  # Output: Ana
pessoa.nome = "Maria"
print(pessoa.nome)  # Output: Maria

try:
    pessoa.idade = -5
except ValueError as e:
    print(e)  # Output: Idade deve ser um número inteiro positivo.