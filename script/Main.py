import os
import ConvertFile
import StaticValues
import Helpers
import HashcatWrapper
import logging

def main():
    ## initialize ##
    logging.basicConfig(filename='/var/log/mbudget0x01-pwnagotchi-util.log', encoding='utf-8', level=logging.DEBUG)
    Helpers.log_info("Main routine started")

    ## Actual Workload ##
    files = []

    ### Transforming the files ###
    Helpers.log_info("Started Session with UUID: " + StaticValues.SESSION_UUID)

    #Preparing Paths
    Helpers.createSessionPaths()
    inputpath = Helpers.getInputPath()

    ConvertFile.convertPcapToHccapx(inputpath)
    Helpers.log_info("Files to hccapx converted")
    ConvertFile.convertPcapToPMKID(inputpath)
    Helpers.log_info("Files to pmkid converted")


    ### Cracking the Files ###
    Helpers.log_info("Starting PKMID attack")
    HashcatWrapper.PMKIDbruteForce()
    Helpers.log_info("Starting WPA2 attack")
    HashcatWrapper.WPA2dictionaryAttack()
    

    #cleanup
    intermediatePath = Helpers.getSessionIntermedPath()
    Helpers.log_info("Starting cleanup")
    files.clear()
    for file in os.listdir(intermediatePath):
        files.append(file)

    for file in files:
        path = os.path.join(intermediatePath, file)
        os.remove(path)



if __name__ == "__main__":
    main()









                                                                                        


