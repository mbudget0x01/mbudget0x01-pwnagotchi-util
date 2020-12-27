# ReadMe

This is a Docker Container with a script to crack pcap files with Hashcat. The aim of the project is to automate the processing of Hashes captured with a pwnagotchi. It's designed to run in the background and grimmley do it's work.
It uses the Docker container [dizcza/docker-hashcat](https://github.com/dizcza/docker-hashcat "dizcza/docker-hashcat"). \
This project is under heavy development.

## Preparation and Usage

I highly recommend to use ```docker-compose```. Please refer to the according documents:

* [single use/docker only](doc/usage/single-use.md "single use/docker only")
* [docker-compose](doc/usage/docker-compose.md "docker-compose")

## Additional Information

### FAQ

Is there a FAQ? [Yes.](doc/faq.md "FAQ")

### .env files

The Script comes with two ```.env``` files. \
The ```default.env``` is used as base ```.env``` konfiguration file. Use it as reference but don't change it. In the ```user.env``` you can overwrite the values from the ```defualt.env``` file and configure your run. These variables are parsed during runtime. This means there is no container rebuild required for diffrent runs if you specify something there. The Key-Value pairs should be selfexplainatory ;-)

### FOLDER STRUCTURE

``` \
  ├─rules
  ├─wordlists
  └─data
     ├─progress.json
     ├─ssid-wordlist.json
     ├─input
     └─[Session-UUID]
              ├─intermediates
              ├─output
              └─error
 ```

The ```progress.json``` is used to track progression, the ```ssid-wordlist.json``` is the master SSID wordlist. It contains some meta data. The acutal export can be found under ```wordlists/ssid-wordlist-export.txt```.

## Todo

- [ ] Implement notification at end of run
- [x] Add in multiple modes for the hascat execution e.g. rules etc
- [x] Make runs configurable
- [x] Keep a list of all attempts and results, to prevent multiple workload
- [x] Write and extend a Wordlist out of SSIDs to use in further runs
- [x] Make Dockerfile configurable through variables
- [x] Implement cleanup
- [ ] Build some sort of communication with pwnagotchi to automate the process
- [ ] Make script to handle docker containers and subsequent workload

## Licensing

For the Containers refer to the manufacterers of the containers.
This project underlies the GPL3 License.
