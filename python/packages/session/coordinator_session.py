import packages.session.docker as docker
import packages.log as log
import logging
import os
import packages.session.file_system as file_system

Coordinator_LOG_TAG = "Coordinator"

def _initialize_log():
    #log.log_file = docker.util.get_string_variable("general_log_location")
    #log.log_level = docker.util.get_string_variable("general_log_level")
    #log.log.initalize_log(Coordinator_LOG_TAG, log.log_level, log.log_file)
    log.log.initalize_log(Coordinator_LOG_TAG, logging.DEBUG, log.static_values.LOG_FILE)

def initialize_session():

    #docker.DockerHandling.initializeEnvVariables()
    _initialize_log()
    if not os.path.exists(file_system.getDataPath()):
        os.mkdir(file_system.getDataPath())

    if not os.path.exists(file_system.getInputPath()):
        os.mkdir(file_system.getInputPath())

    if not os.path.exists(file_system.getBacklogPath()):
        os.mkdir(file_system.getBacklogPath())
    log.log.log_info("Session initialized")