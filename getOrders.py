import os, json
from datetime import datetime
import pandas as pd
import requests

#get orders from site
def getOrder(county,state):
    try:

        auth=(config_data['username'],config_data['password'])
        url = "http://168.61.208.48:8092/api/AutoSearch/GetSearchPending?state="+state+"&county="+county
        response = requests.get(url, auth=auth)
        data=response.json()

        order_df = pd.DataFrame(data)
        #print(order_df)
        columns = ['Order ID','Order No', 'Property Address','Zip','State', 'County Name','City', 'NAME','Product Name','Process ID']

        order_df.columns=columns
        #adding column names
        order_df.insert(2,"APN","",True)
        order_df.insert(9, "Second Name", "", True)
        order_df.insert(10, 'Start_time', "", True)
        order_df.insert(11, "End_time", "", True)


        rows_count = len(order_df.index) #total number of rows

        name = order_df['NAME'].values   #values in NAME column
        secondName= order_df['Second Name'].values   #values in Second Name column

        #splitting name column (if more than 1 value) and storing in second name column
        for i in range(rows_count):
            if ';' in name[i]:
                secondName[i]=str(name[i]).split(';')[1]
                name[i] = str(name[i]).split(';')[0]
            elif "and" in name[i]:
                secondName[i] = str(name[i]).split("and")[1]
                name[i] = str(name[i]).split("and")[0]
            else:
                continue
            i=i+1

        now=datetime.now()
        filepath=os.getcwd() + '\\Input\\Order_' + str(now.strftime("%m-%d-%Y_%H-%M-%S"))
        order_df.to_excel(filepath+ '.xlsx', index=False)
        print("Orders fetched for automation")
    except Exception as e:
        print("Could not get orders from Smartprop ",e)

#get order status id
def getBotstatusID(botstats):
    if botstats == "Pending":
        return 1
    elif botstats == "In Progress":
        return 2
    elif botstats == "Completed":
        return 3
    elif botstats == "Exception":
        return 4
    else:
        return 0

#update order status in site
def updateStatus(orderID,OrderNum,botstats,processId,comments):
    try:
        auth=(config_data['username'],config_data['password'])
        botStatusId=getBotstatusID(botstats) #get order status id
        params = {"OrderId": orderID,"OrderNo": OrderNum,"BotStatusID": botStatusId, "BotStatus": botstats,"ProcessID":processId, "Comments": comments}
        url="http://168.61.208.48:8092/api/AutoSearch/PostOrderBotStatus"


        response = requests.post(url,params=params ,auth=auth)
        if response.status_code == 200 :
            print("Order Status Updated")
    except Exception as e:
        print("status could not be updated "+str(e))

def uploadDocument(orderID,OrderNum,botstats,processId,comments,files):
    try:
        auth = (config_data['username'], config_data['password'])
        botStatusId = getBotstatusID(botstats)  # get order status id
        params={"OrderId":orderID,"OrderNo": OrderNum,"BotstatusID":botStatusId,"Botstatus":botstats,"ProcessID":processId,"DocumentTypeID":31,"comments":comments}


        url="http://168.61.208.48:8092/api/AutoSearch/UploadSearchDocuments"
        response = requests.post(url, params=params,auth=auth,files=files)
        #print(response)
        if response.status_code == 200 :
            print("Document Uploaded")
    except Exception as e:
       print("Document could not be uploaded"+str(e))

with open('config.json', 'r') as f:
    config_data = json.load(f)

county=config_data['county']
state=config_data['state']
getOrder(county, state)


