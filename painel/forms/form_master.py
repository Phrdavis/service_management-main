# from util.modules import *
from util.funcs import *

get_dir = os.getcwd()
fonts = ['Helvetica','Arial']
pos_img = 0
coolors = [
    '#000000', #0 - Black
    '#E7E7E7', #1 - Platinum
    '#ffffff', #2 - White
    '#686963', #3 ~ dim gray
    '#004568', #4 ~ Indigo Dye
    '#477C93', #5 ~ teal blue
    '#618DA0', #6 ~ light slate gray
    '#7B9EB3', #7 ~ air superiority
    '#e63946'  #8 - Orange Web
    ]

class PainelGUI(Functions):
    def __init__(self):
        self.root = tk.Tk()
        self.width_screnn = self.root.winfo_screenwidth()
        self.height_screnn = self.root.winfo_screenheight()   
        self.root.bind("<F11>", self.toggleFullScreen)
        self.root.bind("<Escape>", self.quitFullScreen)
        self.make_root()
        self.make_frame()
        self.widgets_frame1()
        self.widgets_frame2()
        self.widgets_frame3()
        self.widgets_frame4()
        self.validar_mac()
        self.tread_start_server()
        self.relogio()
        self.root.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.root.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.root.attributes("-fullscreen", self.fullScreenState)

    def make_root(self):
        width_root = 1280
        height_root = 700
        pos_x = self.width_screnn/2 - width_root/2
        pos_y = self.height_screnn/2 - height_root/2
        geometry_root = '%dx%d+%d+%d' % (width_root,height_root,pos_x,pos_y)
        icon = fr'{get_dir}\images\sfs.ico'
        self.root.title('Painel de senhas')
        self.root.iconbitmap(default=icon)
        self.root.geometry(geometry_root)
        self.root.maxsize(width=self.width_screnn, height=self.height_screnn)
        self.root.minsize(width=800, height=600)
        self.root.resizable(True, True)
        self.root.attributes('-fullscreen', True)
        self.fullScreenState = False
        self.root.config(background=coolors[1])

    def make_frame(self):
        
        self.frame_1 = Frame(self.root)
        self.frame_1.config(background=coolors[1])
        self.frame_1.place(rely=0.0, relwidth=1, relheight=0.15)

        self.frame_2 = Frame(self.root)
        self.frame_2.config(background=coolors[1])
        self.frame_2.place(rely=0.16, relwidth=0.68, relx=0.01, relheight=0.73)
        self.frame_2.place(rely=0.15, relwidth=0.7, relheight=0.75)

        self.frame_3 = Frame(self.root)
        self.frame_3.config(background=coolors[1])
        self.frame_3.place(relx=0.7, rely=0.15 ,relwidth=0.3, relheight=0.85)

        self.frame_4 = Frame(self.root)
        self.frame_4.config(background=coolors[0])
        self.frame_4.place(rely=0.90, relwidth=1, relheight=0.1)

    def widgets_frame1(self):
        self.label = Label(self.frame_1, text='SECRETARIA MUNICIPAL DE SAÚDE')
        self.label.config(
            font=(fonts[0],40, 'bold'), foreground=coolors[2],
            background=coolors[4], justify='center'
        )
        self.label.place(relwidth=1,relheight=1)

        self.img_sfs = PhotoImage(file=f'{get_dir}\images\sfs.png')
        self.img = Label(self.frame_1, image=self.img_sfs, bd=0)
        self.img.config(background=coolors[4])
        self.img.place(relx=0.01, rely=0.2)

        self.img_sus = PhotoImage(file=f'{get_dir}\images\sus.png')
        self.img = Label(self.frame_1,image=self.img_sus, bd=0)
        self.img.config(background=coolors[4])
        self.img.place(relx=0.88, rely=0.2)

    def widgets_frame2(self):
        self.label = Label(self.frame_2, text='Senha')
        self.label.config(
            font=(fonts[0],50,'bold'), foreground=coolors[5],
            background=coolors[1], justify='center', anchor='s'
        )
        self.label.place(rely=0.02,relwidth=1,relheight=0.10)
        
        # display senha chamada/atualizar
        self.display_senha1 = Label(self.frame_2, text='0000')
        self.display_senha1.config(
            font=(fonts[0],100,'bold'), foreground=coolors[4],
            background=coolors[1], justify='center', anchor='n'
        )
        self.display_senha1.place(rely=0.12,relwidth=1,relheight=0.22)

        self.label = Label(self.frame_2, text='Local')
        self.label.config(
            font=(fonts[0],50,'bold'), foreground=coolors[5],
            background=coolors[1], justify='center', anchor='s'
        )
        self.label.place(rely=0.34,relwidth=1,relheight=0.10)

        self.display_local = Label(self.frame_2, text='')
        self.display_local.config(
            font=(fonts[0],100,'bold'), foreground=coolors[4],
            background=coolors[1], justify='center', anchor='n'
        )
        self.display_local.place(rely=0.44,relwidth=1,relheight=0.22)

        self.label = Label(self.frame_2, text='Atendimento')
        self.label.config(
            font=(fonts[0],50,'bold'), foreground=coolors[5],
            background=coolors[1], justify='center'
        )
        self.label.place(rely=0.66,relwidth=1,relheight=0.10)
        
        self.display_atendimento = Label(self.frame_2, text='')
        self.display_atendimento.config(
            font=(fonts[0],70,'bold'), foreground=coolors[8],
            background=coolors[1], justify='center'
        )
        self.display_atendimento.place(rely=0.76,relwidth=1,relheight=0.22)
    
    def widgets_frame3(self):
        self.label = Label(self.frame_3, text='Senha chamada')
        self.label.config(
            font=(fonts[0],22), foreground=coolors[2],
            background=coolors[0], justify='center'
        )
        self.label.place(rely=0 ,relwidth=1, relheight=0.05)

         # label, senha chamada
        self.label = Label(self.frame_3, text='Senha')
        self.label.config(
            font=(fonts[0],32), foreground=coolors[1],
            background=coolors[4], justify='center', anchor='s'
        )
        self.label.place(rely=0.05, relwidth=1,relheight=0.11)

        # dislpay, senha chamada
        self.display_senha2 = Label(self.frame_3, text='0000')
        self.display_senha2.config(
            font=(fonts[0],55,'bold'), foreground=coolors[2],
            background=coolors[4], justify='center', anchor='n'
        )
        self.display_senha2.place(rely=0.16, relwidth=1,relheight=0.12)

        # label, local/balcão
        self.label = Label(self.frame_3, text='Local')
        self.label.config(
            font=(fonts[0],32), foreground=coolors[1],
            background=coolors[4], justify='center', anchor='s'
        )
        self.label.place(rely=0.28, relwidth=1,relheight=0.06)

        # dislpay, local/balcão
        self.display_local2 = Label(self.frame_3, text='-')
        self.display_local2.config(
            font=(fonts[0],55,'bold'), foreground=coolors[2],
            background=coolors[4], justify='center', anchor='n'
        )
        self.display_local2.place(rely=0.34, relwidth=1,relheight=0.15)

        # label ultimas chamadas
        self.label = Label(self.frame_3, text='últimas chamadas')
        self.label.config(
            font=(fonts[0],22), foreground=coolors[2],
            background=coolors[0], justify='center'
        )
        self.label.place(rely=0.49, relwidth=1,relheight=0.05)

        # display senha 1
        self.display_senha3 = Label(self.frame_3, text='0000')
        self.display_senha3.config(
            font=(fonts[0],40,'bold'), foreground=coolors[0],
            background=coolors[5], justify='center'
        )
        self.display_senha3.place(rely=0.54 ,relwidth=1,relheight=0.12)

        # diplay chamada 3
        self.display_senha4 = Label(self.frame_3, text='0000')
        self.display_senha4.config(
            font=(fonts[0],40,'bold'), foreground=coolors[0],
            background=coolors[6], justify='center'
        )
        self.display_senha4.place(rely=0.66,relwidth=1,relheight=0.12)    

        # diplay chamada 3
        self.display_senha5 = Label(self.frame_3, text='0000')
        self.display_senha5.config(
            font=(fonts[0],40,'bold'), foreground=coolors[0],
            background=coolors[7], justify='center'
        )
        self.display_senha5.place(rely=0.78 , relwidth=1,relheight=0.12)
    
    def widgets_frame4(self):
        self.label_data = Label(self.frame_4, text='São Francisco do Sul - SC')
        self.label_data.config(
            font=(fonts[0],22), foreground=coolors[1],
            background=coolors[0], justify='center'
        )
        self.label_data.place(relwidth=1,relheight=1)