import packages.coordinator_api.request_types as request_types

class request_builder:
    def __init__(self):
        self.requets_type = None
        self.requets_data = None
        #eg. OK, FALSE, ACK, etc..
        self.request_result = None
        self.application_identifier = "mbudget0x01-pwnagotchi-util-coordinator"

    def set_request_type(self, request_type:str) -> 'request_builder':
        self.requets_type =  request_type
        return self

    def set_request_data(self, requets_data:str) -> 'request_builder':
        self.requets_data = requets_data
        return self

    def set_request_result(self, request_result:str) -> 'request_builder':
        self.request_result = request_result
        return self

    def _build_string(self) -> str:
        req = self.application_identifier
        if self.requets_type is None:
            raise Exception(self.requets_type)
        req = self._add_request_part(req,self.requets_type)
        req = self._add_request_part(req, self.requets_data)
        req = self._add_request_part(req, self.request_result)
        return req

    def build(self) -> bytes:
        req = self._build_string()
        return req.encode("utf-8")
        

    def _add_request_part(self,request:str, request_part) -> str:
        if request_part is None:
            request = request + ":" + ""
        else:
            request = request + ":" + request_part
        return request