import os
os.system("cls")

# num = int(input("Digite um numero: "))

# for i in range(11):
#     resultado = num * i
#     print(f'{num} * {i} = {resultado}')

# num = 5

# if num % 2 == 0:
#     print("Numero Par: ")
# else:
#     print("Numero e impar: ")

# for i in range(1, 101):
#     if i % 2 == 0:
#         print("Número par:", i)


# lista = [1000, 800, 2000, 2500, 700, 650, 999]

# meta = 1000

# lista.sort()

# for i in lista:
#     if i >= meta:
#         print(i, " = Parabéns, você ganhou bônus!")
#     else:
#         print(i, " = Não ganhou bônus.")

# notas = [7.5, 8.0, 6.9, 8.7, 5.3, 4.1, 3.8]

# notas.sort(reverse=-1)

# for i in notas:
#     if i >= 7.0:
#         print(i, "Aprovado")
#     elif i < 7 and i >= 5:
#         print(i, "Recuperação")
#     else:
#         print(i, "Reprovado")


# soma = 0

# for i in range(5):
#     num = int(input("Digite um numero: "))
#     soma += num
#     print("A soma dos numero", soma)

# user = "admin"
# password = 1234

# for i in range(1,4):
#     user1 = input("Insira o usuario: ").lower()
#     password1 = int(input("Insira a senha: "))
#     if user1 == user and password1 == password:
#         print("Acesso Permitido")
#         break
#     else:
#         print(f"Acesso Negado, tentativa {i} de 3")
# else:
#     print("Conta Bloqueada")

senha = "senac"

password = input("Digite sua senha: ")

while True:
    if password == senha:
        print("Acesso Permitido")
        break
    else:
        password = input("Acesso negado, Digite a nova senha: ")





    