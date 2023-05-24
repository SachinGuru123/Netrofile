
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import shutil, os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import glob
import re,PyPDF2
from openpyxl import load_workbook
import openpyxl
import requests

import os
'''
chrome_options = Options()
chrome_options.add_argument('--kiosk-printing')
chrome_options.add_argument('--disable-extensions')


driver = webdriver.Chrome(options=chrome_options)
time.sleep(4)
driver.maximize_window()
driver.get('https://crs.cookcountyclerkil.gov/Search')
driver.maximize_window()

driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/form/div[2]/div[2]/div[3]/div/div[2]/input').send_keys("Will smith",Keys.ENTER)

j=1
link=[]
while j< int(80):


    href_ad = driver.find_element(By.XPATH, '//*[@id="tblData"]/tbody/tr[' + str(j) + ']/td[2]/a').get_attribute("href")
    #print(href_ad)
    link.append(href_ad)
    j +=1
    #print(j)

i = 1
for k in link:

    driver.get(k)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[3]/div/div/fieldset/div[1]/div[2]/div/div/div/a')))
    LinkF = driver.find_element(By.XPATH,
                            '/html/body/div[2]/div/div[3]/div/div/fieldset/div[1]/div[2]/div/div/div/a').get_attribute(
        'href')
    print(LinkF)

    max_retry = 3
    retry_count = 0
    while retry_count < max_retry:
        try:
            r = requests.get(LinkF)
            time.sleep(3)  # verify=False
            with open(
                    'D:\\Title_Files\\output\\COOK_COUNTY\\Order No 1170191\\D' + str(i) + '.pdf', 'wb') as fd:
                for chunk in r.iter_content(chunk_size=40):
                    fd.write(chunk)
            break

        except Exception as e:
            retry_count += 1



    i +=1'''
import shutil

source_folder=('D:\\Title_Files\\Output\\COOK_COUNTY\\Order No 1173214')
destination_folder = ('D:\\Title_Files\\Processed')

shutil.move(source_folder,destination_folder)