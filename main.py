import json
import os
import sys
from PIL import Image, ImageTk
import Code.Cook_County_Netro_Search
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
w.geometry('1700x1200')
image = Image.open("D:\\Title_Files\\Images\\Coforge_Logo.jpg")
photo = ImageTk.PhotoImage(image)

lable = tkinter.Label(w, image=photo)
w.iconbitmap("D:\\Title_Files\\Images\\RGBA.ico")
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







