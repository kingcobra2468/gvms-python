import grpc

from gvms.api.v1.gvoice_pb2_grpc import GVoiceStub
import gvms.api.v1.gvoice_pb2 as gvoice_pb2
from gvms.exceptions import GVMSRequestException


class GVMSClient:
    def __init__(self, host, port) -> None:
        """Constructor.

        Args:
            host (str): the GVMS server host.
            port (_type_): the GVMS server port.
        """
        self._host = host
        self._port = port

        self._setup()

    def _setup(self):
        channel = grpc.insecure_channel(f'{self._host}:{self._port}')
        self._stub = GVoiceStub(channel)

    def send_sms(self, gvoice_phone_number, recipient_phone_number, message):
        resp = self._stub.SendSMS(gvoice_pb2.SendSMSRequest(
            gvoice_phone_number=gvoice_phone_number, recipient_phone_number=recipient_phone_number, message=message))

        if not resp.success:
            raise GVMSRequestException(resp.error)

    def get_contact_list(self, gvoice_phone_number):
        resp = self._stub.GetContactList(gvoice_pb2.FetchContactListRequest(
            gvoice_phone_number=gvoice_phone_number))

        if not resp.success:
            raise GVMSRequestException(resp.error)

        return resp.recipient_phone_numbers

    def get_gvoice_numbers(self, gvoice_phone_number, recipient_phone_number, message):
        resp = self._stub.SendSMS(gvoice_pb2.FetchGVoiceNumbersRequest(
            gvoice_phone_number=gvoice_phone_number, recipient_phone_number=recipient_phone_number, message=message))

        if not resp.success:
            raise GVMSRequestException(resp.error)

        return resp.gvoice_phone_numbers

    def get_contact_history(self, gvoice_phone_number, recipient_phone_number, num_messages):
        resp = self._stub.GetContactHistory(gvoice_pb2.FetchContactHistoryRequest(
            gvoice_phone_number=gvoice_phone_number, recipient_phone_number=recipient_phone_number, num_messages=num_messages))

        if not resp.success:
            raise GVMSRequestException(resp.error)

        return resp.messages
