import packages.log
import packages.log.log as log
import packages.session as session
import packages.session.worker_session as worker_session
import packages.session.clean_up as clean_up
import packages.worker.ssid_wordlist_attack as ssid_wordlist_attack

import packages.worker.FileConverter as FileConverter
import packages.worker.attack_coordinator as attack_coordinator

def main():
    worker_session.initialize_session()
    log.log_info_line()
    log.log_info("Main routine started")
    log.log_info("Session ID: " + str(session.static_values.SESSION_UUID))
    log.log_info_line()
    
    #load attacks
    attack_coordinator.prepare()

    input_path = session.file_system.getInputPath()
    log.log_debug("Input Path: " + input_path)
    intermed_path = session.file_system.getSessionIntermedPath()
    log.log_debug("Intermediate Path: " + intermed_path)

    #converting the files
    if attack_coordinator.attack_pmkid_bruteforce or attack_coordinator.attack_pmkid_dictionary or attack_coordinator.attack_pmkid_ssid_dictionary:
        log.log_info("Converting pcap files to pmkid...")
        FileConverter.convert_multiple_pcap_to_pmkid(input_path, intermed_path)


    if attack_coordinator.attack_wpa_bruteforce or attack_coordinator.attack_wpa_dictionary or attack_coordinator.attack_wpa_ssid_dictionary:
        log.log_info("Converting pcap files to hccapx...")
        FileConverter.convert_multiple_pcap_to_hccapx(input_path, intermed_path)

    #check if hascat should write output or if it is a dry run
    output_path = None
    if session.docker.util.get_boolean_variable("hashcat_print_outfiles"):
        output_path = session.file_system.getOutputPath()
    
    #passing the attacks to the attack_coordinator
    attack_coordinator.attack(intermed_path, output_path)

    #cleaning up
    log.log_info_line()

    if session.docker.util.get_boolean_variable("general_cleanup_session"):
        log.log_info("Cleaning up session...")
        clean_up.clean_up_session()

    if session.docker.util.get_boolean_variable("general_cleanup_intermediates") and not session.docker.util.get_boolean_variable("general_cleanup_session"):
        log.log_info("Cleaning up session intermediates...")
        clean_up.clean_up_intermediates()
    if session.docker.util.get_boolean_variable("general_cleanup_input"):
        only_sucessfull = session.docker.util.get_boolean_variable("general_cleanup_input_only_successfull")
        log.log_info("Cleaning up input...")
        if only_sucessfull:
            log.log_info("Only removing sucessfull files")
        clean_up.clean_up_input(only_sucessfull)

    log.log_info("Main routine finished execution")
    log.log_info_line()

if __name__ == "__main__":
    main()
