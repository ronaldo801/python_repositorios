import os
os.system("cls")

# soma = 0

# while True:
#     numero = float(input("Digite um numero par asomar ou 0 para sair: "))
#     if numero == 0:
#         break
#     soma  += numero
#     print(soma)
# print(f"A soma de todos os numero digitado é {soma}")



while True:
    idade = int(input("Digite uma idade: "))
    
    if idade >= 18:
        print("Acesso à festa concedido.")
    else:
        print("Entrada proibida.")
    
    continuar = input("Deseja verificar mais alguma idade [S ou N]: ").upper()
    
    if continuar == "N":
        break
    elif continuar != "S":
        print("Opção inválida. Continuando a verificação...\n")

print("Fim da Verificação")
