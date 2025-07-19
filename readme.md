# 🏪 Sistema de Controle de Inventário de Loja

Este é um sistema simples de gerenciamento de inventário e vendas de uma loja, desenvolvido com **Python**, **Flask** e **Bootstrap**, utilizando **arquivos de texto** para armazenar os dados.

---

## 📦 Funcionalidades

- ✅ Adicionar produtos ao inventário  
- ✅ Remover produtos do inventário  
- ✅ Consultar estoque com filtros  
- ✅ Registrar vendas (com atualização do estoque)  
- ✅ Relatórios de vendas por semana e por mês  
- ✅ Relatório de estoque atual  
- ✅ Exportação dos dados (`.csv`)  

---

## 🗂 Estrutura de Diretórios

```
inventario_loja/
├── app.py                   # Aplicação principal Flask
├── inventario.txt           # Arquivo com produtos do estoque
├── vendas.txt               # Arquivo com vendas registradas
├── templates/               # Páginas HTML
│   ├── base.html
│   ├── index.html
│   ├── adicionar.html
│   ├── remover.html
│   ├── consultar.html
│   ├── vendas.html
│   ├── relatorio.html
│   └── relatorio_estoque.html
├── static/                  # Imagens do carrossel
│   └── img1.jpeg ... img4.jpeg
```

---

## 🚀 Como Executar

### 1. Clone o projeto
```bash
git clone https://github.com/seuusuario/seurepositorio.git
cd seurepositorio/inventario_loja
```

### 2. Crie e ative um ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install flask
```

### 4. Execute o projeto
```bash
python app.py
```

Acesse: [http://localhost:5000](http://localhost:5000)

---

## 🧾 Formatos dos Arquivos

### 📁 `inventario.txt`
Cada linha representa um produto:
```
nome;quantidade;preco_unitario;categoria
```

### 📁 `vendas.txt`
Cada linha representa uma venda:
```
nome;quantidade;preco_unitario;total;data_hora
```

---

## 📊 Relatórios

- **Relatório de Vendas**: agrupados por semana e por mês, com totais em tabelas
- **Relatório de Estoque Atual**: lista todos os produtos com nome, quantidade, preço e categoria
- **Exportações CSV**:
  - 📤 `/exportar_vendas` → `vendas.csv`
  - 📤 `/exportar_estoque` → `estoque.csv`

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x  
- Flask  
- HTML5  
- Bootstrap 5  
- Armazenamento local em arquivos `.txt`

---

## 💡 Boas Práticas Aplicadas

- Separação entre lógica (Python) e visual (templates)
- Interface responsiva com Bootstrap
- Código simples, legível e modular
- Sem dependência de banco de dados externo

---

## 👨‍💻 Autores

Desenvolvido por:

- Alexandre Cleiton  
- Frank  
- Yan  

**IFRN - Grupo 6 – Introdução à Lógica de Programação**