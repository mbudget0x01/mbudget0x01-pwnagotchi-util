import packages.log.log as log
import packages.session as session
import packages.session.docker.util as docker_util
import packages.worker.HashcatWrapper as hashcat
import os
import packages.util.pcap.static_values as pcap_vals
import packages.progress.progress as progress
import packages.worker.ssid_wordlist_attack as ssid_wordlist_attack

progress_ignore_already_processed_files=False

attack_wpa_bruteforce = False
attack_wpa_dictionary = False
attack_wpa_ssid_dictionary = False


attack_pmkid_bruteforce = False
attack_pmkid_dictionary = False
attack_pmkid_ssid_dictionary = False

prepared = False

def _parse_attacks_enabled():
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

def _log_out_attacks_enabled():
    log.log_info("Attack modes parsed...")
    log.log_info("attack_wpa_bruteforce: " + str(attack_wpa_bruteforce))
    log.log_info("attack_wpa_dictionary: " + str(attack_wpa_dictionary))
    log.log_info("attack_wpa_ssid_dictionary: " + str(attack_wpa_ssid_dictionary))
    log.log_info("attack_pmkid_bruteforce: " + str(attack_pmkid_bruteforce))
    log.log_info("attack_pmkid_dictionary: " + str(attack_pmkid_dictionary))
    log.log_info("attack_pmkid_ssid_dictionary: " + str(attack_pmkid_ssid_dictionary))
    log.log_info("progress_ignore_already_processed_files: " + str(progress_ignore_already_processed_files))

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
    
    if attack_pmkid_ssid_dictionary or attack_wpa_ssid_dictionary:
        log.log_info("Generating ssid wordlist...")
        ssid_wordlist_attack.load_from_input()

    if attack_pmkid_ssid_dictionary:
        #ssid_wordlist_attack.launch_pmkid_attack(input_folder,output_folder,progress_ignore_already_processed_files)
        launch_pmkid_ssid_attack(input_folder,output_folder)

    if attack_wpa_ssid_dictionary:
        #ssid_wordlist_attack.launch_wpa_attack(input_folder,output_folder,progress_ignore_already_processed_files)
        launch_wpa_ssid_attack(input_folder,output_folder)
    
    log.log_info_line()
    log.log_info("Attack run ended")
    

def prepare():
    global prepared
    _parse_attacks_enabled()
    _log_out_attacks_enabled()
    prepared = True

def _get_abs_files_in_folder(folder, file_extension):
    files = []
    for file in os.listdir(folder):
        if file.endswith(file_extension):
            files.append(os.path.join(folder, file))
    
    return files

def _skip_file(abs_file):
    if not progress_ignore_already_processed_files:
        return False

    name = os.path.basename(abs_file)
    return not progress.attack_is_recommended(name,abs_file)

def _get_outfile(infile, output_folder):
    if output_folder is None:
        return None
    outfile = os.path.basename(infile).split(".")[0]
    outfile += ".txt"
    return os.path.join(output_folder,outfile)

def _get_rule_file_from_docker(var_name):
    use = docker_util.get_string_variable(var_name)
    if use:
        return docker_util.get_string_variable(var_name.replace("use_","") + "_path")
    else:
        return None

def _get_string_var_from_docker(var_name):
    return docker_util.get_string_variable(var_name)

def _log_skipping_file(abs_file):
    f = os.path.basename(abs_file)
    log.log_info("Skipping: " + str(f) + "...")

def _log_dictionary_crack_attempt(abs_file, wordlist, rulefile=None):
    f = os.path.basename(abs_file)
    log.log_info("Attempting to crack: " + str(f) + " ...")
    log.log_info("Using wordlist: " + str(wordlist))
    if rulefile is None:
        return
    log.log_info("Using rule: " + str(rulefile))

def _log_bruteforce_crack_attempt(abs_file, mask):
    f = os.path.basename(abs_file)
    log.log_info("Attempting to crack: " + str(f) + " ...")
    log.log_info("Using mask: " + str(mask))



