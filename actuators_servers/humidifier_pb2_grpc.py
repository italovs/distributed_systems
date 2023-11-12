# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import humidifier_pb2 as humidifier__pb2


class HumidifierStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.turnOn = channel.unary_unary(
                '/Humidifier/turnOn',
                request_serializer=humidifier__pb2.HumidifierStatus.SerializeToString,
                response_deserializer=humidifier__pb2.HumidifierStatus.FromString,
                )
        self.turnOff = channel.unary_unary(
                '/Humidifier/turnOff',
                request_serializer=humidifier__pb2.HumidifierStatus.SerializeToString,
                response_deserializer=humidifier__pb2.HumidifierStatus.FromString,
                )
        self.requestInfo = channel.unary_unary(
                '/Humidifier/requestInfo',
                request_serializer=humidifier__pb2.HumidifierInfoParams.SerializeToString,
                response_deserializer=humidifier__pb2.HumidifierStatus.FromString,
                )


class HumidifierServicer(object):
    """Missing associated documentation comment in .proto file."""

    def turnOn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def turnOff(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def requestInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HumidifierServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'turnOn': grpc.unary_unary_rpc_method_handler(
                    servicer.turnOn,
                    request_deserializer=humidifier__pb2.HumidifierStatus.FromString,
                    response_serializer=humidifier__pb2.HumidifierStatus.SerializeToString,
            ),
            'turnOff': grpc.unary_unary_rpc_method_handler(
                    servicer.turnOff,
                    request_deserializer=humidifier__pb2.HumidifierStatus.FromString,
                    response_serializer=humidifier__pb2.HumidifierStatus.SerializeToString,
            ),
            'requestInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.requestInfo,
                    request_deserializer=humidifier__pb2.HumidifierInfoParams.FromString,
                    response_serializer=humidifier__pb2.HumidifierStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Humidifier', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Humidifier(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def turnOn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Humidifier/turnOn',
            humidifier__pb2.HumidifierStatus.SerializeToString,
            humidifier__pb2.HumidifierStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def turnOff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Humidifier/turnOff',
            humidifier__pb2.HumidifierStatus.SerializeToString,
            humidifier__pb2.HumidifierStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def requestInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Humidifier/requestInfo',
            humidifier__pb2.HumidifierInfoParams.SerializeToString,
            humidifier__pb2.HumidifierStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
