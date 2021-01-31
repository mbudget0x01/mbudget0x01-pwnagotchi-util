import packages.coordinator.workload_types as workload_types

class workload:
    def __init__(self, type:workload_types.workload_types = workload_types.workload_types.NORMAL):
        self.type = type
        self.workload = []

    def set_workload(self, workload:list):
        self.workload = workload

    def get_type(self) -> workload_types.workload_types:
        return self.type
