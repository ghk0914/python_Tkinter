import tkinter as tk
from tkinter.constants import CENTER
from tkinter.constants import *
from math import factorial as fc
window=tk.Tk()
window.title("計算器")
# window.geometry('400x600')
window.resizable(False,False)
g=""
a=tk.StringVar()

def e0():
    global g,a
    if g=="" or (g[0]=="0" and g[1]==".") or g[0]!=0:
        g+="0"
    a=g
    display['text']=a

def e1():
    global g,a
    g+="1"
    a=g
    display['text']=a

def e2():
    global g,a
    g+="2"
    a=g
    display['text']=a

def e3():
    global g,a
    g+="3"
    a=g
    display['text']=a
    
def e4():
    global g,a
    g+="4"
    a=g
    display['text']=a

def e5():
    global g,a
    g+="5"
    a=g
    display['text']=a
    
def e6():
    global g,a
    g+="6"
    a=g
    display['text']=a

def e7():
    global g,a
    g+="7"
    a=g
    display['text']=a

def e8():
    global g,a
    g+="8"
    a=g
    display['text']=a

def e9():
    global g,a
    g+="9"
    a=g
    display['text']=a

def edot():
    global g,a
    g+="."
    a=g
    display['text']=a
    
def echu():
    global g,a
    g+="/"
    a=g
    display['text']=a

def eplus():
    global g,a
    g+="+"
    a=g
    display['text']=a

def ereduce():
    global g,a
    g+="-"
    a=g
    display['text']=a

def echan():
    global g,a
    g+="*"
    a=g
    display['text']=a

def eclr():
    global g,a
    g=""
    a=g
    display['text']=a

def edw():
    global g,a
    # g+=""
    a=eval(g)
    g=str(a)
    print(g)
    display['text']=a


display=tk.Label(window,width=24,height=2,relief=SUNKEN)
display.grid(column=0,row=0,columnspan=4)

zero=tk.Button(window,text="0",width=11,height=2,command=e0)
zero.grid(column=0,row=5,columnspan=2)

dot=tk.Button(window,text=".",width=5,height=2,command=edot)
dot.grid(column=2,row=5)

dw=tk.Button(window,text="=",width=5,height=5,command=edw)
dw.grid(column=3,row=4,rowspan=2)

one=tk.Button(window,text="1",width=5,height=2,command=e1)
one.grid(column=0,row=4)

two=tk.Button(window,text="2",width=5,height=2,command=e2)
two.grid(column=1,row=4)

three=tk.Button(window,text="3",width=5,height=2,command=e3)
three.grid(column=2,row=4)

four=tk.Button(window,text="4",width=5,height=2,command=e4)
four.grid(column=0,row=3)

five=tk.Button(window,text="5",width=5,height=2,command=e5)
five.grid(column=1,row=3)

six=tk.Button(window,text="6",width=5,height=2,command=e6)
six.grid(column=2,row=3)

seven=tk.Button(window,text="7",width=5,height=2,command=e7)
seven.grid(column=0,row=2)

eight=tk.Button(window,text="8",width=5,height=2,command=e8)
eight.grid(column=1,row=2)

nine=tk.Button(window,text="9",width=5,height=2,command=e9)
nine.grid(column=2,row=2)

plus=tk.Button(window,text="+",width=5,height=5,command=eplus)
plus.grid(column=3,row=2,rowspan=2)

reduce=tk.Button(window,text="-",width=5,height=2,command=ereduce)
reduce.grid(column=3,row=1)

clr=tk.Button(window,text="C",width=5,height=2,command=eclr)
clr.grid(column=0,row=1)

chu=tk.Button(window,text="÷",width=5,height=2,command=echu)
chu.grid(column=1,row=1)

chan=tk.Button(window,text="×",width=5,height=2,command=echan)
chan.grid(column=2,row=1)

window.mainloop()
