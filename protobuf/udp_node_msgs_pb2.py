# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/udp-node-msgs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/udp-node-msgs.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cprotobuf/udp-node-msgs.proto\"\xd3\x03\n\x0bPlayerState\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tworldTime\x18\x02 \x01(\x03\x12\x10\n\x08\x64istance\x18\x03 \x01(\x05\x12\x10\n\x08roadTime\x18\x04 \x02(\x05\x12\x0c\n\x04laps\x18\x05 \x01(\x05\x12\r\n\x05speed\x18\x06 \x01(\x05\x12\x14\n\x0croadPosition\x18\x08 \x01(\x05\x12\x12\n\ncadenceUHz\x18\t \x01(\x05\x12\x11\n\theartrate\x18\x0b \x01(\x05\x12\r\n\x05power\x18\x0c \x01(\x05\x12\x0f\n\x07heading\x18\r \x01(\x03\x12\x0c\n\x04lean\x18\x0e \x01(\x05\x12\x10\n\x08\x63limbing\x18\x0f \x01(\x05\x12\x0c\n\x04time\x18\x10 \x01(\x05\x12\x0b\n\x03\x66\x31\x39\x18\x13 \x01(\x05\x12\x0b\n\x03\x66\x32\x30\x18\x14 \x01(\x05\x12\x10\n\x08progress\x18\x15 \x01(\x05\x12\x17\n\x0f\x63ustomisationId\x18\x16 \x01(\x03\x12\x14\n\x0cjustWatching\x18\x17 \x01(\x05\x12\x10\n\x08\x63\x61lories\x18\x18 \x01(\x05\x12\t\n\x01x\x18\x19 \x01(\x02\x12\x10\n\x08\x61ltitude\x18\x1a \x01(\x02\x12\t\n\x01y\x18\x1b \x01(\x02\x12\x17\n\x0fwatchingRiderId\x18\x1c \x01(\x05\x12\x0f\n\x07groupId\x18\x1d \x01(\x05\x12\r\n\x05sport\x18\x1f \x01(\x03\x12\x0b\n\x03\x66\x33\x34\x18\" \x01(\x02\"\xcc\x01\n\x0e\x43lientToServer\x12\x11\n\tconnected\x18\x01 \x02(\x05\x12\x11\n\tplayer_id\x18\x02 \x02(\x05\x12\x12\n\nworld_time\x18\x03 \x02(\x03\x12\r\n\x05seqno\x18\x04 \x02(\x05\x12\x1b\n\x05state\x18\x07 \x02(\x0b\x32\x0c.PlayerState\x12\n\n\x02\x66\x38\x18\x08 \x02(\x03\x12\n\n\x02\x66\x39\x18\t \x02(\x03\x12\x13\n\x0blast_update\x18\n \x02(\x03\x12\x0b\n\x03\x66\x31\x31\x18\x0b \x02(\x03\x12\x1a\n\x12last_player_update\x18\x0c \x02(\x03\"\xab\x01\n\x0eServerToClient\x12\n\n\x02\x66\x31\x18\x01 \x02(\x05\x12\x11\n\tplayer_id\x18\x02 \x02(\x05\x12\x12\n\nworld_time\x18\x03 \x02(\x03\x12\r\n\x05seqno\x18\x04 \x02(\x05\x12\n\n\x02\x66\x35\x18\x05 \x02(\x05\x12\x1c\n\x06states\x18\x08 \x03(\x0b\x32\x0c.PlayerState\x12\x0b\n\x03\x66\x31\x31\x18\x0b \x02(\x03\x12\x10\n\x08num_msgs\x18\x12 \x02(\x05\x12\x0e\n\x06msgnum\x18\x13 \x02(\x05\"8\n\x05Ghost\x12\x11\n\tplayer_id\x18\x01 \x02(\x05\x12\x1c\n\x06states\x18\x02 \x03(\x0b\x32\x0c.PlayerState\" \n\x06Ghosts\x12\x16\n\x06ghosts\x18\x01 \x03(\x0b\x32\x06.Ghost'
)




