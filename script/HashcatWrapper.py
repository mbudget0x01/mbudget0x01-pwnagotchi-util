import util.hashcat.HashcatUtil as hashcat
import util.shell.ShellInteractions as shell
import Helpers

def execute(command):
    Helpers.log_info(command)
    return shell.executeShellCommandWithCallback(command)

def log_progress(exit_code, file):
    Helpers.trackProgressByExitcode(file, exit_code)
    Helpers.log_info("Hashcat ended with status: " + str(exit_code))

#WPA Attacks
def attack_wpa_bruteforce(infile,mask, outfile = None):
    builder = hashcat.bruteforce_Attack(infile, mask, outfile)
    builder = hashcat.set_wpa_Hash(builder)
    command = hashcat.build(builder)
    exit_code = execute(command)
    #TODO: static value
    log_progress(exit_code, infile.replace(".hccapx",".pcap"))

def attack_wpa_wordlist(infile,wordlist,rulefile=None,outfile=None):
    builder = hashcat.dictionary_Attack(infile,wordlist,rulefile,outfile)
    builder = hashcat.set_wpa_Hash(builder)
    command = hashcat.build(builder)
    exit_code = execute(command)
    #TODO: static value
    log_progress(exit_code, infile.replace(".hccapx",".pcap"))

#PMKID Attack
def attack_pmkid_bruteforce(infile,mask, outfile = None):
    builder = hashcat.bruteforce_Attack(infile, mask, outfile)
    builder = hashcat.set_pmkid_Hash(builder)
    command = hashcat.build(builder)
    exit_code = execute(command)
    #TODO: static value
    log_progress(exit_code, infile.replace(".pmkid",".pcap"))

def attack_pmkid_wordlist(infile,wordlist,rulefile=None,outfile=None):
    builder = hashcat.dictionary_Attack(infile,wordlist,rulefile,outfile)
    builder = hashcat.set_pmkid_Hash(builder)
    command = hashcat.build(builder)
    exit_code = execute(command)
    #TODO: static value
    log_progress(exit_code, infile.replace(".pmkid",".pcap"))