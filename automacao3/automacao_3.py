import pyautogui
import time
import os

def espera(segundos = 2):
    time.sleep(segundos)

def clique(x,y,delay=2):
    espera(delay)
    pyautogui.click(x = x, y = y)

def dois_cliques(x,y,delay=2):
    espera(delay)
    pyautogui.doubleClick(x = x, y = y)

def abrir_site(nome_site, delay=2):
    espera(delay)
    pyautogui.write(nome_site)
    espera(delay)
    pyautogui.press("enter")
    espera(1)

def abrir_pasta(caminho):
    os.startfile(caminho)
    time.sleep(2)

#Verificar cursos do SENA em taquaralto

# clique(1806, 24)
# dois_cliques(41, 331)
# abrir_site("https://www.to.senac.br/")
# clique(969, 68)
# clique(1191, 206)
# clique(1218, 380)


# time.sleep(5)
# pyautogui.click(x=1806, y=24)
# time.sleep(3)
# pyautogui.doubleClick(x=41, y=331)
# time.sleep(4)
# pyautogui.write("https://www.to.senac.br/")
# time.sleep(3)
# pyautogui.press("enter")
# time.sleep(3)
# pyautogui.doubleClick(x=969, y=68)
# time.sleep(3)
# pyautogui.doubleClick(x=1191, y=206)
# time.sleep(3)
# pyautogui.doubleClick(x=1218, y=380)


clique(1806, 24)
dois_cliques(41, 331)
abrir_site("www.gmail.com.br")
abrir_site("ronaldofoccos@gmail.com")
clique(969, 68)
abrir_site("-----")
clique(105, 173)
abrir_site("mateusgn@to.senac.br")
clique(1431, 1002)
# Abre a pasta localizada em (r antes da string indica uma string bruta 
# (raw string). Isso significa que qualquer caractere especial, como barras invertidas (\)), 
# não será interpretado de forma especial pelo Python. 
abrir_pasta(r"C:\Users\DBA_Ronaldo\Desktop\Python")
clique(288, 388)
clique(782, 507)
clique(1309, 995)
clique(1038, 184)





#C:\Users\DBA_Ronaldo\Desktop\Python\automacao1.py
mudanca