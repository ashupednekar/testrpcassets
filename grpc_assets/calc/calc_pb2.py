# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calc.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncalc.proto\"\x1b\n\x03Inp\x12\t\n\x01\x61\x18\x01 \x01(\x03\x12\t\n\x01\x62\x18\x02 \x01(\x03\"\x13\n\x06Result\x12\t\n\x01\x63\x18\x01 \x01(\x03\x32k\n\x04\x43\x61lc\x12\x14\n\x03\x61\x64\x64\x12\x04.Inp\x1a\x07.Result\x12\x19\n\x08subtract\x12\x04.Inp\x1a\x07.Result\x12\x19\n\x08multiply\x12\x04.Inp\x1a\x07.Result\x12\x17\n\x06\x64ivide\x12\x04.Inp\x1a\x07.Resultb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_INP']._serialized_start=14
  _globals['_INP']._serialized_end=41
  _globals['_RESULT']._serialized_start=43
  _globals['_RESULT']._serialized_end=62
  _globals['_CALC']._serialized_start=64
  _globals['_CALC']._serialized_end=171
# @@protoc_insertion_point(module_scope)
