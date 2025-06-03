# Solicita os dados do usuário
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
email = input("Digite o e-mail: ")

# Cria um dicionário com as informações
usuario = {
    "nome": nome,
    "idade": idade,
    "email": email
}

# Exibe o dicionário
print("Cadastro completo:")
print(usuario)
