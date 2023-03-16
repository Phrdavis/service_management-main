from util.gerar_senha import *
from util.espera import *

 ###Classe para Funções###
class func(espera):
    global opcao, setor, atendimento, opc, ref, farmaciaStop

    ###Função para aviso de HORARIO EXCEDENTE
    def horario_ex(self):
        global opcao, setor, atendimento, tela, opc, ref, hora_atual, farmaciaStop
        hora_atual = datetime.now().strftime('%d/%m/%Y %H:%M')
        hora_atual = datetime.strptime(hora_atual, '%d/%m/%Y %H:%M')
        dataA = hora_atual.strftime('%d/%m/%Y') 
        config = ConfigParser()
        get_dir = os.path.dirname(__file__)
        config.read(fr'{get_dir}\settings.ini')
        settings = dict(config['config'])
        horarioStop = datetime.strptime(f"{dataA} {settings['horario']}", '%d/%m/%Y %H:%M')
        farmaciaStop = datetime.strptime(f"{dataA} {settings['farmacia']}", '%d/%m/%Y %H:%M')

        if hora_atual >= horarioStop:
            self.root_hrExcede()

        elif ref == 1:
            self.premir()

        elif ref == 2:
            self.farmacia()

        elif ref == 3:
            self.aut_exa()  

        elif ref == 4:
            self.tfd()

        elif ref == 5:
            self.cartao_sus()

    def root_hrExcede(self):
        self.root_horario = tk.Toplevel() #Variavel para atribuir tela principal
        self.root_horario.title('Sistema de Senhas Secretaria Municipal de Saúde.') #Atribuir titulo a tela
        self.root_horario.configure(background= cores[2]) #Cor de fundo
        self.root_horario.geometry("1000x700") #Dimensões do tamanho da tela cheia
        self.root_horario.attributes('-alpha', 0.0)
        self.root_horario.resizable(False, False) #Negar o redimensionamento da tela
        self.root_horario.minsize(width=800, height= 500) #Definir tamanho minimo da tela   
        self.frame_horario =Frame(self.root_horario, bg = cores[0]) #Definindo um Frame para a tela 
        self.frame_horario.place(anchor='center',relx= 0.5,rely= 0.5, relwidth= 0.96, relheight= 0.96) #Localizando o Frame na tela 

        self.photo_horarios = PhotoImage(file= fr"{get_dir}\Plano de Fundo\Plano de Fundo horarios.png")
        self.logo_horarios = Label(self.frame_horario, image= self.photo_horarios, background= cores[0])
        self.logo_horarios.place(anchor="center", relx=0.5, rely=0.5)

        self.aviso = Label(self.frame_horario, text="A fila de espera para \neste Atendimento \nEXCEDE \no horario de atendimento", background= cores[0], foreground= "red")
        self.aviso.configure(font= tkFont.Font(family="Arial", size=45, weight="bold"))
        self.aviso.place(anchor='center', relx= 0.5, rely= 0.5)

        self.aviso2 = Label(self.frame_horario, text="Horario Atual:", background= cores[0])
        self.aviso2.configure(font= tkFont.Font(family="Arial", size=25))
        self.aviso2.place(anchor='center', relx= 0.5, rely= 0.8)

        self.aviso3 = Label(self.frame_horario, text= hora_atual, background= cores[0])
        self.aviso3.configure(font= tkFont.Font(family="Arial", size=25))
        self.aviso3.place(anchor='center', relx= 0.5, rely= 0.86)

        ###Código para janela abrir no meio da tela###
        self.root_horario.update_idletasks()
        width = self.root_horario.winfo_width()
        frm_width = self.root_horario.winfo_rootx() - self.root_horario.winfo_x()
        win_width = width + 2 * frm_width

        height = self.root_horario.winfo_height()
        titlebar_height = self.root_horario.winfo_rooty() - self.root_horario.winfo_y()
        win_height = height + titlebar_height + frm_width

        x = self.root_horario.winfo_screenwidth() // 2 - win_width // 2
        y = self.root_horario.winfo_screenheight() // 2 - win_height // 2
        self.root_horario.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root_horario.deiconify()
        
        self.root_horario.attributes('-alpha', 1.0)
        self.root_horario.overrideredirect(True)
        self.root_horario.after(8000,self.root_horario.destroy)

    ###Funções de Fechamento de cada tela###
    def fechar_conv(self): #Função fechamento de tela Conv. do TFD, AUT, FAA, FAB, FAE, PRE
        global opcao, setor, atendimento, tela, sigla_db
        atendimento = atend[1]
        sigla_db = opcao
        threading.Thread(target=self.abrir_janela_espera())
        threading.Thread(target=self.gerar_senha).start()
        if tela == 1:
            self.root_premir.destroy()
        elif tela == 2:
            self.root_premir.destroy()
        elif tela == 3:
            self.root_premir.destroy()
            self.rootConsultas.destroy() #Destruir janela 2 Consultas
        elif tela == 4:
            self.root_farmacia.destroy()
            self.root_AB.destroy() #Destruir janela 20
        elif tela == 5:
            self.root_farmacia.destroy()
            self.root_FE.destroy() #Destruir janela 200
        elif tela == 6:
            self.root_farmacia.destroy()
            self.root_FAC.destroy() #Destruir janela 2000
        elif tela == 7:
            self.rootAE.destroy() #Destruir janela 21
        elif tela == 8:
            self.rootTFD.destroy() #Destruir janela 2
        elif tela == 9:
            self.rootCSUS.destroy()

    def fechar_prefe(self): #Função fechamento de tela Pref. do TFD, AUT, FAA, FAB, FAE, PRE
        global opcao, setor, atendimento, tela, opc, sigla_db
        atendimento = atend[0]
        sigla_db = opcao
        opcao = 'P.' + opcao
        threading.Thread(target=self.gerar_senha).start()
        self.abrir_janela_espera()
        if tela == 1:
            self.root_premir.destroy()
        elif tela == 2:
            self.root_premir.destroy()
        elif tela == 3:
            self.root_premir.destroy()
            self.rootConsultas.destroy() #Destruir janela 2 Consultas
        elif tela == 4:
            self.root_farmacia.destroy()
            self.root_AB.destroy() #Destruir janela 20
        elif tela == 5:
            self.root_farmacia.destroy()
            self.root_FE.destroy() #Destruir janela 200
        elif tela == 6:
            self.root_farmacia.destroy()
            self.root_FAC.destroy() #Destruir janela 2000
        elif tela == 7:
            self.rootAE.destroy() #Destruir janela 21
        elif tela == 8:
            self.rootTFD.destroy() #Destruir janela 2
        elif tela == 9:
            self.rootCSUS.destroy()


    def gerar_senha(self):
        verificar_filaEspera()
        global opcao, senha, setor, atendimento, opc, sigla_db
        with connect_server() as conexao: #chama a função para conectar ao banco mysql
            with conexao.cursor() as cursor:
                #caso exista uma sequencia para a opção selecionada na consulta, gera uma senha sequencial.
                if  cursor.execute(f'SELECT senha FROM {tabela} WHERE id IN (SELECT MAX(id) FROM {tabela} WHERE setor = "{setor}" AND atendimento = "{atendimento}");')>0: #realiza consulta em banco
                    resultado = str(cursor.fetchone()['senha']) #retorna resultado da consulta
                    if atendimento == "preferencial": #Preferencial
                        resultado = int(resultado[5:])+1 #converte o resutado, fatiando apenas os valores
                    else: # Convencional
                        resultado = int(resultado[3:])+1 #converte o resutado, fatiando apenas os valores

                    resultado = str(resultado).rjust(3,'0') # adiciona 3 digitos ao resultado
                    senha = opcao + str(resultado) #seta senha
                    sql = f"INSERT INTO {tabela} (setor, opcao, atendimento, senha, data, status) VALUES ('{setor}','{sigla_db}','{atendimento}','{senha}','{data}', 'ESPERA')"  #seta intrução sql
                
                else: #caso não exista uma sequencia para a opção selecionada na consulta, gera uma nova opcao no bloco else. 
                    senha = opcao + str('001') #seta opcao
                    sql = f"INSERT INTO {tabela} (setor, opcao, atendimento, senha, data, status) VALUES ('{setor}','{sigla_db}','{atendimento}','{senha}','{data}', 'ESPERA')"  #seta intrução sql

                cursor.execute(sql) #executa instrução sql
                conexao.commit() #commit para o interprertador entender que deve executar a instrução
                imprimir(senha, setor, atendimento)


