# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os 
from itertools import count

caminho = os.path.join('D:\\','estudos_em_pyrthon', 'aulas', 'modulo_4')
counter = count()
for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, root)

    # for diretorio in dirs:
    #     print(' ', the_counter, 'Dir', diretorio )

    for file in files:
        print(' ', the_counter, 'File', file)
        caminho_completo = os.path.join(root, file)
        print(' ', the_counter, 'Caminho completo', caminho_completo)
        # os.unlink(caminho_completo) # Deleta o arquivo (não rode essa linha sem querer)
