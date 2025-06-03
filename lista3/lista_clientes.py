import os
os.system ("cls")
import pandas as pd # Importa a biblioteca pandas, usada para manipular tabelas (DataFrames)

clientes = [{"nome":"Ana Clara Martins", "email":"ana.martins@email.com", "Telefone": "11991234567", "Data_nascimento": "12/03/1990"},
            {"nome":"Carlos Henrique Lima", "email":"carlos.lima@email.com", "Telefone": "21993456789", "Data_nascimento": "08/07/1985"},
            {"nome":"Juliana Souza Reis", "email":"juliana.reis@email.com", "Telefone": "31998887766", "Data_nascimento": "25/11/1991"},
            {"nome":"Felipe Andrade Rocha", "email":"felipe.rocha@email.com", "Telefone": "11994561234", "Data_nascimento": "03/09/1988"},
            {"nome":"Larissa Gomes Vieira", "email":"larissa.vieira@email.com", "Telefone": "21990011223", "Data_nascimento": "30/01/1995"},
            {"nome":"Bruno Ferreira Costa", "email":"bruno.costa@email.com", "Telefone": "11997885644", "Data_nascimento": "14/06/1991"},
            {"nome":"Patricia Melo Cardoso", "email":"patricia.cardoso@email.com", "Telefone": "31992334455", "Data_nascimento": "22/12/1987"},
            {"nome":"Ricardo Alves Pinto", "email":"ricardo.pinto@email.com", "Telefone": "21997654321", "Data_nascimento": "09/04/1983"},
            {"nome":"Marina Duarte Lopes", "email":"marina.lopes@email.com", "Telefone": "31991112233", "Data_nascimento": "17/08/1996"},
            {"nome":"Diego Ribeiro Teixeira", "email":"diego.teixeira@email.com", "Telefone": "11993216548", "Data_nascimento": "05/10/1989"},

]
df = pd.DataFrame(clientes) # Converte a lista de dicionários em um DataFrame (tabela do pandas)

# Salva como Excel
df.to_excel("C:\\Users\\DBA_Ronaldo\\Desktop\\cadastro_clientes\\cadastro_clientes.xlsx", index=False)
print("Arquivo 'clientes.xlsx' foi criado com sucesso!")