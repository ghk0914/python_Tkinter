import tkinter as tk
from tkinter.constants import CENTER
from tkinter.constants import *
from functools import partial
from threading import Timer
from random import randint
from random import shuffle
window=tk.Tk()
window.title("打地鼠")
window.resizable(False,False)
rat=[]
point=0
stage=1
chel=0
button_list=[]
def hit(i):
    global point,a,chel

    if(button_list[i]["bg"]=="pink" and rat[i]==1):
        point+=1
        chel+=1
        print(chel)
        lb["text"]="分數:"+str(point)+"   stage:"+str(stage)+"   地鼠數量:"+str(a-chel)
        button_list[i]["bg"]="gainsboro"
        rat[i]=0

def level_up():
    global stage,point,a,chel
    chel=0
    if(stage!=5):
        stage+=1
        for i in range(100):
            rat[i]=0
            button_list[i]["bg"]="gainsboro"
        a=randint(3,15)#地鼠數量
        for i in range(1,a+1):
            c=randint(0,99)
            rat[c]=1
            button_list[c]["bg"]="pink"
        t1=Timer(5,level_up)
        t1.start()
        lb["text"]="分數:"+str(point)+"   stage:"+str(stage)+"   地鼠數量:"+str(a)
t1=Timer(5,level_up)
t1.start()

for i in range(100):
    rat.append(0)
    r=i//10
    c=i%10
    b=tk.Button(width=5,height=2,command=partial(hit,i),
                compound=tk.CENTER,bg="gainsboro")
    b.grid(row=r,column=c,sticky=N+S+E+W)
    button_list.append(b)
a=randint(3,15)#地鼠數量
for i in range(1,a+1):
    c=randint(0,99)
    rat[c]=1
    button_list[c]["bg"]="pink"
lb=tk.Label(height=2,text="分數:"+str(point)+"   stage:"+str(stage)+"   地鼠數量:"+str(a))
lb.grid(row=10,column=0,columnspan=10)
# print("a is ",end="")
# print(a)
# print(rat)
window.mainloop()