from .DockerHandling import envVars

def get_string_variable(var_name):
    return envVars[var_name]


def get_boolean_variable(var_name):
    if str(envVars[var_name]).lower() == "true":
        return True
    
    return False