from tkinter import *
from tkinter import font, colorchooser
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

def newfile():
    window.title("Untitled - Text Editor")
    TextArea.delete(1.0, END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", file=[("All Files", "*.*"),("Text Documents", "*.txt")])
    try:
        window.title(os.path.basename(file) + " - Text Editor")
        TextArea.delete(1.0,END)
        file = open(file, "r")
        TextArea.insert(1.0, file.read())
    finally:
        file.close()


def savefile():
    global file
    file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("Text Documents", "*.txt"),("All Files", "*.*")])
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file) + " - Text Editor")
            file = open(file, "w")
            file.write(TextArea.get(1.0,END))
        finally:
            file.close()

def helps():
    showinfo("Text Editor", "Text Editor By Himanshu Patidar")

def about():
    showinfo("About Us - Text Editor", "https://himanshupatidar.infinityfreeapp.com")

def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))


def change_font(*args):
    TextArea.config(font=(font_name.get(), font_size.get()))

def change_color():
    color =colorchooser.askcolor(title="Text Color")
    TextArea.config(fg=color[1])
def change_bg():
    color =colorchooser.askcolor(title="Text Color")
    TextArea.config(bg=color[1])



class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.wm_iconbitmap("icon.ico")
        self.geometry("800x500")
        self.minsize(600,400)


    def menubar(self):
        global font_name, font_size
        MenuBar = Menu(self)

        Filemenu = Menu(MenuBar, tearoff=0)
        Filemenu.add_command(label="New", command=newfile)
        Filemenu.add_command(label="Open", command=openfile)
        Filemenu.add_command(label="Save", command=savefile)
        Filemenu.add_separator()
        Filemenu.add_command(label="Exit", command=exit)
        MenuBar.add_cascade(label="File", menu=Filemenu)

        Editmenu = Menu(MenuBar, tearoff=0)
        Editmenu.add_command(label="Cut", command=cut )
        Editmenu.add_command(label="Copy", command=copy)
        Editmenu.add_command(label="Paste", command=paste)
        MenuBar.add_cascade(label="Edit", menu=Editmenu)


        Helpmenu = Menu(MenuBar, tearoff=0)
        Helpmenu.add_command(label="About", command=about)
        Helpmenu.add_separator()
        Helpmenu.add_command(label="Help", command=helps)
        MenuBar.add_cascade(label="Help", menu=Helpmenu)

       
        self.config(menu=MenuBar)

        menuFrame = Frame(self, height=30, pady=10, padx=10, bg='white')
        menuFrame.pack(fill=X)

        label1 = Label(menuFrame, text="Family :", bg='white').grid(row=0, column=0)
        font_box = OptionMenu(menuFrame, font_name, *font.families(), command=change_font)
        font_box.grid(row=0, column=1, padx=5)

        label2 = Label(menuFrame, text="Size :", bg='white').grid(row=0, column=2)
        sizebox =Spinbox(menuFrame, from_=1, to=100, textvariable=font_size,width=5,command=change_font)
        sizebox.grid(row=0, column=3, padx=5)

        label3 = Label(menuFrame, text="Color :", bg='white').grid(row=0, column=4)
        color = Button(menuFrame, bg='black', width=1, height=1,relief=RAISED,command=change_color).grid(row=0, column=5)

        label4 = Label(menuFrame, text="Background :", bg='white').grid(row=0, column=6)
        bcolor = Button(menuFrame, bg='white', width=1, height=1,relief=RAISED,command=change_bg).grid(row=0, column=7)


    def statusBar(self):
        global chars
        statusFrame = Frame(self, height=5)
        status =Label(statusFrame, text="Text Editor", padx=5, pady=5).grid(row=0, column=1)
        ready =Label(statusFrame, text="Ready", padx=5, pady=5).grid(row=0, column=0)



        statusFrame.pack(side=BOTTOM, fill=X)

   

if __name__ == '__main__':

    window = GUI()
    window.title("Untitled - Text Editor")
    font_name = StringVar(window)
    font_size = StringVar(window)
    font_name.set("Calibri")
    font_size.set("18")
    file = None
    chars= 0
    window.menubar()
    
    pad =Frame(window, width=10, bg='white').pack(side=LEFT)
    TextArea = Text(window, font=(font_name.get(), font_size.get()))
    TextArea.pack(expand=True, fill=BOTH)

    scroll = Scrollbar(TextArea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)
    window.statusBar()
    window.mainloop()