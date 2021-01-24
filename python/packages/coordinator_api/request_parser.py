import packages.coordinator_api.request_builder as builder
from.request_types import request_types

class request_parser:
    def __init__(self, request:bytes):
        self.request = request
        self.request_string = request.decode("utf-8")
        self.request_type = None
        self.request_data = None
        self.request_handled = None
        self.application_identifier = "mbudget0x01-pwnagotchi-util-coordinator"
        if not self._is_valid_request():
            raise Exception(self)
        self._parse_request(self.request_string)

    def _is_valid_request(self):
        if self.request_string.split(":")[0] == self.application_identifier:
            return True
        return False

    def _parse_request(self, request_string:str) -> 'request_parser':
        parts = self.request_string.split(":")
        self.request_type = parts[1]
        self.request_data = parts[2]
        self.request_handled = parts[3]
        return self

    def get_builder(self) -> 'request_builder':
        my_builder = builder.request_builder()
        my_builder.set_request_type(self.request_type)
        my_builder.set_request_data(self.request_data)
        my_builder.set_request_result(self.request_handled)
        return my_builder
