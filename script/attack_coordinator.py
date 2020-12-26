import packages.log.log as log
import packages.session as session
import packages.session.docker.util as docker_util
import HashcatWrapper as hashcat
import os
import packages.util.pcap.static_values as pcap_vals
import packages.progress.progress as progress
import ssid_wordlist_attack

progress_ignore_already_processed_files=False

attack_wpa_bruteforce = False
attack_wpa_dictionary = False
attack_wpa_ssid_dictionary = False


attack_pmkid_bruteforce = False
attack_pmkid_dictionary = False
attack_pmkid_ssid_dictionary = False

prepared = False

def parse_attacks_enabled():
    global attack_wpa_bruteforce
    global attack_wpa_dictionary
    global attack_wpa_ssid_dictionary
    global attack_pmkid_bruteforce
    global attack_pmkid_dictionary
    global attack_pmkid_ssid_dictionary
    global progress_ignore_already_processed_files

    attack_wpa_bruteforce = docker_util.get_boolean_variable("attack_wpa_bruteforce")
    attack_wpa_dictionary = docker_util.get_boolean_variable("attack_wpa_wordlist")
    attack_pmkid_bruteforce = docker_util.get_boolean_variable("attack_pmkid_bruteforce")
    attack_pmkid_dictionary = docker_util.get_boolean_variable("attack_pmkid_wordlist")

    attack_wpa_ssid_dictionary = docker_util.get_boolean_variable("attack_wpa_ssid_wordlist")
    attack_pmkid_ssid_dictionary = docker_util.get_boolean_variable("attack_pmkid_ssid_wordlist")

    progress_ignore_already_processed_files = docker_util.get_boolean_variable("progress_ignore_already_processed_files")

def log_out_attacks_enabled():
    log.log_info("Attack modes parsed...")
    log.log_info("attack_wpa_bruteforce: " + str(attack_wpa_bruteforce))
    log.log_info("attack_wpa_dictionary: " + str(attack_wpa_dictionary))
    log.log_info("attack_wpa_ssid_dictionary: " + str(attack_wpa_ssid_dictionary))
    log.log_info("attack_pmkid_bruteforce: " + str(attack_pmkid_bruteforce))
    log.log_info("attack_pmkid_dictionary: " + str(attack_pmkid_dictionary))
    log.log_info("attack_pmkid_ssid_dictionary: " + str(attack_pmkid_ssid_dictionary))
    log.log_info("progress_ignore_already_processed_files: " + str(progress_ignore_already_processed_files))

def launch_pmkid_bruteforce_attack(input_folder,output_folder=None):
    for file in os.listdir(input_folder):
        if file.endswith(pcap_vals.UTIL_EXTENSION_PKMID):
            if progress_ignore_already_processed_files:
                if not progress.attack_is_recommended(file, os.path.join(input_folder,file)):
                    log.log_info("Skipping: " + str(file) + "...")
                    continue

            log.log_info("Attempting to crack: " + str(file) + " ...")
            infile = os.path.join(input_folder, file)
            outfile = None
            if output_folder is not None:
                outfile = infile.replace(pcap_vals.UTIL_EXTENSION_PKMID,".txt")
                outfile = os.path.join(output_folder,outfile)
            mask = docker_util.get_string_variable("attack_pmkid_bruteforce_mask")
            log.log_info("Using bruteforce: " + str(mask))
            hashcat.attack_pmkid_bruteforce(infile,mask,outfile)

def launch_wpa_bruteforce_attack(input_folder,output_folder=None):
    for file in os.listdir(input_folder):
        if file.endswith(pcap_vals.UTIL_EXTENSION_HCCAPX):
            if progress_ignore_already_processed_files:
                if not progress.attack_is_recommended(file, os.path.join(input_folder,file)):
                    log.log_info("Skipping: " + str(file) + "...")
                    continue
            log.log_info("Attempting to crack: " + str(file) + " ...")
            infile = os.path.join(input_folder, file)
            outfile = None
            if output_folder is not None:
                outfile = infile.replace(pcap_vals.UTIL_EXTENSION_HCCAPX,".txt")
                outfile = os.path.join(output_folder,outfile)
            mask = docker_util.get_string_variable("attack_wpa_bruteforce_mask")
            log.log_info("Using bruteforce: " + str(mask))
            hashcat.attack_pmkid_bruteforce(infile,mask,outfile)

