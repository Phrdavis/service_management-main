from util.modules import *

@contextmanager
def connect_server():
    config = ConfigParser()
    get_dir = os.path.dirname(__file__)
    config.read(fr'{get_dir}\app.ini')
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


class Functions():

    def validar_mac(self):
        mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        ip = socket.gethostbyname(socket.gethostname())

        with connect_server() as conexao:
            with conexao.cursor() as cursor:
                if cursor.execute(f'SELECT * FROM panels WHERE mac = "{mac_address}";')>0:
                    resultado = cursor.fetchall()
                    cursor.execute(f'UPDATE panels SET host = "{ip}" WHERE mac = "{mac_address}";')
                    conexao.commit()
                else:
                    cursor.execute(f'INSERT INTO panels (host, port, mac) VALUES ("{ip}", "50000", "{mac_address}");')
                    conexao.commit()

    def tread_start_server(self):
        t1 = threading.Thread(target=self.start_conect)
        t1.daemon = TRUE
        t1.start()


    def start_conect(self):
        get_dir = os.path.dirname(__file__)
        logs_errors = f'{get_dir}\logs.txt'

        config = ConfigParser()
        config_file = fr'{get_dir}\app.ini'
        try:
            with open(config_file, 'r') as file:
                file.close
        except IOError:
            config['config'] = {
                'local': 'local',
                'port': '50000'
                }
            with open(config_file, 'w', encoding='UTF-8') as file:
                config.write(file)
        
        config.read(config_file)
        HOST = socket.gethostbyname(socket.gethostname())
        PORT = int(config['config']['port'])
        setor = str(config['config']['local']).split(';')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            senha_atual = ''
            chamada0 = ''
            chamada1 = ''
            chamada2 = ''
            chamada3 = ''
            while True:
                try:
                    conn, addr = s.accept()
                    data = conn.recv(1024)    
                    if not data:
                        data = 0
                    else:
                        data = eval(data.decode())
                        senha = str(data[0])
                        senha_local = str(data[1])
                        atendimento = str(data[2])
                        atendimento = atendimento.title()

                        for local in setor:
                            if senha_local == local:
                                
                                try: 
                                    playsound(r'Media\\toque.wav',0)
                                except Exception as e:
                                    data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                                    try:
                                        with open(logs_errors, 'a') as file:
                                            file.write(f'{data}: {e}\n')
                                    except IOError:
                                        with open(logs_errors, 'w') as file:
                                            file.write(f'{data}: {e}\n')

                                self.display_senha1.config(text=senha)
                                self.display_local.config(text=senha_local)
                                self.display_atendimento.config(text=atendimento)

                        if senha != senha_atual:    
                            senha_atual = senha                            
                            chamada3 = chamada2
                            chamada2 = chamada1
                            chamada1 = chamada0
                            chamada0 = f'{senha} - {senha_local}'

                            self.display_senha2.config(text=senha)
                            self.display_local2.config(text=senha_local)
                            self.display_senha3.config(text=chamada1)
                            self.display_senha4.config(text=chamada2)
                            self.display_senha5.config(text=chamada3)
                        
                        for local in setor:
                            if senha_local == local:
                                self.voice(senha)
                        
                        
                except Exception as e:
                    data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    
                    try:
                        with open(logs_errors, 'a') as file:
                            file.write(f'{data}: {e}\n')
                    except IOError:
                        with open(logs_errors, 'w') as file:
                            file.write(f'{data}: {e}\n')
                    
                    

    def voice(self,senha):
        data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        try:
            file_voice = f'Media\\Voices\\{senha}.mp3'
            texto = fr'Senha {senha}, favor dirigir-se ao local de atendimento!'
            tts = gtts.gTTS(texto, lang='pt-br')
            tts.save(file_voice)
        except:
            i += 1
            file_voice = f'Media\\Voices\\{senha}{data}.mp3'
            texto = fr'Senha {senha}, favor dirigir-se ao local de atendimento!'
            tts = gtts.gTTS(texto, lang='pt-br')
            tts.save(file_voice)
        
        playsound(file_voice)  
        os.remove(file_voice)
        
    def relogio(self):
        self.data_atual = datetime.now().strftime('%d/%m/%Y %H:%M')
        self.label_data.after(200, self.relogio)
        self.label_data.config(text=str(F'São Francisco do Sul - SC    {self.data_atual}'))
