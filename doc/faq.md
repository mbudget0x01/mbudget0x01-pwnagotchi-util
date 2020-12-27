# FAQ

## General

### Where can find the retrieved passwords?

The passwords are written to the Session ouput folder.

### I deleted all the Session output, is there a way to retrieve the passwords?

Yes in the ```progress.json``` file are all the passwords stored. In the feauture, there will be a tool to extract them.

## Config

### what does ```hashcat_print_outfiles``` do?

It prevents hascat from writing output files. Just use it if you want to test something or perform a dry run. Like this the only way to get the passwort is from stout. However it will be logged as failed in the progress. To prevent you from not ever gaining the password ;-)

## Log

### What are the numbers in ```general_log_level``` in the ```.env``` files

These are the ```python logging``` log levels: \
**10** means debug \
**20** means info

### What does "Hashcat ended with status: X" mean?

The most common states are the following:
| Code  | Meaning               |
| ----- | --------------------- |
| 0     | sucess                |
| 1     | exhausted, failed     |
| 255   | error e.g. empty hash |
