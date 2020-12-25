import os
from .HashcatCommandBuilder import HashcatCommandBuilder
import StaticValues

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
        builder.setOutputFileFormat("3")

def set_pmkid_Hash(builder):
    builder.setHashType("16800")
    return builder

def set_wpa_Hash(builder):
    builder.setHashType("2500")
    return builder

def build(builder):
    return builder.build()