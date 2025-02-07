import time

def calcular_imposto(faturamento):
    print( faturamento)

def calcular_bonus_funcionarios( vendas):
    for funcionario in vendas:
        venda = vendas[funcionario]
        print( funcionario, "Bônus", venda + 0.5)
        time.sleep(1)

def fechamento():
    vendas = {
        'LUIZ' : 1500,
        'JOÃO': 500,
        'AMANDA': 1400
    }
    faturamento = 1000
    calcular_bonus_funcionarios( vendas)
    calcular_imposto(faturamento)
    print( 'Finalizou')


fechamento()
