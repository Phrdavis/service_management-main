from util.modules import *
from util.Gerar_relatorio.gerar_doc import *




class relatorio():
    global data
    
    def gerar(self):
        consulta(self.mes_entrie.get(), self.nome_entrie.get())
        doc()
        self.nome_entrie.delete(0, END)
        self.mes_entrie.set('')
        self.root_rel.destroy()

    def rel_window(self):
        def center(win):
            win.update_idletasks()

            width = win.winfo_width()
            frm_width = win.winfo_rootx() - win.winfo_x()
            win_width = width + 2 * frm_width

            height = win.winfo_height()
            titlebar_height = win.winfo_rooty() - win.winfo_y()
            win_height = height + titlebar_height + frm_width

            x = win.winfo_screenwidth() // 2 - win_width // 2
            y = win.winfo_screenheight() // 2 - win_height // 2

            win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

            win.deiconify()

        fonte1 = tkFont.Font(family="Arial", size=16)                       #Definindo padrão de fonte
        fonte2 = tkFont.Font(family="Arial", size=35, weight="bold")        #Definindo padrão de fonte
        fonte3 = tkFont.Font(family="Arial", size=16, weight="bold")        #Definindo padrão de fonte
        fonte4 = tkFont.Font(family="Arial", size=12, weight="bold")        #Definindo padrão de fonte
        fonte5 = tkFont.Font(family="Arial", size=10)                       #Definindo padrão de fonte

        fontes = [
            fonte1,     #fontes[0]
            fonte2,     #fontes[1]
            fonte3,     #fontes[2]
            fonte4,     #fontes[3]
            fonte5,     #fontes[4]
        ]        
        self.root_rel = tk.Toplevel()
        self.root_rel.title("Gerar Relatório")
        self.root_rel.geometry("500x300")
        self.root_rel.configure(background= "#A9A9A9")
        self.root_rel.resizable(False,False)
        self.frame_rel = Frame(self.root_rel, bd=4, bg = "#ffffff")
        self.frame_rel.place(anchor= 'center', relx= 0.5, rely=0.5, relwidth= 0.98, relheight= 0.98)
        
        data = datetime.now().strftime("%H:%M - %d/%m/%Y")
        self.label_title = Label(self.frame_rel, bd = 0, text="Gerador de Relatorio de Atendimentos Mensal", background= "#ffffff")
        self.label_title.configure(font=fontes[2])
        self.label_title.place(anchor='center', relx= 0.5, rely= 0.2)

        self.mes = Label(self.frame_rel, bd = 0, text="Escolha o mês: ", background= "#ffffff")
        self.mes.configure(font=fontes[0])
        self.mes.place(anchor='center', relx= 0.5, rely= 0.32)

        self.nome = Label(self.frame_rel, bd = 0, text="Gerado por: ", background= "#ffffff")
        self.nome.configure(font=fontes[0])
        self.nome.place(anchor='center', relx= 0.5, rely= 0.53)

        self.data = Label(self.frame_rel, bd= 0, bg= "#ffffff", text=f"Data e hora Atual: {data}")
        self.data.configure(font=fontes[4])
        self.data.place(anchor='center', relx= 0.5, rely= 0.9)

        self.mes_entrie = ttk.Combobox(self.frame_rel, state="readonly", values=('', "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"), justify="center")
        self.mes_entrie.configure(font= fontes[3])
        self.mes_entrie.place(anchor='center', relx= 0.5, rely= 0.43, relwidth=0.4, relheight= 0.08) 
        
        self.nome_entrie = Entry(self.frame_rel, bd = 1, bg= "#ffffff", justify= "center")
        self.nome_entrie.configure(font= fontes[3])
        self.nome_entrie.place(anchor='center', relx= 0.5, rely= 0.63, relwidth=0.4, relheight= 0.08)   

        self.bt_gerar = Button(self.frame_rel, text= "Gerar", command= self.gerar)
        self.bt_gerar.place(anchor='center', relx= 0.5, rely= 0.75, relwidth=0.2, relheight= 0.08)

        center(self.root_rel)


