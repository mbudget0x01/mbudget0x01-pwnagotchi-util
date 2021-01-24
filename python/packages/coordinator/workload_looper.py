import threading
import packages.coordinator.looper_thread as looper_thread

class workload_looper():

    __instance:'workload_looper' = None
    _is_busy:bool = False
    _looper:looper_thread.looper_thread = None


    _queued_work = []

    def __init__(self):
       if workload_looper.__instance != None:
            raise Exception("This class is a singleton!")
       else:
            workload_looper.__instance = self
            workload_looper._looper = looper_thread.looper_thread(workload_looper._queued_work)
            workload_looper._looper.start()


    
    @staticmethod 
    def getInstance():
        if workload_looper.__instance == None:
            workload_looper()
        return workload_looper.__instance


    def add_workload(self,workload:list):
        #Here wi split up the workload, to prevent problems with the garbage collector -> produce zombies
        while len(workload) > 10:
            new_wl = []
            for i in range(0, 11):
                int(i)
                new_wl.append(workload.pop())
        
            workload_looper._queued_work.append(new_wl)
    

        workload_looper._queued_work.append(workload)