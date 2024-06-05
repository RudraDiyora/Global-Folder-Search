import os
import json
from os.path import isfile, join
from os import walk
import sys

def searchFile(filePath, phrase):

    with open(f"{filePath}", "r", encoding="utf8", errors='ignore') as file:
       # contents = file.read()
        contentLines = file.readlines()

       # print(contentLines)
        for count, line in enumerate(contentLines):
            
            fileDirPath = os.path.abspath(filePath).removeprefix(os.path.dirname(__file__))
            if phrase in line:
                print(f"'{phrase}' found in '{fileDirPath}' line: {count+1}")
                pass

def conductLogicOnFile(parrentPath, phrase, debug):
    for file in os.listdir(parrentPath):
        if file.endswith(".DS_Store") or file.endswith(".import"):
            continue
        fileName = os.path.abspath(file).replace(str(os.getcwd()), '')
        file = parrentPath + fileName
        if debug:
            print(f"{file}    {os.path.isfile(file)}")
        # checks if the path is a folder
        if os.path.isdir(file):
            if debug:
                print(f"{file} is a folder")
            conductLogicOnFile(file, phrase, debug)
        elif os.path.isfile(file):
            searchFile(file, phrase)

def search(phrase, debug = False):
    currentPath = __file__
    parrentPath = os.path.dirname(__file__)

    #parrentPath = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
   # print(parrentPath)
    conductLogicOnFile(parrentPath, phrase, debug)

# input serached prhase here
PHRASE = "ABC"
search(str(PHRASE))