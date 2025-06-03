import os
os.system('cls')

faturamento = 1500
custo = 700
imposto = 0.1 * faturamento
lucro = faturamento - custo - imposto

print(faturamento)
print(custo)
print(imposto)
print(lucro)

#print(f"o faturamento é {faturamento}, Custo é {custo}, Imposto é {imposto}, Lucro é {lucro}")
print("o faturamento é {}, Custo é {}, Imposto é {}, Lucro é {}" .format(faturamento, custo, imposto, lucro))


email_cliente = "ronaldo@gmail.com"
#colocando todas as letras do email maiusculas

email_cliente = email_cliente.upper()
print(email_cliente)


email_cliente = email_cliente.lower()
print(email_cliente)

#Colocando a primeiro letra do nome em maiusculo
nome_cliente = "ronaldo silva"
nome_cliente = nome_cliente.capitalize()
print(nome_cliente)

#Colocando as primeiras letra do nome em maiusculo
nome_cliente = "ronaldo silva"
nome_cliente = nome_cliente.title()
print(nome_cliente)

#encontrar um caracter no texto
print(nome_cliente.find("n"))
print(email_cliente.find("@"))

#contar quantos caracteres tem um texto
print(len(nome_cliente))
print(len(email_cliente))

#pegar um caracter
print(nome_cliente[12])

#pegar um pedaço do texto
print(email_cliente[1:])
print(email_cliente[:2])

#substituir parte do texto
email_cliente = email_cliente.replace("@gmail.com", "@hotmail.com") 
print(email_cliente)

#dividor o texto
email = "qualquercoisa@gmail.com"
provedor = email.split("@")[1]
print("O provedor do email é ", provedor)

nome = "Ronaldo Silva de Almeida"
nome1 = nome.split()[1]
print(nome1)
#0001
#0001

