# projeto_marcelogsf.ip

Este projeto é uma aplicação web desenvolvida com Flask que oferece conteúdo educacional sobre programação, com foco em conceitos fundamentais como estruturas de seleção, repetição, vetores, funções e tratamento de erros. Inclui também um glossário de termos e uma seção "Sobre a Equipe". O projeto demonstra a integração com a API do Google Gemini para funcionalidades de inteligência artificial.

## a. Estrutura do Site e Conteúdo de Cada Seção

O site é organizado em várias seções, acessíveis através de rotas Flask:

* **`/` (Página Inicial)**: `index.html` - Aparentemente a página principal do site, servindo como ponto de entrada.
* **`/sobre-equipe`**: `sobre_equipe.html` - Informações sobre a equipe de desenvolvimento do projeto.
* **`/estruturas-selecao`**: `estruturas_selecao.html` - Conteúdo educacional sobre estruturas de seleção (condicionais).
* **`/estruturas-repeticao`**: `estruturas_repeticao.html` - Conteúdo educacional sobre estruturas de repetição (loops).
* **`/vetores-e-matrizes`**: `vetores_e_matrizes.html` - Conteúdo educacional sobre vetores e matrizes.
* **`/funcoes-e-procedimentos`**: `funcoes_e_procedimentos.html` - Conteúdo educacional sobre funções e procedimentos.
* **`/tratamentos-de-erros`**: `tratamentos_de_erros.html` - Conteúdo educacional sobre tratamento de erros.
* **`/glossario`**: `glossario.html` - Uma seção dedicada a um glossário de termos. Esta seção permite visualizar, adicionar, editar e deletar termos do glossário. Os dados do glossário são persistidos em um arquivo CSV (`bd_glossario.csv`).
    * **`/adicionar-termo`**: Rota para adicionar novos termos ao glossário (requisição POST).
    * **`/editar-termo/<int:termo_id>`**: Rota para renderizar o formulário de edição de um termo específico.
    * **`/salvar-edicao-termo/<int:termo_id>`**: Rota para salvar as edições de um termo (requisição POST).
    * **`/deletar-termo/<int:termo_id>`**: Rota para deletar um termo do glossário.
* **`/gerar-texto-com-ia`**: `gerar_texto_com_ia.html` - Uma seção onde o usuário pode interagir com a API do Gemini para gerar texto com base em um prompt.
    * **`/enviar-prompt`**: Rota para enviar o prompt à API do Gemini e exibir o resultado (requisição POST).

## b. As Tecnologias (linguagem de programação, bibliotecas, ...) Utilizadas

* **Linguagem de Programação**: Python
* **Framework Web**: Flask
* **Manipulação de CSV**: `csv` (módulo embutido do Python)
* **Manipulação de Variáveis de Ambiente/Sistema de Arquivos**: `os` (módulo embutido do Python)
* **Integração com IA**: Google Gemini API (através da biblioteca `google.generativeai`)
* **Frontend**: HTML (com templates Jinja2), CSS (não diretamente visível nos arquivos fornecidos, mas implícito na estrutura web).

## c. Como a Integração com a API do Gemini foi Implementada

A integração com a API do Google Gemini é realizada da seguinte forma:

1.  **Configuração da API Key**:
    A chave da API do Gemini é configurada usando `genai.configure(api_key=os.getenv("GEMINI_API_KEY", "SUA_CHAVE_PADRAO"))`. É altamente recomendado que a chave da API seja definida como uma variável de ambiente (`GEMINI_API_KEY`) para segurança. Uma chave padrão (que *não* deve ser usada em produção, mas sim para fins de desenvolvimento inicial) é fornecida no código.

2.  **Inicialização do Modelo**:
    O modelo generativo é inicializado com `model = genai.GenerativeModel('gemini-1.5-flash')`. O modelo `gemini-1.5-flash` é selecionado por seu bom equilíbrio entre desempenho e custo.

3.  **Endpoint de Geração de Texto**:
    * A rota `/gerar-texto-com-ia` renderiza um formulário (`gerar_texto_com_ia.html`) onde o usuário pode inserir um prompt.
    * Quando o formulário é submetido (via POST para `/enviar-prompt`), o prompt é capturado.
    * A função `model.generate_content(prompt)` é chamada para interagir com a API do Gemini.
    * A resposta gerada pela IA é então passada para o template `gerar_texto_com_ia.html` para ser exibida ao usuário.

## d. Como Executar a Aplicação Flask Localmente

Para executar a aplicação Flask em seu ambiente local, siga os passos abaixo:

1.  **Pré-requisitos**:
    * Python 3.x instalado.
    * `pip` (gerenciador de pacotes do Python).

