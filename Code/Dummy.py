import pandas as pd
import openpyxl
i=1
workbook=openpyxl.load_workbook('D:\Title_Files\Input\Cook_county.xlsx')
sheet=workbook.active
cell_value=sheet['I'+str(i+1)].value

if cell_value is not None:
    print(cell_value)

else:
    print("No element exist")

