from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import webbrowser
from selenium.webdriver.support.ui import WebDriverWait


dataframe1 = pd.read_excel('D:\\Title_Files\\Input\\Hudson_county.xlsx')
data=dataframe1['Doc_No'][0]
print(data)


chrome_driver = 'D:\Title_Files\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver)

driver.maximize_window()
driver.get('https://crs.cookcountyclerkil.gov/Search/Additional')





input()