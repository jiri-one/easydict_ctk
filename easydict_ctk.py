import customtkinter as ctk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("EasyDict-CTK")
        #setting window size
        width=500
        height=1100
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_197=ctk.CTkEntry(root)
        GLineEdit_197["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=20)
        GLineEdit_197["font"] = ft
        GLineEdit_197["fg"] = "#333333"
        GLineEdit_197["justify"] = "center"
        GLineEdit_197["text"] = "Entry"
        GLineEdit_197.place(x=20,y=20,width=70,height=25)

        GListBox_455=ctk.CTkListbox(root)
        GListBox_455["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=20)
        GListBox_455["font"] = ft
        GListBox_455["fg"] = "#333333"
        GListBox_455["justify"] = "center"
        GListBox_455.place(x=20,y=80,width=80,height=25)

        GButton_872=ctk.CTkButton(root)
        GButton_872["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=20)
        GButton_872["font"] = ft
        GButton_872["fg"] = "#000000"
        GButton_872["justify"] = "center"
        GButton_872["text"] = "Button"
        GButton_872.place(x=90,y=20,width=70,height=25)
        GButton_872["command"] = self.GButton_872_command

        GRadio_215=ctk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=20)
        GRadio_215["font"] = ft
        GRadio_215["fg"] = "#333333"
        GRadio_215["justify"] = "center"
        GRadio_215["text"] = "RadioButton"
        GRadio_215.place(x=50,y=50,width=85,height=25)
        GRadio_215["command"] = self.GRadio_215_command

        GRadio_743=ctk.CTkRadiobutton(root)
        ft = tkFont.Font(family='Times',size=20)
        GRadio_743["font"] = ft
        GRadio_743["fg"] = "#333333"
        GRadio_743["justify"] = "center"
        GRadio_743["text"] = "RadioButton"
        GRadio_743.place(x=200,y=50,width=85,height=25)
        GRadio_743["command"] = self.GRadio_743_command

    def GButton_872_command(self):
        print("command")


    def GRadio_215_command(self):
        print("command")


    def GRadio_743_command(self):
        print("command")

if __name__ == "__main__":
    root = ctk.Tk()
    app = App(root)
    root.mainloop()
