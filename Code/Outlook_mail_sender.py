def Final_C():
    import win32com.client as win32
    import glob
    import os
    import shutil

    a = shutil.make_archive('D:\\Title_Files\\Output\\Cook', 'zip', 'D:\\Title_Files\\Output\\COOK_COUNTY')

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'sachin.j@coforge.com'
    mail.Subject = 'Demo Automation'
    mail.Body = 'Please find the attachment'
    #mail.HTMLBody = '<h2>Please find the attachment</h2>'#this field is option #this field is optional

    mail.HTMLBody = 'Hi,<br><br>    Please find the Attachment.<br><br>Regards<br><br>Sachin.j'


# To attach a file to the email (optional):

    folder_path='D:\Title_Files\Output'
    zip_path=glob.glob(os.path.join(folder_path,"*.zip"))
    for path in zip_path:
     print(path)


#attachment  = "D:\\Title_Files\\Order Sheets\\New folder\\.zip"
     mail.Attachments.Add(path)

    mail.Send()

if __name__=='__main__':
    Final_C()
'''


a=shutil.make_archive('D:\\Title_Files\\Output\\Cook', 'zip', 'D:\\Title_Files\\Output\\COOK_COUNTY')

if os.path.exists('E:/Zipped file.zip'):
   print(a)
else:
   print("ZIP file not created")
'''