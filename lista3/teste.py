# Criação da lista vazia
lista_celulares = []

# Adicionando as marcas de celulares
cell1 = input("Digite a marca do primeiro celular: ")
cell2 = input("Digite a marca do segundo celular: ")
cell3 = input("Digite a marca do terceiro celular: ")
cell4 = input("Digite a marca do quarto celular: ")

# Expandindo a lista com as marcas fornecidas
lista_celulares.extend([cell1, cell2, cell3, cell4])

# Solicitando a marca a ser buscada
buscar_marca = input("Buscar Marca: ")

# Verificando se a marca está na lista, ignorando maiúsculas e minúsculas
marca_encontrada = buscar_marca.casefold() in map(str.casefold, lista_celulares)

# Exibindo os resultados
print(f"Marca encontrada: {marca_encontrada}")
print("Lista de marcas:", lista_celulares)
