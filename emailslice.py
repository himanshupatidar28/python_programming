from tkinter import *

def submit():
    useremail = entry.get()
    if useremail.find("@"):
        for i in range(0, len(useremail)):
            if useremail[i] == "@":
                userid = useremail[:i]
                domain = useremail[(i+1):]
                msg = "Username is : "+ userid+" & Domain name is : "+domain
    else:
        msg = "Invaild Email"
    clear()
    output.config(text=msg)

def clear():
    entry.delete(0,END)
    output.config(text="")



window = Tk()
window.geometry("600x300")
window.title("Email Slicer")
mainlabel = Label(text="Enter Your Email :", font=("Times", 18), pady=30)
mainlabel.pack()

entry = Entry(window, font=("Times", 14), width=40)
entry.pack(pady=10)

btnlabel = Label()
btnlabel.pack()

btn_sub = Button(btnlabel, text="Submit", padx=10, pady=5, command=submit)
btn_sub.pack(side=RIGHT)

btn_cl = Button(btnlabel, text="Clear", padx=10, pady=5, command=clear)
btn_cl.pack(side=LEFT)

output = Label(padx=10, pady=20,font=("Times", 16))
output.pack()

window.mainloop()

