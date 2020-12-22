import logging
import os
import StaticValues
import subprocess
import shlex
import ProgressTracker
from datetime import datetime

#Logging
def log_info(message):   
    log(logging.INFO, message)

def log_warning(message):   
    log(logging.WARNING, message)

def log_error(message):   
    log(logging.ERROR, message)

def log(level, message):
    #TODO: make correct
    print( "["+ StaticValues.TAG +"] " + message)
    logging.log(level, "["+ StaticValues.TAG +"] " + message)

#Helper Functions
def getRootPath():
    file = os.path.dirname(os.path.realpath(__file__))
    return os.path.dirname(file)

def getDataPath():
    path = getRootPath()
    return os.path.join(path, StaticValues.FOLDER_DATA)

def getSessionFolderPath():
    return os.path.join(getDataPath(),StaticValues.SESSION_UUID)

def getInputPath():
    return os.path.join(getDataPath(),StaticValues.FOLDER_INPUT)

def getSessionErrorPath():
    return os.path.join(getSessionFolderPath(),StaticValues.FOLDER_ERROR)

def getSessionOutputPath():
    return os.path.join(getSessionFolderPath(),StaticValues.FOLDER_OUTPUT)

def getSessionIntermedPath():
    return os.path.join(getSessionFolderPath(), StaticValues.FOLDER_INTERMEDIATES)

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
    return os.path.join(path, StaticValues.FOLDER_WORDLISTS)

def getRulesPath():
    path = getRootPath()
    return os.path.join(path, StaticValues.FOLDER_RULES)

def getProgressFilePath():
    path = getDataPath()
    return os.path.join(path, StaticValues.FILE_PROGRESS)

#parsing helpers
def fileIsHashCatUsable(file):
    size = os.path.getsize(file)
    if size > 10:
        return True
    else:
        return False

#Shell interaction
def executeShellCommand(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    p_status = p.wait()
    return p_status

def executeShellCommandWithCallback(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        #if output == '' and process.poll() is not None:
        if process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
    return rc

#progress tracking Helpers
def trackProgressByExitcode(name, exitCode, password = "Na"):
    lastEdit = int(datetime.now().timestamp())
    pt = ProgressTracker.ProgressTracker()
    if exitCode == 0:
        pt.AddSuccesfullFile(name,lastEdit,password)
    else:
        pt.AddFailedFile(name, lastEdit)
    pt.saveProgress()
    log_info("Progress saved at" + str(datetime.now().timestamp()))