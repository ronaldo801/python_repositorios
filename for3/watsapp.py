import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import sys
from datetime import date, datetime

# Abrir o WhatsApp Web
webbrowser.open("https://web.whatsapp.com/")
sleep(20)  # Aguarde o carregamento completo do WhatsApp Web

# Carregar a planilha de contatos
workbook = openpyxl.load_workbook("Numeros2.xlsx")
pagina_cliente = workbook["Plan1"]

# Iterar sobre as linhas da planilha
for linha in pagina_cliente.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    status = linha[2].value
    data = linha[3].value

    # Verificar se nome ou telefone estão ausentes
    if nome is None or telefone is None or status is None:
        break


    # Verificar e formatar a data corretamente
    if isinstance(data, (date, datetime)):
        data_formatada = data.strftime("%d/%m/%Y")
    else:
        data_formatada = str(data)

    # Criar a mensagem personalizada
    mensagem = f"Olá {nome}, você possui um {status}, desde o dia {data_formatada}, por favor realize o pagamento."

    # Codificar a mensagem para URL
    mensagem_codificada = quote(mensagem)

    # Criar o link para enviar a mensagem
    link_mensagem_whatsapp = f"https://web.whatsapp.com/send?phone={telefone}&text={mensagem_codificada}"

    # Abrir o link no navegador
    webbrowser.open(link_mensagem_whatsapp)
    sleep(10)  # Aguarde o carregamento da página de conversa

    # Pressionar Enter para enviar a mensagem
    pyautogui.press("enter")
    sleep(5)  # Aguarde o envio da mensagem

    # Fechar a aba do navegador
    pyautogui.hotkey("ctrl", "w")
    sleep(2)  # Aguarde o fechamento da aba

# Finalizar o script
sys.exit()
