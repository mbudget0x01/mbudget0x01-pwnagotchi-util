from .static_values import *
from .docker.DockerHandling import parseDockerEnvFile
from .file_system import createSessionPaths

#create session
parseDockerEnvFile()
createSessionPaths()