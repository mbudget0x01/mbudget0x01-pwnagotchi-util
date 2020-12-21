import Helpers
import json
import os

PROCESSED_FILES = []

class ProgressTracker:


    def __init__(self):
        
        if PROCESSED_FILES == []:
            self.loadProgress(Helpers.getProgressFilePath())

    
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

    def saveProgress(self, path):
        with open(Helpers.getProgressFilePath(), "w") as write_file:
            f = json.dumps([o.dump() for o in PROCESSED_FILES])
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
            PROCESSED_FILES.remove(f)
        PROCESSED_FILES.append(file)

    def FileExists(self, file):
        if PROCESSED_FILES == []:
            return

        for fp in PROCESSED_FILES:
            if fp.name  == file.name:
                if fp.success == False and file.success == True:
                    return fp
                elif fp.modificationDate >= file.modificationDate:
                    return fp
            
            return None

class FileProgress:

    def __init__(self, name, success, modificationDate):
        self.success = success
        self.name = name
        self.modificationDate = modificationDate
        self.password = None
    
    def setPassword(self, password):
        self.password = password

    def dump(self):
        return {"FileProgress": {'success': self.success,
                               'name': self.name,
                               'modificationDate': self.modificationDate,
                               'password': self.password}}