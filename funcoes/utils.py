import sys
import os
import shutil
import tkinter
from tkinter import filedialog
from datetime import datetime


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def selecionar_arquivo_excel():
    print("Aguardando a seleção do arquivo Excel...")
    root = tkinter.Tk()
    root.withdraw()
    tipos_de_arquivo = [("Planilhas Excel", "*.xlsx"), ("Todos os arquivos", "*.*")]
    caminho_do_arquivo = filedialog.askopenfilename(
        title="Selecione a planilha de dados",
        initialdir="dados/",
        filetypes=tipos_de_arquivo,
    )
    return caminho_do_arquivo

def copiar_arquivo_para_dados(caminho_original: str):
    if not caminho_original:
        return None

    try:
        pasta_destino = "dados"
        os.makedirs(pasta_destino, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        novo_nome_arquivo = f"dados_processados_{timestamp}.xlsx"

        caminho_destino_completo = os.path.join(pasta_destino, novo_nome_arquivo)

        shutil.copy(caminho_original, caminho_destino_completo)

        nome_arquivo_original = os.path.basename(caminho_original)

        print(
            f"Arquivo '{nome_arquivo_original}' copiado e renomeado para '{novo_nome_arquivo}' na pasta '{pasta_destino}'."
        )

        return caminho_destino_completo

    except Exception as e:
        print(f"Ocorreu um erro ao tentar copiar e renomear o arquivo: {e}")
        return None
