Aqui está o arquivo README.md formatado em Markdown com todas as instruções necessárias para configurar e executar o projeto.

markdown
Copiar
Editar
# Desafio Técnico: Extração e Modelagem de Dados de Almoxarifado

## Introdução
Este projeto tem como objetivo extrair dados de um arquivo PDF contendo uma lista de estoque de um almoxarifado, modelar esses dados em um banco de dados relacional e carregá-los em tabelas específicas. O código foi desenvolvido em Python e utiliza o MySQL como sistema de gerenciamento de banco de dados (SGBD).

## Tabela de Conteúdos
- [Requisitos](#requisitos)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Passo a Passo para Execução](#passo-a-passo-para-execução)
  - [1. Configuração do Banco de Dados](#1-configuração-do-banco-de-dados)
  - [2. Execução do Script Python](#2-execução-do-script-python)
  - [3. Verificação dos Dados no Banco de Dados](#3-verificação-dos-dados-no-banco-de-dados)
- [Estrutura do Banco de Dados](#estrutura-do-banco-de-dados)
- [Tratamento de Erros](#tratamento-de-erros)
- [Considerações Finais](#considerações-finais)

## Requisitos
Antes de executar o projeto, certifique-se de que os seguintes requisitos estão instalados:

- **Python 3.x**: O código foi desenvolvido em Python. Certifique-se de que o Python está instalado em sua máquina.

  Verifique a instalação com o comando:
  ```bash
  python --version
MySQL: O banco de dados utilizado é o MySQL. Certifique-se de que o MySQL está instalado e em execução.

Verifique a instalação com o comando:

bash
Copiar
Editar
mysql --version
Bibliotecas Python: As bibliotecas necessárias são pdfplumber (para extração de dados do PDF) e mysql-connector-python (para conexão com o banco de dados MySQL).

Instale as bibliotecas com o comando:

bash
Copiar
Editar
pip install pdfplumber mysql-connector-python
Estrutura do Projeto
O projeto consiste nos seguintes arquivos:

extrair_dados.py: Script Python que extrai os dados do PDF e os carrega no banco de dados.
db_almoxarifado.sql: Script SQL para criar o banco de dados e as tabelas necessárias.
Lista_de_estoque_DMP.pdf: Arquivo PDF contendo a lista de estoque a ser processada.
README.md: Este arquivo, contendo instruções detalhadas para configurar e executar o projeto.
Passo a Passo para Execução
1. Configuração do Banco de Dados
Criando o banco de dados e as tabelas:
Execute o script SQL db_almoxarifado.sql no MySQL para criar o banco de dados db_almoxarifado e as tabelas necessárias.

Você pode executar o script diretamente no terminal do MySQL ou usando uma ferramenta gráfica como MySQL Workbench.

Exemplo de execução no terminal:

bash
Copiar
Editar
mysql -u root -p < db_almoxarifado.sql
Verificando a criação do banco de dados:
Conecte-se ao MySQL e verifique se o banco de dados e as tabelas foram criadas.

sql
Copiar
Editar
USE db_almoxarifado;
SHOW TABLES;
2. Execução do Script Python
Preparação:
Coloque o arquivo Lista_de_estoque_DMP.pdf no mesmo diretório que o script Python extrair_dados.py.

Executando o script:
No terminal, navegue até o diretório onde o script está localizado e execute:

bash
Copiar
Editar
python extrair_dados.py
Verificando a saída do script:
O script exibirá mensagens indicando o progresso e sucesso ou erro durante o processo. Exemplo de saída:

yaml
Copiar
Editar
Conexão ao MySQL bem-sucedida!
Grupo inserido: 3004, GAS E OUTROS MATERIAIS ENGARRAFADOS, id_grupo: 1
Item inserido: 3004000000012, GÁS, LIQUEFEITO DE PETRÓLEO - GLP, ENVASADO EM BOTIJÃO 13KG (P-13), UNIDADE, id_grupo: 1
Dados carregados no banco de dados com sucesso!
Conexão ao MySQL fechada.
3. Verificação dos Dados no Banco de Dados
Conecte-se ao banco de dados MySQL e consulte as tabelas para verificar os dados inseridos:

sql
Copiar
Editar
SELECT * FROM Grupo;
SELECT * FROM ItemAlmoxarifado;
Resultado esperado:

A tabela Grupo deve conter os grupos extraídos do PDF.
A tabela ItemAlmoxarifado deve conter os itens associados aos grupos, com o id_grupo correto.
Estrutura do Banco de Dados
O banco de dados db_almoxarifado possui duas tabelas principais:

Tabela Grupo
Coluna	Tipo	Descrição
id_grupo	INT (PK, AUTO_INCREMENT)	Identificador único do grupo
codigo_grupo	VARCHAR(4)	Código do grupo
denominacao_grupo	VARCHAR(255)	Nome ou descrição do grupo
Tabela ItemAlmoxarifado
Coluna	Tipo	Descrição
id_item	INT (PK, AUTO_INCREMENT)	Identificador único do item
codigo_item	VARCHAR(20)	Código do item
denominacao_item	VARCHAR(255)	Nome ou descrição do item
unidade_medida	VARCHAR(50)	Unidade de medida do item
id_grupo	INT (FK)	Referência para id_grupo na tabela Grupo
Tratamento de Erros
O código inclui tratamento de erros para garantir uma execução confiável. Em caso de erro:

A transação é desfeita (rollback), evitando a corrupção de dados.
Mensagens de erro são exibidas no console para facilitar a depuração.
Considerações Finais
PDF com Inconsistências: O código foi projetado para lidar com possíveis inconsistências no formato do PDF, como cabeçalhos, rodapés ou linhas mal formatadas.
Idempotência: O script SQL e o código Python são idempotentes, ou seja, podem ser executados várias vezes sem causar problemas.
Documentação: Este arquivo README.md fornece todas as instruções necessárias para configurar e executar o projeto.
