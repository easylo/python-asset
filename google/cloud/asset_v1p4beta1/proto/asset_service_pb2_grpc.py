# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.cloud.asset_v1p4beta1.proto import (
    asset_service_pb2 as google_dot_cloud_dot_asset__v1p4beta1_dot_proto_dot_asset__service__pb2,
)
from google.longrunning import (
    operations_pb2 as google_dot_longrunning_dot_operations__pb2,
)


class AssetServiceStub(object):
    """Asset service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AnalyzeIamPolicy = channel.unary_unary(
            "/google.cloud.asset.v1p4beta1.AssetService/AnalyzeIamPolicy",
            request_serializer=google_dot_cloud_dot_asset__v1p4beta1_dot_proto_dot_asset__service__pb2.AnalyzeIamPolicyRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_asset__v1p4beta1_dot_proto_dot_asset__service__pb2.AnalyzeIamPolicyResponse.FromString,
        )
        self.ExportIamPolicyAnalysis = channel.unary_unary(
            "/google.cloud.asset.v1p4beta1.AssetService/ExportIamPolicyAnalysis",
            request_serializer=google_dot_cloud_dot_asset__v1p4beta1_dot_proto_dot_asset__service__pb2.ExportIamPolicyAnalysisRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )


class AssetServiceServicer(object):
    """Asset service definition.
    """

    def AnalyzeIamPolicy(self, request, context):
        """Analyzes IAM policies based on the specified request. Returns
        a list of [IamPolicyAnalysisResult][google.cloud.asset.v1p4beta1.IamPolicyAnalysisResult] matching the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ExportIamPolicyAnalysis(self, request, context):
        """Exports IAM policy analysis based on the specified request. This API
        implements the [google.longrunning.Operation][google.longrunning.Operation] API allowing you to keep
        track of the export. The metadata contains the request to help callers to
        map responses to requests.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AssetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "AnalyzeIamPolicy": grpc.unary_unary_rpc_method_handler(
            servicer.AnalyzeIamPolicy,
            request_deserializer=google_dot_cloud_dot_asset__v1p4beta1_dot_proto_dot_asset__service__pb2.AnalyzeIamPolicyRequest.FromString,
            response_serializer=google_dot_cloud_dot_asset__v1p4beta1_dot_proto_dot_asset__service__pb2.AnalyzeIamPolicyResponse.SerializeToString,
        ),
        "ExportIamPolicyAnalysis": grpc.unary_unary_rpc_method_handler(
            servicer.ExportIamPolicyAnalysis,
            request_deserializer=google_dot_cloud_dot_asset__v1p4beta1_dot_proto_dot_asset__service__pb2.ExportIamPolicyAnalysisRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.asset.v1p4beta1.AssetService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class AssetService(object):
    """Asset service definition.
    """

    @staticmethod
    def AnalyzeIamPolicy(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.asset.v1p4beta1.AssetService/AnalyzeIamPolicy",
            google_dot_cloud_dot_asset__v1p4beta1_dot_proto_dot_asset__service__pb2.AnalyzeIamPolicyRequest.SerializeToString,
            google_dot_cloud_dot_asset__v1p4beta1_dot_proto_dot_asset__service__pb2.AnalyzeIamPolicyResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ExportIamPolicyAnalysis(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.cloud.asset.v1p4beta1.AssetService/ExportIamPolicyAnalysis",
            google_dot_cloud_dot_asset__v1p4beta1_dot_proto_dot_asset__service__pb2.ExportIamPolicyAnalysisRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
