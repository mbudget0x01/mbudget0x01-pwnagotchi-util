import os
from .HashcatCommandBuilder import HashcatCommandBuilder
from .StaticValues import UTIL_MODIFIERS_HASHCAT_FILE_FORMAT, UTIL_MODIFIERS_HASHCAT_PMKID_HASH, UTIL_MODIFIERS_HASHCAT_WPA_HASH

def dictionary_Attack(infile,wordlist,rulefile=None,outfile=None):

    builder = HashcatCommandBuilder()
    builder.setInputFile(infile)        
    builder.setWordlist(wordlist)
    
    if outfile is not None:
        builder.setOutputFile(outfile)
        builder.setOutputFileFormat(UTIL_MODIFIERS_HASHCAT_FILE_FORMAT)
    
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
        builder.setOutputFileFormat(UTIL_MODIFIERS_HASHCAT_FILE_FORMAT)
    
    return builder

def set_output_file(outfile,builder,outfileformat=None):
    builder.setOutputFile(outfile)
    
    if outfileformat is None:
        builder.setOutputFileFormat(UTIL_MODIFIERS_HASHCAT_FILE_FORMAT)

def set_pmkid_Hash(builder):
    builder.setHashType(UTIL_MODIFIERS_HASHCAT_PMKID_HASH)
    return builder

def set_wpa_Hash(builder):
    builder.setHashType(UTIL_MODIFIERS_HASHCAT_WPA_HASH)
    return builder

def build(builder):
    return builder.build()