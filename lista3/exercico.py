
import os  # Para trabalhar com arquivos e pastas
from tkinter.filedialog import askdirectory  # Para abrir uma janela e escolher uma pasta
import shutil  # Para copiar arquivos e pastas
import datetime  # Para pegar data e hora atual
import time  # Para fazer pausas no programa

# Loop infinito: o código vai rodar para sempre, fazendo backups a cada 5 minutos
while True:
    # Abre uma janela para o usuário escolher a pasta que deseja fazer backup
    pasta_selecionada = askdirectory()
    print(f"Pasta selecionada: {pasta_selecionada}")

    # Lista todos os arquivos e pastas dentro da pasta selecionada
    lista_arquivos = os.listdir(pasta_selecionada)
    print(f"Arquivos encontrados: {lista_arquivos}")

    # Cria um nome único para a pasta de backup com base na data e hora atual
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_pasta_backup = f"backup_{timestamp}"
    nome_completo_backup = os.path.join(pasta_selecionada, nome_pasta_backup)

    # Cria a nova pasta de backup
    os.mkdir(nome_completo_backup)

    # Para cada item encontrado na pasta original
    for arquivos in lista_arquivos:
        nome_arquivo_completo = os.path.join(pasta_selecionada, arquivos)
        nome_final_arquivo = os.path.join(nome_completo_backup, arquivos)

        # Se o nome contém ponto (provavelmente um arquivo), copia o arquivo
        if "." in arquivos:
            shutil.copy2(nome_arquivo_completo, nome_final_arquivo)
        # Se for uma pasta (não tem ponto no nome), copia a pasta inteira,
        # mas evita copiar a própria pasta de backup recém-criada
        elif arquivos != nome_pasta_backup:
            shutil.copytree(nome_arquivo_completo, nome_final_arquivo)

    # Mostra quando o backup terminou
    horario_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Backup concluído em {horario_atual}")

    # Espera 5 minutos antes de fazer o próximo backup
    print("Aguardando 5 minutos para o próximo backup...")
    time.sleep(10)  # 300 segundos = 5 minutos

