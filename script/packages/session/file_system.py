import os

from .static_values import *


root_path=""
#Path Functions
def getRootPath():
    if root_path == "":
        file = os.path.dirname(os.path.realpath(__file__))
        #move value
        while os.path.basename(file) != "script":
            if file == os.path.dirname(file):
                raise Exception()
            file = os.path.dirname(file)
        
        return os.path.dirname(file)
    else:
        return root_path

def getDataPath():
    path = getRootPath()
    return os.path.join(path, FOLDER_DATA)

def getSessionFolderPath():
    return os.path.join(getDataPath(),SESSION_UUID)

def getInputPath():
    return os.path.join(getDataPath(),FOLDER_INPUT)

def getSessionErrorPath():
    return os.path.join(getSessionFolderPath(),FOLDER_ERROR)

def getSessionOutputPath():
    return os.path.join(getSessionFolderPath(),FOLDER_OUTPUT)

def getSessionIntermedPath():
    return os.path.join(getSessionFolderPath(), FOLDER_INTERMEDIATES)

def createSessionPaths():
    if not os.path.exists(getDataPath()):
        os.mkdir(getDataPath())

    if not os.path.exists(getInputPath()):
        os.mkdir(getInputPath())
    
    os.mkdir(getSessionFolderPath())    
    os.mkdir(getSessionOutputPath())
    os.mkdir(getSessionErrorPath())
    os.mkdir(getSessionIntermedPath())

def getWordlistPath():
    path = getRootPath()
    return os.path.join(path, FOLDER_WORDLISTS)

def getRulesPath():
    path = getRootPath()
    return os.path.join(path, FOLDER_RULES)

def getProgressFilePath():
    path = getDataPath()
    return os.path.join(path, FILE_PROGRESS)