2.  **Clone ou Baixe o Projeto**:
    Se você estiver usando um sistema de controle de versão como Git, clone o repositório:
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <NOME_DA_PASTA_DO_PROJETO>
    ```
    Caso contrário, baixe os arquivos do projeto e navegue até o diretório raiz.

3.  **Crie e Ative um Ambiente Virtual (Recomendado)**:
    É uma boa prática criar um ambiente virtual para isolar as dependências do projeto.
    ```bash
    python -m venv venv
    ```
    * No Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    * No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Instale as Dependências**:
    Instale as bibliotecas necessárias listadas no `app.py` (Flask, google-generativeai).
    ```bash
    pip install Flask google-generativeai
    ```

5.  **Configure a Chave da API do Gemini**:
    Crie um arquivo `.env` na raiz do seu projeto e adicione sua chave da API do Gemini:
    ```
    GEMINI_API_KEY="SUA_VERDADEIRA_CHAVE_DA_API_GEMINI"
    ```
    Ou defina-a diretamente no seu terminal (temporariamente para a sessão):
    * No Windows:
        ```bash
        set GEMINI_API_KEY="SUA_VERDADEIRA_CHAVE_DA_API_GEMINI"
        ```
    * No macOS/Linux:
        ```bash
        export GEMINI_API_KEY="SUA_VERDADEIRA_CHAVE_DA_API_GEMINI"
        ```
    **Substitua `"SUA_VERDADEIRA_CHAVE_DA_API_GEMINI"` pela sua chave de API real do Google Gemini.**

6.  **Execute a Aplicação**:
    Defina a variável de ambiente `FLASK_APP` e execute o Flask:
    ```bash
    export FLASK_APP=app.py # ou set FLASK_APP=app.py no Windows
    flask run
    ```

7.  **Acesse a Aplicação**:
    Abra seu navegador e acesse `http://127.0.0.1:5000/` ou o endereço indicado no terminal.

## e. Uma Breve Descrição das Principais Partes do Código Python (`app.py`)

O arquivo `app.py` é o coração da aplicação Flask. Abaixo estão suas principais partes:

* **Importações**:
    * `google.generativeai as genai`: Para interagir com a API do Google Gemini.
    * `Flask, render_template, url_for, request, redirect` do módulo `flask`: Componentes essenciais para construir a aplicação web.
    * `csv`: Para ler e escrever arquivos CSV (utilizado para o glossário).
    * `os`: Para interagir com o sistema operacional, como acessar variáveis de ambiente.

* **Configuração do Gemini API**:
    ```python
    genai.configure(api_key=os.getenv("GEMINI_API_KEY", "AIzaSyBwU44PFMN26PzjC7EeWOHQbwsOE3_0v9k"))
    model = genai.GenerativeModel('gemini-1.5-flash')
    ```
    Configura a API key e inicializa o modelo do Gemini.

* **Inicialização do Flask**:
    ```python
    app = Flask(__name__)
    ```
    Cria uma instância da aplicação Flask.

* **Rotas de Renderização de Templates (Conteúdo Estático)**:
    ```python
    @app.route('/')
    def ola():
        return render_template('index.html')

    @app.route('/sobre-equipe')
    def sobre_equipe():
        return render_template('sobre_equipe.html')
    # ... e outras rotas para estruturas-selecao, repeticao, etc.
    ```
    Estas funções simplesmente retornam templates HTML para exibir as páginas correspondentes.

* **Gerenciamento do Glossário (CSV)**:
    * **`/glossario`**:
        ```python
        @app.route('/glossario')
        def glossario():
            # ... lê bd_glossario.csv e renderiza glossario.html
        ```
        Lê os termos do glossário de `bd_glossario.csv` e os exibe.
    * **`/adicionar-termo`**:
        ```python
        @app.route('/adicionar-termo', methods=['POST'])
        def adicionar_termo():
            # ... adiciona termo ao bd_glossario.csv
        ```
        Processa requisições POST para adicionar novos termos.
    * **`/editar-termo/<int:termo_id>`**:
        ```python
        @app.route('/editar-termo/<int:termo_id>')
        def editar_termo(termo_id):
            # ... carrega termo específico para edição
        ```
        Exibe o formulário para editar um termo existente.
    * **`/salvar-edicao-termo/<int:termo_id>`**:
        ```python
        @app.route('/salvar-edicao-termo/<int:termo_id>', methods=['POST'])
        def salvar_edicao_termo(termo_id):
            # ... atualiza termo no bd_glossario.csv
        ```
        Processa a submissão do formulário de edição e atualiza o CSV.
    * **`/deletar-termo/<int:termo_id>`**:
        ```python
        @app.route('/deletar-termo/<int:termo_id>')
        def deletar_termo(termo_id):
            # ... remove termo do bd_glossario.csv
        ```
        Remove um termo do glossário.
    As funções de glossário interagem diretamente com `bd_glossario.csv` usando o módulo `csv` para persistir e recuperar dados.

* **Geração de Texto com IA**:
    * **`/gerar-texto-com-ia`**:
        ```python
        @app.route('/gerar-texto-com-ia')
        def gerar_texto_com_ia():
            # ... renderiza o formulário de IA
        ```
        Renderiza a página com o formulário para input do prompt.
    * **`/enviar-prompt`**:
        ```python
        @app.route('/enviar-prompt', methods=['POST'])
        def enviar_prompt():
            # ... chama model.generate_content(prompt)
            # ... retorna resultado para o template
        ```
        Recebe o prompt do usuário, chama a API do Gemini e retorna o texto gerado.
