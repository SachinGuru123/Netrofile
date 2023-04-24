def Final_B():
    import time
    import datetime
    from datetime import timedelta
    import win32com.client

    outlook = win32com.client.Dispatch("Outlook.Application")

    namespace=outlook.GetNamespace('MAPI')
    indbox=namespace.GetDefaultFolder('6')

    message=indbox.Items
    message.Sort("[ReceivedTime]",True)

    senders=[]
    for msg in message:

        outlook_date = msg.senton.date()
        todays_date = datetime.date.today()
    #yes=todays_date-timedelta(1)
    #print(yes)


    #if todays_date != outlook_date:
        #break
        if len(senders)==200:
            break
        sender_name=msg.SenderName
    #sender_name = msg.subject

    #if sender_name not in senders:
        senders.append(sender_name)
        sender_name1 = msg.subject
        print(sender_name,sender_name1)
        attachments = msg.Attachments


    # return the first item in attachments


        for i in range(attachments.Count):
            attachment = attachments.Item(i+1)
         #print(attachment)
        # the name of attachment file
            attachment_name = str(attachment).lower()
        #print(attachment_name)

            if sender_name== 'Sachin J':

             if attachment_name.endswith(".pdf"):

                time.sleep(1)
                attachment.SaveASFile('D:\\Title_Files\\Order Sheets\\' + attachment_name)
                time.sleep(1)
            #print(attachment_name)

             elif attachment_name.endswith(".xlsx"):
              time.sleep(1)
              attachment.SaveASFile('D:\\Title_Files\\Order Sheets\\' + attachment_name)
              time.sleep(1)
              #print(attachment_name)

if __name__=='__main__':
    Final_B()
