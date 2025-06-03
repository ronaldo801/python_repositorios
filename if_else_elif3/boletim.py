#Calculadora Simples IF, ELSI ou ELIF, onde o usuario entrara com dois numero e o oprador. Mostre o resultado
import os
os.system("cls")

num1 = float(input("Digite o Primeiro numero: "))
operador = input("Escolha o Operador: ")
num2 = float(input("Digite o Segundo numero: "))

if operador == '+':
    resultado = num1 + num2
    print("Resultado da Soma", resultado)
elif operador == '-':
    resultado = num1 - num2
    print("Resultado da Subtracao", resultado)
elif operador == '*':
    resultado = num1 * num2
    print("Resultado da Multiplicação", resultado)
elif operador == '/':
    if num2 and num1 !=0:
        resultado = num1 / num2
        print("Resultado da divisão", resultado)
    else:
        print("Erro na divisão")
else:
    print("Operador Invalido: ")
