from enum import Enum, unique

@unique
class request_types(Enum):
    FILE_LIST = "REQ_FILE_LIST"
    COORDINATOR_AVIABLE =  "REQ_COORDINATER_AVIABLE"
    FILE = "REQ_FILE"
    DATA_SEGMENT = "DATA_SEGMENT"
