import os
import packages.session.file_system as file_system
import packages.session.docker as docker
import packages.log as log

WORKER_LOG_TAG = "Worker"

def _createSessionPaths():
    if not os.path.exists(file_system.getDataPath()):
        os.mkdir(file_system.getDataPath())

    if not os.path.exists(file_system.getInputPath()):
        os.mkdir(file_system.getInputPath())
    
    if not os.path.exists(file_system.getOutputPath()):
        os.mkdir(file_system.getOutputPath())
    
    os.mkdir(file_system.getSessionFolderPath())    
    os.mkdir(file_system.getSessionErrorPath())
    os.mkdir(file_system.getSessionIntermedPath())

def _initialize_log():
    log.log_file = docker.util.get_string_variable("general_log_location")
    log.log_level = docker.util.get_string_variable("general_log_level")
    log.log.initalize_log(WORKER_LOG_TAG,log.log_level, log.log_file)
    

def initialize_session():
    docker.DockerHandling.initializeEnvVariables()
    _createSessionPaths()
    _initialize_log()
    log.log.log_info("Session initialized")