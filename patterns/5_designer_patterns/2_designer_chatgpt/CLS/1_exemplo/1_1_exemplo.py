class MinhaClasse:
    valor_da_classe = 10

    @classmethod
    def metodo_de_classe(cls, argumento):
        print(f"Valor da classe: {cls.valor_da_classe}")
        print(f"Argumento recebido: {argumento}")
        return cls.valor_da_classe + argumento

instancia = MinhaClasse()
resultado = MinhaClasse.metodo_de_classe(5)
print(f"Resultado: {resultado}")