###############################################      PREMIR      ###############################################

    ###Função para Tela Premir###
    def abrir_janela_Premir(self):
        global ref
        ref = 1
        self.horario_ex()
    
    def ultrassom(self):
        global senha, setor, set, atendimento, tela, opcao, opc
        opcao= opc[8]
        setor= set[1] 
        tela = 1
        self.fechar_conv()

    def multiprofissionais(self):
        global senha, setor, set, atendimento, tela, opcao, opc
        opcao= opc[6]
        setor= set[1] 
        tela = 2
        self.fechar_conv()
        
    def premir(self):
        self.root_premir = tk.Toplevel()#Abertura da Tela 4 de Opções do Premir
        self.root_premir.configure(background= cores[0]) #Cor do plano de fundo da tela 
        self.root_premir.attributes('-fullscreen', True) #Código que faz com que a tela fique em Fullscreen
        self.frame_premir =Frame(self.root_premir, bd = 4, bg = cores[0]) #Frame definido para a tela 4 com fundo branco
        self.frame_premir.place(anchor='center',relx= 0.5,rely= 0.5, relwidth= 0.96, relheight= 0.96) #Definição do local do frame expresso em porcentagem de tela

        #Imagens na Tela 
        self.fundo_premir = PhotoImage(file= planos[0]) #Plano de fundo principal
        self.bloco = PhotoImage(file= bloco[1]) #Blocos de Cores


        figura_fundo_premir = Label(self.frame_premir, image= self.fundo_premir, bd= 0) #Chamando imagem 
        figura_fundo_premir.place(anchor= 'center',relx=0.5, rely=0.4, width= 550, height= 500) #Localizando a imagem na tela

        bloco_meio = Label(self.frame_premir, image= self.bloco, bd= 0) #Chamando imagem 
        bloco_meio.place(anchor = "center", relx=0.17, rely=0.65) #Localizando a imagem na tela

        bloco_esquerda = Label(self.frame_premir, image= self.bloco, bd= 0) #Chamando imagem 
        bloco_esquerda.place(anchor = "center", relx=0.5, rely=0.65) #Localizando a imagem na tela

        bloco_direita = Label(self.frame_premir, image= self.bloco, bd= 0) #Chamando imagem
        bloco_direita.place(anchor = "center", relx=0.83, rely=0.65) #Localizando a imagem na tela

        fontexemplo0 = tkFont.Font(family= 'Arial Black', size= 15) #Definindo Variavel para fonte padrão
        fontexemplo33 = tkFont.Font(family= 'Arial Black', size= 10) #Definindo Variavel para fonte padrão

        self.bt_consultas = PhotoImage(file = bt[7]) #Imagem botão Consultas
        self.btPconsultas = Button(self.frame_premir, image= self.bt_consultas, relief=FLAT, bd= 0, command= self.abrir_janela_Consultas) #Adicionando a imagem a um botão
        self.btPconsultas.place(anchor='center',relx= 0.5, rely=0.47, width= 270, height= 80) #Localizando o botão na tela

        self.bt_ultrassom = PhotoImage(file= bt[11]) #Imagem botão Ultrassom
        self.btult = Button(self.frame_premir, image= self.bt_ultrassom, relief=FLAT, bd= 0, command= self.ultrassom) #Adicionando a imagem a um botão
        self.btult.place(anchor='center',relx= 0.83, rely=0.47, width= 270, height= 80) #Localizando o botão na tela

        self.bt_multi = PhotoImage(file = bt[9]) #Imagem botão Multiprofissionais
        self.btmult = Button(self.frame_premir, image= self.bt_multi, relief=FLAT, bd= 0, command= self.multiprofissionais) #Adicionando a imagem a um botão
        self.btmult.place(anchor='center', relx= 0.17, rely=0.47, width= 270, height= 80) #Localizando o botão na tela

        self.btconsultas2 = Button(self.frame_premir, text = f"•{esp[0]} \n•{esp[1]} \n•{esp[2]} \n•{esp[3]} \n•{esp[4]} \n•{esp[5]} \n•{esp[6]} \n•{esp[7]}", relief = FLAT, bd = 0, background = cores[4], activebackground = cores[4], command= self.abrir_janela_Consultas) #Adicionando texto a um botão
        self.btconsultas2.configure(font = fontexemplo0) #Configuração fonte padrão
        self.btconsultas2.place(anchor = "center", relx= 0.5, rely=0.7, width= 270, height= 250)  #Localizando o botão na tela
        
        self.btult2 = Button(self.frame_premir, text = "•Agendamento \n•Resultado de \nExames", relief = FLAT, bd = 0, background = cores[4], activebackground = cores[4], command= self.ultrassom) #Adicionando texto a um botão
        self.btult2.configure(font = fontexemplo0) #Configuração fonte padrão
        self.btult2.place(anchor = "center", relx= 0.83, rely=0.7, width= 270, height= 80)  #Localizando o botão na tela
        
        self.btmult2 = Button(self.frame_premir, text = "Multiprofissonais: \n\n•Psícologa \n•Terapia Ocupacional \n•Assistente Social \n •Fonoaudióloga", relief = FLAT, bd = 0, background = cores[4], activebackground = cores[4], command= self.multiprofissionais) #Adicionando texto a um botão
        self.btmult2.configure(font = fontexemplo0) #Configuração fonte padrão
        self.btmult2.place(anchor = "center", relx= 0.17, rely=0.67, width= 270, height= 220)  #Localizando o botão na tela

        self.mult2 = Label(self.frame_premir, text= "*A senha Multiprofissionais atende \na todos os profissionais acima!", background= cores[4])
        self.mult2.configure(font = fontexemplo33)
        self.mult2.place(anchor = "center", relx= 0.17, rely=0.85, width= 270, height= 50)  #Localizando o botão na tela

        self.bt_voltar = PhotoImage(file = bt[12]) #Imagem botão Voltar
        self.btvoltar = Button(self.frame_premir, image = self.bt_voltar, relief=FLAT, bd = 0, command= self.root_premir.destroy) #Adicionando a imagem a um botão
        self.btvoltar.place(anchor='center', relx= 0.13, rely=0.08, width= 200, height= 80) #Localizando o botão na tela

    ###Função Escolha Preferencial ou Convencional PREMIR Consultas###
    def abrir_janela_Consultas(self): 
        self.rootConsultas = tk.Toplevel() #Variavel para atribuir tela principal
        self.rootConsultas.configure(background= cores[0]) #Cor de fundo
        self.rootConsultas.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
        self.fullScreenState = False
        self.frameConsultas =Frame(self.rootConsultas, bg = cores[0]) #Definindo um Frame para a tela 
        self.frameConsultas.place(anchor='center',relx= 0.5,rely= 0.5, relwidth= 0.96, relheight= 0.96)  #Localizando o Frame na tela 
        global senha, setor, set, atendimento, tela, opcao, opc
        opcao= opc[7]
        setor= set[1] 
        tela = 3

        #Imagens na Tela 
        self.fundo_Consultas = PhotoImage(file= planos[1]) #Plano de fundo principal
        figura_fundo_Consultas = Label(self.frameConsultas, image= self.fundo_Consultas, bd= 0) #Chamando imagem 
        figura_fundo_Consultas.place(anchor= 'center',relx=0.5, rely=0.4, width= 550, height= 500) #Localizando a imagem na tela

        self.bt_conv_cons = PhotoImage(file= bt[8]) #Chamando imagem 
        self.figura_bt_conv_cons = Button(self.frameConsultas, image=self.bt_conv_cons, relief=FLAT, bd = 0, command= self.fechar_conv) #Adicionando a imagem a um botão
        self.figura_bt_conv_cons.place(anchor = "center", relx= 0.5, rely=0.5, width= 510, height= 150) #Localizando o botão na tela

        self.bt_prefe_cons = PhotoImage(file= bt[10]) #Chamando imagem 
        self.figura_bt_prefe_cons = Button(self.frameConsultas, image=self.bt_prefe_cons, relief=FLAT, bd = 0, command= self.fechar_prefe)
        self.figura_bt_prefe_cons.place(anchor = "center", relx= 0.5, rely=0.75, width= 510, height= 150) #Localizando o botão na tela

        self.aviso = Label(self.frameConsultas, bg= cores[0], text="*As pessoas portadoras de deficiência, os idosos com idade igualou superior a 60 (sessenta) anos,\nas gestantes, as lactantes e as pessoas acompanhadas por crianças de colo terão\natendimento prioritário")
        self.aviso.configure(font=fontes[0])
        self.aviso.place(anchor='center', relx= 0.5, rely=0.95) #Localizando o botão na tela 

        self.bt_voltar_cons = PhotoImage(file = bt[12]) #Chamando imagem 
        self.figura_bt_voltar_cons = Button(self.frameConsultas, image = self.bt_voltar_cons, relief=FLAT, bd = 0, command= self.rootConsultas.destroy) #Adicionando a imagem a um botão
        self.figura_bt_voltar_cons.place(anchor='center', relx= 0.13, rely=0.08, width= 200, height= 80) #Localizando o botão na tela



