import tkinter as tk
from tkinter.constants import CENTER
from tkinter.constants import *
from functools import partial
from threading import Timer
from PIL import Image,ImageTk
from random import shuffle
from random import randint
window=tk.Tk()
window.title("賭博啦")
window.resizable(False,False)
label_list=[]
image1_list=[]
image2_list=[]
cur=[]
who=0
round=0
r=[]
sec=0.1
ans=[]
def turn():
    global who,sec,round
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
            label_list[who]["bg"]="yellow"
            who+=1

    if round<2 and (who>27 or who==0):
        round+=1
        who=0
    if round==1:
        print(who)
        if who==ans[-1]+1:
            t.cancel()
        if who==ans[-1]-3:
            sec=0.7
        if sec!=0.7:
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
    cur.append(round)
    # print(round)


    # if r.count(1)==ans+3:
    #     t2=Timer(sec,dark)
    #     t2.start()
    # click+=1
    # if click-30==ans:
    #     # who=0
    #     # round=0
    #     # sec=0.1
    #     print("HI")
    # if(who<29+ans):
    #     t1=Timer(sec,turn)
    #     t1.start()
    #     label_list[cur[who]]["bg"]="yellow"
    #     label_list[cur[who-1]]["bg"]="whitesmoke"
    #     who+=1
    # if cur[who]==27:
    #     round+=1
    #     sec=0.3
    # r.append(round)
    # print(click)






    # t2=Timer(1,light(i))
    # t2.start()
    # t3=Timer(1,dark(i))
    # t3.start()
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
    # b=tk.Label(text=str(i))
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

go=tk.Button(text="go",command=turn)
go.grid(row=4,column=4)
ans.append(randint(0,27))#決定在哪個地方會停下來
print(ans)
window.mainloop()