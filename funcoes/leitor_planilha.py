import pandas as pd
from pandas import DataFrame
import tkinter
from tkinter import filedialog


def selecionar_arquivo_excel():
    print("Aguardando a seleção do arquivo Excel...")

    root = tkinter.Tk()
    root.withdraw()

    tipos_de_arquivo = [("Planilhas Excel", "*.xlsx"), ("Todos os arquivos", "*.*")]

    caminho_do_arquivo = filedialog.askopenfilename(
        title="Selecione a planilha de dados", filetypes=tipos_de_arquivo
    )

    return caminho_do_arquivo

def ler_dados_planilha(caminho_do_arquivo: str):
    try:
        print(f"Lendo dados do arquivo: {caminho_do_arquivo}")
        dataframe = pd.read_excel(caminho_do_arquivo)
        print("Dados lidos com sucesso!")
        return dataframe
    except Exception as e:
        print(f"Ocorreu um erro ao ler a planilha: {e}")
        return None

def imprimir_dados(dataframe: DataFrame):
    if dataframe is not None and not dataframe.empty:
        print("\n--- Exibindo Dados Carregados ---")
        print(dataframe.to_string())
        print("---------------------------------\n")
    else:
        print("\n[Aviso] Nenhum dado para exibir (DataFrame vazio ou nulo).\n")
