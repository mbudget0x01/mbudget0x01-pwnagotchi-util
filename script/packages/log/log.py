import logging
from .static_values import *

#Logging
def log_debug(message):
    log(logging.DEBUG, message)

def log_info(message):   
    log(logging.INFO, message)

def log_info_line():
    log_info("----------------------------")

def log_warning(message):   
    log(logging.WARNING, message)

def log_error(message):   
    log(logging.ERROR, message)

def log(level, message):
    #TODO: make correct
    print( "["+ LOG_TAG +"] " + message)
    logging.log(level, "["+ LOG_TAG +"] " + message)


def initalize_log(log_level=None, log_file=None):
    if log_file is None:
        log_file = LOG_FILE
        
    try:
        log_level = int(log_level)
    except Exception:
        log_level = None
    
    if log_level is None:
        logging.DEBUG

    logging.basicConfig(filename=log_file, level=log_level)