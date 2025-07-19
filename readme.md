# 🏪 Sistema de Controle de Inventário de Loja

Este é um sistema simples de gerenciamento de inventário e vendas de uma loja, desenvolvido com **Python**, **Flask** e **Bootstrap**, utilizando **arquivos de texto** para armazenar os dados.

---

## 📦 Funcionalidades

✅ Adicionar produtos ao inventário  
✅ Remover produtos do inventário  
✅ Consultar estoque com filtros  
✅ Registrar vendas (com atualização do estoque)  
✅ Relatórios de vendas por semana e por mês  
✅ Relatório de estoque atual  
✅ Exportação dos dados (`.csv`)  

---

## 🗂 Estrutura de Diretórios

inventario_loja/
│
├── app.py # Aplicação principal Flask
├── inventario.txt # Arquivo com produtos do estoque
├── vendas.txt # Arquivo com vendas registradas
├── templates/ # Arquivos HTML (interface)
│ ├── base.html
│ ├── index.html
│ ├── adicionar.html
│ ├── remover.html
│ ├── consultar.html
│ ├── vendas.html
│ ├── relatorio.html
│ └── relatorio_estoque.html


---

## 🚀 Como Executar

1. **Instale o Flask** (se ainda não tiver):
   ```bash
   pip install flask

python app.py

http://localhost:5000


🧾 Formatos dos Arquivos

📁 inventario.txt
Cada linha representa um produto no formato:

Copiar/Editar
nome;quantidade;preco_unitario;categoria

📁 vendas.txt
Cada linha representa uma venda registrada:

Copiar/Editar
nome;quantidade;preco_unitario;total;data_hora

📊 Relatórios
Relatório de Vendas:
Agrupamento por semana e por mês

Totais exibidos em tabelas HTML

Relatório de Estoque Atual:
Exibe todos os produtos com nome, quantidade, preço e categoria

Exportações:
📤 /exportar_vendas → exporta vendas.csv

📤 /exportar_estoque → exporta estoque.csv

🛠️ Tecnologias Utilizadas

Python 3.x

Flask

HTML5 / Bootstrap 5

Armazenamento em arquivos .txt

📚 Pontos de Boas Práticas
Separação de lógica e visual com templates Flask

Interface intuitiva e responsiva com Bootstrap

Persistência de dados com arquivos simples

Código comentado, legível e modular


