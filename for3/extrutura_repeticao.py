import os
os.system("cls")

# n = int(input("Dgite um numero: "))

# soma = 0

# for i in range(1, n+1):
#     soma += i
#     print(f"A soma dos numeros é {soma}")

# palavra = "python"
# for letra in palavra:
#     print(letra)

lista = []
for i in range(5):
    nome = input("Digite um nome: ").capitalize()
    lista.append(nome)
    print(f"O nome foi digitado é {nome}")
print(lista)
buscar = input("Digite o nome desejado: ").capitalize()
if buscar in lista:
    print("Nome esta na lista: ", buscar)
else:
    print("Nome não esta na lista")