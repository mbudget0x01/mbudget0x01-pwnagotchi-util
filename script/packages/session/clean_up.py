import os
from .file_system import getInputPath, getSessionIntermedPath
from .static_values import FILE_PLACEHOLDER
from ..progress import ProgressTracker as ProgressTracker

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
