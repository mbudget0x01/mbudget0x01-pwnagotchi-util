import logging
import packages.log.static_values as static_values

Log_Tag = "None"
#Logging
def log_debug(message):
    log(logging.DEBUG, message)

def log_info(message):   
    log(logging.INFO, message)

def log_info_tag(tag:str, message:str):
    msg = "["+ tag +"] " + message   
    log(logging.INFO, msg)

def log_info_line():
    log_info("----------------------------")

def log_warning(message):   
    log(logging.WARNING, message)

def log_error(message):   
    log(logging.ERROR, message)

def log(level, message):
    #TODO: make correct
    print( "["+ Log_Tag +"] " + message)
    logging.log(level, "["+ Log_Tag +"] " + message)


def initalize_log(log_tag:str, log_level:int=None, log_file:str=None):
    global Log_Tag
    Log_Tag = log_tag
    
    if log_file is None:
        #Fallback
        log_file = static_values.LOG_FILE
        
    try:
        log_level = int(log_level)
    except Exception:
        log_level = None
    
    if log_level is None:
        logging.DEBUG

    logging.basicConfig(filename=log_file, level=log_level)