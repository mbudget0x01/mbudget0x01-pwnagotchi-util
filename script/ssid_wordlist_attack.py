import os
import packages.session as session
import packages.util.ssid_wordlist as ssid_wl
import packages.util.ssid_wordlist.util as ssid_wl_util

from packages.session.file_system import getInputPath


def load_from_input():
    ssid_wl_util.add_ssids_from_input_folder(getInputPath())
    ssid_wl_util.export_wordlist_for_hashcat()

def get_exported_wordlist():
        wordlist = session.file_system.getWordlistPath()
        wordlist = os.path.join(wordlist,ssid_wl.FILE_WORDLIST_EXPORT)
        return wordlist