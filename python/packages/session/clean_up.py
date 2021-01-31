import os
import shutil
from .file_system import getInputPath, getSessionIntermedPath, getSessionFolderPath, getDataPath
from .static_values import FILE_PLACEHOLDER
from ..progress import ProgressTracker as ProgressTracker
import uuid

def clean_up_intermediates():
    intermed_path = getSessionIntermedPath()
    for file in os.listdir(intermed_path):
        abs_file = os.path.join(intermed_path,file)
        os.remove(abs_file)

def clean_up_input(only_sucessfull=False):
    if only_sucessfull:
        _clean_up_input_only_successfull()
    else:
        _clean_up_input_all()
    

def _clean_up_input_all():
    input_path = getInputPath()
    for file in os.listdir(input_path):
        if file == FILE_PLACEHOLDER:
            continue
        abs_file = os.path.join(input_path,file)
        os.remove(abs_file)

def _clean_up_input_only_successfull():
    pt = ProgressTracker.ProgressTracker.getInstance()
    successfull = pt.getSucessfullFilesWithoutSuffix()
    input_path = getInputPath()
    for file in os.listdir(input_path):
        if file == FILE_PLACEHOLDER:
            continue
        if file.split(".")[0] in successfull:
            abs_file = os.path.join(input_path,file)
            os.remove(abs_file)

def clean_up_session():
    session_folder = getSessionFolderPath()
    shutil.rmtree(session_folder)

def purge_session_folders():
    data = getDataPath()
    purge = []
    for name in os.listdir(data):
        abs_name = os.path.join(data, name)
        if os.path.isdir(abs_name):
            if _is_valid_uuid(name):
                purge.append(abs_name)

    for s in purge:
        shutil.rmtree(s)
    

def _is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False 
