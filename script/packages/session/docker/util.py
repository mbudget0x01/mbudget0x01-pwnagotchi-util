#from .DockerHandling import envVars
import packages.session.docker.DockerHandling as docker

def get_string_variable(var_name):
    return docker.envVars[var_name]


def get_boolean_variable(var_name):
    if str(docker.envVars[var_name]).lower() == "true":
        return True
    
    return False