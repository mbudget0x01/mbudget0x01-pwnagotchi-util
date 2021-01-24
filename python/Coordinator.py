import packages.log
import packages.log.log as log
import packages.udp.broadcast_receiver as broadcast_receiver
import packages.coordinator_api.server.coordinater_aviable_request_handler as coordinater_aviable_request_handler
import packages.session.coordinator_session as session
import packages.coordinator.workload_looper as workload_looper

my_workload_looper = None

def main():
    global my_workload_looper
    session.initialize_session()
    log.log_info_line()
    log.log_info("Coordinator starting")
    log.log_info_line()
    log.log_info("Initializing...")
    log.log_info("Initializing Workload Handling...")
    my_workload_looper = workload_looper.workload_looper.getInstance()
    log.log_info("Start listening for broadcasts...")
    broadcast_receiver.start_listening(5555, coordinater_aviable_request_handler.coordinater_aviable_request_handler)

if __name__ == "__main__":
    main()
