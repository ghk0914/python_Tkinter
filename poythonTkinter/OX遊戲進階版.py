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
    global flag,WinOrFailed,pic1,pic2,button_list,level,count,s
    global rowwin,columnwin,lb1,rightwin,leftwin,gg,kk
    # print(button_list)
    s+=1
    if(count==3):
        count=1
    if(count==1):
        button_list[i].config(image=pic1)
        # print("i is ",end="")
        # print(i)
        lb1["text"]="換玩家2了"
        # button_list[i]["bg"]="black"
    if(count==2):
        button_list[i].config(image=pic2)
        # print("i is ",end="")
        # print(i)
        lb1["text"]="換玩家1了"
        # button_list[i]["bg"]="red"
    WinOrFailed[r][c]=count%3
    count+=1
    button_list[i]["state"]=DISABLED
    button_list[i].config(width=5,height=2)
    print(WinOrFailed)

    for i in range(level):#row
        sumrow=0
        a=WinOrFailed[i][0]
        for j in range(level):
            if a==WinOrFailed[i][j]:
                sumrow+=1
        rowwin[i]=sumrow
    # print("rowwin is ",end="")
    # print(rowwin)
    for i in range(level):
        if rowwin[i]==level:
                    aa=tk.StringVar()
                    aa.set(WinOrFailed[i][i])
                    lb1.config(text="玩家"+aa.get()+"贏了")
                    flag=1
    
    for i in range(level):#column
        sumcolumn=0
        a=WinOrFailed[0][i]
        for j in range(level):
            if a==WinOrFailed[j][i]:
                sumcolumn+=1
        columnwin[i]=sumcolumn
    # print("columnwin is ",end="")
    # print(columnwin)
    for i in range(level):
        if columnwin[i]==level:
                    aa=tk.StringVar()
                    aa.set(WinOrFailed[i][i])
                    lb1.config(text="玩家"+aa.get()+"贏了")
                    flag=1

    for i in range(level):##right
        sumright=0
        a=WinOrFailed[0][0]
        if a==WinOrFailed[i][i]:
            sumright+=1
        rightwin[i]=sumright
    gg=0
    for i in range(level):
        gg+=rightwin[i]
        if gg==level:
            aa=tk.StringVar()
            aa.set(WinOrFailed[0][0])
            lb1.config(text="玩家"+aa.get()+"贏了")
            flag=1
    # print("gg is ",end="")
    # print(gg)
    # print("rightwin is ",end="")
    # print(rightwin)

    for i in range(level):##left
        sumleft=0
        a=WinOrFailed[0][level-1]
        if a==WinOrFailed[i][level-i-1]:
            sumleft+=1
        leftwin[i]=sumleft
    kk=0
    for i in range(level):
        kk+=leftwin[i]
        if kk==level:
            aa=tk.StringVar()
            aa.set(WinOrFailed[0][level-1])
            lb1.config(text="玩家"+aa.get()+"贏了")
            flag=1
    # print("gg is ",end="")
    # print(gg)
    print("leftwin is ",end="")
    print(leftwin)
    if flag==1:
         for i in range(level*level):
              button_list[i]["state"]=DISABLED
    if s==level*level:
        lb1.config(text="平手")
        


def restar(level):
    global WinOrFailed,rowwin,columnwin,flag,rightwin,leftwin,s
    flag=0
    s=0
    for i in range(level):
        for k in range(level):
            WinOrFailed[i][k]=0
    if level%2==0:
        for i in range(level):
            WinOrFailed[i][level-i-1]=10-i
    for i in range(level):
        WinOrFailed[i][i]=3+i
        rowwin[i]=0
        columnwin[i]=0
        rightwin[i]=0
        leftwin[i]=0
    for i in range(level*level):
        button_list[i].config(state=NORMAL,image="")
        lb1.config(text="遊戲開始，玩家1先下")
    global count
    count=1

def next():
    global s,flag,count,level,WinOrFailed
    global button_list,rowwin,columnwin,lb1,leftwin,rightwin
    # for i in range(level*level):##刪除原始組件
    #     button_list[i].destroy()
    for button in button_list:##刪除原始組件
        # print(type(button))
        button.destroy()
    button_list=[]
    # del button_list[:]
    # print(button_list)
    level+=1
    count=1
    s=0
    flag=0
    rowwin=[]
    columswin=[]
    rightwin=[]
    leftwin=[]
    for i in range(level):
        rowwin.append(0)
        columnwin.append(0)
        rightwin.append(0)
        leftwin.append(0)
    # print("level is ",end="")
    # print(level)
    WinOrFailed=[[0]*level for i in range(level)]
    for i in range(level):
        WinOrFailed[i][i]=3+i
    if level%2==0:
        for i in range(level):
            WinOrFailed[i][level-i-1]=10-i
    print(WinOrFailed)
    lb1=tk.Label(text="遊戲開始，玩家1先下",bg="#9932CC",height=2)
    lb1.grid(row=0,column=0,columnspan=level,sticky=N+S+E+W)
    for i in range(level*level):
        r=i//level
        c=i%level
        b=tk.Button(width=5,height=2,command=partial(xy,r,c,i),compound=tk.CENTER)
        b.grid(row=r+1,column=c,sticky=N+S+E+W)
        button_list.append(b)
        # print(i)
    # print(button_list)
    rebutton=tk.Button(text="Restar",height=2,font=("Arial"),command=partial(restar,level))
    rebutton.grid(row=level+1,column=0,columnspan=level-1,sticky=N+S+E+W)
    nebutton=tk.Button(text="下一關",height=2,font=("標楷體"),command=partial(next))
    nebutton.grid(row=level+1,column=level-1,sticky=N+S+E+W)
    

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
count=1
s=0
gg=0
level=3
flag=0
kk=0
# sumrow=0
# sumcolumn=0
rowwin=[]
columnwin=[]
rightwin=[]
leftwin=[]
WinOrFailed=[[0]*level for i in range(level)]
for i in range(level):
    WinOrFailed[i][i]=3+i
lb1=tk.Label(text="遊戲開始，玩家1先下",bg="#9932CC",height=2)
lb1.grid(row=0,column=0,columnspan=level,sticky=N+S+E+W)
for i in range(level):
    rowwin.append(0)
    columnwin.append(0)
    rightwin.append(0)
    leftwin.append(0)

for i in range(level*level):
    r=i//level
    c=i%level
    b=tk.Button(width=5,height=2,command=partial(xy,r,c,i),compound=tk.CENTER)
    b.grid(row=r+1,column=c,sticky=N+S+E+W)
    button_list.append(b)
rebutton=tk.Button(text="Restar",height=2,font=("Arial"),command=partial(restar,level))
rebutton.grid(row=level+1,column=0,columnspan=2,sticky=N+S+E+W)
nebutton=tk.Button(text="下一關",height=2,font=("標楷體"),command=partial(next))
nebutton.grid(row=level+1,column=level-1,sticky=N+S+E+W)
window.mainloop()
