import grpc

from api.v1.gvoice_pb2_grpc import GVoiceStub
import api.v1.gvoice_pb2 as gvoice_pb2

class GVMSClient:
    def __init__(self, host, port) -> None:
        self._host = host
        self._port = port

        self._setup()
        
    def _setup(self):
        channel = grpc.insecure_channel(f'{self._host}:{self._port}')
        self._stub = GVoiceStub(channel)
    
    def get_contact_list(self, gvoice_phone_number):
        resp = self._stub.GetContactList(gvoice_pb2.FetchContactListRequest(gvoice_phone_number=gvoice_phone_number))
        
        if not resp.success: #get resp.error
            raise ValueError()
        
        return list(resp.recipient_phone_numbers)       
        
        