###############################################      FARMACIAS      ###############################################
    ###Função para Tela Farmacias###
    def abrir_janela_Farmacias(self):
        global ref
        ref = 2
        self.horario_ex()

    def farmacia(self):
        self.root_farmacia = tk.Toplevel()#Abertura da tela de opções da farmacia
        self.root_farmacia.configure(background= cores[0]) #Cor do plano de fundo da tela 
        self.root_farmacia.attributes('-fullscreen', True) #Código que faz com que a tela fique em Fullscreen
        self.frame_farmacia =Frame(self.root_farmacia, bd = 4, bg = cores[0]) #Frame definido para a tela 4 com fundo branco
        self.frame_farmacia.place(anchor='center',relx= 0.5,rely= 0.5, relwidth= 0.96, relheight= 0.96) #Definição do local do frame expresso em porcentagem de tela

        #Imagens na Tela 
        self.fundo_farmacia = PhotoImage(file= planos[0]) #Plano de fundo principal
        self.bloco_farmacia = PhotoImage(file= bloco[1]) #Blocos de Cores
        

        figura_fundo_farmacia = Label(self.frame_farmacia, image= self.fundo_farmacia, bd= 0) #Chamando imagem1
        figura_fundo_farmacia.place(anchor= 'center',relx=0.5, rely=0.4, width= 550, height= 500) #Localizando a imagem na tela

        figura_bloco_esquerda = Label(self.frame_farmacia, image= self.bloco_farmacia, bd= 0) #Chamando imagem 
        figura_bloco_esquerda.place(anchor = "center", relx=0.17, rely=0.65) #Localizando a imagem na tela

        figura_meio = Label(self.frame_farmacia, image= self.bloco_farmacia, bd= 0) #Chamando imagem 
        figura_meio.place(anchor = "center", relx=0.5, rely=0.65) #Localizando a imagem na tela

        figura_direita = Label(self.frame_farmacia, image= self.bloco_farmacia, bd= 0) #Chamando imagem
        figura_direita.place(anchor = "center", relx=0.83, rely=0.65) #Localizando a imagem na tela

        fontexemplo0 = tkFont.Font(family= 'Arial Black', size= 18) #Definindo Variavel para fonte padrão

        self.bt_imgFAC= PhotoImage(file = bt[2]) #Imagem botão Farmacia Auto-custo
        self.btFAC = Button(self.frame_farmacia, image= self.bt_imgFAC, relief=FLAT, bd= 0, command= self.abrir_janela_AutoCusto) #Adicionando a imagem a um botão
        self.btFAC.place(anchor = "center", relx= 0.17, rely=0.47, width= 270, height= 90) #Localizando o botão na tela
    
        self.bt_imgFAB = PhotoImage(file= bt[3]) #Imagem botão Farmacia Atenção Básica
        self.btFAB = Button(self.frame_farmacia, image= self.bt_imgFAB, relief=FLAT, bd= 0, command= self.abrir_janela_AtencaoBasica) #Adicionando a imagem a um botão
        self.btFAB.place(anchor = "center", relx= 0.5, rely=0.47, width= 270, height= 90) #Localizando o botão na tela

        self.bt_imgFE = PhotoImage(file = bt[4]) #Imagem botão Farmacia Estado
        self.btFE = Button(self.frame_farmacia, image= self.bt_imgFE, relief=FLAT, bd= 0, command= self.abrir_janela_Estado) #Adicionando a imagem a um botão
        self.btFE.place(anchor = "center", relx= 0.83, rely=0.47, width= 270, height= 90) #Localizando o botão na tela

        self.bt_img_FA = Button(self.frame_farmacia, text= 'Convenio Municípal \n\nFarmâcias Externas \nconveniadas ao \nMunicípio \n', relief = FLAT, bd = 0, background = cores[4], activebackground = cores[4], command= self.abrir_janela_AutoCusto)
        self.bt_img_FA.place(anchor = "center", relx= 0.17, rely=0.73, width= 270, height= 200) #Localizando o botão na tela
        self.bt_img_FA.configure(font= fontexemplo0)

        self.bt_img_FAB = Button(self.frame_farmacia, text= 'CBAF \n\nMedicamentos \nfornecidos pelo \nMunicípio \n', relief = FLAT, bd = 0, background = cores[4], activebackground = cores[4], command= self.abrir_janela_AtencaoBasica)
        self.bt_img_FAB.place(anchor = "center", relx= 0.5, rely=0.73, width= 270, height= 200) #Localizando o botão na tela
        self.bt_img_FAB.configure(font= fontexemplo0)

        self.bt_img_FE = Button(self.frame_farmacia, text= 'CEAF \n\nMedicamentos \nretirados apartir \ndo Estado ou \nJudicial', relief = FLAT, bd = 0, background = cores[4], activebackground = cores[4], command= self.abrir_janela_Estado)
        self.bt_img_FE.place(anchor = "center", relx= 0.83, rely=0.73, width= 270, height= 200) #Localizando o botão na tela
        self.bt_img_FE.configure(font= fontexemplo0)
        
        self.bt_img_voltar = PhotoImage(file = bt[12]) #Imagem botão Voltar 
        self.bt_voltar_farmacias = Button(self.frame_farmacia, image = self.bt_img_voltar, relief=FLAT, bd = 0, command= self.root_farmacia.destroy) #Adicionando a imagem a um botão
        self.bt_voltar_farmacias.place(anchor='center', relx= 0.13, rely=0.08, width= 200, height= 80) #Localizando o botão na tela
        
    ###Função Escolha Preferencial ou Convencional FARMACIA BASICA###
    def abrir_janela_AtencaoBasica(self):
        global senha, setor, set, atendimento, tela, opcao, opc, farmaciaStop
        opcao= opc[4]
        setor= set[4] 
        tela = 4

        if hora_atual >= farmaciaStop:
            self.root_hrExcede()
        else:
            self.root_AB = tk.Toplevel() #Variavel para atribuir tela principal
            self.root_AB.configure(background= cores[0]) #Cor de fundo
            self.root_AB.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
            self.fullScreenState = False 
            self.frame_AB =Frame(self.root_AB, bg = cores[0]) #Definindo um Frame para a tela 
            self.frame_AB.place(anchor='center',relx= 0.5,rely= 0.5, relwidth= 0.96, relheight= 0.96) #Localizando o Frame na tela 
            
            #Imagens na Tela 
            self.fundo_AB = PhotoImage(file= planos[1]) #Plano de fundo principal
            figura_fundo_AB = Label(self.frame_AB, image= self.fundo_AB, bd= 0) #Chamando imagem 
            figura_fundo_AB.place(anchor= 'center',relx=0.5, rely=0.4, width= 550, height= 500) #Localizando a imagem na tela

            self.btconv_imgAB = PhotoImage(file= bt[8]) #Imagem Botão Convencional
            self.btconv_AB = Button(self.frame_AB, image=self.btconv_imgAB, relief=FLAT, bd = 0, command= self.fechar_conv) #Adicionando a imagem a um botão
            self.btconv_AB.place(anchor = "center", relx= 0.5, rely=0.5, width= 510, height= 150) #Localizando o botão na tela

            self.btprefe_imgAB = PhotoImage(file= bt[10]) #Imagem Botão Preferencial
            self.btprefe_AB = Button(self.frame_AB, image=self.btprefe_imgAB, relief=FLAT, bd = 0, command= self.fechar_prefe) #Adicionando a imagem a um botão
            self.btprefe_AB.place(anchor = "center", relx= 0.5, rely=0.75, width= 510, height= 150) #Localizando o botão na tela

            self.aviso = Label(self.frame_AB, bg= cores[0], text="*As pessoas portadoras de deficiência, os idosos com idade igualou superior a 60 (sessenta) anos,\nas gestantes, as lactantes e as pessoas acompanhadas por crianças de colo terão\natendimento prioritário")
            self.aviso.configure(font=fontes[0])
            self.aviso.place(anchor='center', relx= 0.5, rely=0.95) #Localizando o botão na tela 

            self.btvoltar_imgAB = PhotoImage(file = bt[12]) #Imagem Botão Voltar 
            self.btvoltar_AB = Button(self.frame_AB, image = self.btvoltar_imgAB, relief=FLAT, bd = 0, command= self.root_AB.destroy) #Adicionando a imagem a um botão
            self.btvoltar_AB.place(anchor='center', relx= 0.13, rely=0.08, width= 200, height= 80) #Localizando o botão na tela
    
    ###Função Escolha Preferencial ou Convencional FARMACIA ESTADO###
    def abrir_janela_Estado(self):
        global senha, setor, set, atendimento, tela, opcao, opc, hora_atual, farmaciaStop
        opcao= opc[2]
        setor= set[2] 
        tela = 5
        
        if hora_atual >= farmaciaStop:
            self.root_hrExcede()
        else:
            with connect_server() as conexao:
                with conexao.cursor() as cursor:
                    try:
                        if cursor.execute('SELECT config FROM settings WHERE option="F.ESTADO";')>0:
                            src = cursor.fetchone()
                            resultado = src['config']
                    except:
                        print('erro consulta')
            
                if resultado == 'LIBERADO':
                    self.root_FE = tk.Toplevel() #Variavel para atribuir tela principal
                    self.root_FE.configure(background= cores[0]) #Cor de fundo
                    self.root_FE.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
                    self.fullScreenState = False
                    self.frame_FE =Frame(self.root_FE, bg = cores[0]) #Definindo um Frame para a tela 
                    self.frame_FE.place(anchor='center',relx= 0.5,rely= 0.5, relwidth= 0.96, relheight= 0.96) #Localizando o Frame na tela 
                    
                    #Imagens na Tela 
                    self.fundo_FE = PhotoImage(file= planos[1]) #Plano de fundo principal
                    figura_fundo_FE = Label(self.frame_FE, image= self.fundo_FE, bd= 0) #Chamando imagem 
                    figura_fundo_FE.place(anchor= 'center',relx=0.5, rely=0.4, width= 550, height= 500) #Localizando a imagem na tela

                    self.photo2200 = PhotoImage(file= bt[8]) #Imagem Botão Convencional
                    self.btconv = Button(self.frame_FE, image=self.photo2200, relief=FLAT, bd = 0, command= self.fechar_conv) #Adicionando a imagem a um botão
                    self.btconv.place(anchor = "center", relx= 0.5, rely=0.5, width= 510, height= 150) #Localizando o botão na tela

                    self.btprefe_imgFE = PhotoImage(file= bt[10]) #Imagem Botão Preferencial
                    self.btprefe_FE = Button(self.frame_FE, image=self.btprefe_imgFE, relief=FLAT, bd = 0, command= self.fechar_prefe) #Adicionando a imagem a um botão
                    self.btprefe_FE.place(anchor = "center", relx= 0.5, rely=0.75, width= 510, height= 150) #Localizando o botão na tela

                    self.aviso = Label(self.frame_FE, bg= cores[0], text="*As pessoas portadoras de deficiência, os idosos com idade igualou superior a 60 (sessenta) anos,\nas gestantes, as lactantes e as pessoas acompanhadas por crianças de colo terão\natendimento prioritário")
                    self.aviso.configure(font=fontes[0])
                    self.aviso.place(anchor='center', relx= 0.5, rely=0.95) #Localizando o botão na tela 

                    self.btvoltar_imgFE = PhotoImage(file = bt[12]) #Imagem Botão Voltar 
                    self.btvoltar_FE = Button(self.frame_FE, image = self.btvoltar_imgFE, relief=FLAT, bd = 0, command= self.root_FE.destroy) #Adicionando a imagem a um botão
                    self.btvoltar_FE.place(anchor='center', relx= 0.13, rely=0.08, width= 200, height= 80) #Localizando o botão na tela
                
                else:
                    self.root_bloq = tk.Toplevel() #Variavel para atribuir tela principal
                    self.root_bloq.title('Sistema de Senhas Secretaria Municipal de Saúde.') #Atribuir titulo a tela
                    self.root_bloq.configure(background= cores[2]) #Cor de fundo
                    self.root_bloq.geometry("1000x700") #Dimensões do tamanho da tela cheia
                    self.root_bloq.attributes('-alpha', 0.0)
                    self.root_bloq.resizable(False, False) #Negar o redimensionamento da tela
                    self.root_bloq.minsize(width=800, height= 500) #Definir tamanho minimo da tela   
                    self.frame_bloq =Frame(self.root_bloq, bg = cores[0]) #Definindo um Frame para a tela 
                    self.frame_bloq.place(anchor='center',relx= 0.5,rely= 0.5, relwidth= 0.96, relheight= 0.96) #Localizando o Frame na tela 

                    self.photo_bloq = PhotoImage(file= fr"{get_dir}\Plano de Fundo\Plano de Fundo horarios.png")
                    self.logo_bloq = Label(self.frame_bloq, image= self.photo_bloq, background= cores[0])
                    self.logo_bloq.place(anchor="center", relx=0.5, rely=0.5)

                    self.aviso = Label(self.frame_bloq, text="A fila de espera para \neste Atendimento está \nLOTADA", background= cores[0], foreground= "red")
                    self.aviso.configure(font= tkFont.Font(family="Arial", size=45, weight="bold"))
                    self.aviso.place(anchor='center', relx= 0.5, rely= 0.5)

                    self.aviso3 = Label(self.frame_bloq, text= "Agradecemos a sua Compreensão!", background= cores[0])
                    self.aviso3.configure(font= tkFont.Font(family="Arial", size=25))
                    self.aviso3.place(anchor='center', relx= 0.5, rely= 0.86)

                    ###Código para janela abrir no meio da tela###
                    self.root_bloq.update_idletasks()
                    width = self.root_bloq.winfo_width()
                    frm_width = self.root_bloq.winfo_rootx() - self.root_bloq.winfo_x()
                    win_width = width + 2 * frm_width

                    height = self.root_bloq.winfo_height()
                    titlebar_height = self.root_bloq.winfo_rooty() - self.root_bloq.winfo_y()
                    win_height = height + titlebar_height + frm_width

                    x = self.root_bloq.winfo_screenwidth() // 2 - win_width // 2
                    y = self.root_bloq.winfo_screenheight() // 2 - win_height // 2
                    self.root_bloq.geometry('{}x{}+{}+{}'.format(width, height, x, y))
                    self.root_bloq.deiconify()
                    
                    self.root_bloq.attributes('-alpha', 1.0)
                    self.root_bloq.overrideredirect(True)
                    self.root_bloq.after(8000,self.root_bloq.destroy)
        
    ###Função Escolha Preferencial ou Convencional FARMACIA AUTO-CUSTO###
    def abrir_janela_AutoCusto(self): 
        global senha, setor, set, atendimento, tela, opcao, opc
        opcao= opc[5]
        setor= set[5] 
        tela = 6

        self.root_FAC = tk.Toplevel() #Variavel para atribuir tela principal
        self.root_FAC.configure(background= cores[0]) #Cor de fundo
        self.root_FAC.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
        self.fullScreenState = False
        self.frame_FAC =Frame(self.root_FAC, bg = cores[0]) #Definindo um Frame para a tela 
        self.frame_FAC.place(anchor='center',relx= 0.5,rely= 0.5, relwidth= 0.96, relheight= 0.96) #Localizando o Frame na tela 
        
        #Imagens na Tela 
        self.fundo_FAC = PhotoImage(file= planos[1]) #Plano de fundo principal
        figura_fundo_FAC = Label(self.frame_FAC, image= self.fundo_FAC, bd= 0) #Chamando imagem 
        figura_fundo_FAC.place(anchor= 'center',relx=0.5, rely=0.4, width= 550, height= 500) #Localizando a imagem na tela

        self.btconv_imgFAC = PhotoImage(file= bt[8]) #Imagem Botão Convencional
        self.btconv_FAC = Button(self.frame_FAC, image=self.btconv_imgFAC, relief=FLAT, bd = 0, command= self.fechar_conv) #Adicionando a imagem a um botão
        self.btconv_FAC.place(anchor = "center", relx= 0.5, rely=0.5, width= 510, height= 150) #Localizando o botão na tela

        self.btprefe_imgFAC = PhotoImage(file= bt[10]) #Imagem Botão Preferencial
        self.btprefe_FAC = Button(self.frame_FAC, image=self.btprefe_imgFAC, relief=FLAT, bd = 0, command= self.fechar_prefe) #Adicionando a imagem a um botão
        self.btprefe_FAC.place(anchor = "center", relx= 0.5, rely=0.75, width= 510, height= 150) #Localizando o botão na tela

        self.aviso = Label(self.frame_FAC, bg= cores[0], text="*As pessoas portadoras de deficiência, os idosos com idade igualou superior a 60 (sessenta) anos,\nas gestantes, as lactantes e as pessoas acompanhadas por crianças de colo terão\natendimento prioritário")
        self.aviso.configure(font=fontes[0])
        self.aviso.place(anchor='center', relx= 0.5, rely=0.95) #Localizando o botão na tela 

        self.btvoltar_imgFAC = PhotoImage(file = bt[12]) #Imagem Botão Voltar 
        self.btvoltar_FAC = Button(self.frame_FAC, image = self.btvoltar_imgFAC, relief=FLAT, bd = 0, command= self.root_FAC.destroy) #Adicionando a imagem a um botão
        self.btvoltar_FAC.place(anchor='center', relx= 0.13, rely=0.08, width= 200, height= 80) #Localizando o botão na tela   



