from util.modules import *

class Functionsconfig():
    def carregar_config(self):
        try:
            configFile = ConfigParser()
            with open('app.ini', 'r') as file:
                file.close
        except IOError:
            configFile['config'] = {
                'local': 'local',
                'port': '50000'
                }
            with open('app.ini', 'w', encoding='UTF-8') as file:
                configFile.write(file)

        configFile.read('app.ini')
        configFile = dict(configFile['config'])
        self.entry_porta.insert(0,configFile['port'])
        self.entry_local.insert(0,configFile['local'])
    
    def salvar_config(self):
        if messagebox.askyesno('Configurações','Tem certeza que deseja salvar estas alterações?') == YES:
            configFile = ConfigParser()
            configFile.add_section('config')
            configFile.set('config','port', self.entry_porta.get())
            configFile.set('config','local', self.entry_local.get())
            with open('app.ini', 'w', encoding='UTF-8') as file:
                configFile.write(file)
            messagebox.showinfo('Configurações', 'Alterações salvas com sucesso!')
            self.root.destroy()
            
        
class ConfigGUI(Functionsconfig):
    def __init__(self):
        self.root = tk.Tk()
        self.make_root()
        self.make_frame()
        self.make_widgets()
        self.carregar_config()
        self.root.mainloop()

    def make_root(self):
        get_dir = os.path.dirname(__file__)
        icon = fr'{get_dir}\images\sfs.ico'
        width_root = 450
        height_root = 250
        width_screnn = self.root.winfo_screenwidth()
        height_screnn = self.root.winfo_screenheight()
        pos_x = width_screnn/2 - width_root/2
        pos_y = height_screnn/2 - height_root/2
        geometry_root = '%dx%d+%d+%d' % (width_root,height_root,pos_x,pos_y)
        self.root.title('Configurações')
        self.root.iconbitmap(default=icon)
        self.root.geometry(geometry_root)
        self.root.maxsize(width=width_screnn, height=height_screnn)
        self.root.resizable(False, False)
    
    def make_frame(self):
        self.frame = Frame(self.root)
        self.frame.place(relx= 0.1,rely=0, relwidth=0.8, relheight=1)

    def make_widgets(self):

        self.label = Label(self.frame, text='Porta')
        self.label.config(font=(0,12),anchor='w',)
        self.label.place(relwidth=0.5, relheight=0.1, rely=0.25)
        self.entry_porta = Entry(self.frame)
        self.entry_porta.config(font=(0,12),justify='left')
        self.entry_porta.place(relwidth=0.5, relheight=0.1,relx=0.5, rely=0.25)

        self.label = Label(self.frame, text='Local:')
        self.label.config(font=(0,12),anchor='w',)
        self.label.place(relwidth=0.5, relheight=0.1, rely=0.4)
        self.entry_local = Entry(self.frame)
        self.entry_local.config(font=(0,12),justify='left')
        self.entry_local.place(relwidth=0.5, relheight=0.1,relx=0.5, rely=0.4)

        self.btn_salvar = Button(self.frame, text='Salvar')
        self.btn_salvar.place(relwidth=0.5, relheight=0.15,relx=0.5, rely=0.75)
        self.btn_salvar.config(command=self.salvar_config)


ConfigGUI()