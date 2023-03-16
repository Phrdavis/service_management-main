from util.modulos import *
from util.listas import *

###Função para tela de espera de senha###
class espera():
    def abrir_janela_espera(self):
        self.root_espera = tk.Toplevel()
        self.root_espera.title('') #Atribuição do titulo
        self.root_espera.configure(background= cores[1]) #Cor do plano de fundo da tela 
        self.root_espera.geometry('400x500') #Código que faz a tela abrir em modo tela cheia #Código que faz com que a tela fique em Fullscreen
        self.root_espera.attributes('-alpha', 0.0)
        self.root_espera.resizable(False, False) #Negar que o tamanho da tela seja reajustado
        self.frame_espera =Frame(self.root_espera, bd = 5, highlightbackground= cores[2], highlightthickness= 10, bg = cores[3]) #Frame definido para a tela 4 com fundo branco
        self.frame_espera.place(anchor='center', relx= 0.5,rely= 0.5, relwidth= 1, relheight= 1)
        
        fontexemplo5 = tkFont.Font(family= 'Arial Black', size= 20)

        self.aguarde = Label(self.frame_espera, text= 'Aguarde um instante! \nGerando Senha...', background= cores[3], bd = 0)
        self.aguarde.configure(font= fontexemplo5)
        self.aguarde.place(anchor='center', relx= 0.5,rely= 0.2)

        ###Adicionando GIF de Carregamento###
        file= gif[0]
        info = Image.open(file)
        frames = info.n_frames  # gives total number of frames that gif contains
        # creating list of PhotoImage objects for each frames
        im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]
        count = 0
        anim = None
        def animation(count):
            global anim
            im2 = im[count]

            gif_label.configure(image=im2)
            count += 1
            if count == frames:
                count = 0
            anim = self.root_espera.after(50,lambda :animation(count))

        gif_label = tk.Label(self.root_espera)
        gif_label.place(relx= 0.17,rely= 0.35)
        start = tk.Button(self.root_espera,command= animation(count))
        

        ###Código para janela abrir no meio da tela###
        self.root_espera.update_idletasks()
        width = self.root_espera.winfo_width()
        frm_width = self.root_espera.winfo_rootx() - self.root_espera.winfo_x()
        win_width = width + 2 * frm_width

        height = self.root_espera.winfo_height()
        titlebar_height = self.root_espera.winfo_rooty() - self.root_espera.winfo_y()
        win_height = height + titlebar_height + frm_width

        x = self.root_espera.winfo_screenwidth() // 2 - win_width // 2
        y = self.root_espera.winfo_screenheight() // 2 - win_height // 2
        self.root_espera.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root_espera.deiconify()
        
        self.root_espera.attributes('-alpha', 1.0)
        self.root_espera.overrideredirect(True)
        self.root_espera.after(5000,self.root_espera.destroy)
