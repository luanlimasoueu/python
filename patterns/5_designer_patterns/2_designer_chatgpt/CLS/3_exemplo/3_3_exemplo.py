class Configuracao:
    _instancia = None  # Armazena a única instância (atributo de classe)

    def __new__(cls):
        if cls._instancia is None:
            print("🔧 Criando nova instância de Configuracao")
            cls._instancia = super().__new__(cls)
            cls._instancia.debug = False
            cls._instancia.tema = "claro"
        return cls._instancia

    def mostrar_config(self):
        print(f"🔍 Tema: {self.tema}, Debug: {self.debug}")


    # Primeira vez: instancia é criada
c1 = Configuracao()
c1.debug = True
c1.tema = "escuro"
c1.mostrar_config()  # 🔍 Tema: escuro, Debug: True

# Segunda vez: reutiliza a instância existente
c2 = Configuracao()
c2.mostrar_config()  # 🔍 Tema: escuro, Debug: True

# Verifica se são o mesmo objeto
print(c1 is c2)  # True
