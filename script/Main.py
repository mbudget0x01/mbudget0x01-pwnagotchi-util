import os
from ConvertFile import convertPcapToHccapx
import StaticValues
import Helpers
import HashcatWrapper

def main():
    ## Actual Workload ##
    files = []

    ### Transforming the files ###
    Helpers.log_info("Started Session with UUID: " + StaticValues.SESSION_UUID)

    #Preparing Paths
    Helpers.createSessionPaths()
    inputpath = Helpers.getInputPath()

    convertPcapToHccapx(inputpath)
    Helpers.log_info("Files to hccapx converted")


    ### Cracking the Files ###
    HashcatWrapper.dictionaryAttack()

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









                                                                                        


