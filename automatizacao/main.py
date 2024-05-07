import pyautogui as spa
import time
import pandas as pd

spa.PAUSE = 0.5

spa.press("win")
spa.write("chrome")
spa.press("enter")

spa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
spa.press("enter")

time.sleep(3)

spa.press("tab")
spa.write("jorge1filho1@gmail.com")

spa.press("tab")
spa.write("JornadaPython")

spa.press("tab")  
spa.press("enter") 

time.sleep(3)

tabela = pd.read_csv("automatizacao/produtos.csv")

print(tabela)

for linha in tabela.index:
    
    codigo = str(tabela.loc[linha, "codigo"])

    spa.click(x=916, y=259)
    
    spa.write(codigo)
    spa.press("tab")
    
    spa.write(str(tabela.loc[linha, "marca"]))
    spa.press("tab")

    spa.write(str(tabela.loc[linha, "tipo"]))
    spa.press("tab")

    spa.write(str(tabela.loc[linha, "categoria"]))
    spa.press("tab")

    spa.write(str(tabela.loc[linha, "preco_unitario"]))
    spa.press("tab")

    spa.write(str(tabela.loc[linha, "custo"]))
    spa.press("tab")

    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        spa.write(str(tabela.loc[linha, "obs"]))

    spa.press("tab")
    spa.press("enter")
    spa.scroll(5000)