###############################################      AUTORIZAÇÃO DE EXAMES      ###############################################

    ###Função Escolha Preferencial ou Convencional AUTORIZAÇÃO DE EXAMES###
    def abrir_janela_AE(self):
        global ref
        ref = 3
        self.horario_ex()
        
    def aut_exa(self):
        self.rootAE = tk.Toplevel() #Variavel para atribuir tela principal
        self.rootAE.configure(background= cores[0]) #Cor de fundo
        self.rootAE.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
        self.fullScreenState = False
        self.frameAE =Frame(self.rootAE, bg = cores[0]) #Definindo um Frame para a tela 
        self.frameAE.place(anchor='center',relx= 0.5,rely= 0.5, relwidth= 0.96, relheight= 0.96) #Localizando o Frame na tela
        global senha, setor, set, atendimento, tela, opcao, opc
        opcao = opc[5]
        setor= set[5]
        tela = 7

        #Imagens na Tela 
        self.fundo_AE = PhotoImage(file= planos[1]) #Plano de fundo principal
        figura_fundo_AE = Label(self.frameAE, image= self.fundo_AE, bd= 0) #Chamando imagem 
        figura_fundo_AE.place(anchor= 'center',relx=0.5, rely=0.4, width= 550, height= 500) #Localizando a imagem na tela

        self.btconv_imgAE = PhotoImage(file= bt[8]) #Imagem Botão Convencional
        self.btconv_AE = Button(self.frameAE, image=self.btconv_imgAE, relief=FLAT, bd = 0, command= self.fechar_conv) #Adicionando a imagem a um botão
        self.btconv_AE.place(anchor = "center", relx= 0.5, rely=0.5, width= 510, height= 150) #Localizando o botão na tela

        self.btprefe_imgAE = PhotoImage(file= bt[10]) #Imagem Botão Preferencial
        self.btprefe_AE = Button(self.frameAE, image=self.btprefe_imgAE, relief=FLAT, bd = 0, command= self.fechar_prefe) #Adicionando a imagem a um botão
        self.btprefe_AE.place(anchor = "center", relx= 0.5, rely=0.75, width= 510, height= 150) #Localizando o botão na tela

        self.aviso = Label(self.frameAE, bg= cores[0], text="*As pessoas portadoras de deficiência, os idosos com idade igualou superior a 60 (sessenta) anos,\nas gestantes, as lactantes e as pessoas acompanhadas por crianças de colo terão\natendimento prioritário")
        self.aviso.configure(font=fontes[0])
        self.aviso.place(anchor='center', relx= 0.5, rely=0.95) #Localizando o botão na tela 

        self.btvoltar_imgAE = PhotoImage(file = bt[12]) #Imagem Botão Voltar 
        self.btvoltar_AE = Button(self.frameAE, image = self.btvoltar_imgAE, relief=FLAT, bd = 0, command= self.rootAE.destroy) #Adicionando a imagem a um botão
        self.btvoltar_AE.place(anchor='center', relx= 0.13, rely=0.08, width= 200, height= 80) #Localizando o botão na tela 



