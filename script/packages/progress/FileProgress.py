class FileProgress:

    def __init__(self, name, success, modificationDate):
        self.success = success
        self.name = name
        self.modificationDate = modificationDate
        self.password = None
    
    def setPassword(self, password):
        self.password = password

    def getName(self):
        return self.name

    def getSuccess(self):
        return self.success
        
    def dump(self):
        return {"FileProgress": {'success': self.success,
                               'name': self.name,
                               'modificationDate': self.modificationDate,
                               'password': self.password}}