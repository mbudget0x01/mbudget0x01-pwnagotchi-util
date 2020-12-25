import json
import os

from .FileProgress import *
from ..session.file_system import getProgressFilePath

class ProgressTracker:

    PROCESSED_FILES = []
    __instance = None

    @staticmethod 
    def getInstance():
        if ProgressTracker.__instance == None:
            ProgressTracker(getProgressFilePath())
        return ProgressTracker.__instance

    def __init__(self,progress_file_path):

        if ProgressTracker.__instance != None:
         raise Exception("This class is a singleton!")
        else:
         ProgressTracker.__instance = self
        
        
        if self.PROCESSED_FILES == []:
            self.progress_file_path = progress_file_path
            self.loadProgress(progress_file_path)

    
    def loadProgress(self, path):
        if not os.path.exists(path):
            return

        data = None
        with open(path) as f:
            data = json.load(f)

        if data == None:
            return

        for entry in data:
            progress = entry['FileProgress']
            name = progress['name']
            modificationDate = progress['modificationDate']
            password = progress['password']

            if password == 'None':
                self.AddFailedFile(name, modificationDate)
            else:
                self.AddSuccesfullFile(name, modificationDate, password)

    def saveProgress(self):
        with open(self.progress_file_path, "w") as write_file:
            f = json.dumps([o.dump() for o in self.PROCESSED_FILES])
            write_file.write(f)


    def AddSuccesfullFile(self, name, modificationDate, password):
        f = FileProgress(name, True, modificationDate)
        f.setPassword(password)
        self.AddFile(f)

    def AddFailedFile(self, name, modificationDate):
        f = FileProgress(name, False, modificationDate)
        self.AddFile(f)

    def AddFile(self, file):

        f = self.FileExists(file)
        if f is not None:
            self.PROCESSED_FILES.remove(f)
        self.PROCESSED_FILES.append(file)
        self.saveProgress()

    def FileExists(self, file):
        if self.PROCESSED_FILES == []:
            return

        for fp in self.PROCESSED_FILES:
            if fp.name  == file.name:
                if fp.success == False and file.success == True:
                    return fp
                elif fp.modificationDate >= file.modificationDate:
                    return fp
            
            return None