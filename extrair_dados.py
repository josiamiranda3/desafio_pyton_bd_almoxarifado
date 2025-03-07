import pdfplumber
import mysql.connector
from mysql.connector import Error

# Função para extrair dados do PDF
def extract_data_from_pdf(pdf_path):
    data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    # Remove espaços em branco e linhas vazias
                    if any(cell.strip() for cell in row):
                        # Substitui valores nulos por string vazia
                        row = [cell if cell is not None else "" for cell in row]
                        data.append(row)
    return data

# Função para verificar se um grupo já existe no banco de dados
def check_if_group_exists(cursor, codigo_grupo):
    cursor.execute("SELECT id_grupo FROM Grupo WHERE codigo_grupo = %s", (codigo_grupo,))
    return cursor.fetchone() is not None

# Função para verificar se um item já existe no banco de dados
def check_if_item_exists(cursor, codigo_item):
    cursor.execute("SELECT id_item FROM ItemAlmoxarifado WHERE codigo_item = %s", (codigo_item,))
    return cursor.fetchone() is not None

# Função para carregar dados no banco de dados
def load_data_to_db(data):
    try:
        # Conecta ao banco de dados MySQL
        conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            database="db_almoxarifado"
        )
        print("Conexão ao MySQL bem-sucedida!")
        cursor = conn.cursor()

        # Inicia uma transação
        conn.start_transaction()

        # Dicionário para mapear codigo_grupo -> id_grupo
        cursor.execute("SELECT id_grupo, codigo_grupo FROM Grupo")
        grupos = {codigo: id for id, codigo in cursor.fetchall()}

        # Processa as linhas do PDF
        for row in data:
            # Ignora o cabeçalho ou linhas inválidas
            if len(row) < 3 or row[0].strip() == "Código":
                continue

            # Verifica se é um grupo (código com 4 caracteres numéricos)
            if row[0].strip().isdigit() and len(row[0].strip()) == 4:
                codigo_grupo = row[0].strip()
                denominacao_grupo = row[2].strip()

                # Insere o grupo se ele não existir
                if not check_if_group_exists(cursor, codigo_grupo):
                    cursor.execute(
                        "INSERT INTO Grupo (codigo_grupo, denominacao_grupo) VALUES (%s, %s)",
                        (codigo_grupo, denominacao_grupo)
                    )
                    # Obtém o id_grupo gerado automaticamente
                    cursor.execute("SELECT LAST_INSERT_ID()")
                    id_grupo = cursor.fetchone()[0]

                    # Atualiza o dicionário de grupos
                    grupos[codigo_grupo] = id_grupo
                    print(f"Grupo inserido: {codigo_grupo}, {denominacao_grupo}, id_grupo: {id_grupo}")
                else:
                    print(f"Grupo já existe: {codigo_grupo}")

            # Verifica se é um item (código com mais de 4 caracteres numéricos)
            elif len(row) >= 4 and row[1].strip().isdigit() and len(row[1].strip()) > 4:
                codigo_item = row[1].strip()
                denominacao_item = row[2].strip()
                unidade_medida = row[3].strip()

                # Obtém o código do grupo (4 primeiros dígitos do código do item)
                codigo_prefixo = codigo_item[:4]
                id_grupo = grupos.get(codigo_prefixo)

                # Se o grupo não existir, insere um grupo padrão (opcional)
                if id_grupo is None:
                    print(f"Grupo não encontrado para o item: {codigo_item}. Usando id_grupo padrão (1).")
                    id_grupo = 1  # Valor padrão

                # Insere o item se ele não existir
                if not check_if_item_exists(cursor, codigo_item):
                    cursor.execute(
                        "INSERT INTO ItemAlmoxarifado (codigo_item, denominacao_item, unidade_medida, id_grupo) VALUES (%s, %s, %s, %s)",
                        (codigo_item, denominacao_item, unidade_medida, id_grupo)
                    )
                    print(f"Item inserido: {codigo_item}, {denominacao_item}, {unidade_medida}, id_grupo: {id_grupo}")
                else:
                    print(f"Item já existe: {codigo_item}")

            # Ignora linhas inválidas
            else:
                print(f"Ignorado (linha inválida): {row}")

        # Confirma a transação
        conn.commit()
        print("Dados carregados no banco de dados com sucesso!")

    except Error as e:
        print(f"Erro ao conectar ou carregar dados no MySQL: {e}")
        if conn.is_connected():
            conn.rollback()  # Desfaz a transação em caso de erro
            print("Transação desfeita devido a erro.")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Conexão ao MySQL fechada.")

# Caminho do arquivo PDF
pdf_path = "Lista_de_estoque_DMP.pdf"

# Extrai os dados
extracted_data = extract_data_from_pdf(pdf_path)

# Exibe os dados extraídos
print("Dados extraídos:")
for row in extracted_data:
    print(row)

# Remove o cabeçalho da tabela (primeira linha)
if extracted_data:
    extracted_data = extracted_data[1:]

# Carrega os dados no banco de dados
load_data_to_db(extracted_data)
