import packages.log
import packages.log.log as log
import packages.session as session

import FileConverter
import attack_coordinator

def main():
    log.log_info("----------------------------")
    log.log_info("Main routine started")
    log.log_info("----------------------------")

    #load attacks
    attack_coordinator.prepare()

    input_path = session.file_system.getInputPath()
    log.log_debug("Input Path: " + input_path)
    intermed_path = session.file_system.getSessionIntermedPath()
    log.log_debug("Intermediate Path: " + intermed_path)

    #converting the files
    if attack_coordinator.attack_pmkid_bruteforce or attack_coordinator.attack_pmkid_dictionary:
        log.log_info("Converting pcap files to pmkid...")
        FileConverter.convert_multiple_pcap_to_pmkid(input_path, intermed_path)


    if attack_coordinator.attack_wpa_bruteforce or attack_coordinator.attack_wpa_dictionary:
        log.log_info("Converting pcap files to hccapx...")
        FileConverter.convert_multiple_pcap_to_hccapx(input_path, intermed_path)

    #check if hascat should write output or if it is a dry run
        output_path = None
    if session.docker.util.get_boolean_variable("hashcat_print_outfiles"):
        output_path = session.file_system.getSessionOutputPath()
    
    #passing the attacks to the attack_coordinator
    attack_coordinator.attack(intermed_path, output_path)

    #cleaning up


    log.log_info("Main routine finished execution")

if __name__ == "__main__":
    main()









                                                                                        


