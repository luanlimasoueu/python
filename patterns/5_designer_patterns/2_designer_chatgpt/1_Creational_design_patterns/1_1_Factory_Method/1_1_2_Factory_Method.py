class Entrega:
    def realizar_entrega(self, pedido_id):
        raise NotImplementedError("Subclasse deve implementar este método.")

class EntregaPorBicicleta(Entrega):
    def realizar_entrega(self, pedido_id):
        return f"Pedido {pedido_id} será entregue por bicicleta em até 1h."

class EntregaPorMoto(Entrega):
    def realizar_entrega(self, pedido_id):
        return f"Pedido {pedido_id} será entregue por moto em até 30min."

class EntregaPorCaminhao(Entrega):
    def realizar_entrega(self, pedido_id):
        return f"Pedido {pedido_id} será entregue por caminhão em até 24h."

class ServicoEntrega:
    def criar_entrega(self) -> Entrega:
        raise NotImplementedError("Subclasse deve implementar este método.")

    def processar_pedido(self, pedido_id):
        entrega = self.criar_entrega()
        resultado = entrega.realizar_entrega(pedido_id)
        print(resultado)


class ServicoEntregaBicicleta(ServicoEntrega):
    def criar_entrega(self):
        return EntregaPorBicicleta()

class ServicoEntregaMoto(ServicoEntrega):
    def criar_entrega(self):
        return EntregaPorMoto()

class ServicoEntregaCaminhao(ServicoEntrega):
    def criar_entrega(self):
        return EntregaPorCaminhao()

def executar_pedido(tipo_entrega, pedido_id):
    if tipo_entrega == "bicicleta":
        servico = ServicoEntregaBicicleta()
    elif tipo_entrega == "moto":
        servico = ServicoEntregaMoto()
    elif tipo_entrega == "caminhao":
        servico = ServicoEntregaCaminhao()
    else:
        raise ValueError("Tipo de entrega inválido!")

    servico.processar_pedido(pedido_id)

# Testando:
executar_pedido("moto", 101)
executar_pedido("caminhao", 102)
executar_pedido("bicicleta", 103)

