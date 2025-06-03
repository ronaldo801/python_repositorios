# Solicita uma palavra
palavra = input("Digite uma palavra: ").lower()

# Compara a palavra com sua versão invertida
if palavra == palavra[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
