# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: air_cond.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x61ir_cond.proto\"4\n\rAirCondStatus\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x13\n\x0btemperature\x18\x02 \x01(\x05\"+\n\x11\x41irCondInfoParams\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x42\x05\n\x03_id2\xce\x01\n\x07\x41irCond\x12*\n\x06turnOn\x12\x0e.AirCondStatus\x1a\x0e.AirCondStatus\"\x00\x12+\n\x07turnOff\x12\x0e.AirCondStatus\x1a\x0e.AirCondStatus\"\x00\x12\x35\n\x11\x63hangeTemperature\x12\x0e.AirCondStatus\x1a\x0e.AirCondStatus\"\x00\x12\x33\n\x0brequestInfo\x12\x12.AirCondInfoParams\x1a\x0e.AirCondStatus\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'air_cond_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_AIRCONDSTATUS']._serialized_start=18
  _globals['_AIRCONDSTATUS']._serialized_end=70
  _globals['_AIRCONDINFOPARAMS']._serialized_start=72
  _globals['_AIRCONDINFOPARAMS']._serialized_end=115
  _globals['_AIRCOND']._serialized_start=118
  _globals['_AIRCOND']._serialized_end=324
# @@protoc_insertion_point(module_scope)