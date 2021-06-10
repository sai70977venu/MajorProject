
import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font

window = tk.Tk()
window.title("Face_Recogniser")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
window.configure(background='black')

window.attributes('-toolwindow', True)

window.grid_rowconfigure(10, weight=1)
window.grid_columnconfigure(10, weight=1)


message = tk.Label(window, text="Employee Efficiency" ,bg="white"  ,fg="black"  ,width=50  ,height=3,font=('times', 30, 'italic bold')) 

message.place(x=200, y=20)

lbl = tk.Label(window, text="Enter Path",width=20  ,height=2  ,fg="black"  ,bg="white" ,font=('times', 15, ' bold ') ) 
lbl.place(x=400, y=200)

txt = tk.Entry(window,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))

message = tk.Label(window, text="" ,bg="black"  ,fg="black"  ,width=30  ,height=2, activebackground = "black" ,font=('times', 15, ' bold ')) 
message.place(x=700, y=400)

message2 = tk.Label(window, text="" ,fg="black"   ,bg="black",activeforeground = "green",width=30  ,height=2  ,font=('times', 15, ' bold ')) 
message2.place(x=700, y=650)

def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)   
    
 
def TakeImages():
    os.system("python start.py")


def getResults():
    pass


clearButton = tk.Button(window, text="Clear", command=clear  ,fg="black"  ,bg="white"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=950, y=200) 

takeImg = tk.Button(window, text="Start Process", command=TakeImages  ,fg="black"  ,bg="white"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
takeImg.place(x=200, y=500)

trainImg = tk.Button(window, text="Get Results", command=getResults  ,fg="black"  ,bg="white"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
trainImg.place(x=500, y=500)

quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="black"  ,bg="white"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=1100, y=500)

copyWrite = tk.Text(window, background=window.cget("background"), borderwidth=0,font=('times', 30, 'italic bold'))
copyWrite.tag_configure("superscript", offset=10)
copyWrite.configure(state="disabled",fg="red"  )
copyWrite.pack(side="left")
copyWrite.place(x=1200, y=750)

window.mainloop()