import os
from .util import change_file_extension
from .static_values import UTIL_EXTENSION_PKMID, UTIL_EXTENSION_PCAP, UTIL_PATH_HCXPCAPTOOL

def build_pcap_to_pmkid_command(infile, outfolder):
    outfile = os.path.basename(infile)
    outfile = change_file_extension(UTIL_EXTENSION_PCAP,UTIL_EXTENSION_PKMID,outfile)
    os.path.join(outfolder,outfile)
    return UTIL_PATH_HCXPCAPTOOL +" -z "+ outfile + " " + infile