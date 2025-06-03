# Solicita dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita a operação
operacao = input("Digite a operação (+, -, *, /): ")

# Realiza a operação com base no que foi escolhido
if operacao == '+':
    print(f"Resultado: {num1 + num2}")
elif operacao == '-':
    print(f"Resultado: {num1 - num2}")
elif operacao == '*':
    print(f"Resultado: {num1 * num2}")
elif operacao == '/':
    if num2 != 0:
        print(f"Resultado: {num1 / num2}")
    else:
        print("Erro: divisão por zero!")
else:
    print("Operação inválida.")
