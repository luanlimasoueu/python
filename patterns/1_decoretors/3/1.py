def decorator(f):
    def nova_funcao():
        print("Funcionalidade extra")
        f()
    return nova_funcao

@decorator
def funcao_inicial():
    print("Funcionalidade inicial")

funcao_inicial()