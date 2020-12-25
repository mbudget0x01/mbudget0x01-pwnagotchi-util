import os
import time
from datetime import datetime
from .ProgressTracker import ProgressTracker
from .FileProgress import FileProgress

def trackProgressByExitcode(name, exitCode, password = "Na"):
    lastEdit = time.time()
    pt = ProgressTracker.getInstance()
    if exitCode == 0:
        pt.AddSuccesfullFile(name,lastEdit,password)
    else:
        pt.AddFailedFile(name, lastEdit)
    pt.saveProgress()

def attack_is_recommended(name, file_path):
    pt = ProgressTracker.getInstance()
    progress = pt.getFileProgress(name)
    if progress is None:
        return True
    if progress.success == True:
        return False
    if progress.timestamp < time.time(os.path.getmtime(file_path)):
        return False
    return True
