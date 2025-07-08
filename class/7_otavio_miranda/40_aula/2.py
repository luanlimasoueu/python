class BaseDeDados :
    def __init__(self):
        self._dados = {}
    
    def inserir_clientes (self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id:nome}
        else:
            self._dados['clientes'].update({id:nome})

    def lista_clientes ( self, id):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)
    
    def apaga_cliente(self, id):
        del self._dados['clientes'][id]

bd =  BaseDeDados()
bd.inserir_clientes(1, 'Otávio')
bd.inserir_clientes(2, 'Miranda')
print(bd._dados)