def launch_pmkid_dictionary_attack(input_folder,output_folder=None):
    #load wordlist and rulefile
    wordlist = _get_string_var_from_docker("attack_pmkid_wordlist_file_path")
    rules = _get_rule_file_from_docker("attack_pmkid_wordlist_use_rule_file")

    # get all files in folder
    files = _get_abs_files_in_folder(input_folder, pcap_vals.UTIL_EXTENSION_PKMID)
    for file in files:

        #check if file should be skipped
        if _skip_file(file):
            _log_skipping_file(file)
            continue
        
        #logging
        _log_dictionary_crack_attempt(file,wordlist,rules)

        #generate outfile
        outfile = _get_outfile(file,output_folder)

        #attack
        hashcat.attack_pmkid_wordlist(file,wordlist,rules,outfile)


def launch_wpa_dictionary_attack(input_folder,output_folder=None):
    #load wordlist and rulefile
    wordlist = _get_string_var_from_docker("attack_wpa_wordlist_file_path")
    rules = _get_rule_file_from_docker("attack_wpa_wordlist_use_rule_file")

    # get all files in folder
    files = _get_abs_files_in_folder(input_folder, pcap_vals.UTIL_EXTENSION_HCCAPX)
    for file in files:

        #check if file should be skipped
        if _skip_file(file):
            _log_skipping_file(file)
            continue
        
        #logging
        _log_dictionary_crack_attempt(file,wordlist,rules)

        #generate outfile
        outfile = _get_outfile(file,output_folder)

        #attack
        hashcat.attack_wpa_wordlist(file,wordlist,rules,outfile)

def launch_wpa_bruteforce_attack(input_folder,output_folder=None):
    #load mask
    mask = _get_string_var_from_docker("attack_wpa_bruteforce_mask")

    # get all files in folder
    files = _get_abs_files_in_folder(input_folder, pcap_vals.UTIL_EXTENSION_HCCAPX)
    for file in files:

        #check if file should be skipped
        if _skip_file(file):
            _log_skipping_file(file)
            continue
        
        #logging
        _log_bruteforce_crack_attempt(file,mask)

        #generate outfile
        outfile = _get_outfile(file,output_folder)

        #attack
        hashcat.attack_wpa_bruteforce(file,mask,outfile)
    
def launch_pmkid_bruteforce_attack(input_folder,output_folder=None):
    #load mask
    mask = _get_string_var_from_docker("attack_pmkid_bruteforce_mask")

    # get all files in folder
    files = _get_abs_files_in_folder(input_folder, pcap_vals.UTIL_EXTENSION_PKMID)
    for file in files:

        #check if file should be skipped
        if _skip_file(file):
            _log_skipping_file(file)
            continue
        
        #logging
        _log_bruteforce_crack_attempt(file,mask)

        #generate outfile
        outfile = _get_outfile(file,output_folder)

        #attack
        hashcat.attack_pmkid_bruteforce(file,mask,outfile)

def launch_pmkid_ssid_attack(input_folder,output_folder=None):
    #load wordlist and rulefile
    wordlist = ssid_wordlist_attack.get_exported_wordlist()
    rules = _get_rule_file_from_docker("attack_pmkid_ssid_wordlist_use_rule_file")

    # get all files in folder
    files = _get_abs_files_in_folder(input_folder, pcap_vals.UTIL_EXTENSION_PKMID)
    for file in files:

        #check if file should be skipped
        if _skip_file(file):
            _log_skipping_file(file)
            continue
        
        #logging
        _log_dictionary_crack_attempt(file,wordlist,rules)

        #generate outfile
        outfile = _get_outfile(file,output_folder)

        #attack
        hashcat.attack_pmkid_wordlist(file,wordlist,rules,outfile)

def launch_wpa_ssid_attack(input_folder,output_folder=None):
    #load wordlist and rulefile
    wordlist = ssid_wordlist_attack.get_exported_wordlist()
    rules = _get_rule_file_from_docker("attack_wpa_ssid_wordlist_use_rule_file")

    # get all files in folder
    files = _get_abs_files_in_folder(input_folder, pcap_vals.UTIL_EXTENSION_HCCAPX)
    for file in files:

        #check if file should be skipped
        if _skip_file(file):
            _log_skipping_file(file)
            continue
        
        #logging
        _log_dictionary_crack_attempt(file,wordlist,rules)

        #generate outfile
        outfile = _get_outfile(file,output_folder)

        #attack
        hashcat.attack_wpa_wordlist(file,wordlist,rules,outfile)