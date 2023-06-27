import tkinter as tk
import tkinter.font as tkFont
from tkinter.constants import CENTER
from tkinter.constants import *
from functools import partial
from threading import Timer
from PIL import Image,ImageTk
import random

window=tk.Tk()
window.title("TOD")
window.resizable(False,False)
button_list=[[0]*5 for i in range(5)]
word=[]
point=0
counter=0
fall_counter=1
fall_column=[]
point_str=tk.StringVar()
point_str.set("sorce:"+str(point))
def fallen():
    global fall_counter,point
    t=Timer(2,fallen)
    t.start()
    print("fall_counter is ",end="")
    print(fall_counter)
    for i in range(5):
        for j in range(5):
            button_list[i][j]["bg"]="whitesmoke"
    if(fall_counter<=5):
        for i in range(0+point,fall_counter):#fall_counter<=row
            fall_row=i
            button_list[fall_counter-1-fall_row][fall_column[i]]["bg"]="red"
    if(fall_counter>5 and fall_counter<10):
        if fall_counter-5<point:
            for i in range(fall_counter-5+(point-(fall_counter-5)),5):
                button_list[fall_counter-1-i][fall_column[i]]["bg"]="red"
        if fall_counter-5>=point:
            for i in range(fall_counter-5,5):
                button_list[fall_counter-1-i][fall_column[i]]["bg"]="red"
    if(fall_counter<11):
        fall_counter+=1
        
    if(fall_counter==11):
        for i in range(5):
            for j in range(5):
                button_list[i][j]["bg"]="whitesmoke" 
                button_list[i][j]["state"]=DISABLED
        t.cancel()
        
def take(event):
    global counter,point,a,point_str,fall_counter
    ent_str=ent.get()
    # print(ent_str)
    if ent_str == word[counter] and fall_counter<10:
        point+=1
        counter+=1
        a.set(word[counter])
        point_str.set("sorce:"+str(point))
        ent.delete(0,"end")

        
for i in range(5):#決定有幾個單詞
    fall_column.append(random.randint(0,4))#下落圖示的column
    word_num=random.randint(1,5)#決定單詞的字數
    word_str=""
    for j in range(word_num):
        word_content=chr(random.randint(97,122))
        word_str+=word_content#決定單詞內容
    word.append(word_str)
print(fall_column)
a=tk.StringVar()
a.set(word[counter])
for i in range(25):
    r=i//5
    c=i%5
    b=tk.Button(width=5,height=2,compound=tk.CENTER,bg="whitesmoke")
    b.grid(row=r,column=c,sticky=N+S+E+W)
    button_list[r][c]=b
lab=tk.Label(textvariable=a,font=("Arial",15))
lab.grid(row=5,column=0)
ent=tk.Entry(window,justify=("center"),width=5)
ent.grid(row=5,column=2)
ent.focus()
ent.bind("<Return>",take)
point_lab=tk.Label(textvariable=point_str)
point_lab.grid(row=5,column=4)

t1=Timer(1,fallen)
t1.start()
# print(button_list)
window.mainloop()