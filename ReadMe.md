# ReadMe

This is a Docker Container with a script to crack pcap files with Hashcat. The aim of the project is to automate the processing of Hashes captured with a pwnagotchi. As usual time isn't of the essence this can run a long time on a server.
It uses the Docker container dizcza/docker-hashcat. \
This project is under heavy development.

## Preparation

### General

* Make sure you have the appropriate Docker image specified for your hardware, in the Dockerfile.
* Make sure the mountings are specified in your Docker-Compose file.
* As of it is a working state, you have to put a Wordlist in the wordlist folder.
* Optionally you have to do the same for rules.
* Then adjust the files in script/StaticValues.py

### Hashcat

Configuration has To be implemented.

## Usage

Start the Container and it will do its work.

### FOLDER STRUCTURE

\
  ├─rules \
  ├─wordlists \
  └─data \
     ├─input \
     └─[Session-UUID] \
              ├─intermediates \
              ├─output \
              └─error

## Todo

- [ ] implement notification at end of run
- [ ] Add in multiple modes for the hascat execution e.g. rules etc
- [ ] Make runs configurable
- [ ] Keep a list of all attempts and results, to prevent multiple workload

## Licensing

For the Containers refer to the manufacterers of the containers.
This underlies the GPL3 License.
