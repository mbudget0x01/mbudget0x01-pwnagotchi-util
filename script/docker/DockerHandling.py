import os

envVars = {}

def getSehllVariable(varname):
    try:
        return os.environ[varname]
    except KeyError:
        return None

def parseDockerEnvFile():
    #TODO: change
    file = os.path.dirname(os.path.realpath(__file__))
    file = os.path.dirname(file)
    file = os.path.join(file, "docker", "default.env")
    with open(file) as myfile:
        for line in myfile:
            if not line == "":
                name, var = line.partition("=")[::2]
                envVars[name.strip()] = str(var).strip()

def updateVariables():
    for key in envVars.keys():
        val = getSehllVariable(key)
        if not val is None:
            envVars[key] = val

def initializeEnvVariables():
    parseDockerEnvFile()
    updateVariables()