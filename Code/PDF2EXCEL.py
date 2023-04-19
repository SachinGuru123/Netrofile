import glob
import re
import PyPDF2
import pandas as pd
import subprocess
from openpyxl import Workbook
import os
import openpyxl

folder_path='D:\\Title_Files\\Order Sheets'
pdf_path=glob.glob(os.path.join(folder_path,"*.pdf"))

workbook = openpyxl.load_workbook('D:\\Title_Files\\Input\\Cook_county.xlsx')
worksheet = workbook.active

i=0
for path in pdf_path:
    #print(path)

  pdf_file=open(path,'rb')
  pdf_reader=PyPDF2.PdfReader(pdf_file)

  text=''
  #for i in range(len(pdf_reader.pages)):
  page=pdf_reader.pages[0]
  text =page.extract_text()

  #print(text)
  with open('D:\\Title_Files\\Order Sheets\\abc.txt','w') as f:
    #for line in text:
    f.write(text)


  with open('D:\\Title_Files\\Order Sheets\\abc.txt','r') as f:
    text_contents=f.read()

  rows=text_contents.split('\n')
  df=pd.DataFrame(rows)
  df.to_csv('D:\\Title_Files\\Order Sheets\\op.csv',index=False)




  df = pd.read_csv('D:\\Title_Files\\Order Sheets\\op.csv')

  order_numbers=[]
  County=[]
  Borrower=[]
  Address=[]
  APN=[]


  for index, row in df.iterrows():
        order_number_match=re.search(r'Order Number:\s*(\d{7}-\d+)',row["0"])
        order_number_county = re.search(r'County: \w+\s?\w+', row["0"])
        order_Borrower = re.search(r'(\w+?\s?\w+?\s?\w+\s*)(?= Borrower|BORROWER)', row["0"])
        order_Address=re.search(r'Address:\s*(.*)',row["0"])

        if re.search(r'PIN/APN:\s*(.*)', row["0"]):
         order_APN = re.search(r' PIN/APN:\s*(.*)', row["0"])
         if re.search(r'PIN/APN:\s*(.*)', row["0"]):
             APN.append(order_APN.group(1))
         APN_NUMBER = (APN[0].split(' ')[2])
         worksheet['B' + str(int(i + 2))] = APN_NUMBER

        if order_number_match:
         order_numbers.append(order_number_match.group(1))

        if order_number_county:
         County.append(order_number_county.group(0))

        if order_Borrower:
          Borrower.append(order_Borrower.group(0))

        if order_Address:
         Address.append(order_Address.group(0))


        #if re.search(r'PIN/APN:\s*(.*)', row["0"]):
         #APN.append(order_APN.group(1))


  ORDER_NUMBER=(order_numbers[0])
  COUNTY=(County[0].strip('County:'))#[2])#.strip('County:'))
  BORROWER_NAME=(Borrower[0])
  ADDRESS=(Address[0].strip('Address:'))

  #if re.search(r'PIN/APN:\s*(.*)', row["0"]):
  #APN_NUMBER=(APN[0].split(' ')[2])
  #print(APN_NUMBER)
  print("")


  worksheet['A' + str(int(i + 2))] = ORDER_NUMBER
  worksheet['E' + str(int(i + 2))] = COUNTY
  worksheet['C' + str(int(i + 2))] = BORROWER_NAME
  worksheet['D' + str(int(i + 2))] = ADDRESS
  #if re.search(r'PIN/APN:\s*(.*)', row["0"]):
  #worksheet['E' + str(int(i + 2))] = APN_NUMBER
  workbook.save('D:\\Title_Files\\Input\\Cook_county.xlsx')
  i=i+1



