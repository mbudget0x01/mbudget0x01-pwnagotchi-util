import StaticValues
import os
import Helpers

class HashcatCommandBuilder():

    def __init__(self):
        self.ruleFile = ""
        self.hashType = ""
        self.inputFile = ""
        self.outputFile = ""
        self.outputFileFormat = ""
        self.wordlist = ""

    def setHashType(self, type):
        self.hashType = type

    def setRuleFile(self, file):
        self.ruleFile = file
    
    def setInputFile(self, file):
        self.inputFile = file
    
    def setOutputFile(self, file):
        self.outputFile = file
    
    def setOutputFileFormat(self, format):
        self.outputFileFormat = format

    def setWordlist(self, file):
        self.wordlist = file
    
    def build(self):
        #get Hashcat Binary
        command = StaticValues.UTIL_PATH_HASHCAT
        
        #check hash type
        if str(self.hashType) == "":
            command = command + " " + StaticValues.UTIL_MODIFIERS_HASHCAT_MODE
        else:
             command = command + " -m " + self.hashType

        #check rule
        if not str(self.ruleFile) == "":
            command = command + " -r " + self.ruleFile
        
        #check inputfile
        if not str(self.inputFile) == "":
            command = command + " " + self.inputFile
        
        #wordlist
        if str(self.wordlist) == "":
            wl = os.path.join(Helpers.getWordlistPath(), StaticValues.STANDARD_WORDLIST)
            command = command + " " + wl
        else:
            command = command + " " + self.wordlist

        #check outfile
        if not str(self.outputFile) == "":
            command = command + " --outfile=" + self.outputFile
            command = command + " --outfile-format="
            if str(self.outputFileFormat) == "":
                command = command + StaticValues.UTIL_MODIFIERS_HASHCAT_FILE_FORMAT
            else:
                command = command + self.outputFileFormat
        
        return command