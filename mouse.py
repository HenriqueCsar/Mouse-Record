from tkinter import *
from tkinter import messagebox, filedialog
import keyboard, os


os.chdir(r"C:\Users\Henrique1\Desktop\mouse_record")

class home:
    def __init__(self):
        super().__init__()

        self.app = Tk()
        self.app.title("Mouse record PYTHON") 
        self.app.geometry('700x400')
        self.app.configure(bg='#292f3b')
        self.app.iconbitmap('repository\\icone.ico')


        ####MENU

        self.menuBar = Menu(self.app)
        self.menu1 = Menu(self.menuBar, tearoff=0)
        self.menu1.add_command(label="Open Rec", command=self.open_rec)
        self.menu1.add_command(label="Save Rec", command=self.save_rec)
        self.menu1.add_command(label="Add Folder", command=self.add_folder)
        self.menu1.add_command(label="Config Hotkeys", command=self.config_hotkeys)
        self.menuBar.add_cascade(label="File", menu=self.menu1)

        self.app.config(menu=self.menuBar)




        ####RUN WINDOW
        self.app.mainloop()

    def setup(self):
        keyboard.add_hotkey({self.player}, self.play)
        keyboard.add_hotkey({self.pauser}, self.play)
        keyboard.add_hotkey({self.stoper}, self.play)


    def play(self):
        pass


    def stop(self):
        pass
    
    def pause(self):
        pass


    def config_hotkeys(self):
        self.w_hotkeys = Tk()
        self.w_hotkeys.title('Configurar Hotkeys')
        self.w_hotkeys.configure(bg='#f1f1f1')
        self.w_hotkeys.iconbitmap('repository\\icone.ico')
        self.w_hotkeys.geometry('400x200')


        ##Labels hotkey

        self.l1 = Label(self.w_hotkeys, text='Play:', font=('serif', 11))
        self.l1.grid(row=1, column=1)
        self.l2 = Label(self.w_hotkeys, text='Pause:', font=('serif', 11))
        self.l2.grid(row=2, column=1)
        self.l3 = Label(self.w_hotkeys, text='Stop:', font=('serif', 11))
        self.l3.grid(row=3, column=1)

        ##Texto hotkeys

        self.t1 = Text(self.w_hotkeys, height=1, width=10)
        self.t1.grid(row=1, column=2)
        self.t2 = Text(self.w_hotkeys, height=1, width=10)
        self.t2.grid(row=2, column=2)
        self.t3 = Text(self.w_hotkeys, height=1, width=10)
        self.t3.grid(row=3, column=2)



        ###Botões hotkeys


        self.b1 = Button(self.w_hotkeys, text='Save', command=self.s_hotkey)
        self.b1.grid(row=1, column=3)
        self.b2 = Button(self.w_hotkeys, text='Save', command=self.s_hotkey)
        self.b2.grid(row=2, column=3)
        self.b3 = Button(self.w_hotkeys, text='Save', command=self.s_hotkey)
        self.b3.grid(row=3, column=3)



        self.w_hotkeys.mainloop()


    def s_hotkey(self):
        try:
            pass
            messagebox.showinfo('Informação', 'Hotkeys salvas com sucesso')
        except:
            pass

    def add_folder(self):
        pass
    #salvar gravações

    def save_rec(self):
        pass

    def open_rec(self):
        pass
home()
