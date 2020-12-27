#Change here if you have a GPU or Something else
ARG build_hashcat_image=intel-cpu
FROM dizcza/docker-hashcat:${build_hashcat_image}

LABEL Description="This image parses pcap files and attempts to crack them with Hashcat" Vendor="mbudget0x01" Version="1.0"

#Script is written in python
RUN apt-get update && apt-get install -y --no-install-recommends \
		python3

# add data
ADD script /root/mbudget0x01/handshakeparser/script
ADD default.env /root/mbudget0x01/handshakeparser/script/packages/session/docker/default.env

ADD wordlists /root/mbudget0x01/handshakeparser/wordlists
ADD rules /root/mbudget0x01/handshakeparser/rules

#prepare folders
RUN mkdir /root/mbudget0x01/handshakeparser/data
RUN mkdir /root/mbudget0x01/handshakeparser/data/input

#DEBUG
ADD input /root/mbudget0x01/handshakeparser/data/input

#Startup
ENTRYPOINT python3 /root/mbudget0x01/handshakeparser/script/Main.py