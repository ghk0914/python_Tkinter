import tkinter as tk
from PIL import ImageTk,Image
from tkinter.constants import CENTER
from tkinter.constants import *
from functools import partial
from random import shuffle

window=tk.Tk()
window.title("數字配對遊戲")
window.resizable(False,False)
def compand(i):
    global k,g,count,winflag,event,wincount,color,lb
    event.append(i)
    if winflag!=1:
        button_list[i]["state"]=DISABLED
    if count%2==0:
        k=button_list[i]["text"]
    if count%2==1:
        g=button_list[i]["text"]
    if k==g:
        # button_list[event[-2]]["state"]=DISABLED
        button_list[event[-2]].config(state=DISABLED
                                      ,bg=color[wincount%7]
                                      ,fg="black")
        # button_list[i]["state"]=DISABLED
        button_list[i].config(state=DISABLED
                              ,bg=color[wincount%7]
                              ,fg="black")
        winflag=1
        wincount+=1
    reduce=50-wincount
    if k!=g and count!=0 and winflag!=1 and k!=98 and g!=99:
        button_list[event[-2]]["state"]=NORMAL
        button_list[i]["state"]=NORMAL
        k=98
        g=99
        winflag=0
    if winflag==1:
        k=98
        g=99
    if k==98 and g==99:
        winflag=0
    count+=1
    lb["text"]="剩餘"+str(reduce)+"組配對"

button_list=[]
mylist=[]
event=[]
color=["#FF0000","#FF7F00","#FFFF00","#00FF00","#00FFFF","#0000FF","#8B00FF"]
k=98
g=99
count=0
wincount=0
winflag=0
for i in range(10):
    for j in range(10):
        mylist.append(i)
shuffle(mylist)
for i in range(100):
    r=i//10
    c=i%10
    b=tk.Button(width=5,height=2,command=partial(compand,i),
                compound=tk.CENTER,text=mylist[i])
    b.grid(row=r,column=c,sticky=N+S+E+W)
    button_list.append(b)
lb=tk.Label(height=2,text="剩餘50組配對")
lb.grid(row=10,column=0,columnspan=10)

window.mainloop()