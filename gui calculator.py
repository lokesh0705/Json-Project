# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 22:24:41 2021

@author: Lenovo
"""

import tkinter as tk
window=tk.Tk()
window.title("calculator")
label1=tk.Label(text="enter the first no")
label2=tk.Label(text="enter the second no")
entry = tk.Entry(width=10)

entry2=tk.Entry(width=10)
label1.pack()
entry.pack()
label2.pack()

entry2.pack()


def add():
    r1=int(entry.get())
    r2=int(entry2.get())
    r=r1+r2
    rest=r1+r2
    print(rest)
    label3=tk.Label(text=rest)
    label3.pack()
    
def sub():
    r1=int(entry.get())
    r2=int(entry2.get())
    r=r1+r2
    rest=r1-r2
    print(rest)
    label3=tk.Label(text=rest)
    label3.pack()
def multiply():
    r1=int(entry.get())
    r2=int(entry2.get())
    r=r1+r2
    rest=r1*r2
    print(rest)
    label4=tk.Label(text=rest)
    label4.pack()
    
btn=tk.Button(text="ADD",command=add)
btn2=tk.Button(text="Subtract",command=sub)
btn3=tk.Button(text="multiply",command=multiply)
btn.pack()
btn2.pack()
btn3.pack()
    
window.mainloop()