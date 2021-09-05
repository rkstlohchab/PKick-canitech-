from tkinter import *
from tkinter import ttk, messagebox
root = Tk()
root.title("Calculator")

# myLabel = Label(root, text='this is label or heading', bg  ="White", fg='Black', font='Ariel').place(x=400x, y=100)
num = StringVar(root)
e = Entry(root).grid(row=0, column=0)

def button_click(num):
    e.insert(0, e.get() + num)

# Creation of all buttons
button_1 = Button(root, text = '1', command=button_click(1)).grid(row=3,column=0)
button_2 = Button(root, text = '2', command=button_click(2)).grid(row=3,column=1)
button_3 = Button(root, text = '3', command=button_click(3)).grid(row=3,column=2)
button_4 = Button(root, text = '4', command=button_click(4)).grid(row=2,column=0)
button_5 = Button(root, text = '5', command=button_click(5)).grid(row=2,column=1)
button_6 = Button(root, text = '6', command=button_click(6)).grid(row=2,column=2)
button_7 = Button(root, text = '7', command=button_click(7)).grid(row=1,column=0)
button_8 = Button(root, text = '8', command=button_click(8)).grid(row=1,column=1)
button_9 = Button(root, text = '9', command=button_click(9)).grid(row=1,column=2)
button_0 = Button(root, text = '0', command=button_click(0)).grid(row=4,column=0)
# button_dot = Button(root, text = '.', command=button_click(.)).grid(row=4,column=1)
# button_div = Button(root, text = '/', command=button_click(/)).grid(row=4,column=2)
# button_add = Button(root, text = '+', command=button_click(+)).grid(row=1,column=3)
# button_sub = Button(root, text = '-', command=button_click(-)).grid(row=2,column=3)
# button_mult = Button(root, text = '*', command=button_click(*)).grid(row=3,column=3)
# button_equal = Button(root, text = '=', command=button_click(=)).grid(row=4,column=3)

root.mainloop()