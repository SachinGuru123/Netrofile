from datetime import datetime
import http.client
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import openpyxl
import Code.New_update1_title
import Code.Lien_Report
import Code.BRB_Search
import getOrders
import os
from PyPDF2 import PdfMerger
from selenium.common import NoSuchElementException

def mergepdf(orderId):
    source_dir=os.getcwd()+'\\Output\\COOK_COUNTY\\Order no '+orderId+'\\'
    merger = PdfMerger()
    try:
        for item in os.listdir(source_dir):
            if item.endswith('pdf'):
                merger.append(source_dir + item)

        merger.write(source_dir + 'Mergedpdf.pdf')
    except Exception as e:
        print("pdf could not be merged."+str(e))

    merger.close()

def Final_UI(file):

 dataframe1 = pd.read_excel(os.getcwd()+'\\Input\\'+file,engine='openpyxl')

 E = dataframe1[dataframe1.columns[0]].count()
 orderId=""
 for i in range(E):
  try:
    workbook = openpyxl.load_workbook(os.getcwd() + '\\Input\\'+file)
    worksheet = workbook.active
    start_time = datetime.now()
    worksheet['j' + str(int(i + 2))] = start_time
    workbook.save(os.getcwd()+'\\Input\\'+file)
    EXCELADDRESS = str(dataframe1['Property Address'][i].replace("-",''))

    FName = (dataframe1['NAME'][0])
    F = FName.split()[0:1]
    L = FName.split()[-1]


    HOUSENUMBER=(EXCELADDRESS.split()[0:1])
    STREETNAME=(EXCELADDRESS.split()[1:])
    STREETNAME=(" ".join(STREETNAME))


    ORDERN=int(dataframe1['Order No'][i])
    orderId = ORDERN         #to send order id to updatestatus API
    City = str(dataframe1['City'][i])
    CC=City.split()[-1]

    PIN = (dataframe1['State'][i])
    PIN=PIN.split("-")[-1]


    chrome_options = Options()
    chrome_options.add_argument('--kiosk-printing')
    chrome_options.add_argument('--disable-extensions')


    driver = webdriver.Chrome(options=chrome_options)
    time.sleep(4)
    driver.maximize_window()
    driver.get('https://www.cookcountytreasurer.com/setsearchparameters.aspx')
    #driver.maximize_window()

    elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[4]/div[2]/div/div/div[2]/div/div/ul/li[3]/div/span")))
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[1]/div/ul/li[2]/div/ul/li[3]').click()
    time.sleep(2)
    elem1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[4]/div[2]/div/div/div[2]/div/div/ul/li[3]/div/span")))
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_ASPxPanel2_SearchByAddress1_txtStreetName"]').send_keys(STREETNAME)
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_ASPxPanel2_SearchByAddress1_txtHouseNumber"]').send_keys(HOUSENUMBER)
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[3]/div/div[1]/div[2]/div[11]/input').send_keys(PIN)
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[3]/div/div[1]/div[2]/div[9]/div[1]/input').send_keys(City,Keys.ENTER)

    #AXmaincondition=driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[3]/div/div/div[2]/div[1]/span').text


    try:
     #if TAXmaincondition == 'Found one record matching your search criteria.':
        #WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[3]/div/div/div[2]/div[2]/table/tbody/tr[2]/td/div/div[2]/div[2]/div[2]/div[2]/span')))
        time.sleep(4)
        z=driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[3]/div/div/div[2]/div[2]/table/tbody/tr[2]/td/div/div[2]/div[2]/div[2]/div[2]/span').text
        #print(text)

        z1 = (z).split()[0:2]
        z2=" ".join(z1)
        #print(z2.upper())
        Name = str(dataframe1['NAME'][i]).split()[0:2]
        Name1=(" ".join(Name))
        abc=10
       # print("Looping")


        #WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'/ html / body / form / div[4] / div[2] / div / div / div[3] / div / div / div[2] / div[1] / span'))) ==True:
        driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div/div[3]/div/div/div[2]/div[2]/table/tbody/tr[2]/td/div/div[2]/div[3]/a').click()
        text=driver.find_element(By.XPATH,'/html/body/form/div[4]/div/div/div/div[2]/div[4]/div[1]/div[2]/div/div[2]/span').text
        #print(text)

        os.makedirs(os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No " + str(int(ORDERN)))


        workbook = openpyxl.load_workbook(os.getcwd()+'\\Input\\'+file)


        worksheet = workbook.active
        #print("access to excel sheet")
        worksheet['B' + str(int(i+2))] = text
        #worksheet['B' + str(int(i+2))] = text


        workbook.save(os.getcwd()+'\\Input\\'+file)
        #print("saving ")

        driver.execute_script('window.print();')
        time.sleep(3)
        path=os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No "+str(int(ORDERN))
        name="Tax Sheet"
        pyautogui.FAILSAFE = False
        pyautogui.typewrite(path +'\\'+ name + '.pdf')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(4)
        driver.close()

        Code.New_update1_title.Final_A(i)

        Code.Lien_Report.Final_B(ORDERN,F,L,file)


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

        df = pd.read_excel(os.getcwd()+'\\Input\\'+file,engine="openpyxl")



        #print("value of i is "+str(i))
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
        #sheet['B10'] ='REC DATE'
        #sheet['C10']='INST NO'
        #sheet['D10']='BOOK-PAGE '

        workbook1.save(os.getcwd()+'\\Output\\COOK_COUNTY\\' + "Order No " + str(int(ORDERN))+'\\searchNote.xlsx')

        df1 = pd.read_excel(os.getcwd()+'\\Output\\COOK_COUNTY\\' + "Order No " + str(int(ORDERN))+'\\filterd_data.xlsx',engine='openpyxl')
        f = df1[['Doc Number', 'Doc Type', 'Doc Executed', '1st PIN']]

        df2 = pd.read_excel(os.getcwd()+'\\Output\\COOK_COUNTY\\' + "Order No " + str(int(ORDERN))+'\\searchNote.xlsx',engine='openpyxl')

        df_combined = df2.append(f)
        combinedfile = os.getcwd()+'\\Output\\COOK_COUNTY\\' + "Order No " + str(int(ORDERN))+'\\FinalXL.xlsx'
        df_combined.to_excel(combinedfile, index=False)

        end_time = datetime.now()
        worksheet['k' + str(int(i + 2))] = end_time
        workbook.save(os.getcwd()+'\\Input\\'+file)

        #for updating order status
        status="Completed"
        comments="Completed successfully"
        mergepdf(ORDERN)
        files = [
            ('UploadFile',("Mergedpdf.pdf", open(os.getcwd() + '\\Output\\COOK_COUNTY\\'+str(orderId)+'\\Mergedpdf.pdf','rb'), 'pdf'))
        ]

        getOrders.uploadDocument(orderId, status, comments, files)


    except Exception as e:

        print("EXception : "+str(e))
        status = "Exception"
        comments = e
        getOrders.updateStatus(orderId, status, comments)
        try:
            os.makedirs(os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No " + str(ORDERN))
        except Exception as e:
            print("Error : "+str(e))
            status="Exception"
            comments=e

        workbook = openpyxl.load_workbook(os.getcwd()+'\\Input\\'+file)
        worksheet = workbook.active
        worksheet['B' + str(int(i + 2))]='Maximum Retry Error'
        workbook.save(os.getcwd()+'\\Input\\'+file)
        driver.close()
        #print("Closed")

  except Exception as e:
      status = "Exception"
      comments = e
      getOrders.updateStatus(orderId, status, comments)
      print(" Maximum Retry Error."+str(e))









if __name__ == '__main__':
    Final_UI()

