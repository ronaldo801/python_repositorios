import os
os.system("cls" if os.name == "nt" else "clear")

meus_produtos = {"mouse": 150, "teclado": 200, "monitor": 800, "gabinete": 500}

# Mostrar todos os produtos e seus preços
print("Produtos disponíveis:")
for produto, preco in meus_produtos.items():
    print(f"- {produto}: R${preco}")

# Mostrar o preço de um produto informado pelo usuário
nome = input("\nDigite o nome de um produto para ver o preço: ").lower()
if nome in meus_produtos:
    print(f"O preço do(a) {nome} é R${meus_produtos[nome]}")
else:
    print("Produto não encontrado.")

# Atualizar o preço de um produto existente
nome = input("\nDigite o nome de um produto para atualizar o preço: ").lower()
if nome in meus_produtos:
    novo_preco = float(input(f"Digite o novo preço para {nome}: "))
    meus_produtos[nome] = novo_preco
    print(f"Preço de {nome} atualizado para R${novo_preco}")
else:
    print("Produto não encontrado.")

# Adicionar um novo produto
novo_produto = input(
    "\nDigite o nome de um novo produto para adicionar: ").lower()
novo_preco = float(input(f"Digite o preço de {novo_produto}: "))
meus_produtos[novo_produto] = novo_preco
print(f"{novo_produto} adicionado com preço R${novo_preco}")

# Remover um produto
remover = input("\nDigite o nome de um produto para remover: ").lower()
if remover in meus_produtos:
    del meus_produtos[remover]
    print(f"{remover} foi removido do dicionário.")
else:
    print("Produto não encontrado.")

# Mostrar dicionário final
print("\nDicionário final de produtos:")
for produto, preco in meus_produtos.items():
    print(f"- {produto}: R${preco}")


#mostre todos os produtos e seus preços
#peça ao usuario o nome de um produto e mostre o preço (se existir no dicionario.)
#Peça o nome de um produto e um novo preço, e atualize o valor no dicionario.

#Permita que o usuario adicone um novo produto com seu preço ao dicionario

#Solicite o nome de um produto e remova-o do dicionario (Caso exista)