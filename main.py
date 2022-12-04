from tkinter import *

root = Tk()
root.title("Calculator")
# root.iconbitmap("C:\\Users\\tziam\\Desktop\\device_Port-PinkGold.png")

global operator
global first_num


def calculate():
    second_num = entry.get()
    entry.delete(0, END)
    if operator == "+":
        entry.insert(0, first_num + int(second_num))
    elif operator == "-":
        entry.insert(0, first_num - int(second_num))
    elif operator == "*":
        entry.insert(0, first_num * int(second_num))
    else:
        entry.insert(0, first_num / int(second_num))


# Function that inputs your data when button is clicked
def input_data(value):
    num = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(num) + str(value))


# Function for the "clear" key
def clear_data():
    entry.delete(0, END)


# Function to decide which operation to perform
def operation(sign):
    num = entry.get()
    global operator
    global first_num
    first_num = int(num)
    entry.delete(0, END)
    operator = sign


# Creation of input space
entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Creation of buttons and display
button7 = Button(root, text=7, width=7, height=4, command=lambda: input_data(7))
button7.grid(row=1, column=0)

button8 = Button(root, text=8, width=7, height=4, command=lambda: input_data(8))
button8.grid(row=1, column=1)

button9 = Button(root, text=9, width=7, height=4, command=lambda: input_data(9))
button9.grid(row=1, column=2)

button_add = Button(root, text="+", width=7, height=4, command=lambda: operation("+"))
button_add.grid(row=1, column=3)

button4 = Button(root, text=4, width=7, height=4, command=lambda: input_data(4))
button4.grid(row=2, column=0)

button5 = Button(root, text=5, width=7, height=4, command=lambda: input_data(5))
button5.grid(row=2, column=1)

button6 = Button(root, text=6, width=7, height=4, command=lambda: input_data(6))
button6.grid(row=2, column=2)

button_minus = Button(root, text="-", width=7, height=4, command=lambda: operation("-"))
button_minus.grid(row=2, column=3)

button1 = Button(root, text=1, width=7, height=4, command=lambda: input_data(1))
button1.grid(row=3, column=0)

button2 = Button(root, text=2, width=7, height=4, command=lambda: input_data(2))
button2.grid(row=3, column=1)

button3 = Button(root, text=3, width=7, height=4, command=lambda: input_data(3))
button3.grid(row=3, column=2)

button_prod = Button(root, text="*", width=7, height=4, command=lambda: operation("*"))
button_prod.grid(row=3, column=3)

button_clear = Button(root, text="Clear", width=7, height=4, command=clear_data)
button_clear.grid(row=4, column=0)

button0 = Button(root, text=0, width=7, height=4, command=lambda: input_data(0))
button0.grid(row=4, column=1)

button_equal = Button(root, text="=", width=7, height=4, command=calculate)
button_equal.grid(row=4, column=2)

button_div = Button(root, text="/", width=7, height=4, command=lambda: operation("/"))
button_div.grid(row=4, column=3)

root.mainloop()