###############################################      TFD      ###############################################
    
    ###Função Escolha Preferencial ou Convencional TFD###
    def abrir_janela_TFD(self): 
        global ref
        ref = 4
        self.horario_ex()
        
    def tfd(self):
        self.rootTFD = tk.Toplevel() #Variavel para atribuir tela principal
        self.rootTFD.configure(background= cores[0]) #Cor de fundo
        self.rootTFD.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
        self.fullScreenState = False
        self.frameTFD =Frame(self.rootTFD, bg = cores[0]) #Definindo um Frame para a tela 
        self.frameTFD.place(anchor='center',relx= 0.5,rely= 0.5, relwidth= 0.96, relheight= 0.96)  #Localizando o Frame na tela 
        global opcao, setor, set, atendimento, tela, opc
        opcao= opc[0]
        setor= set[0] 
        tela = 8

        #Imagens na Tela 
        self.fundo_TFD = PhotoImage(file= planos[1]) #Plano de fundo principal
        figura_fundo_TFD = Label(self.frameTFD, image= self.fundo_TFD, bd= 0) #Chamando imagem 
        figura_fundo_TFD.place(anchor= 'center',relx=0.5, rely=0.4, width= 550, height= 500) #Localizando a imagem na tela

        self.bt_conv_tfd = PhotoImage(file= bt[8]) #Chamando imagem 
        self.figura_bt_conv_tfd = Button(self.frameTFD, image=self.bt_conv_tfd, relief=FLAT, bd = 0, command= self.fechar_conv) #Adicionando a imagem a um botão
        self.figura_bt_conv_tfd.place(anchor = "center", relx= 0.5, rely=0.5, width= 510, height= 150) #Localizando o botão na tela

        self.bt_prefe_tfd = PhotoImage(file= bt[10]) #Chamando imagem 
        self.figura_bt_prefe_tfd = Button(self.frameTFD, image=self.bt_prefe_tfd, relief=FLAT, bd = 0, command= self.fechar_prefe)
        self.figura_bt_prefe_tfd.place(anchor = "center", relx= 0.5, rely=0.75, width= 510, height= 150) #Localizando o botão na tela

        self.aviso = Label(self.frameTFD, bg= cores[0], text="*As pessoas portadoras de deficiência, os idosos com idade igualou superior a 60 (sessenta) anos,\nas gestantes, as lactantes e as pessoas acompanhadas por crianças de colo terão\natendimento prioritário")
        self.aviso.configure(font=fontes[0])
        self.aviso.place(anchor='center', relx= 0.5, rely=0.95) #Localizando o botão na tela 

        self.bt_voltar_tfd = PhotoImage(file = bt[12]) #Chamando imagem 
        self.figura_bt_voltar_tfd = Button(self.frameTFD, image = self.bt_voltar_tfd, relief=FLAT, bd = 0, command= self.rootTFD.destroy) #Adicionando a imagem a um botão
        self.figura_bt_voltar_tfd.place(anchor='center', relx= 0.13, rely=0.08, width= 200, height= 80) #Localizando o botão na tela 



