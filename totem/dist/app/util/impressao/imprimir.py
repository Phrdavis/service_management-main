from concurrent.futures import thread
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime
import win32print, win32api, os, threading

def mm2p(milimetros): #converte milimetros em pontos
    return milimetros/0.352777

def imprimir(senha, local): 
    try:
        txt_senha = senha
        txt_local = local   
        data = datetime.now().strftime('%d/%m/%Y')
        texto_pdf = ['Atendimento','SENHA', txt_senha, 'LOCAL', txt_local, f'São francisco do Sul, {data}']
        font_style = 'Helvetica'
        font_size = [50,40,110,40,110,30]
        eixo = 210

        dir_app = str(os.path.dirname(__file__))
        senha_pdf = 'senha.pdf'
        # inicializa canvas
        cnv = canvas.Canvas(f'{dir_app}\{senha_pdf}', pagesize=A4)

        # carrega imagem de cabeçalho
        cnv.drawImage(f'{dir_app}\smssfs.jpeg' ,mm2p(0),mm2p(260),mm2p(210),mm2p(28)) 
        # Gerar pdf senha
        i = int(0)
        for txt in texto_pdf:
            cnv.setFont(font_style,font_size[i])
            cnv.drawCentredString(mm2p(110),mm2p(eixo), txt)
            eixo -= (35+i)
            i += 1
            
        threading.Thread(target= cnv.save()).start
        win32api.ShellExecute(0,"print",senha_pdf,None, dir_app,0)
    except:
        pass
