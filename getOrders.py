import os, json
from datetime import datetime
import pandas as pd
import requests
import http.client

#get orders from site
def getOrder(county,state):
    auth=(config_data['username'],config_data['passowrd'])
    url = "http://168.61.208.48:8092/api/AutoSearch/GetSearchPending?state="+state+"&county="+county
    response = requests.get(url, auth=auth)
    data=response.json()

    order_df = pd.DataFrame(data)

    columns = ['Order No', 'APN', 'Property Address','Zip','State', 'County Name','City', 'NAME','Product Name']

    order_df.columns=columns
    #adding column names
    order_df.insert(8, "Second Name", "", True)
    order_df.insert(9, 'Start_time', "", True)
    order_df.insert(10, "End_time", "", True)

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
    print("Orders ready for automation")

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
def updateStatus(orderID,botstats,comments):
    try:
        auth=(config_data['username'],config_data['password'])
        botStatusId=getBotstatusID(botstats) #get order status id
        params = {"OrderId": orderID, "BotStatusID": botStatusId, "BotStatus": botstats, "Comments": comments}
        url="http://168.61.208.48:8092/api/AutoSearch/PostOrderBotStatus"


        response = requests.post(url,params=params ,auth=auth)
        if response.status_code == 200 :
            print("Order Status Updated")
    except Exception as e:
        print("status could not be updated "+str(e))

def uploadDocument(orderID,botstats,comments,files):
    try:
        auth = (config_data['username'], config_data['password'])
        botStatusId = getBotstatusID(botstats)  # get order status id
        params={"OrderId":orderID,"BotstatusID":botStatusId,"Botstatus":botstats,"DocumentTypeID":31,"comments":comments}


        url="http://168.61.208.48:8092/api/AutoSearch/UploadSearchDocuments"
        response = requests.post(url, params=params,auth=auth,files=files)
        if response.status_code == 200 :
            print("Document Uploaded")
    except Exception as e:
        print("Document could not be uploaded"+str(e))

with open('config.json', 'r') as f:
    config_data = json.load(f)

county=config_data['county']
state=config_data['state']

#getOrder(county,state)
uploadDocument(1166519,"In Progress","testing")



