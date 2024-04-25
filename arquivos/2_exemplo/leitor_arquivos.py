from os import listdir
import os
import pandas as pd
from pathlib import Path

caminho = './leitor'

caminho_pastas = os.listdir(caminho)
 
for pastas in caminho_pastas:

    caminho_pastas = os.path.join(caminho, pastas)
    pastas_nivel_1 = os.listdir(caminho_pastas)
 
    for pastas_n1 in pastas_nivel_1:

        local_arquivos = os.path.join(caminho_pastas, pastas_n1)
        lista_arq = listdir(local_arquivos)

        for arquivo in lista_arq:
            if arquivo.split(".")[-1] == 'csv':
                buscar_df_cte = os.path.join(local_arquivos, arquivo)
                dfcte = pd.read_csv(Path(buscar_df_cte ))
                print(dfcte)

      