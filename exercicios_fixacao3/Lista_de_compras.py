# Cria uma lista vazia para armazenar os itens
lista = []

# Solicita 5 itens ao usuário
for i in range(5):
    item = input(f"Digite o item {i + 1} da lista de compras: ")
    lista.append(item)

# Exibe a lista completa
print("Sua lista de compras é:")
for item in lista:
    print(f"- {item}")
