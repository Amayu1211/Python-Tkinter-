#Text
from tkinter import *

w = Tk()

tx = Text(w, height=2, width=30)

tx.pack()

tx.insert(END, 'Hello from Tkinter')

w.mainloop()