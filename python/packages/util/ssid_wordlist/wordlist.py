import json
import os
from ...session.file_system import getSSIDWordlistFilePath, getWordlistPath
from .static_values import FILE_WORDLIST_EXPORT

class wordlist:

    wordlist = {}
    wordlist_location =""
    __instance = None

    def __init__(self, wordlist_location):
        wordlist.wordlist_location = wordlist_location
        if wordlist.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            wordlist.__instance = self
            self.load_wordlist()

    @staticmethod 
    def getInstance():
        if wordlist.__instance == None:
            wordlist(getSSIDWordlistFilePath())
        return wordlist.__instance


    def load_wordlist(self):
        if not os.path.exists(wordlist.wordlist_location):
            return

        data = None

        with open(wordlist.wordlist_location) as f:
            data = json.load(f)

        if data == None:
            return
        
        wordlist.wordlist = data

    def save_wordlist(self):
        with open(wordlist.wordlist_location, "w") as write_file:
            f = json.dumps(wordlist.wordlist)
            write_file.write(f)


    def change_ssid_skip(self,ssid,skip):
        wordlist.wordlist[ssid.strip()] = skip

    def add_ssid(self,ssid,skip=False):
        if ssid in wordlist.wordlist:
            return
        wordlist.wordlist[ssid.strip()] = skip
    
    def export_wordlist_for_hashcat(self):
        if wordlist.wordlist == {}:
            return ""
        
        outfile = os.path.join(getWordlistPath(), FILE_WORDLIST_EXPORT)
        with open(outfile, "w") as write_file:

            for key in wordlist.wordlist:
                if wordlist.wordlist[key] == False:
                    write_file.write(key + "\n")
        return outfile
