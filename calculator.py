from tkinter import *


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
        self.num1 = 0
        self.num2 = 0
        self.result = 0
        self.operation = ''

        # taking input from the keyboard
        def changeText(update):
            if self.text.get() == '0' or self.text.get() == '+' or self.text.get() == '-' or self.text.get() == chr(215) or self.text.get() == chr(247):
                self.text.set(update)
            else:
                update = self.text.get() + str(update)
                self.text.set(update)

        # setting the menu
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.subMenu = Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.subMenu)
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
        self.button_clear = Button(self.buttons_row0, text="CE", command=self.clearText)
        self.button_clear.pack()

        self.buttons_row1 = Frame(self.root)
        self.buttons_row1.pack()
        self.button7 = Button(self.buttons_row1, text="7", command=lambda: changeText(7))
        self.button7.pack(side=LEFT)
        self.button8 = Button(self.buttons_row1, text="8", command=lambda: changeText(8))
        self.button8.pack(side=LEFT)
        self.button9 = Button(self.buttons_row1, text="9", command=lambda: changeText(9))
        self.button9.pack(side=LEFT)
        self.button_divide = Button(self.buttons_row1, text=chr(247), command=self.calcDivide)
        self.button_divide.pack(side=LEFT)

        self.buttons_row2 = Frame(self.root)
        self.buttons_row2.pack()
        self.buttons_row2.option_add("*side", 'LEFT')
        self.button4 = Button(self.buttons_row2, text="4", command=lambda: changeText(4))
        self.button4.pack(side=LEFT)
        self.button5 = Button(self.buttons_row2, text="5", command=lambda: changeText(5))
        self.button5.pack(side=LEFT)
        self.button6 = Button(self.buttons_row2, text="6", command=lambda: changeText(6))
        self.button6.pack(side=LEFT)
        self.button_mult = Button(self.buttons_row2, text=chr(215), command=self.calcMultiply)
        self.button_mult.pack(side=LEFT)

        self.buttons_row3 = Frame(self.root)
        self.buttons_row3.pack()
        self.button1 = Button(self.buttons_row3, text="1", command=lambda: changeText(1))
        self.button1.pack(side=LEFT)
        self.button2 = Button(self.buttons_row3, text="2", command=lambda: changeText(2))
        self.button2.pack(side=LEFT)
        self.button3 = Button(self.buttons_row3, text="3", command=lambda: changeText(3))
        self.button3.pack(side=LEFT)
        self.button_minus = Button(self.buttons_row3, text="-", command=self.calcExtract)
        self.button_minus.pack(side=LEFT)

        self.buttons_row4 = Frame(self.root)
        self.buttons_row4.pack()
        self.button0 = Button(self.buttons_row4, text="0", command=lambda: changeText(0))
        self.button0.pack(side=LEFT)
        self.button_point = Button(self.buttons_row4, text=".", command=lambda: changeText('.'))
        self.button_point.pack(side=LEFT)
        self.button_result = Button(self.buttons_row4, text="=", command=self.show_result)
        self.button_result.pack(side=LEFT)
        self.button_plus = Button(self.buttons_row4, text="+", command=self.calcAdd)
        self.button_plus.pack(side=LEFT)

        self.root.mainloop()

    def clearText(self):
        self.text.set('0')
        self.num1 = 0
        self.num2 = 0
        self.operation = ''

    def calcAdd(self):
        if self.operation == '':
            self.num1 = float(self.text.get())
        self.text.set('+')
        self.operation = 'add'

    def calcExtract(self):
        if self.operation == '':
            self.num1 = float(self.text.get())
        self.text.set('-')
        self.operation = 'extract'

    def calcMultiply(self):
        if self.operation == '':
            self.num1 = float(self.text.get())
        self.text.set(chr(215))
        self.operation = 'multiply'

    def calcDivide(self):
        if self.operation == '':
            self.num1 = float(self.text.get())
        self.text.set(chr(247))
        self.operation = 'divide'

    def show_result(self):
        self.num2 = float(self.text.get())
        if self.operation == 'add':
            self.result = self.num1 + self.num2
        elif self.operation == 'extract':
            self.result = self.num1 - self.num2
        elif self.operation == 'multiply':
            self.result = self.num1 * self.num2
        elif self.operation == 'divide':
            self.result = self.num1 / self.num2

        if self.result - int(self.result) == 0:
            self.result = int(self.result)
        else:
            self.result = round(self.result, 8)

        self.text.set(self.result)
        self.num1 = self.result
        self.num2 = 0
        self.operation = ''


app = Calculator()
