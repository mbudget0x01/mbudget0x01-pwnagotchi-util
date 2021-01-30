# ReadMe

This is a Docker Container with a script to crack pcap files with Hashcat. The aim of the project is to automate the processing of Hashes captured with a pwnagotchi. It's designed to run in the background and grimmley do it's work.
It uses the Docker container [dizcza/docker-hashcat](https://github.com/dizcza/docker-hashcat "dizcza/docker-hashcat"). \
This project is under heavy development.

## Overwiew

This project has three parts, namely:

* pwnagotchi plugin
* [workload coordinator](doc/coordinator/coordinator.md "coordinator")
* worker script

The Worker script takes a bunch of pcap files, converts them and attempts to crack them with hashcat. \
The Coordinator Script loads the files from your pwnagotchi and instantiates the Worker script. \
The pwnagotchi Plugin provides the files to your Coordinator Script. \

## Worker Only

It is possible to use the worker script on it's own. If you want to use this, build only the ```worker_only``` stage and run the docker container.
Please refere to the according document:

* [single use/docker only](doc/usage/single-use.md "single use/docker only")

## Preparation and Usage

I am focussing here on the usage of all the tools combined.
Please refere to this document.

* [docker-compose](doc/usage/docker-compose.md "docker-compose")
* [plugin](doc/usage/plugin.md "plugin")

## Additional Information

### I have problems or found a bug

Please refere to the [FAQ.](doc/faq.md "FAQ")

### FAQ

Is there a FAQ? [Yes.](doc/faq.md "FAQ")

### .env files

The Script comes with two ```.env``` files. \
The ```default.env``` is used as base ```.env``` konfiguration file. Use it as reference but don't change it. In the ```user.env``` you can overwrite the values from the ```defualt.env``` file and configure your run. These variables are parsed during runtime. This means there is no container rebuild required for diffrent runs if you specify something there. If you are yousing the coordinator there is a restart required. The Key-Value pairs should be selfexplainatory ;-)

### FOLDER STRUCTURE

``` \
  ├─rules
  ├─wordlists
  └─data
     ├─progress.json
     ├─ssid-wordlist.json
     ├─backlog
     ├─input
     ├─output
     └─[Session-UUID]
              ├─intermediates
              └─error
 ```

The ```progress.json``` is used to track progression, the ```ssid-wordlist.json``` is the master SSID wordlist. It contains some meta data. The acutal export can be found under ```wordlists/ssid-wordlist-export.txt```.

## Todo

Check out this page: [Roadmap.](doc/roadmap.md "Roadmap")

## Licensing

For the Containers refer to the manufacterers of the containers.
This project underlies the GPL3 License.
