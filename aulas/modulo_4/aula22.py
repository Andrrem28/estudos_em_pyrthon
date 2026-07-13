import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
# Nome de exemplo, caso queira testar este trech de código, alterar para os que sejam iguais ao que estejam em sua máquina
# então, crie os seus arquivos com extensão zip e altere cada nome referente ao que esteja no seu local.
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'diretorio_do_arquivo_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'nome_arquivo_zip.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'nome_arquivo_zip_descompacatado'

shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
# Por medidas de segurança, esta linha se encontra comentada. Então, entenda o que o trecho de código faz, para poder descomentar depois.
# Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# raise Exception()

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)

def criar_arquivos(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = 'arquivo_%s' % i
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)


criar_arquivos(10, CAMINHO_ZIP_DIR)

# Cria o arquivo zip e adiciona arquivos
with ZipFile(CAMINHO_COMPACTADO, 'w') as w_zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            w_zip.write(os.path.join(root, file), file)

# Lendo um arquivo zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as r_zip:
    for arquivo in r_zip.namelist():
        print(arquivo)

# Extraindo o conteúdo de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as e_zip:
    for arquivo in e_zip.namelist():
        e_zip.extractall(CAMINHO_DESCOMPACTADO)
