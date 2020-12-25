from .StaticValues import UTIL_PATH_HASHCAT, UTIL_MODIFIERS_HASHCAT_WPA_HASH, UTIL_MODIFIERS_HASHCAT_FILE_FORMAT
import os

class HashcatCommandBuilder():

    def __init__(self):
        self.ruleFile = ""
        self.hashType = ""
        self.inputFile = ""
        self.outputFile = ""
        self.outputFileFormat = ""
        self.wordlist = ""
        self.attackMode = ""
        self.workloadProfile = ""
        self.bruteForceMask = ""
    
    def setAttackMode(self, mode):
        self.attackMode = mode

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
    
    def setWorkloadProfile(self, profile):
        self.workloadProfile = profile

    def setBruteForceMask(self,mask):
        self.bruteForceMask = mask

    def build(self):
        #get Hashcat Binary
        command = UTIL_PATH_HASHCAT
        
        #check hash type
        if str(self.hashType) == "":
            command = command + " " + UTIL_MODIFIERS_HASHCAT_WPA_HASH
        else:
             command = command + " -m " + self.hashType

        #check attack mode
        if not str(self.attackMode) == "":
            command = command +" -a"+self.attackMode

        #check workload Profile
        if not str(self.workloadProfile) == "":
            command = command +" -w"+self.workloadProfile

        #check rule
        if not str(self.ruleFile) == "":
            command = command + " -r " + self.ruleFile
        
        #check inputfile
        if not str(self.inputFile) == "":
            command = command + " " + self.inputFile
        
        #wordlist
        if not str(self.wordlist) == "":
            command = command + " " + self.wordlist

        #check Brute Force Mask
        if not str(self.bruteForceMask) == "":
            command = command + " '" + self.bruteForceMask + "'"

        #check outfile
        if not str(self.outputFile) == "":
            command = command + " --outfile=" + self.outputFile
            command = command + " --outfile-format="
            if str(self.outputFileFormat) == "":
                command = command + UTIL_MODIFIERS_HASHCAT_FILE_FORMAT
            else:
                command = command + self.outputFileFormat
        
        return command