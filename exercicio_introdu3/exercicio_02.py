import os
os.system("cls")

frase = " Python é uma linguagem MUITO poderosa! Python é incrível "
frase_nova = "Python é uma linguagem MUITO poderosa! Python é incrível "

# remover os espaços em brancos no inicio e no fim da frase

frase_limpa = frase.strip()
print(frase_limpa)

# tranformar a frase em letras minusculas

frase1 = frase.lower()
print(frase1)

# tranformar a frase em letras maiusculas
frase2 = frase.upper()
print(frase2)

#colocar a apenas a primeira letra da primeira palavra da frase com a letra maiuscula
frase_nova = frase_nova.capitalize()
print(frase_nova)

#colocar a primeira letra de todas as palavras da frase em Maiuscula
frase4 = frase.title()
print(frase4)

#substituir Python por Java
frase5 = frase.replace("Python", "Java")
print(frase5)

#Contar quantas vezes o Python aparece na frese original
contagem = frase.count("Python")
print(contagem)

#Encontrar a posição da palavra "poderosa"
posicao = frase.find("poderosa")
print(posicao)
#0001
#0001
#0001