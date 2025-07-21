from flask import Flask, render_template, request, redirect, url_for, Response

# Esse comando importa funções e classes do módulo **Flask**, que é um microframework usado para criar aplicações web em Python. Aqui está o que cada item faz:

# - **`Flask`**: é a classe principal usada para criar uma instância do aplicativo web.
# - **`render_template`**: serve para renderizar arquivos HTML com variáveis (templates Jinja2).
# - **`request`**: permite acessar dados enviados pelo cliente, como formulários e parâmetros de URL.
# - **`redirect`**: redireciona o usuário para outra rota ou URL.
# - **`url_for`**: gera URLs com base no nome de funções (evita usar strings fixas).
# - **`Response`**: permite criar respostas HTTP personalizadas.

from datetime import datetime

# Importa a classe datetime do módulo datetime, que é usada para trabalhar com data e hora atual (por exemplo, registrar o horário de uma ação).

from collections import defaultdict


# Importa **`defaultdict`**, uma variação do dicionário do Python. Ele cria automaticamente um valor padrão se a chave não existir. Por exemplo:
# ```python
# d = defaultdict(int)
# print(d['x'])  # Saída: 0

import os
app = Flask(__name__)

# Importa o módulo **`os`**, que permite interagir com o sistema operacional, como manipular arquivos, diretórios, variáveis de ambiente etc.
# ---
# ### ```python
# app = Flask(__name__)

# Arquivos
INVENTARIO = 'inventario.txt'
VENDAS = 'vendas.txt'

# =======================
# ROTA: ADICIONAR PRODUTO
# =======================

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome'].strip().capitalize()
        quantidade = int(request.form['quantidade'])
        preco = float(request.form['preco'])
        categoria = request.form['categoria'].strip().capitalize()

        with open(INVENTARIO, 'a') as f:
            f.write(f'{nome};{quantidade};{preco};{categoria}\n')

        return redirect(url_for('index'))

    return render_template('adicionar.html')


# =======================
# ROTA: REMOVER PRODUTO
# =======================
@app.route('/remover', methods=['GET', 'POST'])
def remover():
    mensagem = ""
    if request.method == 'POST':
        nome_remover = request.form['nome'].strip().capitalize()
        removido = False

        if os.path.exists(INVENTARIO):
            with open(INVENTARIO, 'r') as f:
                linhas = f.readlines()

            with open(INVENTARIO, 'w') as f:
                for linha in linhas:
                    if not linha.startswith(nome_remover + ";"):
                        f.write(linha)
                    else:
                        removido = True

        mensagem = f"Produto '{nome_remover}' removido com sucesso." if removido else f"Produto '{nome_remover}' não encontrado."

    return render_template('remover.html', mensagem=mensagem)


# =======================
# ROTA: CONSULTAR PRODUTO
# =======================
@app.route('/consultar', methods=['GET', 'POST'])
def consultar():
    produtos = []
    filtro_nome = request.form.get('filtro_nome', '').strip().capitalize()
    filtro_categoria = request.form.get('filtro_categoria', '').strip().capitalize()

    if os.path.exists(INVENTARIO):
        with open(INVENTARIO, 'r') as f:
            for linha in f:
                nome, quantidade, preco, categoria = linha.strip().split(';')
                if (not filtro_nome or filtro_nome in nome) and (not filtro_categoria or filtro_categoria in categoria):
                    produtos.append({
                        'nome': nome,
                        'quantidade': int(quantidade),
                        'preco': float(preco),
                        'categoria': categoria
                    })

    return render_template('consultar.html', produtos=produtos)


# =======================
# ROTA: REGISTRAR VENDA
# =======================
@app.route('/vendas', methods=['GET', 'POST'])
def registrar_venda():
    mensagem = ""
    produtos = []

    if os.path.exists(INVENTARIO):
        with open(INVENTARIO, 'r') as f:
            for linha in f:
                nome, quantidade, preco, categoria = linha.strip().split(';')
                produtos.append({
                    'nome': nome,
                    'quantidade': int(quantidade),
                    'preco': float(preco),
                    'categoria': categoria
                })

    if request.method == 'POST':
        produto_vendido = request.form['produto']
        quantidade_vendida = int(request.form['quantidade'])

        atualizados = []
        venda_realizada = False

        for p in produtos:
            if p['nome'] == produto_vendido:
                if p['quantidade'] >= quantidade_vendida:
                    p['quantidade'] -= quantidade_vendida
                    valor_total = quantidade_vendida * p['preco']
                    data_venda = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open(VENDAS, 'a') as vf:
                        vf.write(f"{produto_vendido};{quantidade_vendida};{p['preco']};{valor_total:.2f};{data_venda}\n")
                    mensagem = "Venda registrada com sucesso!"
                    venda_realizada = True
                else:
                    mensagem = "Quantidade em estoque insuficiente."
            atualizados.append(p)

        if venda_realizada:
            with open(INVENTARIO, 'w') as f:
                for p in atualizados:
                    f.write(f"{p['nome']};{p['quantidade']};{p['preco']};{p['categoria']}\n")

    return render_template('vendas.html', produtos=produtos, mensagem=mensagem)


# ================================
# ROTA: RELATÓRIO DE VENDAS
# ================================
@app.route('/relatorio')
def relatorio():
    vendas_semanal = defaultdict(float)
    vendas_mensal = defaultdict(float)

    if os.path.exists(VENDAS):
        with open(VENDAS, 'r') as f:
            for linha in f:
                nome, qtd, preco, total, data = linha.strip().split(';')
                dt = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
                semana = f"{dt.isocalendar().year}-S{dt.isocalendar().week}"
                mes = dt.strftime("%Y-%m")
                vendas_semanal[semana] += float(total)
                vendas_mensal[mes] += float(total)

    return render_template('relatorio.html',
                           vendas_semanal=dict(vendas_semanal),
                           vendas_mensal=dict(vendas_mensal))


# ================================
# ROTA: RELATÓRIO DE ESTOQUE
# ================================
@app.route('/relatorio_estoque')
def relatorio_estoque():
    estoque = []
    if os.path.exists(INVENTARIO):
        with open(INVENTARIO, 'r') as f:
            for linha in f:
                nome, qtd, preco, categoria = linha.strip().split(';')
                estoque.append({
                    'nome': nome,
                    'quantidade': int(qtd),
                    'preco': float(preco),
                    'categoria': categoria
                })

    return render_template('relatorio_estoque.html', estoque=estoque)


# ================================
# ROTA: EXPORTAR VENDAS
# ================================
@app.route('/exportar_vendas')
def exportar_vendas():
    if not os.path.exists(VENDAS):
        return "Arquivo de vendas não encontrado.", 404

    with open(VENDAS, 'r') as f:
        conteudo = f.read()

    return Response(
        conteudo,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=vendas.csv"}
    )


# ================================
# ROTA: EXPORTAR ESTOQUE
# ================================
@app.route('/exportar_estoque')
def exportar_estoque():
    if not os.path.exists(INVENTARIO):
        return "Arquivo de estoque não encontrado.", 404

    with open(INVENTARIO, 'r') as f:
        conteudo = f.read()

    return Response(
        conteudo,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=estoque.csv"}
    )


# ================================
# ROTA PÁGINA INICIAL 
# ================================
@app.route('/')
def index():
    return render_template('index.html')


# ================================
# INICIAR O SERVIDOR
# ================================
if __name__ == '__main__':
    app.run(debug=True)
