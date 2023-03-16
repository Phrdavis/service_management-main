# from util.modulos import *
import tkinter as tk
from datetime import datetime                   

root = tk.Tk()                                              #Variavel Princiapal das telas 
w, h = root.winfo_screenwidth(), root.winfo_screenheight()  #Variavel que pega as medidas da tela como referência
password = '28512'                                          #Senha para fechamento do programa
atendimento = ""                                            #Variavel para escolha do tipo de atendimento
tabela = 'fila_espera'                                      #Atribuindo nome da tabela 
tela = 0                                                    #Contagem do numero de telas 
data = datetime.now().strftime('%d/%m/%Y')

