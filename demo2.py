#Tkinter Checkbutton
from tkinter import *
w = Tk()
w.geometry("200x200")
chkbtn1 = Checkbutton(w, text="C")
chkbtn1.pack()
chkbtn2 = Checkbutton(w, text="C++")
chkbtn2.pack()
chkbtn3 = Checkbutton(w, text="Java")
chkbtn3.pack()
w.mainloop()