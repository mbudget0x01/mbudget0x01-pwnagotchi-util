#######################################################################
#
# Worker Stage
#
#######################################################################

#Change here if you have a GPU or Something else
ARG build_hashcat_image=intel-cpu
FROM dizcza/docker-hashcat:${build_hashcat_image} AS worker_only

LABEL Description="This image parses pcap files and attempts to crack them with Hashcat, worker_only" Vendor="mbudget0x01" Version="1.1"

#Script is written in python
RUN apt-get update && apt-get install -y --no-install-recommends \
		python3

# add data
ADD python /root/mbudget0x01/script
ADD docker/default.env /root/mbudget0x01/script/packages/session/docker/default.env

ADD docker/wordlists /root/mbudget0x01/wordlists
ADD docker/rules /root/mbudget0x01/rules

#prepare folders
RUN mkdir /root/mbudget0x01/data
RUN mkdir /root/mbudget0x01/data/input

#DEBUG
ADD docker/input /root/mbudget0x01/data/input

#Startup
ENTRYPOINT python3 /root/mbudget0x01/script/Worker.py

#######################################################################
#
# Coordinator Stage
#
#######################################################################
FROM worker_only AS complete

LABEL Description="This image parses pcap files and attempts to crack them with Hashcat" Vendor="mbudget0x01" Version="1.1"

#Run baby, run
ENTRYPOINT python3 /root/mbudget0x01/script/Coordinator.py