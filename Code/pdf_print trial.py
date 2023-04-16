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
import pyautogui

pdf_path='D:\Title_Files\Processed'
name='index'

chrome_driver = 'D:\chromedriver_win32\chromedriver.exe'


chrome_options=Options()
chrome_options.add_argument('--kiosk-printing')
chrome_options.add_argument('--disable-extensions')

driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
driver.get('https://crs.cookcountyclerkil.gov/Search/Additional')
driver.maximize_window()

driver.execute_script('window.print();')
time.sleep(5)
pyautogui.typewrite(pdf_path)
pyautogui.press('enter')
pyautogui.typewrite(name)
pyautogui.press('enter')
print("Hi")
input()


'''
driver.execute_script('window.print();')

#wait for save
save_as_window=driver.window_handles[-1]
driver.switch_to.window(save_as_window)
time.sleep(2)
print("save page Appeared")

#save_button_possition=pyautogui.locateCenterOnScreen('save_button.png')
#pyautogui.click(save_button_possition)
print("Done")
'''


