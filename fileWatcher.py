import json
import os, shutil

import getOrders
from Code import Cookcounty_Tax as cook
import time

watchDirectory = os.getcwd()+'\\Input'
pollTime = 5 #in seconds

from os import listdir
from os.path import isfile, join

#function to return files in a directory
def fileInDirectory(my_dir: str):
    onlyfiles = [f for f in listdir(my_dir) if isfile(join(my_dir, f))]
    return(onlyfiles)


# function comparing two lists

def listComparison(OriginalList: list, NewList: list):
    differencesList = [x for x in NewList if
                       x not in OriginalList]  # Note if files get deleted, this will not highlight them
    return (differencesList)


def triggerBot(newFiles: list):

    print(f'Pending orders {newFiles}')
    for file in newFiles:
        print("starting automation for file ", file)
        cook.Final_UI(file)
        shutil.move(os.getcwd() + '\\Input\\' + file, os.getcwd() + '\\Processed\\' + file)
        time.sleep(2)





def fileWatcher(my_dir: str, pollTime: int):


    county = getOrders.config_data['county']
    state = getOrders.config_data['state']

    while True:
        if 'watching' not in locals():  # Check if this is the first time the function has run
            previousFileList = fileInDirectory(watchDirectory)
            watching = 1
        print("waiting for orders")
        time.sleep(pollTime)

        getOrders.getOrder(county,state)

        newFileList = fileInDirectory(watchDirectory)

        fileDiff = listComparison(previousFileList, newFileList)

        previousFileList = newFileList
        if len(fileDiff) == 0: continue
        triggerBot(fileDiff)



fileWatcher(watchDirectory, pollTime)
#fileInDirectory(watchDirectory)