_PLAYERSTATE = _descriptor.Descriptor(
  name='PlayerState',
  full_name='PlayerState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PlayerState.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='worldTime', full_name='PlayerState.worldTime', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distance', full_name='PlayerState.distance', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roadTime', full_name='PlayerState.roadTime', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='laps', full_name='PlayerState.laps', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed', full_name='PlayerState.speed', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roadPosition', full_name='PlayerState.roadPosition', index=6,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cadenceUHz', full_name='PlayerState.cadenceUHz', index=7,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heartrate', full_name='PlayerState.heartrate', index=8,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='power', full_name='PlayerState.power', index=9,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heading', full_name='PlayerState.heading', index=10,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lean', full_name='PlayerState.lean', index=11,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='climbing', full_name='PlayerState.climbing', index=12,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='PlayerState.time', index=13,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f19', full_name='PlayerState.f19', index=14,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f20', full_name='PlayerState.f20', index=15,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='progress', full_name='PlayerState.progress', index=16,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='customisationId', full_name='PlayerState.customisationId', index=17,
      number=22, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='justWatching', full_name='PlayerState.justWatching', index=18,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='calories', full_name='PlayerState.calories', index=19,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='PlayerState.x', index=20,
      number=25, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='PlayerState.altitude', index=21,
      number=26, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='PlayerState.y', index=22,
      number=27, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='watchingRiderId', full_name='PlayerState.watchingRiderId', index=23,
      number=28, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='groupId', full_name='PlayerState.groupId', index=24,
      number=29, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sport', full_name='PlayerState.sport', index=25,
      number=31, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f34', full_name='PlayerState.f34', index=26,
      number=34, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=500,
)


_CLIENTTOSERVER = _descriptor.Descriptor(
  name='ClientToServer',
  full_name='ClientToServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connected', full_name='ClientToServer.connected', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='ClientToServer.player_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='world_time', full_name='ClientToServer.world_time', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seqno', full_name='ClientToServer.seqno', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='ClientToServer.state', index=4,
      number=7, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f8', full_name='ClientToServer.f8', index=5,
      number=8, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f9', full_name='ClientToServer.f9', index=6,
      number=9, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_update', full_name='ClientToServer.last_update', index=7,
      number=10, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f11', full_name='ClientToServer.f11', index=8,
      number=11, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_player_update', full_name='ClientToServer.last_player_update', index=9,
      number=12, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=707,
)


_SERVERTOCLIENT = _descriptor.Descriptor(
  name='ServerToClient',
  full_name='ServerToClient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='f1', full_name='ServerToClient.f1', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='ServerToClient.player_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='world_time', full_name='ServerToClient.world_time', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seqno', full_name='ServerToClient.seqno', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f5', full_name='ServerToClient.f5', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='states', full_name='ServerToClient.states', index=5,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f11', full_name='ServerToClient.f11', index=6,
      number=11, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_msgs', full_name='ServerToClient.num_msgs', index=7,
      number=18, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msgnum', full_name='ServerToClient.msgnum', index=8,
      number=19, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=710,
  serialized_end=881,
)


_GHOST = _descriptor.Descriptor(
  name='Ghost',
  full_name='Ghost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='Ghost.player_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='states', full_name='Ghost.states', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=883,
  serialized_end=939,
)


_GHOSTS = _descriptor.Descriptor(
  name='Ghosts',
  full_name='Ghosts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ghosts', full_name='Ghosts.ghosts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=941,
  serialized_end=973,
)

_CLIENTTOSERVER.fields_by_name['state'].message_type = _PLAYERSTATE
_SERVERTOCLIENT.fields_by_name['states'].message_type = _PLAYERSTATE
_GHOST.fields_by_name['states'].message_type = _PLAYERSTATE
_GHOSTS.fields_by_name['ghosts'].message_type = _GHOST
DESCRIPTOR.message_types_by_name['PlayerState'] = _PLAYERSTATE
DESCRIPTOR.message_types_by_name['ClientToServer'] = _CLIENTTOSERVER
DESCRIPTOR.message_types_by_name['ServerToClient'] = _SERVERTOCLIENT
DESCRIPTOR.message_types_by_name['Ghost'] = _GHOST
DESCRIPTOR.message_types_by_name['Ghosts'] = _GHOSTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerState = _reflection.GeneratedProtocolMessageType('PlayerState', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERSTATE,
  '__module__' : 'protobuf.udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:PlayerState)
  })
_sym_db.RegisterMessage(PlayerState)

ClientToServer = _reflection.GeneratedProtocolMessageType('ClientToServer', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTTOSERVER,
  '__module__' : 'protobuf.udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:ClientToServer)
  })
_sym_db.RegisterMessage(ClientToServer)

ServerToClient = _reflection.GeneratedProtocolMessageType('ServerToClient', (_message.Message,), {
  'DESCRIPTOR' : _SERVERTOCLIENT,
  '__module__' : 'protobuf.udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:ServerToClient)
  })
_sym_db.RegisterMessage(ServerToClient)

Ghost = _reflection.GeneratedProtocolMessageType('Ghost', (_message.Message,), {
  'DESCRIPTOR' : _GHOST,
  '__module__' : 'protobuf.udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:Ghost)
  })
_sym_db.RegisterMessage(Ghost)

Ghosts = _reflection.GeneratedProtocolMessageType('Ghosts', (_message.Message,), {
  'DESCRIPTOR' : _GHOSTS,
  '__module__' : 'protobuf.udp_node_msgs_pb2'
  # @@protoc_insertion_point(class_scope:Ghosts)
  })
_sym_db.RegisterMessage(Ghosts)


# @@protoc_insertion_point(module_scope)
