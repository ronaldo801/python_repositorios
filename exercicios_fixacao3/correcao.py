import os
os.system("cls" if os.name == "nt" else "clear")

meus_produtos = {"mouse": 150, "teclado": 200, "monitor": 800, "gabinete": 500}

# print(meus_produtos)

# buscar_produto = input("Digite o produto: ")
# if buscar_produto in meus_produtos:
#     print(f"O é{buscar_produto} e o valor e´: ", meus_produtos[buscar_produto])
# else:
#     print("Produto não existe: ")

# nome_produto = input("Digite um produto: ")
# novo_valor = float(input("Digite um novo valor do produto: "))
# meus_produtos[nome_produto] = novo_valor
# print(meus_produtos)

# novo_produto = input("Digite um novo produto: ")
# valor_produto = float(input("Digite um novo valor: "))

# meus_produtos[novo_produto] = valor_produto
# print(meus_produtos)

# remover_produto = input("Digite o produto para remover: ").lower()
# if remover_produto in meus_produtos: 
#     meus_produtos.pop(remover_produto)
#     print(meus_produtos)
# else:
#     print("Produto não existe: ")


for produto in meus_produtos:
    meus_produtos[produto] = meus_produtos[produto] * 0.9
print(meus_produtos)