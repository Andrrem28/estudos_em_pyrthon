# os.listdir para navegar em caminhos
# D:\estudos_em_pyrthon\aulas\modulo_4\aula8.py
# caminho = r"D:\estudos_em_pyrthon\aulas\modulo_4\aula8.py"

import os

caminho = os.path.join('D:\\','estudos_em_pyrthon', 'aulas', 'modulo_4')

print(caminho)

for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)

    if not os.path.isdir(pasta):
        continue

    for item in os.listdir(caminho_completo):
        print(item)

