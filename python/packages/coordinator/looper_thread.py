import packages.log.log as log
import packages.session.clean_up as clean_up
import packages.session.file_system as file_system
import packages.coordinator.workload as workload
import packages.coordinator.workload_types as workload_types
import subprocess
import threading
import time
import shutil
import os

class looper_thread (threading.Thread):

    def __init__(self, workload_list:list):
        threading.Thread.__init__(self)
        self.name ="LOOPER_THREAD"
        self.current_workload:workload.workload = None
        self.workload_list =workload_list
        self._is_busy = False
        self.subprocess = None

    def run(self):
        log.log_debug("Starting thread: " + self.name)
        log.log_debug("Starting Loop")
        while True:
            if self._is_busy:
                if self.subprocess is not None:
                    #Checking subprocess status None means working
                    if self.subprocess.poll() is not None:
                        log.log_info("Worker finished, ready for next workload.")
                        self.subprocess = None
                        self._is_busy = False
                    
                    continue


            if self._get_workload() == None:
                time.sleep(5)
            else:
                if self.current_workload.type == workload_types.workload_types.NORMAL:
                    log.log_debug("Handling workload.")
                    self._handle_workload_worker()
                elif self.current_workload.type == workload_types.workload_types.PURGE_SESSIONS:
                    log.log_debug("Handling Purge")
                    clean_up.purge_session_folders()
                # backlog_path = file_system.getBacklogPath()
                # input_path = file_system.getInputPath()
                # for s in self.current_workload:
                #     infile = os.path.join(backlog_path, s)
                #     outfile = os.path.join(input_path,s)
                #     shutil.copyfile(infile, outfile)

                # #Starting Subprocess for worker
                # log.log_debug("Starting worker.")
                # self.subprocess = subprocess.Popen('python3 /root/mbudget0x01/script/Worker.py', stdout=subprocess.PIPE, shell=True)
                # self._is_busy = True             
                


    def _get_workload(self):
        lock = threading.Lock()
        lock.acquire(blocking=True)
        if len(self.workload_list) > 0:
            log.log_debug("Workload detected")              
            self.current_workload = self.workload_list.pop()
        else:
            self.current_workload = None
        lock.release()
        return self.current_workload

    def _handle_workload_worker(self):
        backlog_path = file_system.getBacklogPath()
        input_path = file_system.getInputPath()
        for s in self.current_workload.workload:
            infile = os.path.join(backlog_path, s)
            outfile = os.path.join(input_path,s)
            shutil.copyfile(infile, outfile)

        #Starting Subprocess for worker
        log.log_debug("Starting worker.")
        self.subprocess = subprocess.Popen('python3 /root/mbudget0x01/script/Worker.py', stdout=subprocess.PIPE, shell=True)
        self._is_busy = True         
        