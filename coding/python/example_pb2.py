# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='easy.example',
  syntax='proto3',
  serialized_pb=_b('\n\rexample.proto\x12\x0c\x65\x61sy.example\"*\n\x0e\x45xampleMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\tb\x06proto3')
)




_EXAMPLEMESSAGE = _descriptor.Descriptor(
  name='ExampleMessage',
  full_name='easy.example.ExampleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='easy.example.ExampleMessage.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='easy.example.ExampleMessage.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=73,
)

DESCRIPTOR.message_types_by_name['ExampleMessage'] = _EXAMPLEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExampleMessage = _reflection.GeneratedProtocolMessageType('ExampleMessage', (_message.Message,), dict(
  DESCRIPTOR = _EXAMPLEMESSAGE,
  __module__ = 'example_pb2'
  # @@protoc_insertion_point(class_scope:easy.example.ExampleMessage)
  ))
_sym_db.RegisterMessage(ExampleMessage)


# @@protoc_insertion_point(module_scope)
