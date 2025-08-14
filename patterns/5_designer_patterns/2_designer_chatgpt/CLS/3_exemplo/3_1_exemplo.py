class Pessoa:
    especie = "humano"

    @classmethod
    def mostrar_especie(cls):
        print(cls.especie)

Pessoa.mostrar_especie()  # humano
