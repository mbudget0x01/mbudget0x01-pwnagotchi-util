from enum import Enum, unique

@unique
class request_types(Enum):
    #FILE TRANSFER REQUESTS
    FILE_LIST = "REQ_FILE_LIST"
    COORDINATOR_AVIABLE =  "REQ_COORDINATER_AVIABLE"
    FILE = "REQ_FILE"
    DATA_SEGMENT = "DATA_SEGMENT"
    #CLI REQUESTS
    UTIL_PURGE_SESSIONS = "REQ_PURGE_SESSIONS"
    UTIL_DO_FILE = "REQ_DO_FILE"
    UTIL_DO_ALL_FILES = "REQ_DO_ALL"
    UTIL_GET_FOUND_PASSWORDS = "REQ_PW_ALL"
    UTIL_GET_FOUND_PASSWORD_FILE = "REQ_PW_FILE"
