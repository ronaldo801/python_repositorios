# Inicializa os contadores
positivos = negativos = zeros = 0

# Solicita 10 números
for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        zeros += 1

# Exibe os resultados
print(f"Positivos: {positivos}, Negativos: {negativos}, Zeros: {zeros}")
