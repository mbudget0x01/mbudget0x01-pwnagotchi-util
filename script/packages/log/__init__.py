from .log import initalize_log, log_info
import packages.session as session
import packages.session.docker.util as docker_util

log_file = docker_util.get_string_variable("general_log_location")
log_level = docker_util.get_string_variable("general_log_level")
initalize_log(log_level, log_file)
log_info("Log initialized")