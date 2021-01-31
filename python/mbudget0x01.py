#so we can import all the libraries
import logging
import sys
import os
#sys.path.append('/etc/pwnagotchi/usr_plugins/')
_add_custom_packages_path()

import packages.tcp.tcp_server as tcp_server
import packages.coordinator_api.server.tcp_file_request_handler as tcp_file_request_handler
import packages.coordinator_api.client.coordinator_aviable_request as coordinator_aviable_request

import pwnagotchi.plugins as plugins



class Coordinator(plugins.Plugin):
    __author__ = 'mbudget0x01'
    __version__ = '1.1.0'
    __license__ = 'GPL3'
    __description__ = 'Plugin to coordinate with the Docker containers.'

    def __init__(self):
        logging.debug("Coordinator Plugin created")

    def on_loaded(self):
        logging.info("Coordinator Plugin loaded")

    def on_internet_available(self, agent):
        try:
            my_ip = self.options['ipaddress']
            if my_ip == "":
                my_ip = '10.0.0.2'
                logging.info("Using default IP, This can be changed in the toml file.")
            logging.info("Host IP is: " + my_ip)
        except Exception as ex:
            my_ip = '10.0.0.2'
            logging.warning("Encounterd invalid IP Config, using: " + my_ip)
         
        
        try:
            logging.debug("Starting attempt to transfer files")
            tcp_server.prepare('',5556,tcp_file_request_handler.tcp_file_request_handler)
            logging.debug("Sending broadcast")
            coordinator_aviable_request.broadcast_request(my_ip)
        except Exception as ex:
            logging.warning("Error on file transfer! " + str(ex))

    def on_unload(self, ui):
        try:
            logging.info("Stopping tcp server.")
            tcp_server.stop_server()
        except Exception as ex:
            logging.warning("Error on Stopping the tcp server " + str(ex))

def _add_custom_packages_path():
    f = os.path.realpath(__file__)
    dir = os.path.dirname(f)
    sys.path.append(dir)