from datetime import datetime
from .ProgressTracker import ProgressTracker

def trackProgressByExitcode(name, exitCode, password = "Na"):
    lastEdit = int(datetime.now().timestamp())
    pt = ProgressTracker.getInstance()
    if exitCode == 0:
        pt.AddSuccesfullFile(name,lastEdit,password)
    else:
        pt.AddFailedFile(name, lastEdit)
    pt.saveProgress()