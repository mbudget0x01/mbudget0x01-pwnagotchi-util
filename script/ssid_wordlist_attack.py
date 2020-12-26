import os
import packages.log.log as log
import packages.session as session
import packages.session.docker.util as docker_util
import packages.util.ssid_wordlist as ssid_wl
import packages.util.ssid_wordlist.util as ssid_wl_util
import packages.util.pcap.static_values as pcap_vals
import packages.progress.progress as progress
import HashcatWrapper as hashcat

from packages.session.file_system import getInputPath


def update_wordlist():
    ssid_wl_util.add_ssids_from_input_folder(getInputPath())
    ssid_wl_util.export_wordlist_for_hashcat()

def launch_wpa_attack(input_folder,output_folder=None, ignore_already_processed_files=False):
    for file in os.listdir(input_folder):
        if file.endswith(pcap_vals.UTIL_EXTENSION_HCCAPX):
            if ignore_already_processed_files:
                if not progress.attack_is_recommended(file, os.path.join(input_folder,file)):
                    log.log_info("Skipping: " + str(file) + "...")
                    continue
            log.log_info("Attempting to crack: " + str(file) + " ...")
            infile = os.path.join(input_folder, file)
            outfile = None
            if output_folder is not None:
                outfile = infile.replace(pcap_vals.UTIL_EXTENSION_HCCAPX,".txt")
            wordlist = _get_exported_wordlist()
            log.log_info("Using wordlist: " + str(wordlist))
            rulefile = None
            if docker_util.get_boolean_variable("attack_wpa_ssid_wordlist_use_rule_file"):
                rulefile = docker_util.get_string_variable("attack_wpa_ssid_wordlist_rule_file_path")
                log.log_info("Using rule: " + str(rulefile))
            hashcat.attack_wpa_wordlist(infile,wordlist,rulefile,outfile)

def launch_pmkid_attack(input_folder,output_folder=None, ignore_already_processed_files=False):
    for file in os.listdir(input_folder):
        if file.endswith(pcap_vals.UTIL_EXTENSION_PKMID):
            if ignore_already_processed_files:
                if not progress.attack_is_recommended(file, os.path.join(input_folder,file)):
                    log.log_info("Skipping: " + str(file) + "...")
                    continue
            log.log_info("Attempting to crack: " + str(file) + " ...")
            infile = os.path.join(input_folder, file)
            outfile = None
            if output_folder is not None:
                outfile = infile.replace(pcap_vals.UTIL_EXTENSION_PKMID,".txt")
            wordlist = _get_exported_wordlist()
            log.log_info("Using wordlist: " + str(wordlist))
            rulefile = None
            if docker_util.get_boolean_variable("attack_pmkid_ssid_wordlist_use_rule_file"):
                rulefile = docker_util.get_string_variable("attack_pmkid_ssid_wordlist_rule_file_path")
                log.log_info("Using rule: " + str(rulefile))
            hashcat.attack_pmkid_wordlist(infile,wordlist,rulefile,outfile)

def _get_exported_wordlist():
        wordlist = session.file_system.getWordlistPath()
        wordlist = os.path.join(wordlist,ssid_wl.FILE_WORDLIST_EXPORT)
        return wordlist