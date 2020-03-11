from tkinter import *
import sqlite3


#defining database paramters

conec = sqlite3.connect('name.db')

cur = conec.cursor()

cur.execute("""CREATE TABLE name (
            first_name text
             )""")

#creating the first text box for name

name_var=Tk()

label_1=Label (name_var, text="Please enter your name:")
entry_1 = Entry(name_var)
button_1=Button(name_var, text="Enter", command=submit)

label_1.grid(row=0, column=0)
entry_1.grid(row=0, column=1)
button_1.grid(row=1, column=0)





conec.commit()

conec.close()


name_var.mainloop()


