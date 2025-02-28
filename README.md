Desafio Técnico: Extração e Modelagem de Dados de Almoxarifado
Este projeto tem como objetivo extrair dados de um arquivo PDF contendo uma lista de estoque de um almoxarifado, modelar esses dados em um banco de dados relacional e carregá-los em tabelas específicas. O código foi desenvolvido em Python e utiliza o MySQL como sistema de gerenciamento de banco de dados (SGBDR).

Requisitos
Antes de executar o projeto, certifique-se de que os seguintes requisitos estão instalados:

Python 3.x: O código foi desenvolvido em Python. Certifique-se de que o Python está instalado em sua máquina.

Verifique a instalação com o comando:

bash
Copy
python --version
MySQL: O banco de dados utilizado é o MySQL. Certifique-se de que o MySQL está instalado e em execução.

Verifique a instalação com o comando:

bash
Copy
mysql --version
Bibliotecas Python: As bibliotecas necessárias são pdfplumber (para extração de dados do PDF) e mysql-connector-python (para conexão com o banco de dados MySQL).

Instale as bibliotecas com o comando:

bash
Copy
pip install pdfplumber mysql-connector-python
Estrutura do Projeto
O projeto consiste nos seguintes arquivos:

extrair_dados.py: Script Python que extrai os dados do PDF e os carrega no banco de dados.

db_almoxarifado.sql: Script SQL para criar o banco de dados e as tabelas necessárias.

Lista_de_estoque_DMP.pdf: Arquivo PDF contendo a lista de estoque a ser processada.

README.md: Este arquivo, contendo instruções detalhadas para configurar e executar o projeto.

Passo a Passo para Execução
1. Configuração do Banco de Dados
Crie o banco de dados e as tabelas:

Execute o script SQL db_almoxarifado.sql no MySQL para criar o banco de dados db_almoxarifado e as tabelas necessárias.

Você pode executar o script diretamente no terminal do MySQL ou usando uma ferramenta gráfica como MySQL Workbench.

Exemplo de execução no terminal:

bash
Copy
mysql -u root -p < db_almoxarifado.sql
Verifique se o banco de dados foi criado:

Conecte-se ao MySQL e verifique se o banco de dados db_almoxarifado e as tabelas Grupo e ItemAlmoxarifado foram criadas.

Exemplo de consulta:

sql
Copy
USE db_almoxarifado;
SHOW TABLES;
2. Execução do Script Python
Coloque o arquivo PDF no diretório correto:

Certifique-se de que o arquivo Lista_de_estoque_DMP.pdf está no mesmo diretório que o script Python extrair_dados.py.

Execute o script Python:

No terminal, navegue até o diretório onde o script está localizado e execute o seguinte comando:

bash
Copy
python extrair_dados.py
Verifique a saída do script:

O script exibirá os dados extraídos do PDF e as mensagens de sucesso ou erro durante o processo de carregamento no banco de dados.

Exemplo de saída:

Copy
Conexão ao MySQL bem-sucedida!
Grupo inserido: 3004, GAS E OUTROS MATERIAIS ENGARRAFADOS, id_grupo: 1
Item inserido: 3004000000012, GÁS, LIQUEFEITO DE PETRÓLEO - GLP, ENVASADO EM BOTIJÃO 13KG (P-13), UNIDADE, id_grupo: 1
Dados carregados no banco de dados com sucesso!
Conexão ao MySQL fechada.
3. Verificação dos Dados no Banco de Dados
Conecte-se ao banco de dados MySQL:

Use o MySQL Workbench ou o terminal para se conectar ao banco de dados db_almoxarifado.

Consulte as tabelas:

Verifique se os dados foram carregados corretamente nas tabelas Grupo e ItemAlmoxarifado.

Exemplo de consulta:

sql
Copy
SELECT * FROM Grupo;
SELECT * FROM ItemAlmoxarifado;
Resultado esperado:

A tabela Grupo deve conter os grupos extraídos do PDF.

A tabela ItemAlmoxarifado deve conter os itens associados aos grupos, com o id_grupo correto.

Estrutura do Banco de Dados
O banco de dados db_almoxarifado possui duas tabelas principais:

Tabela Grupo
id_grupo: Identificador único do grupo (chave primária, autoincremento).

codigo_grupo: Código do grupo (4 caracteres numéricos).

denominacao_grupo: Nome ou descrição do grupo.

Tabela ItemAlmoxarifado
id_item: Identificador único do item (chave primária, autoincremento).

codigo_item: Código do item (mais de 4 caracteres numéricos).

denominacao_item: Nome ou descrição do item.

unidade_medida: Unidade de medida do item.

id_grupo: Chave estrangeira que referencia o id_grupo na tabela Grupo.

Tratamento de Erros
O código inclui tratamento de erros para garantir que falhas durante a execução sejam capturadas e tratadas adequadamente. Em caso de erro:

A transação é desfeita (rollback), garantindo que os dados não sejam corrompidos.

Mensagens de erro são exibidas no console para facilitar a depuração.

Considerações Finais
PDF com Inconsistências: O código foi projetado para lidar com possíveis inconsistências no formato do PDF, como cabeçalhos, rodapés ou linhas mal formatadas.

Idempotência: O script SQL e o código Python são idempotentes, ou seja, podem ser executados várias vezes sem causar problemas.

Documentação: Este arquivo README.md fornece todas as instruções necessárias para configurar e executar o projeto.
