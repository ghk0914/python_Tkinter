import tkinter as tk
from tkinter.constants import CENTER
from tkinter.constants import *
from math import factorial as fc
window=tk.Tk()
window.title("triangle")
window.resizable(False,False)
a=input()
a=int(a)
for n in range(0,a+1):
    for m in range(0,n+1):
        tk.Label(window,text=str(fc(n)//(fc(m)*fc(n-m)))).grid(row=n,column=a-n+2*m)
    #     print(fc(n)//(fc(m)*fc(n-m)),end=" ")
    # print()
window.mainloop()
