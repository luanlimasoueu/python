import time
import asyncio

async def calcular_imposto(faturamento):
    print( faturamento * 0.1)

async def calcular_bonus_funcionarios( vendas):
    for funcionario in vendas:
        venda = vendas[funcionario]
        print( funcionario, "Bônus", venda * 0.05)
        time.sleep(1)

async def fechamento():
    vendas = {
        'LUIZ' : 1500,
        'JOÃO': 500,
        'AMANDA': 1400
    }
    faturamento = 1000
    tarefa_1 = asyncio.create_task( calcular_bonus_funcionarios( vendas) )
    tarefa_2 = asyncio.create_task( calcular_imposto(faturamento) )
    print( 'Finalizou')


asyncio.run( fechamento() )

