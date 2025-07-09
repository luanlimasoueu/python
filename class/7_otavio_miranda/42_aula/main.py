from  classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
carrinho.inserir_produto(p1)

p2 = Produto('Iphone', 10000)

carrinho.inserir_produto(p2)

p1 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)

carrinho.lista_produto()