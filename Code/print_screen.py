'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options=Options()
options.add_argument(('--headless'))
options.add_argument('--disable-gpu')
options.add_argument('--print-to-pdf=output.pdf')


driver = webdriver.Chrome(options=Options())


driver.get('https://crs.cookcountyclerkil.gov/Search/Additional')
driver.implicitly_wait(10)
driver.execute_script("window.print();")
driver.quit()
'''

'''
import pdfkit


path_wkthmltopdf = "C:\\Folder\\where\\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf = path_wkthmltopdf)

pdfkit.from_url("http://google.com", "out.pdf", configuration=config)
'''
'''

import aspose.pdf as ap

input_pdf = DIR_INPUT + "https://docs.aspose.com/pdf/python-net/convert-html-to-pdf/#convert-html-to-pdf"
output_pdf = DIR_OUTPUT + "convert_html_to_pdf.pdf"
options = ap.HtmlLoadOptions()
document = ap.Document(input_pdf, options)
document.save(output_pdf)
'''

'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options=Options()
options.add_argument(('--headless'))
driver = webdriver.Chrome(options=Options())

driver.get('https://crs.cookcountyclerkil.gov/Search/Additional')
screen_shot=driver.get_screenshot_as_png()

with open ('D:\\Title_Files\\screenshot1.png','wb') as f:
    f.write(screen_shot)

'''



'''
from pyhtml2pdf import converter

i_f='https://crs.cookcountyclerkil.gov/Search/ResultAddt?id1=%23collapse2'
o_p='s.pdf'

with open(i_f,'r') as f:
    html=f.read()

pdf=converter.convert(html)
with open(o_p,'wb') as f:
    f.write(pdf)

'''
'''
from pyhtml2pdf import converter

converter.convert("https://crs.cookcountyclerkil.gov/Search/ResultAddt?id1=%23collapse2",'D:\\Title_Files\\s.pdf')


#####################################
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from PIL import Image
from io import BytesIO

options=Options()
options.add_argument("--start-maximizes")
options.add_argument("--headless")
driver=webdriver.Chrome(options=options)
driver.get("https://crs.cookcountyclerkil.gov/Search/ResultAddt?id1=%23collapse2")

height=driver.execute_script("return document.body.scrollHeight")

for i in range (6,height,200):
 driver.execute_script("window.scrollTo(0,{});",format(i))

screenshot=driver.find_element(By.XPATH,'/html').screenshot_as_png

image=Image.open(BytesIO(screenshot))
image.save("D:\\Title_Files\\a.png")

'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver = 'D:\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(chrome_driver)

driver.maximize_window()
driver.get('https://crs.cookcountyclerkil.gov/Search/ResultAddt?id1=%23collapse2')
driver.maximize_window()
height = driver.execute_script("return document.body.scrollHeight")
width = driver.execute_script("return document.body.scrollWidth")

driver.set_window_size(width,height)
screenshot=driver.find_element(By.TAG_NAME,'body').screenshot_as_png

with open ("D:\\Title_Files\\image.png",'wb') as f:
    f.write(screenshot)
