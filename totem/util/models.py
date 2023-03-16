from contextlib import contextmanager
import pymysql.cursors, os
from configparser import ConfigParser
from datetime import date, datetime, timedelta
#Importanto funções para trabalha em banco de dados 
#pip install pymysql

@contextmanager #gerenciador de contexto
def connect_server(): # função conectar banco
    config = ConfigParser()
    get_dir = os.path.dirname(__file__)
    config.read(fr'{get_dir}\settings.ini')
    server_config = dict(config['server'])
    conexao = pymysql.connect(
        host= server_config['host'],
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

def verificar_filaEspera():
    data = date.today()
    tabela = 'fila_espera'
    with connect_server() as conn:
        with conn.cursor() as cursor:
            if  cursor.execute(f'SELECT data FROM {tabela} WHERE id IN (SELECT MAX(id) FROM {tabela});')>0:
                last_date = datetime.strptime(str(cursor.fetchone()['data']), '%d/%m/%Y').date()
                if cursor.execute('SELECT config FROM settings WHERE option="F.ESTADO";')>0:
                    res = cursor.fetchone()
                    if str(res['config']) == 'BLOQUEADO':
                        cursor.execute('UPDATE settings SET config = "LIBERADO" WHERE option="F.ESTADO";')
                        
                if last_date < data:
                    cursor.execute(f'INSERT INTO atendimentos (setor, atendimentos, data) SELECT setor, COUNT(senha) As atendimentos, data from fila_espera GROUP BY setor;')
                    cursor.execute(f'TRUNCATE TABLE {tabela};')
                    conn.commit()
