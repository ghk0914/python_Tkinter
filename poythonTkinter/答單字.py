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
window=tk.Tk()
window.title("答單字")
window.resizable(False,False)
testdata=[]
data=[]
mask=[]
mask_list=[]
counter=0
point=0
def you_sure():
    global counter,point
    if(counter==len(testdata)-1):
        entry["state"]=DISABLED
        sure["state"]=DISABLED

    if(counter<len(testdata)):
        s=entry.get()
        # print("s is ",end="")
        # print(s)
        # print("data counter is ",end="")
        # print(data[counter][0])
        # print("counter is ",end="")
        # print(counter)
        if(s==data[counter][0]):
            point+=1
    if(counter<len(testdata)):
        counter+=1
    if(counter<len(testdata)):
        eng_lab["text"]="English:"+maskdata[counter][0]
        chi_lab["text"]="Chinese:"+data[counter][1]
    crr_lab["text"]="答對題數:"+str(point)+"題"

# data=[["0"*2 for i in range(len(testdata))]]
with open("testdata.txt","r",encoding="utf-8") as fread:
    testdata=fread.read().splitlines()
    # print(testdata)
for i in range(len(testdata)):
    data.append(testdata[i].split(' '))
numpy.random.shuffle(data)
for i in range(len(testdata)):
    mask=sample(range(0,len(data[i][0]))
                ,int(len(data[i][0])*0.7))
    mask_list.append(mask)
# print(mask_list)
maskdata=copy.deepcopy(data)
for i in range(len(testdata)):
    for j in range(len(mask_list[i])):
        maskdata_list=list(maskdata[i][0])
        maskdata_list[mask_list[i][j]]="?"
        maskdata[i][0]="".join(maskdata_list)
print(data)
# print(maskdata)
    # maskdata[counter][0][i]="?"
eng_lab=tk.Label(text="English:"+maskdata[counter][0]
                 ,font=("Fixedsys",25))
eng_lab.grid(row=0,column=0)
chi_lab=tk.Label(text="Chinese:"+data[counter][1]
                 ,font=("Modern",25,"italic"))
chi_lab.grid(row=1,column=0)
crr_lab=tk.Label(text="答對題數:"+str(point)+"題"
                 ,font=("標楷體",25))
crr_lab.grid(row=2,column=0)
entry=tk.Entry(font=("Meiryo UI",25),justify=("center"))
entry.grid(row=3,column=0)
sure=tk.Button(text="確定",font=("微軟黑體",25,"bold")
               ,command=you_sure)
sure.grid(row=4,column=0)
# print(data)
# fontfamilylist = tkFont.families(root=window)#顯示font可用字體
# print(fontfamilylist)
window.mainloop()