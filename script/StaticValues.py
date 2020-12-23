import uuid

FOLDER_INPUT = "input"
FOLDER_OUTPUT = "output"
FOLDER_ERROR = "error"
FOLDER_INTERMEDIATES = "intermediates"
FOLDER_DATA = "data"
FOLDER_WORDLISTS = "wordlists"
FOLDER_RULES = "rules"

FILE_PROGRESS = "progress.json"

## FOLDER STRUCTURE ##
#  ├─rules
#  ├─wordlists
#  └─data
#       ├─input
#       └─[Session-UUID]
#              ├─intermediates
#              ├─output
#              └─error
######################

#OS & Util related Stuff
UTIL_PATH_HCXPCAPTOOL = "/root/hcxtools/hcxpcaptool"
UTIL_PATH_CAP2HCCAPX = "/root/hashcat-utils/src/cap2hccapx.bin"
UTIL_PATH_HASHCAT="/root/hashcat/hashcat"

UTIL_FILE_NAME_INTERMED="intermed"

#Session Related Stuff
#SESSION_UUID = str(uuid.uuid4())
TAG = "Parse-Files"

#Standard Values
STANDARD_RULE = "best64.rule"
STANDARD_WORDLIST = "rockyou.txt"
UTIL_MODIFIERS_HASHCAT_MODE = "-m 2500"
UTIL_MODIFIERS_HASHCAT_FILE_FORMAT = "3"