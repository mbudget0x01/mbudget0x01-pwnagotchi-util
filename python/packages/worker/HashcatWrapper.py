import packages.util.hashcat.HashcatUtil as hashcat
import packages.util.shell.ShellInteractions as shell
import packages.log.log as log
import packages.progress.progress as progress
import os

def execute(command):
    log.log_debug(command)
    return shell.executeShellCommandWithCallback(command)
    
def track_progress(exit_code, file, out_file = None):
    name = os.path.basename(file)
    progress.trackProgressByExitcode(name, exit_code,outfile=out_file)
    log.log_info("Hashcat ended with status: " + str(exit_code))

#WPA Attacks
def attack_wpa_bruteforce(infile,mask, outfile = None):
    builder = hashcat.bruteforce_Attack(infile, mask, outfile)
    builder = hashcat.set_wpa_Hash(builder)
    command = hashcat.build(builder)
    exit_code = execute(command)
    #TODO: static value
    track_progress(exit_code, infile, outfile)

def attack_wpa_wordlist(infile,wordlist,rulefile=None,outfile=None):
    builder = hashcat.dictionary_Attack(infile,wordlist,rulefile,outfile)
    builder = hashcat.set_wpa_Hash(builder)
    command = hashcat.build(builder)
    exit_code = execute(command)
    #TODO: static value
    track_progress(exit_code, infile, outfile)

#PMKID Attack
def attack_pmkid_bruteforce(infile,mask, outfile = None):
    builder = hashcat.bruteforce_Attack(infile, mask, outfile)
    builder = hashcat.set_pmkid_Hash(builder)
    command = hashcat.build(builder)
    exit_code = execute(command)
    #TODO: static value
    track_progress(exit_code, infile, outfile)

def attack_pmkid_wordlist(infile,wordlist,rulefile=None,outfile=None):
    builder = hashcat.dictionary_Attack(infile,wordlist,rulefile,outfile)
    builder = hashcat.set_pmkid_Hash(builder)
    command = hashcat.build(builder)
    exit_code = execute(command)
    #TODO: static value
    track_progress(exit_code, infile, outfile)