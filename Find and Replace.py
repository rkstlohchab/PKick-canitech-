from tkinter import *
from tkinter import ttk,messagebox

root = Tk()

canvas_width, canvas_height = 200,100
w = Canvas(root, width = canvas_width, height = canvas_height)
w.pack()
w.create_rectangle(50,20,150,80, outline="#000000")
w.create_arc(250,225,225,250,fill="black", extent=110)
root.mainloop()