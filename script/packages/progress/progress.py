import os
import time
from datetime import datetime
from .ProgressTracker import ProgressTracker
from .FileProgress import FileProgress

def trackProgressByExitcode(name, exitCode, password = "Na", outfile=None):
    lastEdit = time.time()
    pt = ProgressTracker.getInstance()
    if exitCode == 0:
        if outfile is not None:
            password = _get_password(outfile)
        if password == "Na":
            # in case of file corruption or dry run
            pt.AddFailedFile(name, lastEdit)
        else:
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
    if progress.modificationDate < os.path.getmtime(file_path):
        return False
    return True

def _get_password(outfile):
    if os.path.exists(outfile):
        with open(outfile) as f:
            pw = f.readline()
            pw = pw.strip()
            return pw
    return "Na"