# ReadMe

This is a Docker Container with a script to crack pcap files with Hashcat. The aim of the project is to automate the processing of Hashes captured with a pwnagotchi. It's designed to run in the background and grimmley do it's work.
It uses the Docker container [dizcza/docker-hashcat](https://github.com/dizcza/docker-hashcat "dizcza/docker-hashcat"). \
This project is under heavy development.

## Preparation

### General

* Make sure you have the appropriate Docker image specified for your hardware, in the [Docker File](DockerFile "DockerFile").
* Make sure the mountings are specified in your [Docker-Compose file](docker-compose.yml "Docker-Compose file").
* Optional:
  * Put custom wordlists and rule files in the according folders

## Usage

If you don't want to use ```docker-compose```, make sure you pass your variables and have set the mappings.

### .env files

The Script comes with two ```.env``` files. \
The ```default.env``` is used as base ```.env``` konfiguration file. Use it as reference but don't change it. In the ```user.env``` you can overwrite the values from the ```defualt.env``` file and configure your run. These variables are parsed during runtime. This means there is no container rebuild required for diffrent runs if you specify something there. The Key-Value pairs should be selfexplainatory ;-)

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

``` \
  ├─rules
  ├─wordlists
  └─data
     ├─progress.json
     ├─input
     └─[Session-UUID]
              ├─intermediates
              ├─output
              └─error
 ```

The ```progress.json``` is used to track progression.

## Todo

- [ ] implement notification at end of run
- [x] Add in multiple modes for the hascat execution e.g. rules etc
- [x] Make runs configurable
- [x] Keep a list of all attempts and results, to prevent multiple workload
- [ ] Write and extend a Wordlist out of SSIDs to use in further runs
- [ ] Make Dockerfile configurable through variables
- [ ] Implement cleanup

## Licensing

For the Containers refer to the manufacterers of the containers.
This project underlies the GPL3 License.
