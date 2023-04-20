import datetime
import sys
import threading
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


chrome_driver = 'D:\chromedriver_win32\chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument('--kiosk-printing')
chrome_options.add_argument('--disable-extensions')

driver = webdriver.Chrome(options=chrome_options)
##################################################

driver.get('https://crs.cookcountyclerkil.gov/Search/ResultByPin?id1=03043000281295')
driver.maximize_window()
b=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/form/div[3]/div[1]/div/span').text
print(b)
i=1
Mortgage=0
Deed=0
while i<int(b):
    a = driver.find_element(By.XPATH, '//table//tr['+str(int(i))+']//td[6]').text

    print(i)

    if Mortgage<1:
     if a =='MORTGAGE':
        c= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/form/div[3]/div[4]/table/tbody/tr['+str(i)+']/td[2]/a').get_attribute('href')
        print(c)

        Mortgage=Mortgage+1

     if Deed < 1:
         if a == 'MORTGAGE':
             c = driver.find_element(By.XPATH,
                                     '/html/body/div[2]/div/div[3]/div/form/div[3]/div[4]/table/tbody/tr[' + str(
                                         i) + ']/td[2]/a').get_attribute('href')
             print(c)
             Deed = Deed + 1


    i = i + 1