# Cria uma lista para armazenar os números
numeros = []

# Solicita 5 números
for i in range(5):
    n = float(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

# Mostra o maior e o menor
print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")
