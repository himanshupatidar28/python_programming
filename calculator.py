from tkinter import *

def btnpress(num):
    global equation_text

    equation_text = equation_text + str(num)
    eqn_label.set(equation_text)

def equal():
    global equation_text

    try:
        total = str(eval(equation_text))

        eqn_label.set(total)
    except ZeroDivisionError:
        equation_text = ""
        eqn_label.set("Arithmic error")
    except SyntaxError:
        equation_text = ""
        eqn_label.set("Synatx error")



def clear():
    global equation_text
    equation_text = ""
    eqn_label.set("")


window = Tk()
window.geometry("300x400")
window.resizable(False, False)
window.title("Calculator")

equation_text=""
eqn_label = StringVar()

display = Label(textvariable=eqn_label, font=("Times", 22, "bold"), pady=15, bg='#ffffff', width=100)
display.pack()

body = Frame(window)
body.pack()

btn1 = Button(body,text="1", width=4, height=1, font=('Arial', 18, 'bold'), command=lambda:btnpress(1))
btn1.grid(row=0, column=0)
btn2 = Button(body,text="2", width=4, height=1, font=('Arial', 18, 'bold'), command=lambda:btnpress(2))
btn2.grid(row=0, column=1)
btn3 = Button(body,text="3", width=4, height=1, font=('Arial', 18, 'bold'), command=lambda:btnpress(3))
btn3.grid(row=0, column=2)
btn4 = Button(body,text="4", width=4, height=1, font=('Arial', 18, 'bold'), command=lambda:btnpress(4))
btn4.grid(row=1, column=0)
btn5 = Button(body,text="5", width=4, height=1, font=('Arial', 18, 'bold'), command=lambda:btnpress(5))
btn5.grid(row=1, column=1)
btn6 = Button(body,text="6", width=4, height=1, font=('Arial', 18, 'bold'), command=lambda:btnpress(6))
btn6.grid(row=1, column=2)
btn7 = Button(body,text="7", width=4, height=1, font=('Arial', 18, 'bold'), command=lambda:btnpress(7))
btn7.grid(row=2, column=0)
btn8 = Button(body,text="8", width=4, height=1, font=('Arial', 18, 'bold'), command=lambda:btnpress(8))
btn8.grid(row=2, column=1)
btn9 = Button(body,text="9", width=4, height=1, font=('Arial', 18, 'bold'), command=lambda:btnpress(9))
btn9.grid(row=2, column=2)
btn0 = Button(body,text="0", width=4, height=1, font=('Arial', 18, 'bold'), command=lambda:btnpress(0))
btn0.grid(row=3, column=0)


plus = Button(body,text="+", width=4, height=1, font=('Arial', 18, 'bold'), command=lambda:btnpress("+"))
plus.grid(row=1, column=3)
minus = Button(body,text="-", width=4, height=1, font=('Arial', 18, 'bold'), command=lambda:btnpress("-"))
minus.grid(row=2, column=3)
multiply = Button(body,text="*", width=4, height=1, font=('Arial', 18, 'bold'), command=lambda:btnpress("*"))
multiply.grid(row=3, column=3)
divide = Button(body,text="/", width=4, height=1, font=('Arial', 18, 'bold'), command=lambda:btnpress("/"))
divide.grid(row=3, column=2)
clear = Button(body,text="AC", width=4, height=1, font=('Arial', 18, 'bold'), command=clear)
clear.grid(row=0, column=3)
equal = Button(body,text="=", width=4, height=1, font=('Arial', 18, 'bold'), command=equal)
equal.grid(row=3, column=1)


window.mainloop()