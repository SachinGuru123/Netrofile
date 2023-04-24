
import json
import os
import sys
from PIL import Image, ImageTk
import Code.Cook_County_Netro_Search
import Code.Outlook_Automation_Files_Extraction
import Code.Outlook_mail_sender
from tkinter import Tk
import tkinter
from tkinter import ttk
import openpyxl,datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import click
import threading
import glob
import re
import PyPDF2
from tkinter import ttk

def B():
    messege_lable1 = tkinter.Label(lable2, text="Processing........", font=('Ariel', 12), fg='green', bg='white')
    messege_lable1.place(x=145, y=45)
    Code.Outlook_Automation_Files_Extraction.Final_B()
    messege_lable1 = tkinter.Label(lable2, text="completed           ", font=('Ariel', 12), fg='green', bg='white')
    messege_lable1.place(x=145, y=45)

def C():
    messege_lable2 = tkinter.Label(lable2, text="Processing........", font=('Ariel', 12), fg='green', bg='white')
    messege_lable2.place(x=185, y=450)
    Code.Outlook_mail_sender.Final_C()
    messege_lable2 = tkinter.Label(lable2, text="completed           ", font=('Ariel', 12), fg='green', bg='white')
    messege_lable2.place(x=185, y=450)


def Close():
    w.destroy()

def click():
    count_file = "D:\\Title_Files\\Config\\count.txt"

    if not os.path.exists(count_file):
        with open(count_file, 'w') as f:
            f.write("0")

    with open(count_file, 'r') as f:
        count = int(f.read())

    count +=1

    with open(count_file, 'w') as f:
        f.write(str(count))

    print(count)
    workbook = openpyxl.load_workbook('D:\\Title_Files\\Logs\\Logs.xlsx')
    worksheet = workbook.active
    start_time = datetime.datetime.now()
    worksheet["A" + str(count)] = os.getlogin()
    worksheet["B" + str(count)] = start_time
    workbook.save('D:\\Title_Files\\Logs\\Logs.xlsx')

    #getting Key from JSON file
    with open('D:\\Title_Files\\Config\\Title_conig_file.json', 'r') as f:

        data = json.load(f)
        for i in data:
            print(i)
            if os.path.isfile('D:\\Title_Files\\Input\\Cook_county.xlsx'):
             if i == 'Cook':
                Code.Cook_County_Netro_Search.Final_A()

    End_time = datetime.datetime.now()
    worksheet['C' + str(count)] = End_time
    worksheet['D' + str(count)] = "Task Completed"
    workbook.save('D:\\Title_Files\\Logs\\Logs.xlsx')

#if __name__=='__main__':
    #click()

w=Tk()
w.title("Netro_Smartsearch")
w.geometry('1900x1500')
w.iconbitmap("D:\\Title_Files\\Images\\RGBA.ico")

image = Image.open("D:\\Title_Files\\Images\\Coforge_Logo.jpg")

notebook = ttk.Notebook(w)

notebook.pack(pady=5, expand=True)

frame1 = ttk.Frame(notebook, width=4000, height=2080)  # for Frame 1 Tab

photo = ImageTk.PhotoImage(image)
lable = tkinter.Label(frame1, image=photo)

Start_button = tkinter.Button(frame1, text="Start", command=lambda: threading.Thread(target=click).start(), font=('Ariel', 13), bg="lightblue", fg='black')
Start_button.place(x=330,y=160,height=35, width=150)
close_button=tkinter.Button(frame1,text="Close",command=Close,font=('Ariel', 13), bg="lightblue", fg='black')
close_button.place(x=630,y=160,height=35, width=150)

messege_lable1 = tkinter.Label(frame1, text="NetroSmart Search ", font=('Ariel', 22), fg='green', bg='white')
messege_lable1.place(x=460, y=110)
messege_lable2 = tkinter.Label(frame1, text="Digital Platform - Innovations", font=('Ariel', 20), fg='green', bg='white')
messege_lable2.place(x=850, y=480)
lable.pack()

frame1.pack(fill='both', expand=True)
notebook.add(frame1, text=' Netro Search')

frame2 = ttk.Frame(notebook, width=4000, height=2080)  ## for Frame 2 Tab

image2 = Image.open("D:\\Title_Files\\Images\\outlook-featured-2100x1200.jpg")
photo2 = ImageTk.PhotoImage(image2)
lable2 = tkinter.Label(frame2, image=photo2)

Start_button2 = tkinter.Button(frame2, text="Outlook Mails Extraction", command=lambda: threading.Thread(target=B).start(), font=('Ariel', 13), bg="green", fg='black')
Start_button2.place(x=245,y=85,height=35, width=450)

Start_button3 = tkinter.Button(frame2, text="Outlook Mails Sender", command=lambda: threading.Thread(target=C).start(), font=('Ariel', 13), bg="green", fg='black')
Start_button3.place(x=245,y=500,height=35, width=450)



lable2.pack()
frame2.pack(fill='both', expand=True)
notebook.add(frame2, text='Outlook Automation')

w.mainloop()












































































































































