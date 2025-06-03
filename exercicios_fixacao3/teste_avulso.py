import re

def validar_cpf(cpf):
    """
    Função para validar um CPF brasileiro.
    
    Parâmetros:
    cpf (str): O CPF a ser validado, podendo estar no formato 'xxx.xxx.xxx-xx' ou 'xxxxxxxxxxx'.
    
    Retorna:
    bool: True se o CPF for
      válido, False caso contrário.
    """
    # Remove caracteres não numéricos (pontos e hífens)
    cpf = re.sub(r'\D', '', cpf)
    
    # Verifica se o CPF possui exatamente 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais (exemplo: 111.111.111-11)
    if cpf == cpf[0] * 11:
        return False
    
    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if int(cpf[9]) != resto:
        return False
    
    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if int(cpf[10]) != resto:
        return False
    
    return True

# Exemplo de uso
cpf = input("Digite o CPF para validação: ")
if validar_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")
