# from app_modules import *


# get_dir = os.path.dirname(__file__)
# icon = fr'{get_dir}\images\sfs.ico'
# config = ConfigParser()
# configFile = 'app.ini'

# class Functionsconfig():
#     def salvar_config(self):
#         '''
#         # salvar configuração do arquivo .ini
#             ConfigParser - iterpretador/analisador do arquivo
#                 .add_section('nome da seção definida')
#                 .set('nome da seção definida','opção/chave','valor opção/chave')

#             with - garantir que os recursos serão finalizados
#                 .write('arquivo de configuração passado no metodo with') - pertence ao ConfigParser

#         '''
#         global config, configFile
#         if messagebox.askyesno('Configurações','Tem certeza que deseja salvar estás alterações?') == YES:
#             config = ConfigParser()
#             config.add_section('server')
#             config.set('server','host', self.entry_servidor.get())
#             config.set('server','user', self.entry_username.get())
#             config.set('server','password', '')
#             config.set('server','db', self.entry_tabela.get())
#             config.set('server','setor', self.entry_setor.get())
#             with open(configFile,'w', encoding='UTF-8') as file:
#                 config.write(file)
#             messagebox.showinfo('Configurações','Alterações salvas com sucesso!')
#             self.root.destroy()

#     def loadConfigFile(self):
#         '''
#         # carrega configuração do arquivo .ini em try:, caso o arquivo não exista gera um novo arquivo em except:
        
#         .read('arquivo ConfigParser') #lê o arquivo
#         .dict('arquivo ConfigParser['seção definida']') #cria um dicionário para o interpretador
#         '''
#         global config, configFile
#         try:
#             with open(configFile,'r') as file:
#                 file.close()
#         except IOError:
#             config['server'] = {
#                 'host': 'localhost',
#                 'user': 'sms',
#                 'password': '',
#                 'db': 'database_att',
#                 'setor': ''
#             }
#             with open(configFile, 'w', encoding='UTF-8') as file:
#                 config.write(file)

#         config.read(configFile)
#         server_config = dict(config['server'])
#         self.entry_servidor.insert(0,server_config['host'])
#         self.entry_username.insert(0,server_config['user'])
#         self.entry_tabela.insert(0,server_config['db'])
#         self.entry_setor.insert(0,server_config['setor'])

# class ConfigGUI(Functionsconfig):
#     def __init__(self):
#         self.root = tk.Tk()
#         self.make_root()
#         self.make_frame()
#         self.make_widgets()
#         self.loadConfigFile()
#         self.root.mainloop()

#     def make_root(self):
#         width_root = 450
#         height_root = 250
#         width_screnn = self.root.winfo_screenwidth()
#         height_screnn = self.root.winfo_screenheight()
#         pos_x = width_screnn/2 - width_root/2
#         pos_y = height_screnn/2 - height_root/2
#         geometry_root = '%dx%d+%d+%d' % (width_root,height_root,pos_x,pos_y)
#         self.root.title('Configurações - chamar senha')
#         self.root.iconbitmap(default=icon)
#         self.root.geometry(geometry_root)
#         self.root.maxsize(width=width_screnn, height=height_screnn)
#         self.root.resizable(False, False)
    
#     def make_frame(self):
#         self.frame = Frame(self.root)
#         self.frame.place(relx= 0.1,rely=0, relwidth=0.8, relheight=1)

#     def make_widgets(self):
#         self.label = Label(self.frame, text='Hostname:')
#         self.label.config(font=(0,12),anchor='w',)
#         self.label.place(relwidth=0.5, relheight=0.1, rely=0.1)
#         self.entry_servidor = Entry(self.frame)
#         self.entry_servidor.config(font=(0,12),justify='left')
#         self.entry_servidor.place(relwidth=0.5, relheight=0.1,relx=0.5, rely=0.1)

#         self.label = Label(self.frame, text='Username:')
#         self.label.config(font=(0,12),anchor='w',)
#         self.label.place(relwidth=0.5, relheight=0.1, rely=0.25)
#         self.entry_username = Entry(self.frame)
#         self.entry_username.config(font=(0,12),justify='left')
#         self.entry_username.place(relwidth=0.5, relheight=0.1,relx=0.5, rely=0.25)

#         self.label = Label(self.frame, text='Database:')
#         self.label.config(font=(0,12),anchor='w',)
#         self.label.place(relwidth=0.5, relheight=0.1, rely=0.4)
#         self.entry_tabela = Entry(self.frame)
#         self.entry_tabela.config(font=(0,12),justify='left')
#         self.entry_tabela.place(relwidth=0.5, relheight=0.1,relx=0.5, rely=0.4)

#         self.label = Label(self.frame, text='Setor:')
#         self.label.config(font=(0,12),anchor='w',)
#         self.label.place(relwidth=0.5, relheight=0.1, rely=0.55)
#         self.entry_setor = Entry(self.frame)
#         self.entry_setor.config(font=(0,12),justify='left')
#         self.entry_setor.place(relwidth=0.5, relheight=0.1,relx=0.5, rely=0.55)

#         self.btn_salvar = Button(self.frame, text='Salvar')
#         self.btn_salvar.place(relwidth=0.5, relheight=0.15,relx=0.5, rely=0.75)
#         self.btn_salvar.config(command=self.salvar_config)

# ConfigGUI()