import os
import shutil
import Helpers
import StaticValues

def convertPcapToHccapx(inputpath):

    _files = []

    for file in os.listdir(inputpath):
        if file.endswith('.pcap'):
            _files.append(file)

    Helpers.log_info(str(len(_files)) +" Files found")

    hccapx_file = os.path.join(Helpers.getSessionIntermedPath(), StaticValues.UTIL_FILE_NAME_CAP2HCCAPX_INTERMED)
    for file in _files:
        infile = os.path.join(inputpath, file)
        outfile = hccapx_file + "_" + file.replace(".pcap",".hccapx") 
        resp = Helpers.executeShellCommand(StaticValues.UTIL_PATH_CAP2HCCAPX +" "+ infile + " " + outfile)

        if resp == 0:
        
            #move unusable files to error
            if os.path.exists(outfile):
                if not Helpers.fileIsHashCatUsable(outfile):
                    errorfile = os.path.join(Helpers.getSessionErrorPath(),file)
                    shutil.move(infile, errorfile)
                    os.remove(outfile)
                else:
                    os.remove(infile)
