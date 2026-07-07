# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy

import os
import shutil

DISK = 'D:\\'
# HOME = os.path.expanduser('D:\\')
# DESTKOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGEM = os.path.join(DISK, 'estudos_em_pyrthon', 'aulas', 'modulo_4', 'conteudo_para_teste')
# NOVA_PASTA = os.path.join(DISK, 'estudos_em_pyrthon', 'aulas', 'modulo_4', 'conteudo_teste_2')
NOVA_PASTA = os.path.join(DISK, 'estudos_em_pyrthon', 'aulas', 'modulo_4', 'conteudo_teste')
# OBS: Quando já esxite uma pasta do mesmo nome, ele não duplica a pasta, apenas copia os arquivos para dentro dela.

# print(DISK, PASTA_ORIGEM, NOVA_PASTA)

os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGEM):
    for diretorio in dirs:
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGEM, NOVA_PASTA), diretorio
        )
        os.makedirs(caminho_novo_diretorio, exist_ok=True)

    for file in files:
       caminho_original = os.path.join(root, file)
       caminho_novo_arquivo = os.path.join(
           root.replace(PASTA_ORIGEM, NOVA_PASTA), file
        )
       shutil.copy(caminho_original, caminho_novo_arquivo)