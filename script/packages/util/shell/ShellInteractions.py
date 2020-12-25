import subprocess
import shlex

#Shell interaction
def executeShellCommand(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    p_status = p.wait()
    return p_status

def executeShellCommandWithCallback(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        #if output == '' and process.poll() is not None:
        if process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
    return rc