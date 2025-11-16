from funcoes.utils import copiar_arquivo_para_dados, selecionar_arquivo_excel
from funcoes.leitor_planilha import ler_dados_planilha, imprimir_dados
from funcoes.acoes_navegador import (
    abrir_navegador_e_site,
    clicar_botao_start,
    preencher_primeiro_nome,
    preencher_ultimo_nome,
    preencher_nome_empresa,
    preencher_funcao,
    preencher_endereco,
    preencher_email,
    preencher_telefone,
    clicar_submit,
)
import time


def main():
    print("--- INÍCIO DA AUTOMAÇÃO COMPLETA DO DESAFIO ---")
    caminho_original_planilha = selecionar_arquivo_excel()

    if not caminho_original_planilha:
        print("Nenhum arquivo selecionado. Encerrando o programa.")
    else:
        caminho_final_planilha = copiar_arquivo_para_dados(caminho_original_planilha)

        if not caminho_final_planilha:
            print(
                "ERRO: Falha ao copiar o arquivo para a pasta de dados. O programa será encerrado."
            )
        else:
            dados = ler_dados_planilha(caminho_final_planilha)

            if dados is not None:
                dados.columns = dados.columns.str.strip()
                imprimir_dados(dados)

                navegador = abrir_navegador_e_site("https://rpachallenge.com/")

                if navegador:
                    clicar_botao_start(navegador)
                    
                    for indice, linha in dados.iterrows():
                        print(f"\n--- Preenchendo dados da linha {indice + 1} ---")
                        preencher_primeiro_nome(navegador, linha["First Name"])
                        preencher_ultimo_nome(navegador, linha["Last Name"])
                        preencher_nome_empresa(navegador, linha["Company Name"])
                        preencher_funcao(navegador, linha["Role in Company"])
                        preencher_endereco(navegador, linha["Address"])
                        preencher_email(navegador, linha["Email"])
                        preencher_telefone(navegador, linha["Phone Number"])

                        clicar_submit(navegador)
                        time.sleep(0.5)

                    print("\n--- DESAFIO CONCLUÍDO COM SUCESSO! ---")
                    print("O navegador será fechado em 10 segundos...")
                    time.sleep(10)
                    navegador.quit()
                    print("Navegador fechado.")
            else:
                print("ERRO: Falha ao carregar dados. O programa será encerrado.")

    print("\n--- FIM DO PROGRAMA ---")
