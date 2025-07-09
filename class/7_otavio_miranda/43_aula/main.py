from classes import Cliente, Endereco

cliente1 = Cliente('Luiz', 32)
cliente1.inserir_endereco('Belo Horizonte', 'MG')
print( cliente1.nome)
cliente1.lista_enderecos()
print()