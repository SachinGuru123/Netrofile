from selenium.common import NoSuchElementException


def Final_A(i):

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
    import pyautogui
    import glob
    import re, PyPDF2
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from bs4 import BeautifulSoup
    from datetime import datetime
    import math

    time.sleep(1)
    dataframe1 = pd.read_excel(os.getcwd()+'\\Input\\Cook_county.xlsx')


    E = dataframe1[dataframe1.columns[0]].count()
    #print(dataframe1['County Name'][0])
    print("Running Recorder Page")

    #try:
    if dataframe1['County Name'][i]== ('Cook'):

            EXCELAPN = str(dataframe1['APN'][i])  # .replace("-",''))
            #print(EXCELAPN)

            EXCELNAME = dataframe1['NAME'][i]

            ExCELADDRESS = dataframe1['Property Address'][i]
            aa = ExCELADDRESS.split()[0:3]
            ab = (' '.join(map(str, aa)))

            #print(ab)
            EXCELORDERNO = int(dataframe1['Order No'][i])
            #print(EXCELORDERNO)

            # order number is created
            # os.makedirs("Output\\COOK_COUNTY\\" + "Order No " + str(int(EXCELORDERNO)))

            chrome_driver = 'chromedriver_win32\chromedriver.exe'

            chrome_options = Options()
            chrome_options.add_argument('--kiosk-printing')
            chrome_options.add_argument('--disable-extensions')

            driver = webdriver.Chrome(options=chrome_options)
            time.sleep(2)
            driver.get('https://crs.cookcountyclerkil.gov/Search')
            driver.maximize_window()
            time.sleep(2)

            # driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div[3]/div[2]/h2/button').click()
            # time.sleep(3)
            # driver.find_element(By.XPATH, '//*[@id="RecordedFromDate"]').send_keys(StartDate)
            # driver.find_element(By.XPATH, '//*[@id="RecordedToDate"]').send_keys(EndDate)

            driver.find_element(By.XPATH,
                                '/html/body/div[2]/div/div[3]/div/div/form/div[2]/div[2]/div[3]/div/div[2]/input').send_keys(
                EXCELNAME + " " + ab, Keys.ENTER)


            aq=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/form[1]/div[2]/div/div[2]').text

            workbook = openpyxl.load_workbook(os.getcwd()+'\\Input\\Cook_county.xlsx')
            worksheet = workbook.active
            GIT=aq.split("|")[0]
            worksheet['H' + str(int(i + 2))] =GIT
            workbook.save(os.getcwd()+'\\Input\\Cook_county.xlsx')

            # converter.convert(driver., "D:\Title_Files\PN Results.pdf")
            a = driver.find_element(By.XPATH, '//table')
            df = pd.read_html(a.get_attribute('outerHTML'))[0]


            # to take print of Index Value
            driver.execute_script('window.print();')
            time.sleep(5)


            path = os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No " + str(EXCELORDERNO)
            time.sleep(3)
            name = "Name Index"
            pyautogui.FAILSAFE = False
            pyautogui.typewrite(path + '\\' + name + '.pdf')
            pyautogui.press('enter')
            time.sleep(1)

            #print("Done")

            a = driver.find_element(By.XPATH, '//table')
            df = pd.read_html(a.get_attribute('outerHTML'))[0]

            time.sleep(2)
            COunt = driver.find_element(By.XPATH, '//*[@id="result"]/div[1]/div/span').text
            #print(str(COunt))
            COunt = int(COunt) + 1
            #print(COunt)

            workbook = openpyxl.load_workbook(
                os.getcwd()+'\\Input\\Cook_county.xlsx')
            worksheet = workbook.active
            #start_time = datetime.datetime.now()
            #worksheet['F' + str(int(i + 2))] = start_time
            k = 1 #for DOC counting Reference

            df.to_excel(
                os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No " + str(int(EXCELORDERNO)) + '\\Name Results.xlsx',
                index=False)
            workbook.save(os.getcwd() + '\\Input\\Cook_county.xlsx')
            ####################Test 5-23-2023###################################
            j = 1
            link = [] #all
            while j < int(COunt):
                href_ad = driver.find_element(By.XPATH,
                                              '//*[@id="tblData"]/tbody/tr[' + str(j) + ']/td[2]/a').get_attribute(
                    "href")
                # print(href_ad)
                link.append(href_ad)
                j += 1
                # print(j)

            N=1
            for k in link:

                driver.get(k)
                WebDriverWait(driver, 15).until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[2]/div/div[3]/div/div/fieldset/div[1]/div[2]/div/div/div/a')))
                d = driver.find_element(By.XPATH,
                                        '/html/body/div[2]/div/div[3]/div/div/fieldset/div[1]/div[1]/div[1]/table/tbody/tr[1]/td').text
                LinkF = driver.find_element(By.XPATH,
                                            '/html/body/div[2]/div/div[3]/div/div/fieldset/div[1]/div[2]/div/div/div/a').get_attribute(
                    'href')
                #print(LinkF)

                max_retry = 5
                retry_count = 0
                while retry_count < max_retry:
                    try:

                        r = requests.get(LinkF)
                        time.sleep(1)

                        with open('Output\\COOK_COUNTY\\' + "Order No " + str(int(EXCELORDERNO))
                                        + '\\Doc' + str(N) + '   ' + str(d) + '.pdf', 'wb') as fd:
                            for chunk in r.iter_content(chunk_size=40):
                                fd.write(chunk)

                        break

                    except Exception as e:
                        retry_count += 1

                N += 1

            '''
            while k < int(COunt):
               
                try:
                    #print("A1")
                    if bool(driver.find_element(By.XPATH,
                                                '//*[@id="tblData"]/tbody/tr['+str(k)+']/td[2]/a')) == True:
                        #print("A2")

                        hr=driver.find_element(By.XPATH,
                                                 '/html/body/div[2]/div/div[3]/div/form[2]/div[4]/div[4]/table/tbody/tr[' + str(
                                                    k) + ']/td[2]/a').get_attribute("href")
                        #driver.find_element(By.XPATH,'//*[@id="tblData"]/tbody/tr['+str(k)+']/td[2]/a').click()
                        #print("A3")
                        driver.get(hr)
                        time.sleep(2)
                        #WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[3]/div/div/fieldset/div[1]/div[1]/div[1]/table/tbody/tr[1]/td')))
                        d = driver.find_element(By.XPATH,
                                                '/html/body/div[2]/div/div[3]/div/div/fieldset/div[1]/div[1]/div[1]/table/tbody/tr[1]/td').text

                        A = driver.find_element(By.XPATH,
                                                '/html/body/div[2]/div/div[3]/div/div/fieldset/div[1]/div[2]/div/div/div/a').get_attribute(
                            'href')
                        pdf_url = A
                        url = A
                        
                        max_retry = 3
                        retry_count = 0
                        while retry_count < max_retry:
                            try:
                                r = requests.get(url)  # verify=False
                                with open(
                                        'Output\\COOK_COUNTY\\' + "Order No " + str(int(EXCELORDERNO))
                                        + '\\Doc' + str(k) + '   ' + str(d) + '.pdf', 'wb') as fd:
                                    for chunk in r.iter_content(chunk_size=2000):
                                        fd.write(chunk)
                                retry_count += 1
                                break

                            except Exception as e:
                                retry_count += 1
                        time.sleep(6)
                        #driver.back()

                       
                except Exception as Err:
                    # print(Err)
                    k = k + 1
                    #print("A")
                    driver.back()
                    '''


            ###############
            driver.get('https://crs.cookcountyclerkil.gov/Search')

            driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/form/div[2]/div[2]/div[3]/div/div[2]/input').clear()
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/form/div[2]/div[2]/div[3]/div/div[2]/input').send_keys(
                EXCELAPN, Keys.ENTER)
            time.sleep(3)
            aa = driver.find_element(By.XPATH, '//table')
            df1 = pd.read_html(aa.get_attribute('outerHTML'))[0]
            df1.to_excel(
                os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No " + str(int(EXCELORDERNO)) + '\\APN Results.xlsx',
                index=False)

            df2 = pd.read_excel(os.getcwd()+'\\Output\\COOK_COUNTY\\' + "Order No " + str(int(EXCELORDERNO))+'\\Name Results.xlsx')
            lastdate=(df2['Doc Recorded'].iloc[-1])



            data_frame = pd.read_excel(os.getcwd()+'\\Output\\COOK_COUNTY\\' + "Order No " + str(int(EXCELORDERNO))+'\\APN Results.xlsx')

            data_frame['Doc Recorded'] = pd.to_datetime(data_frame['Doc Recorded'], format='%m/%d/%Y')

            filterd_data = data_frame[data_frame['Doc Recorded'] >= lastdate]

            filterd_data.to_excel(
                os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No " + str(int(EXCELORDERNO))+"\\filterd_data.xlsx",
                index=False)

            df2 = pd.read_excel(os.getcwd()+'\\Output\\COOK_COUNTY\\' + "Order No " + str(int(EXCELORDERNO))+'\\Name Results.xlsx')
            df3 = pd.read_excel(os.getcwd()+'\\Output\\COOK_COUNTY\\' + "Order No " + str(int(EXCELORDERNO))+'\\filterd_data.xlsx')

            col1 = df2['Doc Number']
            col2 = df3['Doc Number']

            # print(lastdate)
            list = []
            mask = ~col1.isin(col2)
            non_matching_values = col1[~mask]
            non_comapred_values = col2[~col2.isin(col1)]
            #print(df2['Doc Number'].iloc[-1])
            lastdate = (df2['Doc Recorded'].iloc[-1])
            #print(non_comapred_values)
            L=[]
            for x in non_comapred_values:
                L.append(x)



            ####new####
            Total_files_No = driver.find_element(By.XPATH,
                                                 '/html/body/div[2]/div/div[3]/div/form[2]/div[4]/div[1]/div/span').text
            driver.execute_script('window.print();')
            time.sleep(4)
            #print(Total_files_No)
            path = os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No " + str(EXCELORDERNO)
            name = "ParcelNumber_index"
            time.sleep(1)
            pyautogui.typewrite(path + '\\' + name + '.pdf')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            #print(L)

            M = 1
            for M in range(int(Total_files_No)):

                try:

                    if int(M) <= int(Total_files_No):

                        # print(i)
                        DateAPN = driver.find_element(By.XPATH,
                                                      '/html/body/div[2]/div/div[3]/div/form[2]/div[4]/div[4]/table/tbody/tr[' + str(
                                                        M) + ']/td[5]/span').text
                        #print(DateAPN)
                        DOCNO=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/form[2]/div[4]/div[4]/table/tbody/tr['+str(M)+']/td[3]/span/span').text
                        #print(DOCNO)

                        if int(DOCNO) in L:
                             #print("DOC Exist")
                             qq = driver.find_element(By.XPATH,
                                                     '/html/body/div[2]/div/div[3]/div/form[2]/div[4]/div[4]/table/tbody/tr[' + str(
                                                         M) + ']/td[3]/span/span').text
                             #print("DOC Exist2")
                             qqq=driver.find_element(By.XPATH,
                                                      '/html/body/div[2]/div/div[3]/div/form[2]/div[4]/div[4]/table/tbody/tr['+str(M)+']/td[2]/a').get_attribute('href')

                             driver.get(qqq)

                             F = driver.find_element(By.XPATH,
                                                    '/html/body/div[2]/div/div[3]/div/div/fieldset/div[1]/div[2]/div/div/div/a').get_attribute(
                                'href')
                             pdf_url = F
                             url=F
                             '''
                             try:
                                url = F
                                respnse = requests.get(url)
                                with open(
                                        os.getcwd()+'\\Output\\COOK_COUNTY\\' + "Order No " + str(int(EXCELORDERNO))
                                        + '\\APN Doc' +" "+ str(qq) + " " + '.pdf', 'wb') as f:
                                    f.write(respnse.content)

                             except Exception:
                                 print("Retrying")

                             else:
                                url = F
                                respnse = requests.get(url)
                                with open(
                                        os.getcwd()+'\\Output\\COOK_COUNTY\\' + "Order No " + str(int(EXCELORDERNO))
                                        + '\\APN Doc' +" "+ str(qq) + " " + '.pdf', 'wb') as f:
                                    f.write(respnse.content)
                             '''
                             max_retry = 5
                             retry_count = 0
                             while retry_count < max_retry:
                                 try:
                                     r = requests.get(url)
                                     time.sleep(2)# verify=False
                                     with open(
                                             os.getcwd() + '\\Output\\COOK_COUNTY\\' + "Order No " + str(
                                                 int(EXCELORDERNO))
                                             + '\\APN Doc' + " " + str(qq) + " " + '.pdf', 'wb') as f:
                                         for chunk in r.iter_content(chunk_size=40):
                                             f.write(chunk)

                                         retry_count += 1
                                         break


                                 except Exception as e:
                                     retry_count += 1

                             driver.back()

                        M += 1

                except Exception as Err:
                    M += 1
                    #driver.back()
            print("APN SITE COMPLETED")

            #############################################Second Name###################


            workbook = openpyxl.load_workbook('Input\Cook_county.xlsx')
            sheet = workbook.active

            cell_value = sheet['I'+str(i+2)].value
            #print(cell_value)

            if cell_value is  None:
                print("Second name not Exist")


            else:

                driver.get('https://crs.cookcountyclerkil.gov/Search')
                time.sleep(5)

                # driver.find_element(By.XPATH,
                # '/html/body/div[2]/div/div[3]/div/div/form/div[2]/div[2]/div[3]/div/div[2]/input').clear()
                driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/div[3]/div/div/form/div[2]/div[2]/div[3]/div/div[2]/input').send_keys(
                    cell_value, Keys.ENTER)

                z = driver.find_element(By.XPATH, '//*[@id="result"]/div[1]/div/span[1]').text
                z = (z.replace(",", ""))
                total = int(z)  # (int(z) // int(100) - 1)
                df1 = pd.DataFrame()
                #print(total)

                Cnumber=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/form[2]/div[4]/div[1]/div/span[1]').text
                #print(Cnumber)


                if total >= int(100):
                    qq = driver.find_element(By.XPATH, '//*[@id="Paging"]/div/ul/li[2]/a').get_attribute("href")
                    qq = qq[:len(qq)-1]
                    #print(qq)
                    time.sleep(2)
                    a = driver.find_element(By.XPATH, '//table')
                    df = pd.read_html(a.get_attribute('outerHTML'))[0]
                    df1 = df1._append(df)
                    time.sleep(3)
                    r = requests.get(qq)
                    time.sleep(3)
                    soup = BeautifulSoup(r.text, 'lxml')

                    df1 = pd.DataFrame()
                    j = 1

                    CC = int(total) / 100
                    roundoff = round(CC)
                    #print(roundoff)

                    while int(j) <= int(roundoff):
                        Np = soup.find("a", rel='next').get("href")
                        cnp = "https://crs.cookcountyclerkil.gov" + Np
                        url = cnp
                        # r = requests.get(url,verify=False)
                        time.sleep(1) ############################################################################################
                        #updated = url[:-1]
                        updated = url.rstrip('0123456789')
                        #print(j)
                        updated = updated + str(j)
                        #print(updated)

                        max_retry = 2
                        retry_count = 0
                        while retry_count < max_retry:
                            try:
                                r = requests.get(updated)  # verify=False
                                # print(r.content)
                                #print(updated)
                                break
                                #retry_count += 1

                            except Exception as e:
                                retry_count += 1

                        soup = BeautifulSoup(r.content, 'html.parser')
                        table = soup.find('table')
                        df = pd.read_html(str(table))[0]
                        # print(df)
                        df1 = df1._append(df)
                        #print(df1)

                        j += 1
                        # print(j)

                    # df1.to_excel('D:\Title_Files\Output\COOK_COUNTY\Order No 1192237\c.xlsx', index=False)  # index=False
                    df1.to_excel(os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No " + str(
                        EXCELORDERNO) + '\\DataExtraction1.xlsx', index=False)

                    df = pd.read_excel(os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No " + str(
                        EXCELORDERNO) + '\\DataExtraction1.xlsx')

                    df['APN Number'] = df['1st PIN'].str.split(' ').str[0]
                    APN = str(EXCELAPN)  # '02-08-400-010-0000'
                    indices = df.loc[df['APN Number'] == APN].index.tolist()
                    a = []
                    # print indices of all matches one by one
                    for i in indices:
                        if i / 100 < 1:
                            print("Index: 1")
                        else:
                            #print("Index:", round(i / 100))
                            a.append(round(i / 100))

                    unique_numbers = []
                    [unique_numbers.append(num) for num in a if num not in unique_numbers]
                    print(unique_numbers)

                    l = 1
                    for k in unique_numbers:
                        driver.get(qq + str(k))
                        driver.execute_script('window.print();')
                        time.sleep(5)
                        pyautogui.press('enter')
                        path = os.getcwd()+'\\Output\\COOK_COUNTY\\' + "Order No " + str(
                            int(EXCELORDERNO)) + '\\secondName Search' + str(l) + '.pdf'
                        pyautogui.typewrite(path)

                        pyautogui.press('enter')
                        time.sleep(8)
                        l += 1

                else:
                    #print("Docs IS LESS Than 1OO")
                    driver.execute_script('window.print();')
                    time.sleep(5)
                    path = os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No " + str(int(EXCELORDERNO))
                    name = "Full_Name_search_Index2"
                    #pyautogui.FAILSAFE = False
                    pyautogui.typewrite(path + '\\' + name + '.pdf')
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(4)
                    #driver.close()

            #print("Second completd")

            ###################################################
            time.sleep(4)
            driver.get('https://crs.cookcountyclerkil.gov/Search')
            time.sleep(5)

            #driver.find_element(By.XPATH,
                                #'/html/body/div[2]/div/div[3]/div/div/form/div[2]/div[2]/div[3]/div/div[2]/input').clear()
            driver.find_element(By.XPATH,
                                '/html/body/div[2]/div/div[3]/div/div/form/div[2]/div[2]/div[3]/div/div[2]/input').send_keys(
                EXCELNAME, Keys.ENTER)


            z = driver.find_element(By.XPATH, '//*[@id="result"]/div[1]/div/span[1]').text
            z = (z.replace(",", ""))
            total = int(z)          #(int(z) // int(100) - 1)
            df1 = pd.DataFrame()
            #print(total)

            Cnumber1 = driver.find_element(By.XPATH,
                                          '/html/body/div[2]/div/div[3]/div/form[2]/div[4]/div[1]/div/span[1]').text
            #print(Cnumber1)


            if total >= int(100):

             qq = driver.find_element(By.XPATH, '//*[@id="Paging"]/div/ul/li[2]/a').get_attribute("href")
             qq = qq[:len(qq) - 1]
             #print(qq)
             time.sleep(2)
             a = driver.find_element(By.XPATH, '//table')
             df = pd.read_html(a.get_attribute('outerHTML'))[0]
             #print(df)
             df1 = df1._append(df)
             #df1= df1.append(df)

             r = requests.get(qq)
             time.sleep(2)
             soup = BeautifulSoup(r.text, 'lxml')

             df1 = pd.DataFrame()
             j = 1

             CC = int(total) / 100
             roundoff1 = round(CC)
             #print(roundoff1)

             while int(j) < int(roundoff1):
                Np = soup.find("a", rel='next').get("href")
                cnp = "https://crs.cookcountyclerkil.gov" + Np
                url = cnp
                # r = requests.get(url,verify=False)
                time.sleep(1)
                #updated = url[:-1]
                updated=url.rstrip('0123456789')
                #print(j)
                updated = updated + str(j)
                #updated = url.rstrip('0123456789')
                #print(updated)


                max_retry = 3
                retry_count = 0
                while retry_count < max_retry:
                    try:
                        r = requests.get(updated)  # verify=False
                        # print(r.content)
                        #print(updated)
                        retry_count += 1
                        break

                    except Exception as e:
                        retry_count += 1

                soup = BeautifulSoup(r.content, 'html.parser')
                table = soup.find('table')
                time.sleep(3)
                df = pd.read_html(str(table))[0]
                time.sleep(1)
                #print(df)
                df1 = df1._append(df)
                #print(df1)

                j += 1
                # print(j)


             #df1.to_excel('D:\Title_Files\Output\COOK_COUNTY\Order No 1192237\c.xlsx', index=False)  # index=False
             df1.to_excel(os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No " + str(EXCELORDERNO)+'\\DataExtraction.xlsx',index=False)

             df = pd.read_excel(os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No " + str(EXCELORDERNO)+'\\DataExtraction.xlsx',engine='openpyxl')


             df['APN Number'] = df['1st PIN'].str.split(' ').str[0]
             APN = str(EXCELAPN)#'02-08-400-010-0000'
             indices = df.loc[df['APN Number'] == APN].index.tolist()


             a = []
             # print indices of all matches one by one
             for w in indices:
                if w / 100 < 1:
                    print("Index: 1")
                else:
                    print("Index:", round(w / 100))
                    a.append(round(w / 100))


             unique_numbers = []
             [unique_numbers.append(num) for num in a if num not in unique_numbers]
             #print(unique_numbers)

             l = 1
             for k in unique_numbers:
                driver.get(qq + str(k))
                driver.execute_script('window.print();')
                time.sleep(5)
                pyautogui.press('enter')
                path = os.getcwd()+'\\Output\\COOK_COUNTY\\'+"Order No "+ str(int(EXCELORDERNO))+'\\Name Search' + str(l) + '.pdf'
                pyautogui.typewrite(path)

                pyautogui.press('enter')
                time.sleep(8)
                l += 1

            else:
                #print("Docs IS LESS Than 1OO")
                driver.execute_script('window.print();')
                time.sleep(5)
                path = os.getcwd()+"\\Output\\COOK_COUNTY\\" + "Order No " + str(int(EXCELORDERNO))
                name = "Full_Name_search_Index"
                pyautogui.FAILSAFE = False
                pyautogui.typewrite(path + '\\' + name + '.pdf')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(6)
                driver.close()



    #except Exception:
        #print(" The Recorder site server is down.")





    #print("Completed")
    time.sleep(2)


if __name__ == '__main__':
    Final_A()
