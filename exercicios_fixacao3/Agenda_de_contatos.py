# Dicionário para armazenar os contatos
agenda = {}

# Cadastro de 3 contatos
for i in range(3):
    nome = input(f"Digite o nome do contato {i+1}: ")
    telefone = input("Digite o telefone: ")
    agenda[nome] = telefone

# Exibe todos os contatos
print("Contatos cadastrados:")
for nome, telefone in agenda.items():
    print(f"{nome}: {telefone}")
