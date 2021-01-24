# Singel Usage

## General

If you want to spawn this container and have as less persistent data as possible then follow this guide.
But be aware it comes with some drawbacks:

* The progress is not tracked.
* In case you use the ssid wordlist, it contains only the ssids from the actual run.
* Your output is not mapped anywhere. Don't use the default docker ```entrypoint```.
* You have to rebuild your container to change anything, except the ```user.env```.

## Preparation to build

* Put the pcap files, you wan't to attempt to crack in the ```input``` folder.
* Static Files:
  * Put all the wordlist(s) you want to use in the ```wordlists``` folder.
  * Put all the rule(s) you want to use in the ```rules``` folder.
* Make sure what image you want to use for hashcat, see [dizcza/docker-hashcat](https://github.com/dizcza/docker-hashcat "dizcza/docker-hashcat").

## Preparation tun run

* Make sure to specify all the values in the ```user.env``` according to your wishes.
* Make sure to specify the mappings according to your wishes and use them accordingly.

## Helpful Commands

Build the container: \
```docker build --target worker_only --tag mbudget0x01-pwnagotchi-util --build-arg build_hashcat_image=intel-cpu .```

Run the container: \
```docker run -it --env-file=user.env mbudget0x01-pwnagotchi-util```

Run the container with different ```entrypoint```: \
```docker run -it --entrypoint /bin/bash --env-file=user.env mbudget0x01-pwnagotchi-util```

Start the script: \
```python3 /root/mbudget0x01/handshakeparser/script/Worker.py```

Start the script, no unnecessary output: \
```python3 /root/mbudget0x01/handshakeparser/script/Worker.py >> /dev/null```
