from tkinter import messagebox, filedialog
from ttkthemes import ThemedStyle
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
import tkinter as tk
import keyboard, os, pyautogui, random
from threading import Thread
import tkinter.font as tkFont
from time import sleep

class home:
    def __init__(self):
        super().__init__()

        ####Designer

        self.app = tk.Tk()
        self.app.title("Mouse record PYTHON") 
        self.app.geometry('700x400')
        self.app.iconbitmap('repository\\icone.ico')
        self.app.resizable(height=0, width=0)
        
        self.style = ThemedStyle(self.app)
        self.style.theme_use("equilux") 

        bg = self.style.lookup('TLabel', 'background')
        fg = self.style.lookup('TLabel', 'foreground')

        self.app.configure(bg=self.style.lookup('TLabel', 'background'))




        #####Configure        
        def play():
            Thread(target=self.play, ).start()
        def stop():
            Thread(target=self.stop, ).start()




        ####Container de componentes


       ####imagens buttons 
        self.photo = PhotoImage(file=r'repository\play.png')
        self.photoimage = self.photo.subsample(20, 20)

        self.photo_two = PhotoImage(file=r'repository\stop.png')
        self.photoimage_two = self.photo_two.subsample(12,12)

        ###Buttons


        self.btn_play = tk.Button(self.app, image=self.photoimage, compound=LEFT, command=play, bd=0, bg="#464646")
        self.btn_play.place(x=10, y=20)

        self.btn_stop = tk.Button(self.app, image=self.photoimage_two, compound=LEFT, command=stop, bd=0, bg="#464646")
        self.btn_stop.place(x=10, y=100)

        ####Texto de exibição Positions
        self.label_text = tk.Label(text="Resultados:", bg="#464646", fg="white", font=('sans serif', 15))
        self.label_text.place(x=85, y=20)


        self.fonts = tkFont.Font(family='sans serif', size=12, weight='bold')
        self.text_exi = tk.Listbox(self.app, fg="black", width=60, font=self.fonts)
        self.text_exi.place(x=85, y=60)


        ####MENU

        self.menuBar = tk.Menu(self.app)
        self.menu1 = tk.Menu(self.menuBar, tearoff=0)
        self.menu1.add_command(label="Open Rec", command=self.open_rec)
        self.menu1.add_command(label="Save Rec", command=self.save_rec)
        self.menu1.add_command(label="Add Folder", command=self.add_folder)
        self.menu1.add_command(label="Config Hotkeys", command=self.config_hotkeys)
        self.menuBar.add_cascade(label="File", menu=self.menu1)

        self.app.config(menu=self.menuBar)




        ####RUN WINDOW
        self.app.mainloop()

    def play():
        Thread(target=self.play, ).start()

    def setup(self):
        keyboard.add_hotkey({self.player}, self.play)
        keyboard.add_hotkey({self.pauser}, self.play)
        keyboard.add_hotkey({self.stoper}, self.play)


    def play(self):
        self.save_rec = random.randint(10000,99999)
        self.save_rec = str(self.save_rec)
        self.infos = True

        with open("rec.rec", "a") as create:
            create.write('')

        while os.path.exists('rec.rec'):
            if self.infos == False:
                break

            x, y = pyautogui.position()
            sleep(0.5)
            self.x=str(x)
            self.y=str(y)
            with open(f"records\\{self.save_rec}.rec", "a") as posi:
                posi.write(f'{self.x}x{self.y}\n')
                self.text_exi.insert("end", f' Mouse position: {self.x} x {self.y} ')


    def stop(self):
        os.remove('rec.rec')

    
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

    def save_rec(self):
        pass

    def open_rec(self):
        self.file_open_rec = filedialog.askopenfilename(initialdir='/', title='Escolha seu arquivo .rec', filetypes=[("file .rec", "*.rec")])
        
home()
