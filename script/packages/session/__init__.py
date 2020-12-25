from .static_values import *
from .docker.DockerHandling import initializeEnvVariables
from .file_system import createSessionPaths

#create session
initializeEnvVariables()
createSessionPaths()