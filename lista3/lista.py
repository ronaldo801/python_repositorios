import os
os.system("cls")

#lista
frutas = ["Uva", "Manga", "Laranja", "Abacate"]
numero = [1,2,3,4,5,2,3,2,1,2]
variados = [1, "dois", 3 , "quatro", True]

#imprimir por posição
print(frutas)


print(frutas[3])

print(numero[-1])

print(variados[2])

#substituir valor da lista

frutas[1] = "Abacaxi"
print(frutas)

variados[1] = 2
print(variados)

#adicionar um novo elemento a lista sempre por ultimo
numero.append(6)
print(numero)

#adiciona por posição
frutas.insert(1, "Tomate")
print(frutas)

#removor um item da lista
frutas.remove("Tomate")
print(frutas)

#removar sempre o ultimo item da lista
frutas.pop()
print(frutas)

#Conta quantas vezes o valor aparece na lista

print(numero.count(2))

#conta quantos elementos tem na lista
print(len(numero))

#ondem alfabetica

frutas.sort()
print(frutas)

numero.reverse()
print(numero)



