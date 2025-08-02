class Transporte:
    def entregar(self):
        raise NotImplementedError("Subclasse deve implementar este método.")

class Caminhao(Transporte):
    def entregar(self):
        return "Entrega realizada por caminhão."

class Navio(Transporte):
    def entregar(self):
        return "Entrega realizada por navio."

class Aviao(Transporte):
    def entregar(self):
        return "Entrega realizada por avião."


class TransporteFactory:
    def criar_transporte(self, tipo):
        if tipo == "caminhao":
            return Caminhao()
        elif tipo == "navio":
            return Navio()
        elif tipo == "aviao":
            return Aviao()
        else:
            raise ValueError(f"Tipo de transporte desconhecido: {tipo}")


# Cliente
factory = TransporteFactory()

for tipo in ["caminhao", "navio", "aviao"]:
    transporte = factory.criar_transporte(tipo)
    print(transporte.entregar())

