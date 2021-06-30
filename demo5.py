#Message
from tkinter import *

w = Tk()

msg ='Hello from Tkinter'

i = Message(w, text = msg, bg='blue')

i.pack()

w.mainloop()