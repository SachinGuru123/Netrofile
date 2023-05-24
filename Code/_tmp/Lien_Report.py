<<<<<<< HEAD:Code/Dummy.py

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
=======
from selenium.common import NoSuchElementException


def Final_B(ORDERN,F,L):
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

    dataframe1 = pd.read_excel(os.getcwd()+'\\Input\\Cook_county.xlsx')
    EXCELADDRESS = str(dataframe1['NAME'][0].replace("-",''))
    Firstname=(EXCELADDRESS.split()[0:1])
    Lastname=(EXCELADDRESS.split()[-1])
    # ORDERN=(dataframe1['Order No'][0])#.replace("-",''))
    print(Lastname)
    print(Firstname)
    County='CooK'

    #try:
    chrome_options = Options()
    chrome_options.add_argument('--kiosk-printing')
    chrome_options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(options=chrome_options)
    time.sleep(3)
    driver.maximize_window()
    driver.get('https://mytax.illinois.gov/?link=TaxLienReg')
    #driver.maximize_window()

    elem = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//html/body/div[2]/div/div[1]/div/div/main/div/div/div[2]/div[2]/form/div[1]/div/div[2]/div[1]/div/div/div/ul/li[2]/a/span/span")))
    elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[1]/div/div/main/div/div/div[2]/div[2]/form/div[1]/div/div[2]/div[1]/div/div/div/ul/li[2]/a/span/span')))
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/main/div/div/div[2]/div[2]/form/div[1]/div/div[2]/div[1]/div/div/div/ul/li[2]/a/span/span').click()
    time.sleep(1)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[1]/div/div/main/div/div/div[2]/div[2]/form/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/table/tbody/tr[3]/td[1]/div/div/div/input')))
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/main/div/div/div[2]/div[2]/form/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/table/tbody/tr[3]/td[1]/div/div/div/input').send_keys(F)
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/main/div/div/div[2]/div[2]/form/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/table/tbody/tr[4]/td/div/div/div/input').send_keys(L)
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/main/div/div/div[2]/div[2]/form/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/table/tbody/tr[4]/td[1]/div/div/div/input').send_keys("Cook")
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/main/div/div/div[2]/div[2]/form/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/table/tbody/tr[4]/td[1]/div/div/div/input').send_keys(Keys.ENTER)
    time.sleep(1)
    elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[1]/div/div/main/div/div/div[2]/div[2]/form/div[1]/div/div[2]/div[2]/div/div/div[5]/div/div/div/div[1]/table/tbody/tr[2]/td[3]/div/div/div/button/span/span')))
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/main/div/div/div[2]/div[2]/form/div[1]/div/div[2]/div[2]/div/div/div[5]/div/div/div/div[1]/table/tbody/tr[2]/td[3]/div/div/div/button/span/span').click()
    time.sleep(1)
>>>>>>> 062168a37bf55e848ea4e8f582cd440647d1cc5c:Code/_tmp/Lien_Report.py

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

<<<<<<< HEAD:Code/Dummy.py


    i +=1'''
import shutil

source_folder=('D:\\Title_Files\\Output\\COOK_COUNTY\\Order No 1173214')
destination_folder = ('D:\\Title_Files\\Processed')

shutil.move(source_folder,destination_folder)
=======
    time.sleep(8)

    driver.execute_script('window.print();')

    path=os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No "+str(int(ORDERN))

    name="Lien_Report"
    time.sleep(3)
    pyautogui.typewrite(path +'\\'+ name + '.pdf')
    pyautogui.press('enter')
    time.sleep(5)

    driver.close()

    #except Exception:
        #print(" The Recorder site server is down.")
if __name__ == '__main__':
    Final_B()



>>>>>>> 062168a37bf55e848ea4e8f582cd440647d1cc5c:Code/_tmp/Lien_Report.py
