# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generic_request.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='generic_request.proto',
  package='master',
  serialized_pb='\n\x15generic_request.proto\x12\x06master\"\xcc\x01\n\x0cProtoRequest\x12\x13\n\x0bservicename\x18\x01 \x02(\t\x12\x0e\n\x06\x63\x61ller\x18\x02 \x02(\t\x12\x10\n\x08ipadress\x18\x03 \x01(\t\x12\x34\n\x08priority\x18\x04 \x01(\x0e\x32\x1d.master.ProtoRequest.Priority:\x03LOW\x12\'\n\x1breq_additionaldata_donotuse\x18\x05 \x03(\tB\x02\x18\x01\"&\n\x08Priority\x12\x08\n\x04HIGH\x10\x01\x12\x07\n\x03STD\x10\x02\x12\x07\n\x03LOW\x10\x03\"\x8e\x01\n\rProtoResponse\x12!\n\x03req\x18\x01 \x02(\x0b\x32\x14.master.ProtoRequest\x12\x17\n\x0b\x63omputetime\x18\x02 \x02(\x03:\x02-1\x12\x17\n\x0fserver_ipadress\x18\x03 \x01(\t\x12(\n\x1cresp_additionaldata_donotuse\x18\x04 \x03(\tB\x02\x18\x01\"B\n\rSimpleRequest\x12!\n\x03req\x18\x01 \x02(\x0b\x32\x14.master.ProtoRequest\x12\x0e\n\x06youpla\x18\x02 \x02(\t\"C\n\x0eSimpleResponse\x12#\n\x04resp\x18\x01 \x02(\x0b\x32\x15.master.ProtoResponse\x12\x0c\n\x04\x62oum\x18\x02 \x02(\t')



_PROTOREQUEST_PRIORITY = _descriptor.EnumDescriptor(
  name='Priority',
  full_name='master.ProtoRequest.Priority',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HIGH', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STD', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOW', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=200,
  serialized_end=238,
)


_PROTOREQUEST = _descriptor.Descriptor(
  name='ProtoRequest',
  full_name='master.ProtoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='servicename', full_name='master.ProtoRequest.servicename', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caller', full_name='master.ProtoRequest.caller', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipadress', full_name='master.ProtoRequest.ipadress', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='priority', full_name='master.ProtoRequest.priority', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='req_additionaldata_donotuse', full_name='master.ProtoRequest.req_additionaldata_donotuse', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROTOREQUEST_PRIORITY,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=34,
  serialized_end=238,
)


_PROTORESPONSE = _descriptor.Descriptor(
  name='ProtoResponse',
  full_name='master.ProtoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='req', full_name='master.ProtoResponse.req', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='computetime', full_name='master.ProtoResponse.computetime', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_ipadress', full_name='master.ProtoResponse.server_ipadress', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resp_additionaldata_donotuse', full_name='master.ProtoResponse.resp_additionaldata_donotuse', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=241,
  serialized_end=383,
)


_SIMPLEREQUEST = _descriptor.Descriptor(
  name='SimpleRequest',
  full_name='master.SimpleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='req', full_name='master.SimpleRequest.req', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='youpla', full_name='master.SimpleRequest.youpla', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=385,
  serialized_end=451,
)


_SIMPLERESPONSE = _descriptor.Descriptor(
  name='SimpleResponse',
  full_name='master.SimpleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='master.SimpleResponse.resp', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boum', full_name='master.SimpleResponse.boum', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=453,
  serialized_end=520,
)

_PROTOREQUEST.fields_by_name['priority'].enum_type = _PROTOREQUEST_PRIORITY
_PROTOREQUEST_PRIORITY.containing_type = _PROTOREQUEST;
_PROTORESPONSE.fields_by_name['req'].message_type = _PROTOREQUEST
_SIMPLEREQUEST.fields_by_name['req'].message_type = _PROTOREQUEST
_SIMPLERESPONSE.fields_by_name['resp'].message_type = _PROTORESPONSE
DESCRIPTOR.message_types_by_name['ProtoRequest'] = _PROTOREQUEST
DESCRIPTOR.message_types_by_name['ProtoResponse'] = _PROTORESPONSE
DESCRIPTOR.message_types_by_name['SimpleRequest'] = _SIMPLEREQUEST
DESCRIPTOR.message_types_by_name['SimpleResponse'] = _SIMPLERESPONSE

class ProtoRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROTOREQUEST

  # @@protoc_insertion_point(class_scope:master.ProtoRequest)

class ProtoResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROTORESPONSE

  # @@protoc_insertion_point(class_scope:master.ProtoResponse)

class SimpleRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SIMPLEREQUEST

  # @@protoc_insertion_point(class_scope:master.SimpleRequest)

class SimpleResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SIMPLERESPONSE

  # @@protoc_insertion_point(class_scope:master.SimpleResponse)


_PROTOREQUEST.fields_by_name['req_additionaldata_donotuse'].has_options = True
_PROTOREQUEST.fields_by_name['req_additionaldata_donotuse']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')
_PROTORESPONSE.fields_by_name['resp_additionaldata_donotuse'].has_options = True
_PROTORESPONSE.fields_by_name['resp_additionaldata_donotuse']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')
# @@protoc_insertion_point(module_scope)
