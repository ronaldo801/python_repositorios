import pandas as pd

# Lista de novos clientes a serem adicionados
clientes = [
    {"nome": "Ana Clara Martins", "email": "ana.martins@email.com", "Telefone": "11991234567", "Data_nascimento": "12/03/1990"},
    {"nome": "Carlos Henrique Lima", "email": "carlos.lima@email.com", "Telefone": "21993456789", "Data_nascimento": "08/07/1985"},
    {"nome": "Juliana Souza Reis", "email": "juliana.reis@email.com", "Telefone": "31998887766", "Data_nascimento": "25/11/1991"},
    {"nome": "Felipe Andrade Rocha", "email": "felipe.rocha@email.com", "Telefone": "11994561234", "Data_nascimento": "03/09/1988"},
    {"nome": "Larissa Gomes Vieira", "email": "larissa.vieira@email.com", "Telefone": "21990011223", "Data_nascimento": "30/01/1995"},
    {"nome": "Bruno Ferreira Costa", "email": "bruno.costa@email.com", "Telefone": "11997885644", "Data_nascimento": "14/06/1991"},
    {"nome": "Patricia Melo Cardoso", "email": "patricia.cardoso@email.com", "Telefone": "31992334455", "Data_nascimento": "22/12/1987"},
    {"nome": "Ricardo Alves Pinto", "email": "ricardo.pinto@email.com", "Telefone": "21997654321", "Data_nascimento": "09/04/1983"},
    {"nome": "Marina Duarte Lopes", "email": "marina.lopes@email.com", "Telefone": "31991112233", "Data_nascimento": "17/08/1996"},
    {"nome": "Diego Ribeiro Teixeira", "email": "diego.teixeira@email.com", "Telefone": "11993216548", "Data_nascimento": "05/10/1989"},
]

# Caminho para o arquivo Excel
arquivo_excel = r'C:\Users\DBA_Ronaldo\Desktop\cadastro_clientes\cadastro_clientes_2.xlsx'  # Adicionar a extensão .xlsx

# Carregar a planilha existente
try:
    df_existente = pd.read_excel(arquivo_excel)
except FileNotFoundError:
    print(f"O arquivo {arquivo_excel} não foi encontrado.")
    exit()

# Converter os novos dados em DataFrame
df_novos_clientes = pd.DataFrame(clientes)

# Adicionar os novos dados ao final da tabela existente
df_atualizado = pd.concat([df_existente, df_novos_clientes], ignore_index=True)

# Caminho para salvar o arquivo atualizado
cadastro_clientes_2 = r'C:\Users\DBA_Ronaldo\Desktop\cadastro_clientes\cadastro_clientes_2.xlsx'  # Adicionar a extensão .xlsx

# Salvar o arquivo Excel com os dados atualizados
df_atualizado.to_excel(cadastro_clientes_2, index=True)

print("Arquivo atualizado com sucesso!")
