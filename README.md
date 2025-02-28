# 📦 Desafio Técnico: Extração e Modelagem de Dados de Almoxarifado

## 📌 Introdução
Este projeto tem como objetivo **extrair dados** de um arquivo PDF contendo uma **lista de estoque** de um almoxarifado, **modelar** esses dados em um **banco de dados relacional** e **carregá-los** em tabelas específicas.  

O código foi desenvolvido em **Python** e utiliza **MySQL** como sistema de gerenciamento de banco de dados (**SGBD**).

---

## 📑 Tabela de Conteúdos
- [📌 Introdução](#📌-introdução)
- [⚙️ Requisitos](#⚙️-requisitos)
- [📂 Estrutura do Projeto](#📂-estrutura-do-projeto)
- [🚀 Passo a Passo para Execução](#🚀-passo-a-passo-para-execução)
  - [1️⃣ Configuração do Banco de Dados](#1️⃣-configuração-do-banco-de-dados)
  - [2️⃣ Execução do Script Python](#2️⃣-execução-do-script-python)
  - [3️⃣ Verificação dos Dados no Banco de Dados](#3️⃣-verificação-dos-dados-no-banco-de-dados)
- [🛢️ Estrutura do Banco de Dados](#🛢️-estrutura-do-banco-de-dados)
- [❌ Tratamento de Erros](#❌-tratamento-de-erros)
- [📌 Considerações Finais](#📌-considerações-finais)

---

## ⚙️ Requisitos

Antes de executar o projeto, certifique-se de que os seguintes requisitos estão instalados:

### 📌 Python 3.x  
Verifique a instalação com o comando:
```bash
python --version
📌 MySQL
Verifique a instalação com o comando: mysql --version
📌 Bibliotecas Python
Instale as bibliotecas necessárias com o comando: pip install pdfplumber mysql-connector-python

📂 Estrutura do Projeto
O projeto contém os seguintes arquivos:

📌 extrair_dados.py → Script Python para extrair os dados do PDF e carregar no MySQL.
📌 db_almoxarifado.sql → Script SQL para criar o banco de dados e as tabelas.
📌 Lista_de_estoque_DMP.pdf → Arquivo PDF contendo a lista de estoque.
📌 README.md → Este arquivo com as instruções detalhadas.

🚀 Passo a Passo para Execução
1️⃣ Configuração do Banco de Dados
Execute o script SQL para criar o banco de dados e tabelas:

mysql -u root -p < db_almoxarifado.sql

Verifique se o banco foi criado corretamente:

USE db_almoxarifado;
SHOW TABLES;

2️⃣ Execução do Script Python
Certifique-se de que o arquivo Lista_de_estoque_DMP.pdf está no mesmo diretório que extrair_dados.py.
No terminal, navegue até o diretório do projeto e execute:

python extrair_dados.py

O script exibirá mensagens indicando o progresso da extração, inserção e possíveis erros.

Exemplo de saída esperada:

Conexão ao MySQL bem-sucedida!
Grupo inserido: 3004, GAS E OUTROS MATERIAIS ENGARRAFADOS, id_grupo: 1
Item inserido: 3004000000012, GÁS, LIQUEFEITO DE PETRÓLEO - GLP, ENVASADO EM BOTIJÃO 13KG (P-13), UNIDADE, id_grupo: 1
Dados carregados no banco de dados com sucesso!
Conexão ao MySQL fechada.





