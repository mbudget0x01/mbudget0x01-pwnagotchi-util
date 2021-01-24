import os

import packages.util.pcap.static_values as pcap
import packages.util.pcap.pcap_to_pmkid as pcap_to_pmkid
import packages.util.pcap.pcap_to_hccapx as pcap_to_hccapx
import packages.util.shell.ShellInteractions as shell
import packages.log.log as log

# pcap_to_hccapx
def convert_single_pcap_to_hccapx(infile, outfolder):
    command = pcap_to_hccapx.build_pcap_to_hccapx_command(infile,outfolder)
    log.log_debug("Attempting to convert "+ infile + " to hccapx")
    pipe = shell.executeShellCommand(command)
    return pipe

def convert_multiple_pcap_to_hccapx(infolder, outfolder):
    files = get_pcap_files_in_folder(infolder)
    
    for file in files:
        convert_single_pcap_to_hccapx(file, outfolder)

# pcap_to_pmkid
def convert_single_pcap_to_pmkid(infile, outfolder):
    command = pcap_to_pmkid.build_pcap_to_pmkid_command(infile,outfolder)
    log.log_debug("Attempting to convert "+ infile + " to pmkid")
    pipe = shell.executeShellCommand(command)
    return pipe

def convert_multiple_pcap_to_pmkid(infolder, outfolder):
    files = get_pcap_files_in_folder(infolder)
    
    for file in files:
        convert_single_pcap_to_pmkid(file, outfolder)

# util function
def get_pcap_files_in_folder(infolder):
    files = []

    for file in os.listdir(infolder):
        if file.endswith(pcap.UTIL_EXTENSION_PCAP):
            f = os.path.join(infolder, file)
            files.append(f)

    
    return files