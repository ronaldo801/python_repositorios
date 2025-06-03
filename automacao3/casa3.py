import os
import shutil
from datetime import datetime

def backup_excel(arquivo, pasta_backup=None):
    if not os.path.exists(arquivo):
        print(f"Arquivo não encontrado: {arquivo}")
        return

    # Define a pasta de backup
    if not pasta_backup:
        pasta_backup = "backups"
    os.makedirs(pasta_backup, exist_ok=True)

    # Cria nome do backup com data e hora
    base = os.path.basename(arquivo)
    nome, ext = os.path.splitext(base)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    nome_backup = f"{nome}_backup_{timestamp}{ext}"
    caminho_backup = os.path.join(pasta_backup, nome_backup)

    # Copia o arquivo
    shutil.copy2(arquivo, caminho_backup)
    print(f"Backup criado: {caminho_backup}")

    # Limita a 5 backups mais recentes
    backups = sorted(
        [f for f in os.listdir(pasta_backup) if f.startswith(nome) and f.endswith(ext)],
        key=lambda f: os.path.getmtime(os.path.join(pasta_backup, f))
    )
    for f in backups[:-5]:
        os.remove(os.path.join(pasta_backup, f))
        print(f"Backup antigo removido: {f}")

# Exemplo de uso
backup_excel(
    r"C:\Users\DBA_Ronaldo\Desktop\cadastro_clientes\cadastro_clientes_2.xlsx",
    r"C:\Users\DBA_Ronaldo\Desktop\cadastro_clientes"
)

mudanca
