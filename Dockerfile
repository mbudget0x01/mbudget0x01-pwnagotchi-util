#Change here if you have a GPU or Something else
FROM dizcza/docker-hashcat:intel-cpu

LABEL Description="This image parses pcap files and attempts to crack them with Hashcat" Vendor="mbudget0x01" Version="0.9"

#Script is written in python
RUN apt-get update && apt-get install -y --no-install-recommends \
		python3

# add data
ADD script /root/mbudget0x01/handshakeparser/script
ADD wordlists /root/mbudget0x01/handshakeparser/wordlists
ADD rules /root/mbudget0x01/handshakeparser/rules

#prepare folders
RUN mkdir /root/mbudget0x01/handshakeparser/data
RUN mkdir /root/mbudget0x01/handshakeparser/data/input

#Startup
ENTRYPOINT python3 /root/mbudget0x01/handshakeparser/script/Main.py