def launch_pmkid_dictionary_attack(input_folder,output_folder=None):
    for file in os.listdir(input_folder):
        if file.endswith(pcap_vals.UTIL_EXTENSION_PKMID):
            if progress_ignore_already_processed_files:
                if not progress.attack_is_recommended(file, os.path.join(input_folder,file)):
                    log.log_info("Skipping: " + str(file) + "...")
                    continue
            log.log_info("Attempting to crack: " + str(file) + " ...")
            infile = os.path.join(input_folder, file)
            outfile = None
            if output_folder is not None:
                outfile = infile.replace(pcap_vals.UTIL_EXTENSION_PKMID,".txt")
                outfile = os.path.join(output_folder,outfile)
            wordlist = docker_util.get_string_variable("attack_pmkid_wordlist_file_path")
            log.log_info("Using wordlist: " + str(wordlist))
            rulefile = None
            if docker_util.get_boolean_variable("attack_pmkid_wordlist_use_rule_file"):
                rulefile = docker_util.get_string_variable("attack_pmkid_wordlist_rule_file_path")
                log.log_info("Using rule: " + str(rulefile))
            hashcat.attack_pmkid_wordlist(infile,wordlist,rulefile,outfile)

def launch_wpa_dictionary_attack(input_folder,output_folder=None):
    for file in os.listdir(input_folder):
        if file.endswith(pcap_vals.UTIL_EXTENSION_HCCAPX):
            if progress_ignore_already_processed_files:
                if not progress.attack_is_recommended(file, os.path.join(input_folder,file)):
                    log.log_info("Skipping: " + str(file) + "...")
                    continue
            log.log_info("Attempting to crack: " + str(file) + " ...")
            infile = os.path.join(input_folder, file)
            outfile = None
            if output_folder is not None:
                outfile = infile.replace(pcap_vals.UTIL_EXTENSION_HCCAPX,".txt")
                outfile = os.path.join(output_folder,outfile)
            wordlist = docker_util.get_string_variable("attack_wpa_wordlist_file_path")
            log.log_info("Using wordlist: " + str(wordlist))
            rulefile = None
            if docker_util.get_boolean_variable("attack_wpa_wordlist_use_rule_file"):
                rulefile = docker_util.get_string_variable("attack_wpa_wordlist_rule_file_path")
                log.log_info("Using rule: " + str(rulefile))
            hashcat.attack_wpa_wordlist(infile,wordlist,rulefile,outfile)

def attack(input_folder,output_folder=None):

    global prepared
    
    if prepared == False:
        prepare()

    log.log_info("Starting attack run")
    log.log_info_line()
    
    if attack_pmkid_dictionary:
        launch_pmkid_dictionary_attack(input_folder,output_folder)
    
    if attack_wpa_dictionary:
        launch_wpa_dictionary_attack(input_folder,output_folder)

    if attack_pmkid_bruteforce:
        launch_pmkid_bruteforce_attack(input_folder,output_folder)
    
    if attack_wpa_bruteforce:
        launch_wpa_bruteforce_attack(input_folder,output_folder)
    
    if attack_wpa_ssid_dictionary or attack_wpa_ssid_dictionary:
        log.log_info("Generating ssid wordlist...")
        ssid_wordlist_attack.update_wordlist()

    if attack_pmkid_ssid_dictionary:
        ssid_wordlist_attack.launch_pmkid_attack(input_folder,output_folder,progress_ignore_already_processed_files)
    
    if attack_wpa_ssid_dictionary:
        ssid_wordlist_attack.launch_wpa_attack(input_folder,output_folder,progress_ignore_already_processed_files)
    
    log.log_info("Attack run ended")
    log.log_info_line()

def prepare():
    global prepared
    parse_attacks_enabled()
    log_out_attacks_enabled()
    prepared = True