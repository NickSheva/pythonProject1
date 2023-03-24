import tkinter
import tkinter.ttk as tk
from tkinter import *

root = tkinter.Tk()
root.geometry('230x230')

frame= tk.Frame(root)
frame.grid(column=0, row=0)

Button(frame, text="Open file", command=None).grid(column=0, row=1)
Label(frame, bg='red', fg="white", text="test test test test test test ").grid(column=0, row=2 )

root.config(background="black")
root.mainloop()