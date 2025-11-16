<style>
  .code-block {
    background-color: #f6f8fa; 
    padding: 15px;
    border-radius: 5px;
    font-family: monospace;
    overflow-x: auto;
  }
  .summary-title {
    font-size: 1.25em;
    font-weight: 600;
    padding: 8px 0px;
    cursor: pointer;
  }
</style>

<h2>🚀 Guia Rápido: Como Fazer o Robô Funcionar</h2>
<p>Siga os passos abaixo para configurar e executar o robô em qualquer computador com Windows.</p>

<details>
  <summary><span class="summary-title">🖥️ 1. Pré-requisitos (O que você precisa ter)</span></summary>
  <br>
  <ul style="list-style-type: disc; margin-left: 20px;">
    <li><strong>Python</strong> instalado no computador (versão 3.8+).</li>
    <li><strong>Google Chrome</strong> instalado e atualizado (o navegador).</li>
    <li>A <strong>pasta do projeto</strong> (com todos os arquivos e subpastas).</li>
  </ul>
</details>

<hr>

<details>
  <summary><span class="summary-title">⚙️ 2. Configuração (O que fazer uma única vez)</span></summary>
  <br>
  <div style="margin-left: 20px;">
    <h3>Passo 2.1: Abra o Terminal na Pasta do Projeto</h3>
    <p>Abra seu terminal (Prompt de Comando, PowerShell, etc.) e navegue até a pasta principal do projeto.</p>
    <div class="code-block">
      <pre><code># Exemplo:
cd D:\projetos\rpa_challenge</code></pre>
    </div>
    
    <h3>Passo 2.2: (Opcional, mas Recomendado) Crie um Ambiente Virtual</h3>
    <p>Isso isola as bibliotecas do nosso projeto e evita conflitos.</p>
    <div class="code-block">
      <pre><code>python -m venv venv
# No Windows, ative com:
venv\Scripts\activate</code></pre>
    </div>

    <h3>Passo 2.3: Instale as Dependências (Obrigatório)</h3>
    <p>Este comando instala todas as bibliotecas que o robô precisa (Pandas, Selenium, etc.) de uma só vez, lendo o arquivo <code>requirements.txt</code>.</p>
    <div class="code-block">
      <pre><code>pip install -r requirements.txt</code></pre>
    </div>
  </div>
</details>

<hr>

<details open> <summary><span class="summary-title">▶️ 3. Execução (Como usar o robô)</span></summary>
  <br>
  <div style="margin-left: 20px;">
    <h3>Passo 3.1: Execute o Programa</h3>
    <p>Com o terminal na pasta do projeto (e o ambiente virtual ativado, se você o criou), execute o arquivo <code>main.py</code>:</p>
    <div class="code-block">
      <pre><code>python main.py</code></pre>
    </div>

    <h3>Passo 3.2: Selecione a Planilha</h3>
    <p>Uma janela do explorador de arquivos irá aparecer. Selecione a planilha <code>.xlsx</code> que contém os dados que você quer processar.</p>

    <h3>Passo 3.3: Assista à Automação</h3>
    <p>Pronto! O robô irá copiar o arquivo selecionado, abrir o Google Chrome e começar a preencher o formulário automaticamente, linha por linha.</p>
  </div>
</details>
