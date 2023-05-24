import pandas as pd
import openpyxl
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

df1=pd.read_excel('D:\\Title_Files\\Output\\COOK_COUNTY\\Order No 1189333\\filterd_data.xlsx')
f=df1[['Doc Number','Doc Type','Doc Executed','1st PIN']]
print(f)
df2=pd.read_excel('D:\\Title_Files\\Output\\COOK_COUNTY\\Order No 1189333\\searchNote.xlsx')

df_combined=df2._append(f)
combinedfile='D:\\Title_Files\\Output\\COOK_COUNTY\\Order No 1189333\\Dummy.xlsx'
df_combined.to_excel(combinedfile,index=False)


'''
df1=pd.read_excel('D:\\Title_Files\\Output\\COOK_COUNTY\\Order No 1192237\\Name Results.xlsx')
df2=pd.read_excel('D:\\Title_Files\\Output\\COOK_COUNTY\\Order No 1192237\\APN Results.xlsx')
df3=pd.read_excel('D:\\Title_Files\\Output\\COOK_COUNTY\\Order No 1192237\\searchNote.xlsx')

lastdate=(df1['Doc Recorded'].iloc[-1])
#print(lastdate)

data_frame = pd.read_excel('D:\\Title_Files\\Output\\COOK_COUNTY\\Order No 1192237\\APN Results.xlsx')

data_frame['Doc Recorded'] = pd.to_datetime(data_frame['Doc Recorded'], format='%m/%d/%Y')

filterd_data = data_frame[data_frame['Doc Recorded'] >= lastdate]



filterd_data.to_excel(
                "D:\\Title_Files\\Output\\COOK_COUNTY\\Order No 1192237\\Filterdemo.xlsx",
                index=False)

dd=pd.read_excel("D:\\Title_Files\\Output\\COOK_COUNTY\\Order No 1192237\\Filterdemo.xlsx")
fd=dd[['Doc Recorded','1st PIN']]
print(fd)

df4=pd.read_excel('D:\\Title_Files\\Output\\COOK_COUNTY\\Order No 1192237\\Filterdemo.xlsx')
combine_df=pd.concat([df3,df4],ignore_index=True)
combine_df.to_excel('D:\\Title_Files\\Output\\COOK_COUNTY\\Order No 1192237\\Combinedxl.xlsx',index=False)
'''