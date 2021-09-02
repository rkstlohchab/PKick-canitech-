from tkinter import *
from tkinter import messagebox, ttk

root = Tk()
title = title(root,text="Bmi Calculator")
myLabel = Label(root, text="Enter your weight in kg").pack()
weight=DoubleVar(root)
weight_entry = Entry(root, textvariable=weight,  width=20).pack()
myLabel1 = Label(root, text="Enter your height in m").pack()
height = DoubleVar(root)
height_entry = Entry(root, textvariable=height, width=20).pack()
bmi = DoubleVar(root)
def calculate_bmi():
    bmi.set(round((weight.get()) / (height.get() * height.get()), 2))
calculate = Button(root, text="Calculate", command=calculate_bmi)
calculate.pack()
bentry = Entry(root, textvariable=bmi)
bentry.pack()

root.mainloop()