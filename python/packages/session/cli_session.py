import packages.session.docker as docker
import packages.log as log
import logging
import os

Coordinator_LOG_TAG = "CLI"

def _initialize_log():
    #log.log_file = docker.util.get_string_variable("general_log_location")
    #log.log_level = docker.util.get_string_variable("general_log_level")
    #log.log.initalize_log(Coordinator_LOG_TAG, log.log_level, log.log_file)
    log.log.initalize_log(Coordinator_LOG_TAG, logging.DEBUG, log.static_values.LOG_FILE)

def initialize_session():

    #docker.DockerHandling.initializeEnvVariables()
    _initialize_log()
    log.log.log_info("Session initialized")