import Helpers
import StaticValues
import os
import HashcatCommandBuilder

def dictionaryAttack():
    files = []
    intermediatePath = Helpers.getSessionIntermedPath()  
    for file in os.listdir(intermediatePath):
        files.append(file)

    outpath = Helpers.getSessionOutputPath()
    #prepare wordlist
    wordlist = os.path.join(Helpers.getWordlistPath(), StaticValues.STANDARD_WORDLIST)
    rule = os.path.join(Helpers.getRulesPath(), StaticValues.STANDARD_RULE)

    #build & execute hashcat command
    for file in files:
        #preparing files
        infile = os.path.join(intermediatePath, file)
        outfile = file.replace(StaticValues.UTIL_FILE_NAME_CAP2HCCAPX_INTERMED+"_", '')
        outfile = outfile.replace(".hccapx",".txt")
        outfile = os.path.join(outpath,outfile)
        
        #building hashcat_command
        builder = HashcatCommandBuilder.HashcatCommandBuilder()
        builder.setInputFile(infile)
        builder.setOutputFile(outfile)
        builder.setOutputFileFormat("3")
        builder.setWordlist(wordlist)
        builder.setRuleFile(rule)

        command = builder.build()
        print(command)
 
        #pipe = executeShellCommand(command)
        pipe = Helpers.executeShellCommandWithCallback(command)
        Helpers.log_info("Hashcat ended with status: " + str(pipe))