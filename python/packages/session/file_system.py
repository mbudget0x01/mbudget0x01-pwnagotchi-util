import os

import packages.session.static_values as static_values


root_path=""
#Path Functions
def getRootPath():
    global root_path
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
    return os.path.join(path, static_values.FOLDER_DATA)

def getSessionFolderPath():
    return os.path.join(getDataPath(),static_values.SESSION_UUID)

def getInputPath():
    return os.path.join(getDataPath(),static_values.FOLDER_INPUT)

def getBacklogPath():
    return os.path.join(getDataPath(),static_values.FOLDER_BACKLOG)

def getSessionErrorPath():
    return os.path.join(getSessionFolderPath(),static_values.FOLDER_ERROR)

def getOutputPath():
    return os.path.join(getDataPath(),static_values.FOLDER_OUTPUT)

def getSessionIntermedPath():
    return os.path.join(getSessionFolderPath(), static_values.FOLDER_INTERMEDIATES)

def getWordlistPath():
    path = getRootPath()
    return os.path.join(path, static_values.FOLDER_WORDLISTS)

def getRulesPath():
    path = getRootPath()
    return os.path.join(path, static_values.FOLDER_RULES)

def getProgressFilePath():
    path = getDataPath()
    return os.path.join(path, static_values.FILE_PROGRESS)

def getSSIDWordlistFilePath():
    path = getDataPath()
    return os.path.join(path, static_values.FILE_SSID_WORDLIST)