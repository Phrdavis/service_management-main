from util.funcs import *
from util.parametros import *
from util.models import *

try:
    ###Tela Inicial###        
    class Application(func):
        def __init__(self): #Tela Incial Conv. e Pref.
            try:
                self.root = root #Variavel para atribuir tela principal
                self.root.bind('<F11>', self.toggleFullScreen) #Variavel para ligar e desligar o modo Fullscreen
                self.root.bind('<Escape>', self.quitFullScreen) #Variavel para escapar do modo Fullscreen
                self.tela() #Variavel para atribuir Configurações da tela
                self.frames() #Variavel para atribuir a divisão dos frames
                self.widgets() #Variavel para atribuir botões na tela
                root.mainloop() #Variavel que faz com que a tela permaneça aberta enquanto em uso 
            except:
                pass

        def quitFullScreen(self, event):
            self.fullScreenState = False
            self.root.attributes("-fullscreen", self.fullScreenState)
        
        def toggleFullScreen(self, event):
            self.fullScreenState = True
            self.root.attributes("-fullscreen", self.fullScreenState)
        
        def tela(self):
            self.root.title('Sistema de Senhas Secretaria Municipal de Saúde.') #Atribuição do titulo
            self.root.configure(background= cores[0]) #Cor do plano de fundo da tela
            self.root.geometry("1350x720") #Código que faz a tela abrir em modo tela cheia
            self.root.attributes('-fullscreen', True) #Código que faz com que a tela fique em Fullscreen
            self.root.resizable(False, False) #Permite que o tamanho da tela seja reajustado
            self.root.minsize(width=800, height= 500) #Tamanhos minimos para diminuir a tela
        
        def frames(self):
            self.frame =Frame(self.root, bd = 4, bg = cores[0]) #Frame definido para a tela 4 com fundo branco
            self.frame.place(anchor='center', relx= 0.5,rely= 0.5, relwidth= 0.96, relheight= 0.96) #Definição do local do frame expresso em porcentagem de tela
            
            ###Imagens na Tela### 
            self.photo_plano_de_fundo = PhotoImage(file= planos[0]) #Plano de fundo principal
            plano_de_fundo = Label(self.frame, image= self.photo_plano_de_fundo, bd= 0) #Chamando imagem 
            plano_de_fundo.place(anchor= 'center',relx=0.5, rely=0.4, width= 550, height= 500) #Localizando a imagem na tela         
        
        def widgets(self):
            ###Botões###
            self.photo_BT_AUT_EXAMES = PhotoImage(file = bt[0]) #Imagem botão Autorização de Exames
            self.bt_Aut = Button(self.frame, image = self.photo_BT_AUT_EXAMES, bd = 0, relief=FLAT, command= self.abrir_janela_AE) #Adicionando a imagem a um botão
            self.bt_Aut.place(anchor= 'center',relx= 0.25, rely=0.45, width= 425, height= 160) #Localizando o botão na tela

            self.photo_bt_PREMIR = PhotoImage(file = bt[5]) #Imagem botão PREMIR    
            self.bt_premir = Button(self.frame, image = self.photo_bt_PREMIR, bd = 0, relief=FLAT, command= self.abrir_janela_Premir) #Adicionando a imagem a um botão
            self.bt_premir.place(anchor= 'center',relx= 0.75, rely=0.45, width= 425, height= 160) #Localizando o botão na tela

            self.photo_bt_FARMARCIA = PhotoImage(file = bt[1]) #Imagem botão Farmacia
            self.bt_F = Button(self.frame, image= self.photo_bt_FARMARCIA, relief=FLAT, bd= 0, command= self.abrir_janela_Farmacias) #Adicionando a imagem a um botão
            self.bt_F.place(anchor= 'center',relx= 0.25, rely=0.65, width= 425, height= 160) #Localizando o botão na tela

            self.photo_bt_TFD = PhotoImage(file = bt[6]) #Imagem botão Farmacia
            self.bt_TFD = Button(self.frame, image= self.photo_bt_TFD, relief=FLAT, bd= 0, command= self.abrir_janela_TFD) #Adicionando a imagem a um botão
            self.bt_TFD.place(anchor= 'center',relx= 0.75, rely=0.65, width= 425, height= 160) #Localizando o botão na tela
            
            self.photo_bt_CSUS = PhotoImage(file = bt[13]) #Imagem botão Cartão SUS
            self.bt_SUS = Button(self.frame, image = self.photo_bt_CSUS, bd = 0, relief=FLAT, command= self.abrir_janela_CSUS) #Adicionando a imagem a um botão
            self.bt_SUS.place(anchor= 'center',relx= 0.5, rely=0.86, width= 425, height= 160) #Localizando o botão na tela



except Exception as e:
    print(e)
    pass

def on_closing():
    password_close = simpledialog.askstring(title='', prompt='Informe a senha',show= '*')
    if password_close == password:
        root.destroy() 

root.protocol('WM_DELETE_WINDOW', on_closing)   


