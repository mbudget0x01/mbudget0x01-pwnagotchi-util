from enum import Enum, unique

@unique
class workload_types(Enum):
    NORMAL = "Normal"
    PURGE_SESSIONS = "Purge_Sessions"
    DO_ALL_FILES = "Full_Backlog"