###############################################      Cartão SUS      ###############################################

    ###Função Escolha Preferencial ou Convencional AUTORIZAÇÃO DE EXAMES###
    def abrir_janela_CSUS(self):
        global ref
        ref = 5
        self.horario_ex()
        
    def cartao_sus(self):
        self.rootCSUS = tk.Toplevel() #Variavel para atribuir tela principal
        self.rootCSUS.configure(background= cores[0]) #Cor de fundo
        self.rootCSUS.attributes('-fullscreen', True) #Modo tela Fullscreen ligado
        self.fullScreenState = False
        self.frameCSUS =Frame(self.rootCSUS, bg = cores[0]) #Definindo um Frame para a tela 
        self.frameCSUS.place(anchor='center',relx= 0.5,rely= 0.5, relwidth= 0.96, relheight= 0.96) #Localizando o Frame na tela
        global opcao, opc, atendimento, tela, setor, set
        opcao = opc[9]
        setor = set[6]
        tela = 9

        #Imagens na Tela 
        self.fundo_CSUS = PhotoImage(file= planos[1]) #Plano de fundo principal
        figura_fundo_CSUS = Label(self.frameCSUS, image= self.fundo_CSUS, bd= 0) #Chamando imagem 
        figura_fundo_CSUS.place(anchor= 'center',relx=0.5, rely=0.4, width= 550, height= 500) #Localizando a imagem na tela

        self.btconv_imgCSUS = PhotoImage(file= bt[8]) #Imagem Botão Convencional
        self.btconv_CSUS = Button(self.frameCSUS, image=self.btconv_imgCSUS, relief=FLAT, bd = 0, command= self.fechar_conv) #Adicionando a imagem a um botão
        self.btconv_CSUS.place(anchor = "center", relx= 0.5, rely=0.5, width= 510, height= 150) #Localizando o botão na tela

        self.btprefe_imgCSUS = PhotoImage(file= bt[10]) #Imagem Botão Preferencial
        self.btprefe_CSUS = Button(self.frameCSUS, image=self.btprefe_imgCSUS, relief=FLAT, bd = 0, command= self.fechar_prefe) #Adicionando a imagem a um botão
        self.btprefe_CSUS.place(anchor = "center", relx= 0.5, rely=0.75, width= 510, height= 150) #Localizando o botão na tela

        self.aviso = Label(self.frameCSUS, bg= cores[0], text="*As pessoas portadoras de deficiência, os idosos com idade igualou superior a 60 (sessenta) anos,\nas gestantes, as lactantes e as pessoas acompanhadas por crianças de colo terão\natendimento prioritário")
        self.aviso.configure(font=fontes[0])
        self.aviso.place(anchor='center', relx= 0.5, rely=0.95) #Localizando o botão na tela 

        self.btvoltar_imgCSUS = PhotoImage(file = bt[12]) #Imagem Botão Voltar 
        self.btvoltar_CSUS = Button(self.frameCSUS, image = self.btvoltar_imgCSUS, relief=FLAT, bd = 0, command= self.rootCSUS.destroy) #Adicionando a imagem a um botão
        self.btvoltar_CSUS.place(anchor='center', relx= 0.13, rely=0.08, width= 200, height= 80) #Localizando o botão na tela 


