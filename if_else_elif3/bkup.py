import os

from tkinter.filedialog import askdirectory

import shutil

pasta_selecionada = askdirectory()
print(pasta_selecionada)

lista_arquivos = os.listdir(pasta_selecionada)
print(lista_arquivos)

nome_pasta_backup = "backup"
nome_completo_backup = f"{pasta_selecionada}/{nome_pasta_backup}"

if not os.path.exists(nome_completo_backup):

    os.mkdir(nome_completo_backup)

for arquivos in lista_arquivos:
  
    nome_arquivo_completo = f"{pasta_selecionada}/{arquivos}"

    nome_final_arquivo = f"{nome_completo_backup}/{arquivos}"
    if "." in arquivos:

        shutil.copy2(nome_arquivo_completo, nome_final_arquivo)
    elif "backup" != arquivos:
        shutil.copytree(nome_arquivo_completo, nome_final_arquivo)