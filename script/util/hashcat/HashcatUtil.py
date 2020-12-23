import os
from .HashcatCommandBuilder import HashcatCommandBuilder
import StaticValues
#from ..shell.ShellInteractions import executeShellCommandWithCallback




#TODO:Split up in bruteforce and dictionary Attack then split in pmkid and wpa

def dictionary_Attack(infile,wordlist,rulefile=None,outfile=None):

    builder = HashcatCommandBuilder()
    builder.setInputFile(infile)        
    builder.setWordlist(wordlist)
    
    if outfile is not None:
        builder.setOutputFile(outfile)
        builder.setOutputFileFormat("3")
    
    if rulefile is not None:
        builder.setRuleFile(rulefile)

    return builder

def bruteforce_Attack(infile,mask,outfile=None):
    
    builder = HashcatCommandBuilder()
    builder.setInputFile(infile)
    builder.setAttackMode("3")
    builder.setWorkloadProfile("3")
    builder.setBruteForceMask(mask)

    if outfile is not None:
        builder.setOutputFile(outfile)
        builder.setOutputFileFormat("3")
    
    return builder

def set_output_file(outfile,builder,outfileformat=None):
    builder.setOutputFile(outfile)
    
    if outfileformat is None:
        outfileformat = StaticValues.UTIL_MODIFIERS_HASHCAT_FILE_FORMAT
    builder.setOutputFileFormat("3")

def set_pmkid_Hash(builder):
    builder.setHashType("16800")
    return builder

def set_wpa_Hash(builder):
    builder.setHashType("2500")
    return builder

def build(builder):
    return builder.build()


    #Helpers.log_info(command)
 
    #pipe = executeShellCommand(command)
    #pipe = executeShellCommandWithCallback(command)
    #Helpers.trackProgressByExitcode(builder.outputFile.replace(".txt",".pcap"),pipe)
    #Helpers.log_info("Hashcat ended with status: " + str(pipe))

""" def WPA2dictionaryAttack(userulefile=False):
    files = []
    intermediatePath = Helpers.getSessionIntermedPath()  
    for file in os.listdir(intermediatePath):
        #Move To STATIC Values
        if file.endswith(".hccapx"):
            files.append(file)

    outpath = Helpers.getSessionOutputPath()
    #prepare wordlist
    wordlist = os.path.join(Helpers.getWordlistPath(), StaticValues.STANDARD_WORDLIST)
    if userulefile:
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
        #TODO implement cascadic at given time
        if userulefile:
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
        Helpers.log_info("Hashcat ended with status: " + str(pipe)) """
