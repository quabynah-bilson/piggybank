# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import auth_pb2 as auth__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


class AuthServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.login = channel.unary_unary(
                '/auth.AuthService/login',
                request_serializer=auth__pb2.LoginRequest.SerializeToString,
                response_deserializer=auth__pb2.Account.FromString,
                )
        self.create_account = channel.unary_unary(
                '/auth.AuthService/create_account',
                request_serializer=auth__pb2.CreateAccountRequest.SerializeToString,
                response_deserializer=auth__pb2.Account.FromString,
                )
        self.reset_password = channel.unary_unary(
                '/auth.AuthService/reset_password',
                request_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                )
        self.send_otp = channel.unary_unary(
                '/auth.AuthService/send_otp',
                request_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                )
        self.verify_otp = channel.unary_unary(
                '/auth.AuthService/verify_otp',
                request_serializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                )
        self.update_password = channel.unary_unary(
                '/auth.AuthService/update_password',
                request_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                )
        self.logout = channel.unary_unary(
                '/auth.AuthService/logout',
                request_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.verify_token = channel.unary_unary(
                '/auth.AuthService/verify_token',
                request_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.FromString,
                )


class AuthServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def create_account(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def reset_password(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def send_otp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def verify_otp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update_password(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def logout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def verify_token(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'login': grpc.unary_unary_rpc_method_handler(
                    servicer.login,
                    request_deserializer=auth__pb2.LoginRequest.FromString,
                    response_serializer=auth__pb2.Account.SerializeToString,
            ),
            'create_account': grpc.unary_unary_rpc_method_handler(
                    servicer.create_account,
                    request_deserializer=auth__pb2.CreateAccountRequest.FromString,
                    response_serializer=auth__pb2.Account.SerializeToString,
            ),
            'reset_password': grpc.unary_unary_rpc_method_handler(
                    servicer.reset_password,
                    request_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                    response_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            ),
            'send_otp': grpc.unary_unary_rpc_method_handler(
                    servicer.send_otp,
                    request_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                    response_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            ),
            'verify_otp': grpc.unary_unary_rpc_method_handler(
                    servicer.verify_otp,
                    request_deserializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.FromString,
                    response_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            ),
            'update_password': grpc.unary_unary_rpc_method_handler(
                    servicer.update_password,
                    request_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                    response_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            ),
            'logout': grpc.unary_unary_rpc_method_handler(
                    servicer.logout,
                    request_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'verify_token': grpc.unary_unary_rpc_method_handler(
                    servicer.verify_token,
                    request_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                    response_serializer=google_dot_protobuf_dot_wrappers__pb2.BoolValue.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth.AuthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.AuthService/login',
            auth__pb2.LoginRequest.SerializeToString,
            auth__pb2.Account.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def create_account(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.AuthService/create_account',
            auth__pb2.CreateAccountRequest.SerializeToString,
            auth__pb2.Account.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def reset_password(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.AuthService/reset_password',
            google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def send_otp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.AuthService/send_otp',
            google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def verify_otp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.AuthService/verify_otp',
            google_dot_protobuf_dot_wrappers__pb2.Int32Value.SerializeToString,
            google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update_password(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.AuthService/update_password',
            google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def logout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.AuthService/logout',
            google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def verify_token(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.AuthService/verify_token',
            google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            google_dot_protobuf_dot_wrappers__pb2.BoolValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)