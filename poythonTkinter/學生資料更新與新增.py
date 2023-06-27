import tkinter as tk
import numpy
import tkinter.font as tkFont
from tkinter.constants import CENTER
from tkinter.constants import *
from functools import partial
from threading import Timer
from PIL import Image,ImageTk
from random import sample
from random import randint
import copy
data=[]
data2=[]
lab_list=[]
ent_list=[]
ent_text_list=[]
radiobutton_list=[]
button_list=[]
page_count=0
val=""
have_add=0
window=tk.Tk()
window.title("更新學生資料")
window.resizable(False,False)
with open("student_data.txt","r") as fread:
    data=fread.read().splitlines()
for i in range(len(data)):
    data2.append(data[i].split(' '))
print(data2)
val=tk.StringVar()
ent_text0=tk.StringVar()
ent_text1=tk.StringVar()
ent_text2=tk.StringVar()
ent_text3=tk.StringVar()
ent_text4=tk.StringVar()
ent_text_list.append(ent_text0)
ent_text_list.append(ent_text1)
ent_text_list.append(ent_text2)
ent_text_list.append(ent_text3)
ent_text_list.append(ent_text4)
def before():
    global page_count
    if page_count>0:
        page_count-=1
    print("page_count=",end="")
    print(page_count)
    if page_count==0:
        button_list[0]["state"]=DISABLED
        if len(data2)==2:
            if page_count==0:
                button_list[4]["state"]=NORMAL
    else:
        # button_list[0]["state"]=NORMAL
        button_list[4]["state"]=NORMAL
    
    for i in range(len(title)):
        ent_text_list[i].set(data2[page_count][i])
    if(data2[page_count][5]=="男"):
        radiobutton_list[0].select()
    else:
        radiobutton_list[1].select()
    

def up():
    global have_add,val,page_count
    student=[]
    for i in range(len(title)):
        student.append(ent_list[i].get())
    student.append(val.get())
    if have_add==1:
        data2.append(student)
    else:
        data2[page_count]=student
    print(data2)
    with open("student_data.txt","w") as fwrite:
        for i in range(len(data2)):
            for j in range(6):
                fwrite.write(data2[i][j])
                if j<5:
                    fwrite.write(" ")
            fwrite.write("\n")
    have_add=0

def dele():
    global page_count
    del data2[page_count]
    if page_count==len(data2):
        for i in range(5):
            s=""
            ent_text_list[i].set(s)
        page_count-=1
    page_count+1
    if page_count!=len(data2):
        for i in range(len(title)):
            ent_text_list[i].set(data2[page_count][i])
        if(data2[page_count][5]=="男"):
            radiobutton_list[0].select()
        else:
            radiobutton_list[1].select()
    with open("student_data.txt","w") as fwrite:
        for i in range(len(data2)):
            for j in range(6):
                fwrite.write(data2[i][j])
                if j<5:
                    fwrite.write(" ")
            fwrite.write("\n")
    # print(data2)

def ad():
    global have_add
    have_add=1
    for i in range(len(title)):
        ent_text_list[i].set("")

def next():
    global page_count
    page_count+=1
    print("page_count=",end="")
    print(page_count)
    if page_count==(len(data2)-1):
        button_list[4]["state"]=DISABLED
        if len(data2)==2:
            if page_count==1:
                button_list[0]["state"]=NORMAL
    else:
        button_list[0]["state"]=NORMAL
        # button_list[4]["state"]=NORMAL
    
    for i in range(len(title)):
        ent_text_list[i].set(data2[page_count][i])
    if(data2[page_count][5]=="男"):
        radiobutton_list[0].select()
    else:
        radiobutton_list[1].select()
    

title=["學號：","姓名：","系所：","地址：","電話："]
button_text=["<<","Update","Delet","Add",">>"]
button_function=[before,up,dele,ad,next]
gender=["男","女"]
for i in range(len(title)):
    a=tk.Label(window,text=title[i])
    lab_list.append(a)
    a.grid(row=i,column=0)
for i in range(len(title)):
    ent_text_list[i].set(data2[page_count][i])
    a=tk.Entry(window,textvariable=ent_text_list[i])
    ent_list.append(a)
    a.grid(row=i,column=1,columnspan=4)
for i in range(2):
    a=tk.Radiobutton(window,variable=val,
                     value=gender[i],
                     text=gender[i])
    radiobutton_list.append(a)
    a.grid(row=5,column=i+1)
if(data2[page_count][5]=="男"):
    radiobutton_list[0].select()
else:
    radiobutton_list[1].select()
for i in range(5):
    a=tk.Button(window,text=button_text[i],
                command=button_function[i],
                width=5,height=2)
    button_list.append(a)
    a.grid(row=6,column=i)
if page_count==0:
    button_list[0]["state"]=DISABLED
# print(ent_list)
window.mainloop()