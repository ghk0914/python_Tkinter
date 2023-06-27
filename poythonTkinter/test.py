import tkinter as tk
from PIL import ImageTk,Image
from tkinter.constants import CENTER
from tkinter.constants import *
from functools import partial
def delet():
    global mylist
    for i in range(2):
        mylist[i].destroy()
    mylist=[]
    print("mylist delet is ",end="")
    print(mylist)
def new():
    global mylist
    for i in range(2):
        b=tk.Button(window,text="SO?",width=5,height=2)
        b.pack()
        mylist.append(b)
    print("mylist new is ",end="")
    print(mylist)

window=tk.Tk()
window.title("OX game")
window.resizable(False,False)
mylist=[]
for i in range(2):
    b=tk.Button(window,text="HI",width=5,height=2)
    b.pack()
    mylist.append(b)
back=tk.Button(window,text="delet",width=5,height=2,command=delet)
back.pack()
newb=tk.Button(window,text="new",width=5,height=2,command=new)
newb.pack()
print("mylist main is ",end="")
print(mylist)
window.mainloop()
