# FAQ

## General

### Where can find the retrieved passwords?

The passwords are written to the Session ouput folder.

### I deleted all the Session output, is there a way to retrieve the passwords?

Yes in the ```progress.json``` file are all the passwords stored. In the feauture, there will be a tool to extract them.

### I would love to have a feauture implemented, how do i get in contact?

The best thing to do is, open a github issue.

### I found a bug, how do i get in contact?

The best thing to do is, open a github issue.

### Is there some sort of roadmap?

Yes there is, click [here.](roadmap.md "Roadmap")

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

## Worker

### How do i just use the worker Container?

If you want to use this, build only the ```worker_only``` stage and run the docker container.

## Coordinator

### Why ist there just a Workload of 10 pcap Files at time?

With larger ammounts Hashcat tends to become a Zombie process and the whole script gets blocked.

### Is there a way to access all .pcap files?

Yes, check out the **backlog** folder.

## Plugin

### The plugin somehow doesn't find my computer

This can have multiple reasons.

  1. The plugin is executed with the ```on_internet_available``` function. Check if your pwnagotchi has internet aviable.
  2. If you are running ```Docker Desktop``` make sure your PC can be discovered on the Network.
  3. There is sometimes a Socket on the pwnagotchi witch blocks further sockets. Reboot your pwnagotchi.
