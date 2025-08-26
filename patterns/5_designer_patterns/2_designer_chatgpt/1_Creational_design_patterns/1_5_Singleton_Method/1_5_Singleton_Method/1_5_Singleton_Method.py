class Singleton:
    _instance = None  # atributo estático (único para a classe)

    def __new__(cls):
        if cls._instance is None:
            # cria só a primeira vez
            cls._instance = super(Singleton, cls).__new__(cls)
            print("🔑 Criando a única instância do Singleton")
        return cls._instance

    def operation(self):
        print("Executando uma operação do Singleton")


# -------- Exemplo de uso ----------
if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print("s1 é s2?", s1 is s2)  # True -> mesma instância
    s1.operation()
