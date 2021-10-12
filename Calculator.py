# https://www.delftstack.com/howto/python-tkinter/how-to-pass-arguments-to-tkinter-button-command/

from tkinter import *

calculator = Tk()
calculator.title("Calculator")
calculator.geometry("330x220")
calculator.configure(background="#fadadd")

expression = ""
equation = StringVar()

def inputting(numberEntered):
    global expression
    expression += str(numberEntered)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def answer():
    try:
        global expression
        output = str(eval(expression))
        equation.set(output)
        expression = ""

    except Exception as e:
        if type(e) == ZeroDivisionError:
            equation.set("Division by zero is not allowed.")
        elif type(e) == SyntaxError:
            equation.set("Not allowed.")
        expression = ""

expression_field = Entry(calculator, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)

button1 = Button(calculator, text=" 1 ", fg="black", command=lambda: inputting(1), height=2, width=7)
button1.grid(row=2, column=0)

button2 = Button(calculator, text=" 2 ", fg="black", command=lambda: inputting(2), height=2, width=7)
button2.grid(row=2, column=1)

button3 = Button(calculator, text=" 3 ", fg="black", command=lambda: inputting(3), height=2, width=7)
button3.grid(row=2, column=2)

plus = Button(calculator, text=" + ", fg="black", command=lambda: inputting("+"), height=2, width=7)
plus.grid(row=2, column=3)

button4 = Button(calculator, text=" 4 ", fg="black", command=lambda: inputting(4), height=2, width=7)
button4.grid(row=3, column=0)

button5 = Button(calculator, text=" 5 ", fg="black", command=lambda: inputting(5), height=2, width=7)
button5.grid(row=3, column=1)

button6 = Button(calculator, text=" 6 ", fg="black", command=lambda: inputting(6), height=2, width=7)
button6.grid(row=3, column=2)

minus = Button(calculator, text=" - ", fg="black", command=lambda: inputting("-"), height=2, width=7)
minus.grid(row=3, column=3)

button7 = Button(calculator, text=" 7 ", fg="black", command=lambda: inputting(7), height=2, width=7)
button7.grid(row=4, column=0)

button8 = Button(calculator, text=" 8 ", fg="black", command=lambda: inputting(8), height=2, width=7)
button8.grid(row=4, column=1)

button9 = Button(calculator, text=" 9 ", fg="black", command=lambda: inputting(9), height=2, width=7)
button9.grid(row=4, column=2)

multiply = Button(calculator, text=" * ", fg="black", command=lambda: inputting("*"), height=2, width=7)
multiply.grid(row=4, column=3)

decimalPoint = Button(calculator, text=".", fg="black", command=lambda: inputting("."), height=2, width=7)
decimalPoint.grid(row=5, column=0)

button0 = Button(calculator, text=" 0 ", fg="black", command=lambda: inputting(0), height=2, width=7)
button0.grid(row=5, column=1)

equal = Button(calculator, text=" = ", fg="black", command=answer, height=2, width=7)
equal.grid(row=5, column=2)

divide = Button(calculator, text=" / ", fg="black", command=lambda: inputting("/"), height=2, width=7)
divide.grid(row=5, column=3)

clear = Button(calculator, text="Clear", fg="black", command=clear, height=2, width=7)
clear.grid(row=6, column=0)

buttonEnd = Button(calculator, fg="black", text="Finish", height=2, width=7, command=calculator.quit)
buttonEnd.grid(row=6, column=1)

openBracket = Button(calculator, text=" ( ", fg="black", command=lambda: inputting("("), height=2, width=7)
openBracket.grid(row=6, column=2)

closeBracket = Button(calculator, text=" ) ", fg="black", command=lambda: inputting(")"), height=2, width=7)
closeBracket.grid(row=6, column=3)

calculator.mainloop()
