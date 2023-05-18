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

    dataframe1 = pd.read_excel('D:\\Title_Files\\Input\\Cook_county.xlsx')
    EXCELADDRESS = str(dataframe1['NAME'][0].replace("-",''))
    Firstname=(EXCELADDRESS.split()[0:1])
    Lastname=(EXCELADDRESS.split()[-1])
    ORDERN=(dataframe1['Order No'][0])#.replace("-",''))
    print(Lastname)
    print(Firstname)
    County='CooK'


    chrome_options = Options()
    chrome_options.add_argument('--kiosk-printing')
    chrome_options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get('https://mytax.illinois.gov/?link=TaxLienReg')
    driver.maximize_window()

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

    elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[1]/div/div/main/div/div/div[2]/div[2]/form/div[1]/div/div[1]/div[1]/table/tbody/tr[2]/td/div/div/div/h3')))

    time.sleep(8)

    driver.execute_script('window.print();')

    path="D:\\Title_Files\\Output\\COOK_COUNTY\\" + "Order No "+str(int(ORDERN))

    name="Lien_Report"
    time.sleep(3)
    pyautogui.typewrite(path +'\\'+ name + '.pdf')
    pyautogui.press('enter')
    time.sleep(5)

    driver.close()
if __name__ == '__main__':
    Final_B()



