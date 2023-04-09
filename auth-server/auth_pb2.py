# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='auth.proto',
  package='auth',
  syntax='proto3',
  serialized_options=b'\n\025io.qcodelabsllc.qiggyB\020QiggyAuthServiceP\001Z com.github/qcodelabsllc/qiggy;ms',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nauth.proto\x12\x04\x61uth\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"N\n\x0c\x41uthResponse\x12\x1e\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\r.auth.Account\x12\x1e\n\x07session\x18\x02 \x01(\x0b\x32\r.auth.Session\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"f\n\x14\x43reateAccountRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x14\n\x0cphone_number\x18\x04 \x01(\t\"Y\n\x07\x41\x63\x63ount\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x14\n\x0cphone_number\x18\x04 \x01(\t\"\xf1\x01\n\x07Session\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x37\n\x13\x61\x63\x63\x65ss_token_expiry\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x14refresh_token_expiry\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nsession_id\x18\x05 \x01(\t\x12\x32\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02(\x01\x32\xf6\x04\n\x0b\x41uthService\x12/\n\x05login\x12\x12.auth.LoginRequest\x1a\x12.auth.AuthResponse\x12@\n\x0e\x63reate_account\x12\x1a.auth.CreateAccountRequest\x1a\x12.auth.AuthResponse\x12L\n\x0ereset_password\x12\x1c.google.protobuf.StringValue\x1a\x1c.google.protobuf.StringValue\x12\x46\n\x08send_otp\x12\x1c.google.protobuf.StringValue\x1a\x1c.google.protobuf.StringValue\x12G\n\nverify_otp\x12\x1b.google.protobuf.Int32Value\x1a\x1c.google.protobuf.StringValue\x12M\n\x0fupdate_password\x12\x1c.google.protobuf.StringValue\x1a\x1c.google.protobuf.StringValue\x12>\n\x06logout\x12\x1c.google.protobuf.StringValue\x1a\x16.google.protobuf.Empty\x12<\n\rrefresh_token\x12\x1c.google.protobuf.StringValue\x1a\r.auth.Session\x12H\n\x0cverify_token\x12\x1c.google.protobuf.StringValue\x1a\x1a.google.protobuf.BoolValueBM\n\x15io.qcodelabsllc.qiggyB\x10QiggyAuthServiceP\x01Z com.github/qcodelabsllc/qiggy;msb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_AUTHRESPONSE = _descriptor.Descriptor(
  name='AuthResponse',
  full_name='auth.AuthResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='auth.AuthResponse.account', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session', full_name='auth.AuthResponse.session', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=192,
)


_LOGINREQUEST = _descriptor.Descriptor(
  name='LoginRequest',
  full_name='auth.LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='auth.LoginRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='auth.LoginRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=244,
)


_CREATEACCOUNTREQUEST = _descriptor.Descriptor(
  name='CreateAccountRequest',
  full_name='auth.CreateAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='auth.CreateAccountRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='auth.CreateAccountRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='auth.CreateAccountRequest.display_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='auth.CreateAccountRequest.phone_number', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=246,
  serialized_end=348,
)


_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='auth.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='auth.Account.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='auth.Account.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='auth.Account.display_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='auth.Account.phone_number', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=439,
)


_SESSION = _descriptor.Descriptor(
  name='Session',
  full_name='auth.Session',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='auth.Session.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='refresh_token', full_name='auth.Session.refresh_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_token_expiry', full_name='auth.Session.access_token_expiry', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='refresh_token_expiry', full_name='auth.Session.refresh_token_expiry', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='auth.Session.session_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='auth.Session.created_at', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=442,
  serialized_end=683,
)

_AUTHRESPONSE.fields_by_name['account'].message_type = _ACCOUNT
_AUTHRESPONSE.fields_by_name['session'].message_type = _SESSION
_SESSION.fields_by_name['access_token_expiry'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SESSION.fields_by_name['refresh_token_expiry'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SESSION.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['AuthResponse'] = _AUTHRESPONSE
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['CreateAccountRequest'] = _CREATEACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['Session'] = _SESSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthResponse = _reflection.GeneratedProtocolMessageType('AuthResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUTHRESPONSE,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.AuthResponse)
  })
_sym_db.RegisterMessage(AuthResponse)

LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.LoginRequest)
  })
_sym_db.RegisterMessage(LoginRequest)

CreateAccountRequest = _reflection.GeneratedProtocolMessageType('CreateAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEACCOUNTREQUEST,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.CreateAccountRequest)
  })
_sym_db.RegisterMessage(CreateAccountRequest)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.Account)
  })
_sym_db.RegisterMessage(Account)

Session = _reflection.GeneratedProtocolMessageType('Session', (_message.Message,), {
  'DESCRIPTOR' : _SESSION,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.Session)
  })
_sym_db.RegisterMessage(Session)


DESCRIPTOR._options = None
_SESSION.fields_by_name['created_at']._options = None

_AUTHSERVICE = _descriptor.ServiceDescriptor(
  name='AuthService',
  full_name='auth.AuthService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=686,
  serialized_end=1316,
  methods=[
  _descriptor.MethodDescriptor(
    name='login',
    full_name='auth.AuthService.login',
    index=0,
    containing_service=None,
    input_type=_LOGINREQUEST,
    output_type=_AUTHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='create_account',
    full_name='auth.AuthService.create_account',
    index=1,
    containing_service=None,
    input_type=_CREATEACCOUNTREQUEST,
    output_type=_AUTHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='reset_password',
    full_name='auth.AuthService.reset_password',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE,
    output_type=google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='send_otp',
    full_name='auth.AuthService.send_otp',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE,
    output_type=google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='verify_otp',
    full_name='auth.AuthService.verify_otp',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_wrappers__pb2._INT32VALUE,
    output_type=google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update_password',
    full_name='auth.AuthService.update_password',
    index=5,
    containing_service=None,
    input_type=google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE,
    output_type=google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='logout',
    full_name='auth.AuthService.logout',
    index=6,
    containing_service=None,
    input_type=google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='refresh_token',
    full_name='auth.AuthService.refresh_token',
    index=7,
    containing_service=None,
    input_type=google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE,
    output_type=_SESSION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='verify_token',
    full_name='auth.AuthService.verify_token',
    index=8,
    containing_service=None,
    input_type=google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE,
    output_type=google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTHSERVICE)

DESCRIPTOR.services_by_name['AuthService'] = _AUTHSERVICE

# @@protoc_insertion_point(module_scope)
