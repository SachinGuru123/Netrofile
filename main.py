# import json
# import sys
from PIL import Image, ImageTk
from tkinter import Tk
import tkinter
# from tkinter import ttk
# import datetime
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import click
import threading
# import glob
# import re
# import PyPDF2
import Code.New_update1_title
import Code.Lien_Report
import Code.BRB_Search
import Code.Cookcounty_Tax as cook
import os

def Close():
    w.destroy()

def click():
    cook.Final_UI()


w=Tk()
w.title("Netro_Smartsearch")
w.geometry('1700x1200')

#image = Image.open("D:\\Title_Files\\Images\\Coforge_Logo.jpg")
image = Image.open(os.getcwd()+"\\Images\\Coforge_Logo.jpg")
#dirpath=os.getcwd()


photo = ImageTk.PhotoImage(image)

lable = tkinter.Label(w, image=photo)

#w.iconbitmap("D:\\Title_Files\\Images\\RGBA.ico")
w.iconbitmap(os.getcwd()+"\\Images\\RGBA.ico")


Start_button = tkinter.Button(w, text="Start", command=lambda: threading.Thread(target=click).start(), font=('Ariel', 13), bg="lightblue", fg='black')
Start_button.place(x=330,y=160,height=35, width=150)
close_button=tkinter.Button(w,text="Close",command=Close,font=('Ariel', 13), bg="lightblue", fg='black')
close_button.place(x=630,y=160,height=35, width=150)


messege_lable1 = tkinter.Label(w, text="NetroSmart Search ", font=('Ariel', 22), fg='green', bg='white')
messege_lable1.place(x=460, y=110)
messege_lable2 = tkinter.Label(w, text="Digital Platform - Innovations", font=('Ariel', 20), fg='green', bg='white')
messege_lable2.place(x=850, y=480)

lable.pack()
w.mainloop()







