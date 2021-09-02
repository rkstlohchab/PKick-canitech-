from tkinter import *
root = Tk()
root.title("Calculator")

# Creation of all buttons
button_1 = Button(root, text = '1',).grid(row=2,column=0)
button_2 = Button(root, text = '2',).grid(row=2,column=1)
button_3 = Button(root, text = '3',).grid(row=2,column=2)
button_4 = Button(root, text = '4',).grid(row=1,column=0)
button_5 = Button(root, text = '5',).grid(row=1,column=1)
button_6 = Button(root, text = '6',).grid(row=1,column=2)
button_7 = Button(root, text = '7',).grid(row=0,column=0)
button_8 = Button(root, text = '8').grid(row=0,column=1)
button_9 = Button(root, text = '9',).grid(row=0,column=2)
button_0 = Button(root, text = '0',).grid(row=3,column=0)
button_dot = Button(root, text = '.').grid(row=3,column=1)
button_div = Button(root, text = '/').grid(row=3,column=2)
button_add = Button(root, text = '+').grid(row=0,column=3)
button_sub = Button(root, text = '-').grid(row=1,column=3)
button_mult = Button(root, text = '*').grid(row=2,column=3)
button_equal = Button(root, text = '=').grid(row=3,column=3)

root.mainloop()