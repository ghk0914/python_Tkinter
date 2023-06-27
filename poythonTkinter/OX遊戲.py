import tkinter as tk
from PIL import ImageTk,Image
from tkinter.constants import CENTER
from tkinter.constants import *
from functools import partial

window=tk.Tk()
window.title("OX game")
window.resizable(False,False)

def xy(r,c,i):
    window.columnconfigure(c,minsize=50)
    window.rowconfigure(r+1,minsize=48)
    global count
    global s
    global flag
    s+=1
    if(count==3):
        count=1
    if(count==1):
        button_list[i].config(image=pic1)
        lb1["text"]="換玩家2了"
        # button_list[i]["bg"]="black"
    if(count==2):
        button_list[i].config(image=pic2)
        lb1["text"]="換玩家1了"
        # button_list[i]["bg"]="red"
    WinOrFailed[r][c]=count%3

    count+=1
    button_list[i]["state"]=DISABLED
    button_list[i].config(width=5,height=2)
    print(WinOrFailed)

    for i in range(3):#row
        a=WinOrFailed[i][1]
        if a==WinOrFailed[i][0] and a==WinOrFailed[i][2]:
            aa=tk.StringVar()
            aa.set(a)
            lb1.config(text="玩家"+aa.get()+"贏了")
            flag=1
        
    for i in range(3):#column
        a=WinOrFailed[1][i]
        if a==WinOrFailed[0][i] and a==WinOrFailed[2][i]:
            aa=tk.StringVar()
            aa.set(a)
            lb1.config(text="玩家"+aa.get()+"贏了")
            flag=1
    
    if(WinOrFailed[0][0]==WinOrFailed[1][1]==WinOrFailed[2][2]):
        a=WinOrFailed[0][0]
        aa=tk.StringVar()
        aa.set(a)
        lb1.config(text="玩家"+aa.get()+"贏了")
        flag=1  

    if(WinOrFailed[0][2]==WinOrFailed[1][1]==WinOrFailed[2][0]):
        a=WinOrFailed[0][2]
        aa=tk.StringVar()
        aa.set(a)
        lb1.config(text="玩家"+aa.get()+"贏了")
        flag=1  
    if flag==1:
        for i in range(9):
            button_list[i].config(state=DISABLED,bg="black")
    if s==9:
       lb1.config(text="平手")

img=Image.open("O.png")
img=ImageTk.PhotoImage(img)
img2=Image.open("X.jpg")
img2=ImageTk.PhotoImage(img2)
pic1=Image.open("O.png")
pic2=Image.open("X.jpg")
pic1=pic1.resize((55,50))
pic2=pic2.resize((55,50))
pic1=ImageTk.PhotoImage(pic1)
pic2=ImageTk.PhotoImage(pic2)
button_list=[]
flag=0
WinOrFailed=[[0]*3 for i in range(3)]
for i in range(3):
    WinOrFailed[i][i]=3+i
lb1=tk.Label(text="遊戲開始，玩家1先下",bg="#9932CC",width=18,height=2)
lb1.grid(row=0,column=0,columnspan=3)
count=1
s=0
for i in range(9):
    r=i//3
    c=i%3
    b=tk.Button(width=5,height=2,command=partial(xy,r,c,i),compound=tk.CENTER)
    b.grid(row=r+1,column=c,sticky=N+S+E+W)
    button_list.append(b)
window.mainloop()
