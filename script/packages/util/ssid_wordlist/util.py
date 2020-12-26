import os
from .wordlist import wordlist
from ..pcap.static_values import UTIL_EXTENSION_PCAP

def add_ssids_from_input_folder(input_folder):
    wl = wordlist.getInstance()
    for file in os.listdir(input_folder):
        if file.endswith(UTIL_EXTENSION_PCAP):
            s = file.replace(UTIL_EXTENSION_PCAP,"")
            s = s.split("_")
            if len(s) < 2:
                continue
            s.pop()
            s = s.pop()
            wl.add_ssid(s.strip())
    wl.save_wordlist()

def export_wordlist_for_hashcat():
    wl = wordlist.getInstance()
    wl.export_wordlist_for_hashcat()