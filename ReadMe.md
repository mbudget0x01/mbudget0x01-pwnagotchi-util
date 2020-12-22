# ReadMe

This is a Docker Container with a script to crack pcap files with Hashcat. The aim of the project is to automate the processing of Hashes captured with a pwnagotchi. As usual time isn't of the essence this can run a long time on a server.
It uses the Docker container dizcza/docker-hashcat. \
This project is under heavy development.

## Preparation

### General

* Make sure you have the appropriate Docker image specified for your hardware, in the [Docker File](DockerFile "DockerFile").
* Make sure the mountings are specified in your [Docker-Compose file](docker-compose.yml "Docker-Compose file").
* Optional:
  * Put custom wordlists and rule files in the according folders

### Hashcat

Configuration has To be implemented.

## Usage

If you don't want to use ```docker-compose```, make sure you pass your variables and have set the mappings.

### Repetitive Usage

1. Configure the user.env file according to your wishes
2. Start the Container and it will do its work, I highly reccomend to use docker compose.
    * Navigate to the ```docker-compose.yml``` file
    * ```docker-compose up -d```

### After adding or removing wordlists/rule files

1. Configure the user.env file according to your wishes
2. Start the Container and it will do its work, I highly reccomend to use docker compose.
    * Navigate to the ```docker-compose.yml``` file
    * ```docker-compose build```
    * ```docker-compose up -d```

## FOLDER STRUCTURE

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
This project underlies the GPL3 License.
