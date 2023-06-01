from datetime import datetime

from selenium.common import NoSuchElementException


def Final_UI(file):
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

 import openpyxl
 import Code.New_update1_title
 import Code.Lien_Report
 import Code.BRB_Search
 import os

 time.sleep(1)
 dataframe1 = pd.read_excel(os.getcwd()+'\\Input\\'+file,engine='openpyxl')



 E = dataframe1[dataframe1.columns[0]].count()




 for i in range(E):
  try:
    workbook = openpyxl.load_workbook(os.getcwd() + '\\Input\\'+file)
    worksheet = workbook.active
    start_time = datetime.now()

    worksheet['j' + str(int(i + 2))] = start_time

    workbook.save(os.getcwd()+'\\Input\\'+file)

    EXCELADDRESS = str(dataframe1['Property Address'][i].replace("-",'')).lower()


    FName = (dataframe1['NAME'][i])
    F = FName.split()[0:1]
    L = FName.split()[-1]


    HOUSENUMBER=(EXCELADDRESS.split()[0:1])
    STREETNAME=(EXCELADDRESS.split()[1:])

    STREETNAME=(" ".join(STREETNAME)).lower()


    #if 'unit' in EXCELADDRESS:
        #UNIT = str(EXCELADDRESS.split('unit')[-1])
        #print(UNIT)




    if "avenue" in STREETNAME: # added to replace AVenue, AVENUE words and also to remove after the Avenue word
        STREETNAME = STREETNAME.replace("avenue", "ave")
        STREETNAME = STREETNAME.split("ave")
        STREETNAME = STREETNAME[0]

    elif "ave" in STREETNAME: # added to replace AVenue, AVENUE words and also to remove after the Avenue word

        STREETNAME = STREETNAME.split("ave")
        STREETNAME = STREETNAME[0]


    print(STREETNAME)


    ORDERN=int(dataframe1['Order No'][i])
    City = str(dataframe1['City'][i])

    #CC=City.split()[-1]

    PIN = str(dataframe1['Zip'][i])
    #PIN=PIN.split("-")[-1]


    chrome_options = Options()
    chrome_options.add_argument('--kiosk-printing')
    chrome_options.add_argument('--disable-extensions')


    driver = webdriver.Chrome(options=chrome_options)
    time.sleep(4)
    driver.maximize_window()
    driver.get('https://www.cookcountytreasurer.com/setsearchparameters.aspx')# opening Tax page
    #driver.maximize_window()
    print("Running Tax Page")
    elem = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/form/div[4]/div[2]/div/div/div[2]/div/div/ul/li[3]/div/span")))
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[1]/div/ul/li[2]/div/ul/li[3]').click()
    time.sleep(2)
    elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[4]/div[2]/div/div/div[2]/div/div/ul/li[3]/div/span")))
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_ASPxPanel2_SearchByAddress1_txtStreetName"]').send_keys(STREETNAME)
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_ASPxPanel2_SearchByAddress1_txtHouseNumber"]').send_keys(HOUSENUMBER)
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[3]/div/div[1]/div[2]/div[11]/input').send_keys(PIN)
    time.sleep(1)

    if 'unit' in EXCELADDRESS:
        UNIT = str(EXCELADDRESS.split('unit')[-1])
        print(UNIT)

        driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[3]/div/div[1]/div[2]/div[7]/input').send_keys(UNIT)


    driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[3]/div/div[1]/div[2]/div[9]/div[1]/input').send_keys(City,Keys.ENTER)

    TAXmaincondition=driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[3]/div/div/div[2]/div[1]/span').text



    try:
     if (TAXmaincondition) == 'Found one record matching your search criteria.':
        print("Direct Search")

        time.sleep(4)
        z=driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[3]/div/div/div[2]/div[2]/table/tbody/tr[2]/td/div/div[2]/div[2]/div[2]/div[2]/span').text # for checking elemnts in Tax page
        #print(text)

        z1 = (z).split()[0:2]
        z2=" ".join(z1)
        #print(z2.upper())
        Name = str(dataframe1['NAME'][i]).split()[0:2]
        Name1=(" ".join(Name))
        abc=10


        driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[3]/div/div/div[2]/div[2]/table/tbody/tr[2]/td/div/div[2]/div[3]/a').click()
        text=driver.find_element(By.XPATH,'/html/body/form/div[4]/div/div/div/div[2]/div[4]/div[1]/div[2]/div/div[2]/span').text #for getting APN number from Tax page
        #print(text)

        os.makedirs(os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No " + str(int(ORDERN)))


        workbook = openpyxl.load_workbook(os.getcwd()+'\\Input\\'+file)


        worksheet = workbook.active
        #print("access to excel sheet")

        worksheet['B' + str(int(i+2))] = text
        worksheet['M1']='GTD'
        worksheet['N1'] = 'Comments'


        workbook.save(os.getcwd()+'\\Input\\'+file)
        #print("saving ")

        driver.execute_script('window.print();')
        time.sleep(3)
        path=os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No "+str(int(ORDERN))
        name="Tax Sheet"
        #pyautogui.FAILSAFE = False
        pyautogui.typewrite(path +'\\'+ name + '.pdf')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(4)
        driver.close()

        Code.New_update1_title.Final_A(i,file)

        #Code.Lien_Report.Final_B(ORDERN,F,L,file)


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

        print("reading excel sheet")
        df = pd.read_excel(os.getcwd()+'\\Input\\'+file,engine="openpyxl")



        Ordernumber = df['Order No'][i]

        BORROWERNAME = df['NAME'][i]

        ADDRESS = df['Property Address'][i]

        COUNTY = df['County Name'][i]

        APN = df['APN'][i]

        NAMESRUN1 = df['NAME'][i]

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

        time.sleep(2)
        workbook1.save(os.getcwd()+'\\Output\\COOK_COUNTY\\' + "Order No " + str(int(ORDERN))+'\\Note.xlsx')

        df1 = pd.read_excel(os.getcwd()+'\\Output\\COOK_COUNTY\\' + "Order No " + str(int(ORDERN))+'\\filterd_data.xlsx',engine='openpyxl')
        f = df1[['Doc Number', 'Doc Type', 'Doc Executed', '1st PIN']]


        df2 = pd.read_excel(os.getcwd()+'\\Output\\COOK_COUNTY\\' + "Order No " + str(int(ORDERN))+'\\Note.xlsx',engine='openpyxl')

        df_combined = df2._append(f)
        combinedfile = os.getcwd()+'\\Output\\COOK_COUNTY\\' + "Order No " + str(int(ORDERN))+'\\SearchNoteXL.xlsx'
        df_combined.to_excel(combinedfile, index=False)

        end_time = datetime.now()
        worksheet['k' + str(int(i + 2))] = end_time
        workbook.save(os.getcwd()+'\\Input\\'+file)

        source_folder = (os.getcwd() + "\\Output\\COOK_COUNTY\\" + "Order No " + str(ORDERN))
        destination_folder = (os.getcwd() + "\\Processed")

        shutil.move(source_folder, destination_folder)
        print("Completed:"+str(int(i)+int(1)))

     else:
         driver.close()
         try:
             os.makedirs(os.getcwd() + "\\Output\\COOK_COUNTY\\" + "Order No " + str(ORDERN))
         except Exception:
             print("Error")
         workbook = openpyxl.load_workbook(os.getcwd() + '\\Input\\' + file)
         worksheet = workbook.active
         worksheet['N1']='Comments'
         worksheet['N' + str(int(i + 2))] = 'Multiple Property Available'
         workbook.save(os.getcwd() + '\\Input\\' + file)


    except Exception:
        print("Max Retry Error in Tax Page")

        try:
            os.makedirs(os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No " + str(ORDERN))
        except Exception :
            print("Error")
        workbook = openpyxl.load_workbook(os.getcwd()+'\\Input\\'+file)
        worksheet = workbook.active
        worksheet['B' + str(int(i + 2))]='Max Retry Error in Tax Page/ Recorder Page'
        workbook.save(os.getcwd()+'\\Input\\'+file)
        driver.close()


        #print("Closed")

  except Exception:
        print(" Maximum Retry Error.")





if __name__ == '__main__':
    Final_UI()

