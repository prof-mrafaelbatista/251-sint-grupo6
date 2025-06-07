import google.generativeai as genai
from flask import Flask, render_template, url_for, request, redirect
import csv
import os # Importe o módulo os para usar variáveis de ambiente

genai.configure(api_key=os.getenv("GEMINI_API_KEY", "AIzaSyBwU44PFMN26PzjC7EeWOHQbwsOE3_0v9k"))

model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

@app.route('/')
def ola():
    return render_template('index.html')

@app.route('/sobre-equipe')
def sobre_equipe():
    return render_template('sobre_equipe.html')

@app.route('/estruturas-selecao')
def estruturas_selecao():
    return render_template('estruturas_selecao.html')

@app.route('/estruturas-repeticao')
def estruturas_repeticao():
    return render_template('estruturas_repeticao.html')

@app.route('/vetores-e-matrizes')
def vetores_e_matrizes():
    return render_template('vetores_e_matrizes.html')

@app.route('/funcoes-e-procedimentos')
def funcoes_e_procedimentos():
    return render_template('funcoes_e_procedimentos.html')

@app.route('/tratamentos-de-excecao')
def tratamentos_de_excecao():
    return render_template('tratamentos_de_excecao.html')

# --- Nova Rota: Pergunte ao Gemini ---
@app.route('/pergunte-ao-gemini', methods=['GET', 'POST'])
def pergunte_ao_gemini():
    resposta_gemini = None
    pergunta_usuario = "" # Inicializa a pergunta do usuário

    if request.method == 'POST':
        pergunta_usuario = request.form.get('pergunta', '').strip() # Pega a pergunta do formulário
        if pergunta_usuario: # Verifica se a pergunta não está vazia
            try:
                # Gera a resposta do Gemini
                response = model.generate_content(pergunta_usuario)
                resposta_gemini = response.text
            except Exception as e:
                # Captura erros na chamada da API
                resposta_gemini = f"Ops! Ocorreu um erro ao chamar o Gemini: {e}"
        else:
            resposta_gemini = "Por favor, digite uma pergunta para o Gemini."

    # Renderiza o template, passando a pergunta anterior e a resposta do Gemini
    return render_template('pergunte_ao_gemini.html',
                           pergunta_anterior=pergunta_usuario,
                           resposta=resposta_gemini)

@app.route('/glossario')
def glossario():
    glossario_de_termos = []
    # É uma boa prática verificar se o arquivo existe antes de tentar abri-lo
    if os.path.exists('bd_glossario.csv'):
        with open('bd_glossario.csv', 'r', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo, delimiter=';')
            for linha in reader:
                glossario_de_termos.append(linha)
    return render_template('glossario.html', glossario=glossario_de_termos)

@app.route('/novo-termo')
def novo_termo():
    return render_template('novo_termo.html')

@app.route('/criar_termo', methods=['POST'])
def criar_termo():
    termo = request.form['termo']
    definicao = request.form['definicao']
    with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo, delimiter=';')
        writer.writerow([termo, definicao])
    return redirect(url_for('glossario'))

@app.route('/alterar-termo/<int:termo_id>')
def alterar_termo(termo_id):
    glossario_de_termos = []
    if os.path.exists('bd_glossario.csv'):
        with open('bd_glossario.csv', 'r', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo, delimiter=';')
            for linha in reader:
                glossario_de_termos.append(linha)

    if 0 <= termo_id < len(glossario_de_termos):
        termo_a_alterar = glossario_de_termos[termo_id]
        return render_template('alterar_termo.html', termo=termo_a_alterar, termo_id=termo_id)
    else:
        return redirect(url_for('glossario'))

@app.route('/editar_termo/<int:termo_id>', methods=['POST'])
def editar_termo(termo_id):
    novo_termo = request.form['termo']
    nova_definicao = request.form['definicao']

    glossario_de_termos = []
    if os.path.exists('bd_glossario.csv'):
        with open('bd_glossario.csv', 'r', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo, delimiter=';')
            for linha in reader:
                glossario_de_termos.append(linha)

    if 0 <= termo_id < len(glossario_de_termos):
        glossario_de_termos[termo_id] = [novo_termo, nova_definicao]

        with open('bd_glossario.csv', 'w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo, delimiter=';')
            writer.writerows(glossario_de_termos)

    return redirect(url_for('glossario'))

@app.route('/deletar-termo/<int:termo_id>')
def deletar_termo(termo_id):
    glossario_de_termos = []
    if os.path.exists('bd_glossario.csv'):
        with open('bd_glossario.csv', 'r', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo, delimiter=';')
            for linha in reader:
                glossario_de_termos.append(linha)

    if 0 <= termo_id < len(glossario_de_termos):
        del glossario_de_termos[termo_id]

        with open('bd_glossario.csv', 'w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo, delimiter=';')
            writer.writerows(glossario_de_termos)

    return redirect(url_for('glossario'))

app.run(debug=True)