# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1/gvoice.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x61pi/v1/gvoice.proto\"^\n\x0eSendSMSRequest\x12\x1b\n\x13gvoice_phone_number\x18\x01 \x02(\t\x12\x1e\n\x16recipient_phone_number\x18\x02 \x02(\t\x12\x0f\n\x07message\x18\x03 \x02(\t\"3\n\x0fSendSMSResponse\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x0f\n\x05\x65rror\x18\x02 \x01(\t:\x00\"6\n\x17\x46\x65tchContactListRequest\x12\x1b\n\x13gvoice_phone_number\x18\x01 \x02(\t\"]\n\x18\x46\x65tchContactListResponse\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x0f\n\x05\x65rror\x18\x02 \x01(\t:\x00\x12\x1f\n\x17recipient_phone_numbers\x18\x03 \x03(\t\"\x1b\n\x19\x46\x65tchGVoiceNumbersRequest\"\\\n\x1a\x46\x65tchGVoiceNumbersResponse\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x0f\n\x05\x65rror\x18\x02 \x01(\t:\x00\x12\x1c\n\x14gvoice_phone_numbers\x18\x03 \x03(\t\"r\n\x1a\x46\x65tchContactHistoryRequest\x12\x1b\n\x13gvoice_phone_number\x18\x01 \x02(\t\x12\x1e\n\x16recipient_phone_number\x18\x02 \x02(\t\x12\x17\n\x0cnum_messages\x18\x03 \x02(\x04:\x01\x30\"_\n\x1b\x46\x65tchContactHistoryResponse\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x0f\n\x05\x65rror\x18\x02 \x01(\t:\x00\x12\x1e\n\x08messages\x18\x03 \x03(\x0b\x32\x0c.MessageNode\"J\n\x0bMessageNode\x12\x11\n\ttimestamp\x18\x01 \x02(\x04\x12\x18\n\x10message_contents\x18\x02 \x02(\t\x12\x0e\n\x06source\x18\x03 \x02(\x08\x32\xa2\x02\n\x06GVoice\x12.\n\x07SendSMS\x12\x0f.SendSMSRequest\x1a\x10.SendSMSResponse\"\x00\x12G\n\x0eGetContactList\x12\x18.FetchContactListRequest\x1a\x19.FetchContactListResponse\"\x00\x12M\n\x10GetGVoiceNumbers\x12\x1a.FetchGVoiceNumbersRequest\x1a\x1b.FetchGVoiceNumbersResponse\"\x00\x12P\n\x11GetContactHistory\x12\x1b.FetchContactHistoryRequest\x1a\x1c.FetchContactHistoryResponse\"\x00\x42.Z,github.com/kingcobra2468/cot/internal/gvoice')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1.gvoice_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z,github.com/kingcobra2468/cot/internal/gvoice'
  _globals['_SENDSMSREQUEST']._serialized_start=23
  _globals['_SENDSMSREQUEST']._serialized_end=117
  _globals['_SENDSMSRESPONSE']._serialized_start=119
  _globals['_SENDSMSRESPONSE']._serialized_end=170
  _globals['_FETCHCONTACTLISTREQUEST']._serialized_start=172
  _globals['_FETCHCONTACTLISTREQUEST']._serialized_end=226
  _globals['_FETCHCONTACTLISTRESPONSE']._serialized_start=228
  _globals['_FETCHCONTACTLISTRESPONSE']._serialized_end=321
  _globals['_FETCHGVOICENUMBERSREQUEST']._serialized_start=323
  _globals['_FETCHGVOICENUMBERSREQUEST']._serialized_end=350
  _globals['_FETCHGVOICENUMBERSRESPONSE']._serialized_start=352
  _globals['_FETCHGVOICENUMBERSRESPONSE']._serialized_end=444
  _globals['_FETCHCONTACTHISTORYREQUEST']._serialized_start=446
  _globals['_FETCHCONTACTHISTORYREQUEST']._serialized_end=560
  _globals['_FETCHCONTACTHISTORYRESPONSE']._serialized_start=562
  _globals['_FETCHCONTACTHISTORYRESPONSE']._serialized_end=657
  _globals['_MESSAGENODE']._serialized_start=659
  _globals['_MESSAGENODE']._serialized_end=733
  _globals['_GVOICE']._serialized_start=736
  _globals['_GVOICE']._serialized_end=1026
# @@protoc_insertion_point(module_scope)
