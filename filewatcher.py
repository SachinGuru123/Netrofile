import os, shutil
from Code import Cookcounty_Tax as cook
import getOrders as orders

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
    print(f'I would do things with file(s) {newFiles}')
    for file in newFiles:
        print("starting automation for file ", file)
        cook.Final_UI(file)
        shutil.move(os.getcwd() + '\\Input\\' + file, os.getcwd() + '\\Processed\\' + file)
        time.sleep(2)



import time


def fileWatcher(my_dir: str, pollTime: int):
    while True:
        if 'watching' not in locals():  # Check if this is the first time the function has run
            previousFileList = fileInDirectory(watchDirectory)
            watching = 1

        time.sleep(pollTime)

        newFileList = fileInDirectory(watchDirectory)

        fileDiff = listComparison(previousFileList, newFileList)

        previousFileList = newFileList
        if len(fileDiff) == 0: continue
        triggerBot(fileDiff)


fileWatcher(watchDirectory, pollTime)
#fileInDirectory(watchDirectory)
