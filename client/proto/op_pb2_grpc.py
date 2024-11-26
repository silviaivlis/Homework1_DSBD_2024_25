# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import op_pb2 as op__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in op_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class User_serviceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterUser = channel.unary_unary(
                '/User_service/RegisterUser',
                request_serializer=op__pb2.RegUserRequest.SerializeToString,
                response_deserializer=op__pb2.RegUserResponse.FromString,
                _registered_method=True)
        self.UpdateUser = channel.unary_unary(
                '/User_service/UpdateUser',
                request_serializer=op__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=op__pb2.UpdateUserResponse.FromString,
                _registered_method=True)
        self.DeleteUser = channel.unary_unary(
                '/User_service/DeleteUser',
                request_serializer=op__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=op__pb2.DeleteUserResponse.FromString,
                _registered_method=True)
        self.GetLatestValue = channel.unary_unary(
                '/User_service/GetLatestValue',
                request_serializer=op__pb2.GetLatestValueRequest.SerializeToString,
                response_deserializer=op__pb2.GetLatestValueResponse.FromString,
                _registered_method=True)
        self.CalcAvarageValue = channel.unary_unary(
                '/User_service/CalcAvarageValue',
                request_serializer=op__pb2.CalcAvarageValueRequest.SerializeToString,
                response_deserializer=op__pb2.CalcAvarageValueResponse.FromString,
                _registered_method=True)


class User_serviceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterUser(self, request, context):
        """Funzionalità di gestione degli utenti
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLatestValue(self, request, context):
        """Funzionalità di recupero delle informazioni
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CalcAvarageValue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_User_serviceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterUser': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterUser,
                    request_deserializer=op__pb2.RegUserRequest.FromString,
                    response_serializer=op__pb2.RegUserResponse.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=op__pb2.UpdateUserRequest.FromString,
                    response_serializer=op__pb2.UpdateUserResponse.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=op__pb2.DeleteUserRequest.FromString,
                    response_serializer=op__pb2.DeleteUserResponse.SerializeToString,
            ),
            'GetLatestValue': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLatestValue,
                    request_deserializer=op__pb2.GetLatestValueRequest.FromString,
                    response_serializer=op__pb2.GetLatestValueResponse.SerializeToString,
            ),
            'CalcAvarageValue': grpc.unary_unary_rpc_method_handler(
                    servicer.CalcAvarageValue,
                    request_deserializer=op__pb2.CalcAvarageValueRequest.FromString,
                    response_serializer=op__pb2.CalcAvarageValueResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'User_service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('User_service', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class User_service(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User_service/RegisterUser',
            op__pb2.RegUserRequest.SerializeToString,
            op__pb2.RegUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User_service/UpdateUser',
            op__pb2.UpdateUserRequest.SerializeToString,
            op__pb2.UpdateUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User_service/DeleteUser',
            op__pb2.DeleteUserRequest.SerializeToString,
            op__pb2.DeleteUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetLatestValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User_service/GetLatestValue',
            op__pb2.GetLatestValueRequest.SerializeToString,
            op__pb2.GetLatestValueResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CalcAvarageValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/User_service/CalcAvarageValue',
            op__pb2.CalcAvarageValueRequest.SerializeToString,
            op__pb2.CalcAvarageValueResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
