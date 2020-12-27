# docker-compose Usage

## General

If you want to use the container to it's full extend, I recommend using it this way. But first let's do the basic configuration ;-)

## Preparation to build

### docker-compose.yml

* Set the ```build_hashcat_image``` to the value, fitting your system (refernce: [dizcza/docker-hashcat](https://github.com/dizcza/docker-hashcat "dizcza/docker-hashcat")).
* Mappings:
  * Set the ```data``` folder mapping using: ```{your host system path}:/root/mbudget0x01/handshakeparser/data```
  * Set the ```wordlists``` folder mapping using: ```{your host system path}:/root/mbudget0x01/handshakeparser/wordlists```
  * Set the ```rules``` folder mapping using: ```{your host system path}:/root/mbudget0x01/handshakeparser/rules```

## Preparation to run

* Make sure to specify all the values in the ```user.env``` according to your wishes.

### First run

The first run is a bit special as it needs to create all the needed paths. It is possible to run with workload from the start. To do some work in the first run put the ```.pcap``` files in the ```input``` folder.

However be aware that this files will not be cleaned up after the run and stay there. I recommend to build the container and do a dry run.

The same goes for the worlists and rules.

### Subsequent runs

The subsequent runs are pretty straight-forward.

* Put the ```.pcap``` files you want to crack on your host system in the mapped ```{your host system path}/data/input``` folder
* Optional:
  * Adjust your ```user.env``` file according to your needs
  * supplement the wordlists and rules like the ```.pcap``` files

### Let's go

1. Navigate to the ```docker-compose.yml```
2. If you made changes to the  ```docker-compose.yml```, run ```docker-compose build```
3. run ```docker-compose up -d```

## Helpful stuff

### I want to save thel logfile on my host

You can modify the logfile path with your ```user.env``` file. From there you can redirect it to an existing mapping or add a new mapping to your ```docker-compose.yml```.\
The variable you are looking for ,to set in your ```user.env```, is ```general_log_location```.
