import logging
from .static_values import *

#Logging
def log_debug(message):
    log(logging.DEBUG, message)

def log_info(message):   
    log(logging.INFO, message)

def log_warning(message):   
    log(logging.WARNING, message)

def log_error(message):   
    log(logging.ERROR, message)

def log(level, message):
    #TODO: make correct
    print( "["+ LOG_TAG +"] " + message)
    logging.log(level, "["+ LOG_TAG +"] " + message)


def initalize_log(log_level):
    logging.basicConfig(filename=LOG_FILE, level=log_level)