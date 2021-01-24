from enum import Enum, unique

#A Mapping for Keywords and Boolean succes values
@unique
class request_results(Enum):
    ACK = "ACK"
    NACK = "NACK"