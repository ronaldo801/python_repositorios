# Solicita o CPF
cpf = input("Digite o CPF (somente números): ")

# Verifica se tem 11 dígitos e se são todos numéricos
if len(cpf) == 11 and cpf.isdigit():
    print("CPF válido.")
else:
    print("CPF inválido. Deve conter exatamente 11 dígitos numéricos.")
