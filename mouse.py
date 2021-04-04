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
        self.menu1.add_command(label="Open Rec", command=self.config_hotkeys)
        self.menu1.add_command(label="Save Rec", command=self.config_hotkeys)
        self.menu1.add_command(label="Add Folder")
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
        pass
home()