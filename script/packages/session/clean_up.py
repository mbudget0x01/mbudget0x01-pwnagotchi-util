import os
from .file_system import getInputPath, getSessionIntermedPath
from .static_values import FILE_PLACEHOLDER

def clean_up_intermediates():
    intermed_path = getSessionIntermedPath()
    for file in os.listdir(intermed_path):
        abs_file = os.path.join(intermed_path,file)
        os.remove(abs_file)

def clean_up_input():
    input_path = getInputPath()
    for file in os.listdir(input_path):
        if file == FILE_PLACEHOLDER:
            continue
        abs_file = os.path.join(input_path,file)
        os.remove(abs_file)