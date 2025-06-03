# Solicita uma palavra
palavra = input("Digite uma palavra: ").lower()

# Define as vogais
vogais = 'aeiou'

# Conta as vogais na palavra
contador = sum(1 for letra in palavra if letra in vogais)

# Exibe o total de vogais
print(f"Número de vogais: {contador}")
