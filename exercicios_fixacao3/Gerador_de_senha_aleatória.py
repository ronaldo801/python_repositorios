import random
import string

# Caracteres permitidos: letras, números e símbolos
caracteres = string.ascii_letters + string.digits + string.punctuation

# Gera uma senha de 8 caracteres aleatórios
senha = ''.join(random.choice(caracteres) for _ in range(8))

print(f"Senha gerada: {senha}")
