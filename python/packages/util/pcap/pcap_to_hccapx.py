import os
from .util import change_file_extension
from .static_values import UTIL_EXTENSION_HCCAPX, UTIL_EXTENSION_PCAP, UTIL_PATH_CAP2HCCAPX

def build_pcap_to_hccapx_command(infile, outfolder):
    outfile = os.path.basename(infile)
    outfile = change_file_extension(UTIL_EXTENSION_PCAP,UTIL_EXTENSION_HCCAPX,outfile)
    outfile = os.path.join(outfolder,outfile)
    return UTIL_PATH_CAP2HCCAPX +" "+ infile + " " + outfile