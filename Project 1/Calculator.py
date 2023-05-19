from tkinter import *

root = Tk()
root.title("Simple Calculator")

root.maxsize(295,435)

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column= 0, columnspan=3, padx = 10, pady = 10)

# Adding Functionalities to Buttons

def button_Add():
    first_number = e.get()
    global f_num
    global math
    math = "Addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_Click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_Clear():
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "Addition":
        e.insert(0, f_num + int(second_number))
    if math == "Subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "Multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "Division":
        e.insert(0, f_num / int(second_number))
    if math == "Modulus":
        e.insert(0, f_num % int(second_number))
    if math == "Power":
        e.insert(0, f_num ** int(second_number))

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "Subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "Multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "Division"
    f_num = int(first_number)
    e.delete(0, END)

def button_mod():
    first_number = e.get()
    global f_num
    global math
    math = "Modulus"
    f_num = int(first_number)
    e.delete(0, END)

def button_pow():
    first_number = e.get()
    global f_num
    global math
    math = "Power"
    f_num = int(first_number)
    e.delete(0, END)


# defining Button
button_1 = Button(root, text="1", padx = 40, pady = 20, command = lambda: button_Click(1))
button_2 = Button(root, text="2", padx = 40, pady = 20, command = lambda: button_Click(2))
button_3 = Button(root, text="3", padx = 40, pady = 20, command = lambda: button_Click(3))
button_4 = Button(root, text="4", padx = 40, pady = 20, command = lambda: button_Click(4))
button_5 = Button(root, text="5", padx = 40, pady = 20, command = lambda: button_Click(5))
button_6 = Button(root, text="6", padx = 40, pady = 20, command = lambda: button_Click(6))
button_7 = Button(root, text="7", padx = 40, pady = 20, command = lambda: button_Click(7))
button_8 = Button(root, text="8", padx = 40, pady = 20, command = lambda: button_Click(8))
button_9 = Button(root, text="9", padx = 40, pady = 20, command = lambda: button_Click(9))
button_0 = Button(root, text="0", padx = 40, pady = 20, command = lambda: button_Click(0))
button_add = Button(root, text="+", padx = 39, pady = 20, command= button_Add)
button_sub = Button(root, text="-", padx = 41, pady = 20, command= button_sub)
button_mul = Button(root, text="*", padx = 40, pady = 20, command= button_mul)
button_div = Button(root, text="/", padx = 40, pady = 20, command= button_div)
button_mod = Button(root, text="%", padx = 39, pady = 20, command= button_mod)
button_pow = Button(root, text="P", padx = 40, pady = 20, command= button_pow)
button_equal = Button(root, text="=", padx = 91, pady = 20, command= button_equal)
button_clear = Button(root, text="C", padx = 40, pady = 20, command= button_Clear)

# Aligning Buttons
button_7.grid(row = 1, column= 0)
button_8.grid(row = 1, column= 1)
button_9.grid(row = 1, column= 2)
button_4.grid(row = 2, column= 0)
button_5.grid(row = 2, column= 1)
button_6.grid(row = 2, column= 2)
button_1.grid(row = 3, column= 0)
button_2.grid(row = 3, column= 1)
button_3.grid(row = 3, column= 2)
button_0.grid(row = 4, column= 0)
button_add.grid(row=4, column=1)
button_sub.grid(row=4, column=2)
button_mul.grid(row=5, column=1)
button_div.grid(row=5, column=2)
button_mod.grid(row=6, column=0)
button_pow.grid(row=5, column=0)
button_clear.grid(row =5, column=2)
button_equal.grid(row=6, column=1, columnspan=2)

root.mainloop()