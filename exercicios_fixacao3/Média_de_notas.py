# Solicita 3 notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Verifica a situação do aluno com base na média
if media >= 7:
    print(f"Média {media:.2f} - Aprovado")
elif media >= 5:
    print(f"Média {media:.2f} - Recuperação")
else:
    print(f"Média {media:.2f} - Reprovado")
