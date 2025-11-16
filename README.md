1. Pré-requisitos (O que você precisa ter)
Python instalado no computador.
Google Chrome instalado (o navegador).
A pasta do nosso projeto (com todos os arquivos e subpastas: automacao, funcoes, main.py, etc.).

2. Configuração (O que fazer uma única vez)
Abra o Terminal na Pasta do Projeto: Abra o seu terminal (Prompt de Comando, PowerShell, ou VS Code) e navegue até a pasta principal do nosso projeto.
(Opcional, mas Recomendado) Crie um Ambiente Virtual: Isso isola as bibliotecas do nosso projeto.
E depois ative-o:
Instale as Dependências: Este é o passo mais importante. Temos um arquivo, o requirements.txt, que é a "lista de compras" de todas as bibliotecas que o nosso robô precisa (Pandas, Selenium, etc.). O comando abaixo lê essa lista e instala tudo de uma vez.
E é só isso! Você não precisa de baixar o chromedriver.exe manualmente, pois o nosso código agora usa o webdriver-manager para fazer isso automaticamente.

3. Execução (O que fazer sempre que quiser usar)
Execute o Arquivo Principal: Com o terminal ainda na pasta do projeto (e com o ambiente virtual ativado, se você o criou), execute o main.py:
Selecione a Planilha:
Uma janela do explorador de arquivos irá aparecer.
Selecione a planilha .xlsx que contém os dados que você quer preencher.
Assista à Automação:
O robô irá copiar e renomear o arquivo selecionado para a pasta dados (para o seu controlo).
O Google Chrome abrirá automaticamente.
O robô começará a preencher o formulário, linha por linha, até terminar.
