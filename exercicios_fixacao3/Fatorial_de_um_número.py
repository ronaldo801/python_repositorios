# Solicita o número
num = int(input("Digite um número inteiro: "))

# Calcula o fatorial
fatorial = 1
for i in range(2, num + 1):
    fatorial *= i

# Mostra o resultado
print(f"{num}! = {fatorial}")
