import Helpers
import StaticValues
import os
import HashcatCommandBuilder

def WPA2dictionaryAttack():
    files = []
    intermediatePath = Helpers.getSessionIntermedPath()  
    for file in os.listdir(intermediatePath):
        #Move To STATIC Values
        if file.endswith(".hccapx"):
            files.append(file)

    outpath = Helpers.getSessionOutputPath()
    #prepare wordlist
    wordlist = os.path.join(Helpers.getWordlistPath(), StaticValues.STANDARD_WORDLIST)
    rule = os.path.join(Helpers.getRulesPath(), StaticValues.STANDARD_RULE)

    #build & execute hashcat command
    for file in files:
        #preparing files
        infile = os.path.join(intermediatePath, file)
        outfile = file.replace(StaticValues.UTIL_FILE_NAME_INTERMED+"_", '')
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
        Helpers.log_info(command)
 
        #pipe = executeShellCommand(command)
        pipe = Helpers.executeShellCommandWithCallback(command)
        Helpers.trackProgressByExitcode(outfile.replace(".txt",".pcap"),pipe)
        Helpers.log_info("Hashcat ended with status: " + str(pipe))

def PMKIDbruteForce():
    files = []
    intermediatePath = Helpers.getSessionIntermedPath()  
    for file in os.listdir(intermediatePath):
        #Move To STATIC Values
        if file.endswith(".pmkid"):
            files.append(file)

    outpath = Helpers.getSessionOutputPath()

    #build & execute hashcat command
    for file in files:
        #preparing files
        infile = os.path.join(intermediatePath, file)
        outfile = file.replace(StaticValues.UTIL_FILE_NAME_INTERMED+"_", '')
        outfile = outfile.replace(".pmkid",".txt")
        outfile = os.path.join(outpath,outfile)
        
        #building hashcat_command
        builder = HashcatCommandBuilder.HashcatCommandBuilder()
        builder.setInputFile(infile)
        builder.setOutputFile(outfile)
        builder.setOutputFileFormat("3")
        builder.setAttackMode("3")
        builder.setWorkloadProfile("3")
        builder.setHashType("16800")
        builder.setBruteForceMask("?d?d?d?d?d?d?d?d")

        command = builder.build()
        Helpers.log_info(command)
 
        #pipe = executeShellCommand(command)
        pipe = Helpers.executeShellCommandWithCallback(command)
        Helpers.trackProgressByExitcode(outfile.replace(".txt",".pcap"),pipe)
        Helpers.log_info("Hashcat ended with status: " + str(pipe))