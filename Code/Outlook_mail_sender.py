import win32com.client as win32
import glob
import os
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'sachin.j@coforge.com'
mail.Subject = 'Demo Automation'
mail.Body = 'Please find the attachment'
#mail.HTMLBody = '<h2>Please find the attachment</h2>'#this field is option #this field is optional

mail.HTMLBody = 'Hi,<br><br>    Please find the Attachment.<br><br>Regards<br><br>Sachin.j'


# To attach a file to the email (optional):

folder_path='D:\\Title_Files\\Order Sheets\\New folder'
pdf_path=glob.glob(os.path.join(folder_path,"*.pdf"))
for path in pdf_path:
    print(path)


#attachment  = "D:\\Title_Files\\Order Sheets\\New folder\\.zip"
    mail.Attachments.Add(path)

mail.Send()