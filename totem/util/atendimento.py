from util.modulos import *
from util.listas import *
from util.aut_exames.aut_exames import *

class fechar(aut_exames):
    ###Funções de Fechamento de cada tela###
    def fechar_conv(self): #Função fechamento de tela Conv. do TFD, AUT, FAA, FAB, FAE, PRE
        global senha, opc, atendimento, tela
        atendimento = atend[1]
        threading.Thread(target=self.abrir_janela_espera())
        threading.Thread(target=self.gerar_senha).start()
        if tela == 1:
            self.root_premir.destroy()
            self.rootMult.destroy() #Destruir janela 2 Mult
        elif tela == 2:
            self.root_premir.destroy()
            self.rootUltrassom.destroy() #Destruir janela 2 Ultrassom
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

    def fechar_prefe(self): #Função fechamento de tela Pref. do TFD, AUT, FAA, FAB, FAE, PRE
        global senha, opc, atendimento, tela, senhal
        atendimento = atend[0]
        senha = 'P' + senha
        threading.Thread(target=self.gerar_senha).start()
        self.abrir_janela_espera()
        if tela == 1:
            self.root_premir.destroy()
            self.rootMult.destroy() #Destruir janela 2 Mult
        elif tela == 2:
            self.root_premir.destroy()
            self.rootUltrassom.destroy() #Destruir janela 2 Ultrassom
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