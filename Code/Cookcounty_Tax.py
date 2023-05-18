def Final_UI():
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
 import Code.New_update1_title
 import Code.Lien_Report
 import Code.BRB_Search
 import os


 dataframe1 = pd.read_excel('D:\\Title_Files\\Input\\Cook_county.xlsx')



 E = dataframe1[dataframe1.columns[0]].count()




 for i in range(E):
    EXCELADDRESS = str(dataframe1['Property Address'][i].replace("-",''))

    FName = (dataframe1['NAME'][0])
    F = FName.split()[0:1]
    L = FName.split()[-1]


    HOUSENUMBER=(EXCELADDRESS.split()[0:1])
    STREETNAME=(EXCELADDRESS.split()[1:])
    STREETNAME=(" ".join(STREETNAME))
    print(STREETNAME)

    ORDERN=int(dataframe1['Order No'][i])
    City = str(dataframe1['City'][i])
    CC=City.split()[-1]
    print(CC)
    PIN = (dataframe1['State'][i])
    PIN=PIN.split("-")[-1]
    print(PIN)

    print(str(ORDERN))


    print(EXCELADDRESS)

    chrome_options = Options()
    chrome_options.add_argument('--kiosk-printing')
    chrome_options.add_argument('--disable-extensions')


    driver = webdriver.Chrome(options=chrome_options)
    time.sleep(4)
    driver.maximize_window()
    driver.get('https://www.cookcountytreasurer.com/setsearchparameters.aspx')
    #driver.maximize_window()

    elem = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/form/div[4]/div[2]/div/div/div[2]/div/div/ul/li[3]/div/span")))

    driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[1]/div/ul/li[2]/div/ul/li[3]').click()
    elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[4]/div[2]/div/div/div[2]/div/div/ul/li[3]/div/span")))
    driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_ASPxPanel2_SearchByAddress1_txtStreetName"]').send_keys(STREETNAME)
    driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_ASPxPanel2_SearchByAddress1_txtHouseNumber"]').send_keys(HOUSENUMBER)
    driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[3]/div/div[1]/div[2]/div[11]/input').send_keys(PIN)

    driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[3]/div/div[1]/div[2]/div[9]/div[1]/input').send_keys(City,Keys.ENTER)

    try:
        z=driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[3]/div/div/div[2]/div[2]/table/tbody/tr[2]/td/div/div[2]/div[2]/div[2]/div[2]/span').text

        z1 = (z).split()[0:2]
        z2=" ".join(z1)
        print(z2.upper())
        Name = str(dataframe1['NAME'][i]).split()[0:2]
        Name1=(" ".join(Name))
        abc=10
        print("Looping")


        #WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'/ html / body / form / div[4] / div[2] / div / div / div[3] / div / div / div[2] / div[1] / span'))) ==True:
        driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[3]/div/div/div[2]/div[2]/table/tbody/tr[2]/td/div/div[2]/div[3]/a').click()
        aaa=driver.find_element(By.XPATH,'/html/body/form/div[4]/div/div/div/div[2]/div[4]/div[1]/div[2]/div/div[2]/span').text
        print(aaa)

        os.makedirs("D:\\Title_Files\\Output\\COOK_COUNTY\\" + "Order No " + str(int(ORDERN)))

        workbook = openpyxl.load_workbook('D:\\Title_Files\\Input\\Cook_county.xlsx')


        worksheet = workbook.active

        worksheet['B' + str(int(i+2))] = aaa
        #worksheet['B' + str(int(i+2))] = aaa


        workbook.save('D:\\Title_Files\\Input\\Cook_county.xlsx')


        driver.execute_script('window.print();')
        time.sleep(3)
        path="D:\\Title_Files\\Output\\COOK_COUNTY\\" + "Order No "+str(int(ORDERN))
        name="Tax Sheet"
        pyautogui.FAILSAFE = False
        pyautogui.typewrite(path +'\\'+ name + '.pdf')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(4)
        driver.close()

        Code.New_update1_title.Final_A(i)

        Code.Lien_Report.Final_B(ORDERN,F,L)


        Code.BRB_Search.Final_C(ORDERN,F,L)

        workbook1 = openpyxl.Workbook()
        sheet = workbook1.active

        sheet['A1'] = 'Order Number:'
        sheet['A2'] = 'BORROWER NAME:'
        sheet['A3'] = 'ADDRESS:'
        sheet['A4'] = 'COUNTY:'
        sheet['A5'] = 'APN:'
        sheet['A6'] = 'Legal:'
        sheet['A7'] = 'GTD:'
        sheet['A8'] = 'NAMES RUN:'
        sheet['A9'] = '###################################################################################'
        #sheet['A10']='DOC ID '

        df = pd.read_excel('D:\Title_Files\Input\Cook_county.xlsx')
        Ordernumber = df['Order No'][i]
        print(Ordernumber)
        BORROWERNAME = df['NAME'][i]
        print(BORROWERNAME)
        ADDRESS = df['Property Address'][i]
        print(ADDRESS)
        COUNTY = df['County Name'][i]
        print(COUNTY)
        APN = df['APN'][i]
        print(APN)
        NAMESRUN1 = df['NAME'][i]
        print(NAMESRUN1)
        GIT = df['GTD'][i]

        sheet['B1'] = Ordernumber
        sheet['B2'] = BORROWERNAME
        sheet['B3'] = ADDRESS
        sheet['B4'] = COUNTY
        sheet['B5'] = APN
        sheet['B6']="(NOT need for IL)"
        sheet['B7']=GIT
        sheet['B8'] = NAMESRUN1
        sheet['B9']="#############"
        #sheet['B10'] ='REC DATE'
        #sheet['C10']='INST NO'
        #sheet['D10']='BOOK-PAGE '

        workbook1.save('D:\\Title_Files\\Output\\COOK_COUNTY\\' + "Order No " + str(int(ORDERN))+'\\searchNote.xlsx')

        df1 = pd.read_excel('D:\\Title_Files\\Output\\COOK_COUNTY\\' + "Order No " + str(int(ORDERN))+'\\filterd_data.xlsx')
        f = df1[['Doc Number', 'Doc Type', 'Doc Executed', '1st PIN']]
        #print(f)

        df2 = pd.read_excel('D:\\Title_Files\\Output\\COOK_COUNTY\\' + "Order No " + str(int(ORDERN))+'\\searchNote.xlsx')

        df_combined = df2._append(f)
        combinedfile = 'D:\\Title_Files\\Output\\COOK_COUNTY\\' + "Order No " + str(int(ORDERN))+'\\FinalXL.xlsx'
        df_combined.to_excel(combinedfile, index=False)






    except:
        print("Mailing address is not matching")
        try:
            os.makedirs("D:\\Title_Files\\Output\\COOK_COUNTY\\" + "Order No " + str(ORDERN))
        except Exception:
            print("Error")
        workbook = openpyxl.load_workbook('D:\\Title_Files\\Input\\Cook_county.xlsx')
        worksheet = workbook.active
        worksheet['B' + str(int(i + 2))]='APN not Found'
        workbook.save('D:\\Title_Files\\Input\\Cook_county.xlsx')
        driver.close()
        print("Closed")


if __name__ == '__main__':
    Final_UI()

