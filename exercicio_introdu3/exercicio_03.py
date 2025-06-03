#Criar lista com 05 itens de mercado
#Remova 02 itens
#adicione 03 novo itens
#Mostre a lista final em ordem alfaberica


#limpar o terminal toda vez e executando um novo comando
import os
os.system("cls")

# #Criando lista
# nomes = ["Macarrao", "Arroz", "Feijao", "Oleo", "Açucar"]

# #Remover itens de uma lista
# nomes.remove("Macarrao")
# nomes.remove("Arroz")
# nomes.remove("Feijao")

# #Inserir novos elementos a lista
# nomes.insert(0, "Sal")
# nomes.insert(1, "Sardinha")
# nomes.insert(2, "Ovos")

# #Colocar em ordem Alfabetica
# nomes.sort()

# print(nomes)


# lista_carros = []

# carro1 = input("Digite o carro1: ")
# carro2 = input("Digite o carro2: ")
# carro3 = input("Digite o carro3: ")

# # lista_carros.append(carro1)
# # lista_carros.append(carro2)
# # lista_carros.append(carro3)

# carro1 = carro1.lower()
# carro2 = carro2.lower()
# carro3 = carro3.lower()
# #adicionar mais de um elemento de uma só vez
# lista_carros.extend([carro1, carro2, carro3])

# #print(lista_carros)
#0001
#0001
#0001


# #Procurar valor dentro de uma lista
# print("palio" in lista_carros)


# lista_times = []
# time1 = input("Digite o primeiro time: ")
# time2 = input("Digite o primeiro time: ")
# time3 = input("Digite o primeiro time: ")

# time1 = time1.capitalize()
# time2 = time2.capitalize()
# time2 = time2.capitalize()


# lista_times.extend([time1, time2, time3])

# buscar_time = input("Buscar Time: ")

# print(buscar_time in lista_times)


#Crie uma lista vazia 
#com input adcione 4 marcas de celulares
#crie uma variavel para buscar a marca de celular
#coloque metodo que transforme o texto da busca do celular que encotra o produto nao importando como o texeto esta
#print a lista com todas marcas
#Print se produto esta na lista ou nao

lista_celulares = []
cell1 = input("Digite a marcada do primeiro celular: ").capitalize()
cell2 = input("Digite a marcada do segundo celular: ").capitalize()
cell3 = input("Digite a marcada do terceiro celular: ").capitalize()
cell4 = input("Digite a marcada do quarto celular: ").capitalize()

#adcionar a lista
lista_celulares.extend([cell1, cell2, cell3, cell4])


buscar_marca = input("Buscar Marca: ").capitalize()

#buscar_marca = buscar_marca.lower()
# buscar_marca = buscar_marca.title()
# buscar_marca = buscar_marca.upper()
# buscar_marca = buscar_marca.title()


print(buscar_marca in lista_celulares)
print(lista_celulares)






