def Final_A():

    print("HI")

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

    chrome_driver = 'D:\Title_Files\chromedriver_win32\chromedriver.exe'
    driver = webdriver.Chrome(chrome_driver)

    dataframe1 = pd.read_excel(
        'D:\\Title_Files\\Input\\Cook_county.xlsx')

    E = dataframe1[dataframe1.columns[0]].count()
    for i in range(E):

            EXCELAPN = dataframe1['APN'][i]

            EXCELNAME = dataframe1['NAME'][i]



            # chrome_driver = 'D:\chromedriver_win32\chromedriver.exe'

            # driver = webdriver.Chrome(chrome_driver)

            driver.maximize_window()
            driver.get('https://crs.cookcountyclerkil.gov/Search/Additional')
            driver.maximize_window()
            time.sleep(2)
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div[3]/div[2]/h2/button').click()
            time.sleep(3)
            # driver.find_element(By.XPATH, '//*[@id="RecordedFromDate"]').send_keys(StartDate)
            # driver.find_element(By.XPATH, '//*[@id="RecordedToDate"]').send_keys(EndDate)

            driver.find_element(By.XPATH,
                                '/html/body/div[2]/div/div[3]/div/div/div[3]/div[2]/div/div/form/div[1]/div/input').send_keys(
                EXCELNAME, Keys.ENTER)

            time.sleep(3)
            a = driver.find_element(By.XPATH, '//table')
            df = pd.read_html(a.get_attribute('outerHTML'))[0]
            #df.to_excel("C:\\Users\\sachin.j\\PycharmProjects\\pythonProject5\\venv\\Excel.xlsx", index=False)

            q = driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div/div[3]/div/form/div[5]/div[4]/table/tbody/tr[2]/td[11]/a').get_attribute(
                'href')

            # print(q.split("=",4))

            driver.get('https://crs.cookcountyclerkil.gov/Search/ResultByPin?id1=' + str(EXCELAPN))
            COunt = driver.find_element(By.XPATH, '//*[@id="result"]/div[1]/div/span').text
            print(str(COunt))
            COunt = int(COunt) + 1
            print(COunt)

            # start_time = datetime.datetime.now()
            # print(start_time)
            workbook = openpyxl.load_workbook(
                'D:\\Title_Files\\Input\\Cook_county.xlsx')
            worksheet = workbook.active
            start_time = datetime.datetime.now()
            worksheet['C' + str(int(i + 2))] = start_time
            k = 1
            os.makedirs("D:\\Title_Files\\Output\\COOK_COUNTY\\" + str(EXCELAPN))
            while k < int(COunt):
                try:
                    # if k < int(COunt):

                    if bool(driver.find_element(By.XPATH,
                                                '//*[@id="result"]/div[4]/table/tbody/tr[' + str(
                                                    k) + ']/td[2]/a')) == True:

                        Q = driver.find_element(By.XPATH,
                                                '/html/body/div[2]/div/div[3]/div/form/div[3]/div[4]/table/tbody/tr[' + str(
                                                    k) + ']/td[3]/span').text
                        print(Q)
                        # worksheet['G' + str(int(k + 1))]=Q
                        d = driver.find_element(By.XPATH,
                                                '/html/body/div[2]/div/div[3]/div/form/div[3]/div[4]/table/tbody/tr[' + str(
                                                    k) + ']/td[2]/a').get_attribute('href')
                        print(d)
                        driver.get(d)

                        A = driver.find_element(By.XPATH,
                                                '/html/body/div[2]/div/div[3]/div/div/fieldset/div[1]/div[2]/div/div/div/a').get_attribute(
                            'href')
                        pdf_url = A
                        #os.makedirs("D:\\Title_Files\\Output\\COOK_COUNTY\\"+str(EXCELAPN))
                        try:
                            url = A
                            r = requests.get(url, stream=True)
                            print(r.status_code)
                            with open(
                                    'D:\\Title_Files\\Output\\COOK_COUNTY\\' + str(
                                        int(EXCELAPN)) + '\\Doc' + str(k) + '   ' + str(Q) + '.pdf', 'wb') as fd:
                                for chunk in r.iter_content(chunk_size=10):
                                    fd.write(chunk)

                        finally:
                            url = A
                            r = requests.get(url, stream=True)
                            print(r.status_code)
                            with open(
                                    'D:\\Title_Files\\Output\\COOK_COUNTY\\' + str(
                                        int(EXCELAPN)) + '\\Doc' + str(k) + '   ' + str(Q) + '.pdf', 'wb') as fd:
                                time.sleep(1)
                                for chunk in r.iter_content(chunk_size=10):
                                    fd.write(chunk)

                        k = k + 1
                        print(k)
                        driver.back()

                except Exception as Err:
                    print(Err)
                    k = k + 1
                    driver.back()

    end_time = datetime.datetime.now()
    worksheet['D' + str(int(i + 2))] = end_time
    worksheet['E' + str(int(i + 2))] = "Completed"
    worksheet['G' + str(int(i + 2))] = str(int(COunt))
    workbook.save('D:\\Title_Files\\Input\\Cook_county.xlsx')
    source = 'D:\\Title_Files\\Input\\Cook_county.xlsx'
    destination = 'D:\\Title_Files\\Processed\\Cook_county.xlsx'
    shutil.move(source, destination)

    print("Completed")

    driver.close()



if __name__=='__main__':
    Final_A()
