import tkinter as tk
from tkinter.constants import CENTER
from tkinter.constants import *
from functools import partial
from threading import Timer
from PIL import Image,ImageTk
from random import shuffle
from random import randint
window=tk.Tk()
window.title("賭博啦_下注")
window.resizable(False,False)
label_list=[]
entry_list=[]
image1_list=[]
image2_list=[]
display_label=[]
power=[2,2,77,3,3,5,100,5]
cur=[]
who=0
round=0
point=0
r=[]
sec=0.1
ans=[]
def turn():
    global who,sec,round,point
    for i in range(28):
        label_list[i]["bg"]="whitesmoke"
    t=Timer(sec,turn)
    t.start()
    # print(who)
    if who<28 and round<2:
            if who==27:
                label_list[26]["bg"]="whitesmoke"
            else:
                label_list[who-1]["bg"]="whitesmoke"
            label_list[who]["bg"]="gold"
            who+=1

    if round<2 and (who>27 or who==0):
        round+=1
        who=0
    if round==1:
        # print(who)
        if who==ans[-1]+1:
            t.cancel()
        if who==ans[-1]-3:
            sec=0.5
        if sec!=0.5:
            sec=0.3
    
    if cur.count(1)==ans[-1]+1:
        sec=0.1
        round=0
        # print(who)
        if who==ans[-1]+1:
            who=0
            for i in range(len(cur)):
                cur[i]=0
            ans.append(randint(0,27))#決定在哪個地方會停下來
            print(ans)
            img_str=label_list[ans[-2]]["image"]#抽到的圖片是甚麼
            print(int(img_str[-1])-1)
            img_str=str(int(img_str[-1])-1)
            point=point+(int(entry_list[int(img_str)].get())*power[int(img_str)])
            # print(label_list[ans[-2]]["image"])
    point_lab["text"]="目前分數是:"+str(point)
    cur.append(round)
    # for i in range(8):
    #     print(entry_list[i].get(),end=",")

for i in range(1,9):##加入圖片
    pic=ImageTk.PhotoImage(Image.open(f"./ma_a_ti/{str(i)}.png"))
    image1_list.append(pic)

for i in range(0,6):
    image2_list.append(image1_list[0])
for i in range(6,12):
    image2_list.append(image1_list[1])
for i in range(12,17):
    image2_list.append(image1_list[3])
for i in range(17,22):
    image2_list.append(image1_list[4])
for i in range(22,24):
    image2_list.append(image1_list[5])
for i in range(24,26):
    image2_list.append(image1_list[7])
image2_list.append(image1_list[2])
image2_list.append(image1_list[6])
shuffle(image2_list)
for i in range(28):
    b=tk.Label(image=image2_list[i],bg="whitesmoke")
    label_list.append(b)

##開始按順時針排序
for i in range(8):
    label_list[i].grid(row=0,column=i)
for i in range(8,14):
    label_list[i].grid(row=i-7,column=7)
s=7
for i in range(14,22):
    label_list[i].grid(row=7,column=i-s)
    s+=2
s=16
for i in range(22,28):
    label_list[i].grid(row=i-s,column=0)
    s+=2

for i in range(8):#顯示賭注的圖像
    display_label.append(tk.Label(image=image1_list[i]
                                  ,bg="darkorchid"))
    display_label[i].grid(row=8,column=i)
    
for i in range(8):#顯示賭注倍率
    display_label.append(tk.Label(text="X"+str(power[i])+"倍"
                                  ,bg="orchid"
                                  ,font=("思源黑體",10)))
    display_label[8+i].grid(row=9,column=i)
display_label[14].config(font=("思源黑體",11))

for i in range(8):#輸入賭注金
    entry_list.append(tk.Entry(width=6,bg="blueviolet"
                               ,fg="lightgrey"
                               ,font=("Arial",13,"bold")
                               ,justify=("center")))
    entry_list[i].grid(row=10,column=i)
    entry_list[i].insert(0,"0")
go=tk.Button(text="go",command=turn)
go.grid(row=4,column=4)
point_lab=tk.Label(text="目前分數是:"+str(point)
                   ,justify=("center"))
point_lab.grid(row=2,column=4)
ans.append(randint(0,27))#決定在哪個地方會停下來
print(ans)
window.mainloop()