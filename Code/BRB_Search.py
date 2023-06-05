from selenium.common import NoSuchElementException


def  Final_C(ORDERN,F,L):
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

    time.sleep(1)
    print("Running BRB Search")

    chrome_options = Options()
    chrome_options.add_argument('--kiosk-printing')
    chrome_options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(options=chrome_options)
    time.sleep(3)
    #try:
    driver.maximize_window()
    driver.get('https://casesearch.cookcountyclerkofcourt.org/CivilCaseSearchAPI.aspx ')
    driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div/div/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/input').click()


    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="MainContent_txtFirstName"]')))
    driver.find_element(By.XPATH,'//*[@id="MainContent_txtFirstName"]').send_keys(F)
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/input').send_keys(L,Keys.ENTER)

    driver.execute_script('window.print();')
    par_dir = os.path.dirname(os.getcwd())
    path = par_dir+"\\Output\\COOK_COUNTY\\" + "Order No "+str(int(ORDERN))

    name = "BRB Search"
    time.sleep(4)
    pyautogui.typewrite(path + '\\' + name + '.pdf')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(2)
    driver.close()

   # except Exception:
        #print(" The Recorder site server is down.")
if __name__ == '__main__':
    Final_C()

