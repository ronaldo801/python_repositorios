import time

# Solicita um número
num = int(input("Digite um número para a contagem regressiva: "))

# Faz a contagem até 0 com intervalo de 1 segundo
for i in range(num, -1, -1):
    print(i)
    time.sleep(1)

print("Contagem finalizada!")
