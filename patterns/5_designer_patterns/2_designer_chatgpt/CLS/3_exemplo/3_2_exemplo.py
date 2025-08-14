class Pessoa:
    especie = "Humano"  # Atributo da classe (usado com cls)

    def __init__(self, nome):
        self.nome = nome  # Atributo da instância (usado com self)

    def mostrar_nome(self):
        # Método de instância → usa self
        print(f"Meu nome é {self.nome}")

    @classmethod
    def mostrar_especie(cls):
        # Método de classe → usa cls
        print(f"Somos da espécie: {cls.especie}")

# Criar objetos
p1 = Pessoa("Alice")
p2 = Pessoa("Bob")

# Chamar métodos
p1.mostrar_nome()        # Meu nome é Alice
p2.mostrar_nome()        # Meu nome é Bob

# Método de classe
Pessoa.mostrar_especie() # Somos da espécie: Humano
