from tkinter import *
from tkinter import messagebox
import math

class Calculator:

    def __init__(self):
        self.root = Tk()
        self.root.title('Calculator')
        self.root.iconbitmap('calc.ico')
        self.root.option_add("*Font", 'Calibri 18 bold')
        self.root.option_add("*Button.width", '5')
        self.text = StringVar()
        self.text.set(0)

        # Variables
        self.num = 0
        self.result = 0
        self.error = 0
        self.operation = ''

        # taking input from the keyboard
        def changeText(update):
            if self.text.get() == '0' or self.text.get() == '+' or self.text.get() == '-' or self.text.get() == chr(215) or self.text.get() == chr(247):
                if update == '.':
                    self.text.set('0.')
                else:
                    self.text.set(update)
            else:
                if self.text.get() == 'Error':
                    self.text.set(update)
                else:
                    update = self.text.get() + str(update)
                    self.text.set(update)

        # setting the menu
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.subMenu = Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.subMenu)
        self.subMenu.add_command(label='About', font=("Calibri", 10), command=lambda: messagebox.showinfo("About", "Calculator ver. 1.11 \n Ivan Georgiev"))
        self.subMenu.add_command(label='Exit', font=("Calibri", 10), command=quit)

        # Configure the main window and its size
        self.frame = Frame(self.root)
        self.frame.pack(fill=X)

        # Configure the results display
        self.display = Label(self.frame, textvariable=self.text, bg='light grey', fg='black', font=("Calibri", 36),
                             anchor=E)
        self.display.pack(fill=X)

        # Buttons
        self.buttons_row0 = Frame(self.root)
        self.buttons_row0.pack(anchor=E)
        self.button_pl_mi = Button(self.buttons_row0, text=chr(177), command=self.changeSign)
        self.button_sqr = Button(self.buttons_row0, text=chr(8730), command=self.calcSqrt)
        self.button_clear = Button(self.buttons_row0, text="CE", command=self.clearText)
        self.button_pl_mi.pack(side=LEFT)
        self.button_sqr.pack(side=LEFT)
        self.button_clear.pack()

        self.buttons_row1 = Frame(self.root)
        self.buttons_row1.pack()
        self.button7 = Button(self.buttons_row1, text="7", command=lambda: changeText(7))
        self.button8 = Button(self.buttons_row1, text="8", command=lambda: changeText(8))
        self.button9 = Button(self.buttons_row1, text="9", command=lambda: changeText(9))
        self.button_divide = Button(self.buttons_row1, text=chr(247), command=self.calcDivide)
        self.button7.pack(side=LEFT)
        self.button8.pack(side=LEFT)
        self.button9.pack(side=LEFT)
        self.button_divide.pack()

        self.buttons_row2 = Frame(self.root)
        self.buttons_row2.pack()
        self.buttons_row2.option_add("*side", 'LEFT')
        self.button4 = Button(self.buttons_row2, text="4", command=lambda: changeText(4))
        self.button5 = Button(self.buttons_row2, text="5", command=lambda: changeText(5))
        self.button6 = Button(self.buttons_row2, text="6", command=lambda: changeText(6))
        self.button_mult = Button(self.buttons_row2, text=chr(215), command=self.calcMultiply)
        self.button4.pack(side=LEFT)
        self.button5.pack(side=LEFT)
        self.button6.pack(side=LEFT)
        self.button_mult.pack()

        self.buttons_row3 = Frame(self.root)
        self.buttons_row3.pack()
        self.button1 = Button(self.buttons_row3, text="1", command=lambda: changeText(1))
        self.button2 = Button(self.buttons_row3, text="2", command=lambda: changeText(2))
        self.button3 = Button(self.buttons_row3, text="3", command=lambda: changeText(3))
        self.button_minus = Button(self.buttons_row3, text="-", command=self.calcExtract)
        self.button1.pack(side=LEFT)
        self.button2.pack(side=LEFT)
        self.button3.pack(side=LEFT)
        self.button_minus.pack()

        self.buttons_row4 = Frame(self.root)
        self.buttons_row4.pack()
        self.button0 = Button(self.buttons_row4, text="0", command=lambda: changeText(0))
        self.button_point = Button(self.buttons_row4, text=".", command=lambda: changeText('.'))
        self.button_result = Button(self.buttons_row4, text="=", command=self.show_result)
        self.button_plus = Button(self.buttons_row4, text="+", command=self.calcAdd)
        self.button0.pack(side=LEFT)
        self.button_point.pack(side=LEFT)
        self.button_result.pack(side=LEFT)
        self.button_plus.pack()

        self.root.mainloop()

    def clearText(self):
        self.text.set('0')
        self.num = 0
        self.operation = ''

    def calcAdd(self):
        if self.text.get() == 'Error':
            self.clearText()
        else:
            if self.operation == '':
                self.num = float(self.text.get())
                self.text.set('+')
                self.operation = 'add'
            else:
                self.show_result()

    def calcExtract(self):
        if self.text.get() == 'Error':
            self.clearText()
        else:
            if self.operation == '':
                self.num = float(self.text.get())
                self.text.set('-')
                self.operation = 'extract'
            else:
                self.show_result()

    def calcMultiply(self):
        if self.text.get() == 'Error':
            self.clearText()
        else:
            if self.operation == '':
                self.num = float(self.text.get())
                self.text.set(chr(215))
                self.operation = 'multiply'
            else:
                self.show_result()

    def calcDivide(self):
        if self.text.get() == 'Error':
            self.clearText()
        else:
            if self.operation == '':
                self.num = float(self.text.get())
                self.text.set(chr(247))
                self.operation = 'divide'
            else:
                self.show_result()

    def calcSqrt(self):
        if self.text.get() == 'Error':
            self.clearText()
        else:
            if self.operation == '':
                self.operation = 'sqrt'
                self.show_result()

    def changeSign(self):
        if float(self.text.get()) > 0:
            update = '-' + self.text.get()
            self.text.set(update)
        elif float(self.text.get()) < 0:
            update = -float(self.text.get())
            if update - int(update) == 0:
                update = int(update)
            else:
                update = round(update, 8)
            self.text.set(update)

    def show_result(self):
        if self.text.get() != '+' and self.text.get() != '-' and self.text.get() != chr(215) and self.text.get() != chr(247) and self.text.get() != 'Error':
            if self.operation == 'add':
                self.result = self.num + float(self.text.get())
            elif self.operation == 'extract':
                self.result = self.num - float(self.text.get())
            elif self.operation == 'multiply':
                self.result = self.num * float(self.text.get())
            elif self.operation == 'divide':
                if float(self.text.get()) == 0:
                    self.error = 1
                else:
                    self.result = self.num / float(self.text.get())
            elif self.operation == 'sqrt':
                if float(self.text.get()) > 0:
                    self.result = math.sqrt(float(self.text.get()))
                else:
                    self.error = 1

            if not self.error:
                if self.result - int(self.result) == 0:
                    self.result = int(self.result)
                else:
                    self.result = round(self.result, 8)
                self.text.set(self.result)
                self.num = self.result
            else:
                self.result = 'Error'
                self.text.set(self.result)
                self.error = 0

            self.operation = ''


app = Calculator()
