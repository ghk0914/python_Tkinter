import tkinter as tk
from tkinter.constants import CENTER
from tkinter.constants import *
window=tk.Tk()
window.title("改變顏色")
window.geometry('500x500')
window.resizable(False,False)
window.iconbitmap("C:/Users/Adimn/Downloads/stock-folder-icons-3-by-hamza-saleem/ico/Group Folder.ico")
lbtext=tk.StringVar()
a=tk.StringVar()
b=tk.StringVar()
c=tk.StringVar()
colarr=[]
colarr.append("#")
for i in range(3):
    colarr.append("FF")

# def enter1():
#     a=int(entry1.get())
#     global colarr
#     global color
#     if a>255 or a<0:
#         label1['text']="非法輸入"
#     else:
#         colarr[1]="{:02X}".format(a)
#         label1['text']="合法輸入"
#         color="".join(colarr)
#         label2["bg"]=color
#         print(colarr,end="||")
#         print(color)
# def enter2():
#     b=int(entry2.get())
#     global colarr
#     global color
#     if b>255 or b<0:
#         label1['text']="非法輸入"
#     else:
#          colarr[2]="{:02X}".format(b)
#          label1['text']="合法輸入"
#          color=''
#          color="".join(colarr)
#          label2["bg"]=color
#          print(colarr,end="||")
#          print(color)
# def enter3():
#     c=int(entry3.get())    
#     global color
#     global colarr
#     if c>255 or c<0:
#         label1['text']="非法輸入"
#     else:
#          colarr[3]="{:02X}".format(c)
#          label1['text']="合法輸入"
#          color="".join(colarr)
#          label2["bg"]=color
#          print(colarr,end="||")
#          print(color)
def entersum():
    a=int(entry1.get())  
    b=int(entry2.get())  
    c=int(entry3.get())    
    global color
    global colarr
    if a>255 or a<0:
        label1['text']="非法輸入"
    if b>255 or b<0:
        label1['text']="非法輸入"
    if c>255 or c<0:
        label1['text']="非法輸入"
    else:
         colarr[1]="{:02X}".format(a)
         colarr[2]="{:02X}".format(b)
         colarr[3]="{:02X}".format(c)
         label1['text']="合法輸入"
         color="".join(colarr)
         label2["bg"]=color
         print(colarr,end="||")
         print(color)
color=''
for i in range(4):
    color+=colarr[i]
entry1=tk.Entry(window,font=("標楷體",10),textvariable=a)
entry1.place(x=5,y=250,anchor=W)
button1=tk.Button(window,text="red",bg="red")
button1.place(x=5,y=280,anchor=W)

entry2=tk.Entry(window,font=("標楷體",10),textvariable=b)
entry2.place(x=250,y=250,anchor=CENTER)
button2=tk.Button(window,text="green",bg="green")
button2.place(x=250,y=280,anchor=CENTER)

entry3=tk.Entry(window,font=("標楷體",10),textvariable=c)
entry3.place(x=480,y=250,anchor=E)
button3=tk.Button(window,text="blue",bg="#00BFFF")
button3.place(x=480,y=280,anchor=E)

buttonsum=tk.Button(window,text="合成",command=entersum)
buttonsum.place(x=232,y=310)

label1=tk.Label(window,font=("標楷體",25),bg="white",width=10,height=1)
label1.place(x=160,y=350)
label2=tk.Label(window,font=("標楷體",25),width=30,height=6)
label2.place(x=0,y=10)

window.mainloop()