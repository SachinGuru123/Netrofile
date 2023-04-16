import datetime
import sys
import threading
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import shutil, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from openpyxl import load_workbook
from selenium.webdriver.common.action_chains import ActionChains
from tkinter import Tk
import tkinter
import pandas as pd
import selenium.webdriver
import requests
from PIL import Image, ImageTk
from tkinter import ttk
import requests
import shutil
import threading
import openpyxl
from urllib.parse import urljoin
import requests
from pyhtml2pdf import converter
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import math
from selenium.webdriver.common.action_chains import ActionChains
import sys
from PIL import Image
import glob
import img2pdf
from PIL import Image
import os
from pypdf import PdfMerger
import glob


chrome_driver = 'D:\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(chrome_driver)

driver.maximize_window()
driver.get('https://crs.cookcountyclerkil.gov/Search/Additional')
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div[3]/div[2]/h2/button').click()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[3]/div[2]/div/div/form/div[1]/div/input').send_keys("MOIRA ZALE")
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[3]/div[2]/div/div/form/div[1]/div/input').send_keys(Keys.ENTER)

Viewport_height=driver.execute_script("return window.innerHeight")
page_height=driver.execute_script('return document.body.scrollHeight')

scrolls_required=math.ceil(int(page_height / Viewport_height))
print(scrolls_required)
action=ActionChains(driver)
scrolls_required=int(scrolls_required+1)

for i in range(int(scrolls_required)):
   #action.send_keys(Keys.PAGE_DOWN)
   action.perform()
   driver.maximize_window()
   time.sleep(2)
   screenshot = driver.find_element(By.TAG_NAME, 'body').screenshot_as_png
   action.send_keys(Keys.PAGE_DOWN)
   #screenshot=driver.save_screenshot("D:\\Title_Files\\Logs\\image"+str(i)+".png")


   with open("D:\\Title_Files\\Logs\\image"+str(i)+".png", 'wb') as f:

       f.write(screenshot)



list_im = []
folder='D:\\Title_Files\\Logs'
png_path=glob.glob(os.path.join(folder,"*.png"))

for i in png_path:
   list_im.append(i)


i=1
for j in list_im:
    image = Image.open(j)
    pdf_bytes = img2pdf.convert(image.filename)
    file = open('D:\\Title_Files\\Logs\\'+str(i)+'.pdf', "wb")
    print(j)
    file.write(pdf_bytes)
    time.sleep(1)
    image.close()
    file.close()
    i=i+1


################
pdfs = []

folder="D:\\Title_Files\\Logs"
png_path=glob.glob(os.path.join(folder,"*.pdf"))
for i in png_path:
    pdfs.append(i)

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("D:\\Title_Files\\Logs\\result.pdf")
merger.close()
input()
