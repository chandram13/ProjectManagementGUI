# Marvish Chandra

import tkinter as tk

from tkinter import *

TK_SILENCE_DEPRECATION=1

root = tk.Tk()

root.geometry("500x500")
root.title("My Project Management App")

label = tk.Label(root, text="Welcome to using PMA!",font=('Arial',18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=6, font=('Arial',16))
textbox.pack(padx=10,pady=20)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)
buttonframe.columnconfigure(3,weight=1)

btn1 = tk.Button(buttonframe,text="Today",font=('Arial',18))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe,text="Tomorrow",font=('Arial',18))
btn2.grid(row=0,column=1,sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe,text="Later",font=('Arial',18))
btn3.grid(row=0,column=2,sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe,text="Completed",font=('Arial',18))
btn3.grid(row=0,column=3,sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

root.mainloop()