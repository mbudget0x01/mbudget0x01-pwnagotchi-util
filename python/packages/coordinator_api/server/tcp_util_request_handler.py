from socketserver import BaseRequestHandler
from packages.coordinator_api.request_types import request_types
from packages.coordinator_api.request_results import request_results
import packages.log.log as log
import packages.coordinator_api.request_parser as request_parser
import packages.coordinator_api.tcp_request as tcp_request
import Coordinator as Coordinator
import packages.coordinator.workload as workload
import packages.coordinator.workload_types as workload_types
import packages.session.file_system as file_system
import os

class tcp_util_request_handler(BaseRequestHandler):

    def handle(self):
        log.log_debug("Handle tcp request")
        raw = self.request.recv(1024)
        socket = self.request
        my_request_parser = request_parser.request_parser(raw)
        request_type = my_request_parser.request_type
        log.log_debug("Received request of type: " + request_type)
        if request_type == request_types.UTIL_PURGE_SESSIONS.value:
            log.log_info_tag("USER-ACTION", "Purging of Session files scheduled")
            resp = tcp_request.handle_request(raw,request_results.ACK)
            socket.send(resp)
            wl =  workload.workload(workload_types.workload_types.PURGE_SESSIONS)
            Coordinator.my_workload_looper.add_special_workload(wl,True)


        elif request_type == request_types.UTIL_DO_ALL_FILES.value:
            log.log_info_tag("USER-ACTION", "Scheduling all Files in backlog as workload")
            resp = tcp_request.handle_request(raw,request_results.ACK)
            socket.send(resp)
            wlf = []
            for f in os.listdir(file_system.getBacklogPath()):
                wlf.append(f)
            Coordinator.my_workload_looper.add_workload(wlf)   

        else:
            log.log_info_tag("USER-ACTION", "Invalid request")
            resp = tcp_request.handle_request(raw,request_results.NACK)
            socket.send(resp)
            