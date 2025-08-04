class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Criando nova instância Singleton")
            cls._instance = super(Singleton, cls).__new__(cls)
        else:
            print("Usando instância existente")
        return cls._instance

    def __init__(self):
        self.valor = 42

def main():
    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2)  # True
    print(s1.valor, s2.valor)
    s2.valor = 99
    print(s1.valor)  # 99 pois é a mesma instância
    print(s1 is s2) 

if __name__ == "__main__":
    main()
