from tkinter import *

name_var=Tk()

label_1=Label (name_var, text="Please enter your name:")
entry_1 = Entry(name_var)
button_1=Button(name_var, text="Enter")

label_1.grid(row=0, column=0)
entry_1.grid(row=0, column=1)
button_1.grid(row=1, column=0)

name_var.mainloop()


