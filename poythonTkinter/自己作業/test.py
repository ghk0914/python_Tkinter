import tkinter as tk
from tkinter.constants import CENTER
from tkinter.constants import *
window=tk.Tk()
lbtext=tk.StringVar()
btext=tk.StringVar()
btext.set("我只是個按鈕")
a=0
def add():
    global a
    a+=1
    lbtext.set(a)
    if a>15:
        btext.set("不要再按了")
def reset():
    global a
    a=0
    lbtext.set(a)
    btext.set("我只是個按鈕")
window.title("只是test")
window.geometry('500x500')
window.resizable(False,False)
window.iconbitmap("C:/Users/Adimn/Downloads/stock-folder-icons-3-by-hamza-saleem/ico/Group Folder.ico")
button1=tk.Button(window,textvariable=btext,command=add)
button1.place(x=250,y=250,anchor=CENTER)
button2=tk.Button(window,text="Rest",command=reset)
button2.place(x=232,y=265)
label1=tk.Label(window,textvariable=lbtext,font=("標楷體",15))
label1.place(x=243,y=200)
window.mainloop()