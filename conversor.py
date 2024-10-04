import pandas as pd
from dbfread import DBF

# Função para converter o arquivo DBC para CSV
def convert_dbc_to_csv(dbc_file_path, csv_file_path):
    # Ler o arquivo .DBC como uma tabela DBF
    table = DBF(dbc_file_path, encoding='latin-1')

    # Converter os registros para um DataFrame do pandas
    df = pd.DataFrame(iter(table))

    # Salvar como arquivo CSV
    df.to_csv(csv_file_path, index=False)

    print(f'Arquivo {csv_file_path} criado com sucesso!')

# Nome do arquivo
dbc_file = 'D:\Documentos\PESQUISA\Programas\HCPA1301.dbc'
csv_file = 'D:\Documentos\PESQUISA\Programas\HCPA1301.csv'

# Chamar a função para converter
convert_dbc_to_csv(dbc_file, csv_file)
