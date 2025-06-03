#cria lista com 5 nomes
#adcionar mais 3 nomes
#excluir 2
#Colocar em ordem alfabetica
import os
os.system ("cls")
nomes = ["Ronaldo", "Pedro", "Amanda", "Nonata", "Kaio"]
nomes.insert(1, "Maria")
nomes.insert(2, "Jose")
nomes.insert(3, "Joaquina")

nomes.remove("Ronaldo")
nomes.remove("Pedro")
nomes.remove("Kaio")

nomes.sort()

print(nomes)

