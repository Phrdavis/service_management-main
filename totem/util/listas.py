import os
# from datetime import datetime, date               
from util.modulos import *

###Definindo variaveis para especialidades###
esp = [
    "Clínico Geral",
    "Ginecologista",
    "Obstetrícia",
    "Pediatra",
    "Cardiologista",
    "Dermatologista",
    "Pequenas Cirurgias",
    "Ortopedista"
    ]
###Definindo variaveis para senha###
set = [
    "TFD", 
    "PREMIR",
    "F.ESTADO", 
    "F.AUTO C.", 
    "F.BASICA", 
    "AUT_EXAMES",
    "Cartão SUS"
    ]
opc = [
    "TFD", #TFD
    "PRE", #Premir  
    "FAE", #Farmacia Estada
    "FAA", #Farmacia Auto-custo
    "FAB", #Farmacia Atenção Básica
    "EXA", #Autorização de Exames
    "MUL", #Multiprofissionais 
    "CON", #Consultas
    "ULT", #Ultrassom
    "SUS"
    ]
###Definindo variaveis para tipo de atendimento###
atend = [
    "preferencial", 
    "convencional"
    ]

###Definindo variavel com o nome do local fonte dos arquivos###
get_dir = os.getcwd()+ r'\imagens'

###Definindo Variaveis para Botões e seus diretorios###

#Diretorios para os botões
btAUT = fr"{get_dir}\Botões\btAUT.png"
btF = fr"{get_dir}\Botões\btF.png"
btFA = fr"{get_dir}\Botões\btFA.png" 
btFAB = fr"{get_dir}\Botões\btFAB.png"
btFE = fr"{get_dir}\Botões\btFE.png"
btPREMIR = fr"{get_dir}\Botões\btPREMIR.png"
btTFD = fr"{get_dir}\Botões\btTFD.png"
btcon = fr"{get_dir}\Botões\btcon.png"
btconv = fr"{get_dir}\Botões\btconv.png"
btmult = fr"{get_dir}\Botões\btmult.png"
btpref = fr"{get_dir}\Botões\btpref.png"
btult = fr"{get_dir}\Botões\btult.png"
btvoltar = fr"{get_dir}\Botões\btvoltar.png"
btCSUS = fr"{get_dir}\Botões\btCSUS.png"

#Atribuindo Lista de Botões 
bt = [ 
    btAUT,
    btF,
    btFA,
    btFAB,
    btFE,
    btPREMIR,
    btTFD,
    btcon,
    btconv,
    btmult,
    btpref,
    btult,
    btvoltar,
    btCSUS
    ]

###Definindo variaveis para os blocos e seus diretorios###
bloco_grande = fr"{get_dir}\Blocos\Bloco cinza.png"
bloco_medio = fr"{get_dir}\Blocos\Bloco cinza2.png"

bloco = [
    bloco_grande, 
    bloco_medio
    ]

###Definindo variavel para GIF e seu diretorio###
gif_carregamento = fr"{get_dir}\Gif\Icone carregamento.gif"

gif = [
    gif_carregamento
    ]

###Definindo variaveis para Icones e seu diretorio###
icone_borda = fr"{get_dir}\Icones\loader blue.png"

icone = [
    icone_borda
    ]

###Definindo variavel para Plano de Fundo e seus diretorios###
plano_principal = fr"{get_dir}\Plano de fundo\Plano de Fundo principal.png"
plano_final = fr"{get_dir}\Plano de fundo\Plano de Fundo final.png"
plano_aviso = fr"{get_dir}\Plano de fundo\Plano de Fundo de aviso.png"

planos = [
    plano_principal,
    plano_final,
    plano_aviso
    ]

###Definindo variavel para cores###
cores = [
    'white',
    "blue",
    '#125dab',
    '#f0f0f0',
    '#c7d0d8',
    ]

###Definindo variaveis para fontes
fonte0 = tkFont.Font(family= "Arial", size= 15, weight= "bold")

fontes = [
    fonte0
]
