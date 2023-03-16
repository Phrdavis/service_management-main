# from util.modules import *
from contextlib import contextmanager
from configparser import ConfigParser
import pymysql.cursors, threading, os, socket

@contextmanager
def start_connect():
    config = ConfigParser()
    get_dir = os.path.dirname(__file__)
    config.read(fr'{get_dir}\settings.ini')
    server_config = dict(config['server'])
    conexao = pymysql.connect(
        host=server_config['host'],
        user=server_config['user'],
        password=server_config['password'],
        db=server_config['db'],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    try: #Tratamento de exeções
        yield conexao 
    finally: #Executa independente da exeção 
        conexao.close() #Finaliza conexão

def consulta_database(sql):
    with start_connect() as conexao:
        with conexao.cursor() as cursor:
            try:
                if cursor.execute(sql)>0:
                    resultado = cursor.fetchall()
                    return resultado
            except:
                print('erro consulta')

def consulta_fila(sql):
    with start_connect() as conexao:
        with conexao.cursor() as cursor:
            try:
                if cursor.execute(sql)>0:
                    resultado = cursor.fetchone()
                    return resultado['total']
            except:
                print('erro consulta')

def consulta_state(sql):
    with start_connect() as conexao:
        with conexao.cursor() as cursor:
            try:
                if cursor.execute(sql)>0:
                    resultado = cursor.fetchone()
                    return resultado['config']
            except:
                print('erro consulta')

def update_databe(sql):
    with start_connect() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            conexao.commit()

def list_panels():
    listpanels = []
    sql = 'SELECT host, port FROM panels;'
    consulta = consulta_database(sql)
    for i in consulta:
        listpanels.append([i['host'],i['port']])
    return listpanels
        

def chamar_senha(data):
    listpanels = list_panels()
    for i in listpanels:
        HOST = str(i[0])
        PORT = int(i[1])
        try:
            threading.Thread(target=run_panel, args=[HOST, PORT, data]).start()
        except:
            continue
            # messagebox.showwarning('Erro temporário!','Falha na comunicação com o servidor remoto!\nTente novamnete em alguns instantes!')

def run_panel(HOST, PORT,data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(str.encode(str(data)))
    except:
        print(f'Erro de conexão: {HOST} {PORT}')
