import os
from datetime import datetime
import pandas as pd
import requests


username = "coforge"
password = "coforge123"

#get orders from site
def getOrder():
    url = "http://168.61.208.48:8092/api/AutoSearch/GetSearchPending"
    response = requests.get(url, auth=(username, password))
    data=response.json()
    order_df = pd.DataFrame(data)

    columns = ['Order No', 'APN', 'Property Address','Zip','State', 'County Name', 'NAME','Product Name']

    order_df.columns=columns
    #adding column names
    order_df.insert(7, "Second Name", "", True)
    order_df.insert(8, 'Start_time', "", True)
    order_df.insert(9, "End_time", "", True)

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

    order_df.to_excel(os.getcwd() + '\\Input\\OrderInput_' + str(datetime.now()) + '.xlsx', index=False)
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
        botStatusId=getBotstatusID(botstats) #get order status id

        url="http://168.61.208.48:8092/api/AutoSearch/PostOrderBotStatus?OrderId=451587&BotstatusID=1&Botstatus=Pending&Comments=Testing"
        params={"OrderId":orderID,"BotStatusID":botStatusId,"BotStatus":botstats,"Comments":comments}

        response = requests.post(url,params=params ,auth=(username, password))
        if response.status_code == 200 :
            print("Order Status Updated")
    except Exception as e:
        print("status could not be updated "+str(e))

getOrder()



