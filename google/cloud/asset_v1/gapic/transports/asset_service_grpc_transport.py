# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import google.api_core.grpc_helpers
import google.api_core.operations_v1

from google.cloud.asset_v1.proto import asset_service_pb2_grpc


class AssetServiceGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.asset.v1 AssetService API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self, channel=None, credentials=None, address="cloudasset.googleapis.com:443"
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive.",
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            "asset_service_stub": asset_service_pb2_grpc.AssetServiceStub(channel),
        }

        # Because this API includes a method that returns a
        # long-running operation (proto: google.longrunning.Operation),
        # instantiate an LRO client.
        self._operations_client = google.api_core.operations_v1.OperationsClient(
            channel
        )

    @classmethod
    def create_channel(
        cls, address="cloudasset.googleapis.com:443", credentials=None, **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def export_assets(self):
        """Return the gRPC stub for :meth:`AssetServiceClient.export_assets`.

        Exports assets with time and resource types to a given Cloud Storage
        location/BigQuery table. For Cloud Storage location destinations, the
        output format is newline-delimited JSON. Each line represents a
        ``google.cloud.asset.v1.Asset`` in the JSON format; for BigQuery table
        destinations, the output table stores the fields in asset proto as
        columns. This API implements the ``google.longrunning.Operation`` API ,
        which allows you to keep track of the export. We recommend intervals of
        at least 2 seconds with exponential retry to poll the export operation
        result. For regular-size resource parent, the export operation usually
        finishes within 5 minutes.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["asset_service_stub"].ExportAssets

    @property
    def batch_get_assets_history(self):
        """Return the gRPC stub for :meth:`AssetServiceClient.batch_get_assets_history`.

        Batch gets the update history of assets that overlap a time window.
        For IAM_POLICY content, this API outputs history when the asset and its
        attached IAM POLICY both exist. This can create gaps in the output
        history. Otherwise, this API outputs history with asset in both
        non-delete or deleted status. If a specified asset does not exist, this
        API returns an INVALID_ARGUMENT error.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["asset_service_stub"].BatchGetAssetsHistory

    @property
    def create_feed(self):
        """Return the gRPC stub for :meth:`AssetServiceClient.create_feed`.

        Creates a feed in a parent project/folder/organization to listen to its
        asset updates.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["asset_service_stub"].CreateFeed

    @property
    def get_feed(self):
        """Return the gRPC stub for :meth:`AssetServiceClient.get_feed`.

        Gets details about an asset feed.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["asset_service_stub"].GetFeed

    @property
    def list_feeds(self):
        """Return the gRPC stub for :meth:`AssetServiceClient.list_feeds`.

        Lists all asset feeds in a parent project/folder/organization.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["asset_service_stub"].ListFeeds

    @property
    def update_feed(self):
        """Return the gRPC stub for :meth:`AssetServiceClient.update_feed`.

        Updates an asset feed configuration.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["asset_service_stub"].UpdateFeed

    @property
    def delete_feed(self):
        """Return the gRPC stub for :meth:`AssetServiceClient.delete_feed`.

        Deletes an asset feed.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["asset_service_stub"].DeleteFeed

    @property
    def search_all_resources(self):
        """Return the gRPC stub for :meth:`AssetServiceClient.search_all_resources`.

        Searches all the resources within the given accessible scope (e.g., a
        project, a folder or an organization). Callers should have
        cloud.assets.SearchAllResources permission upon the requested scope,
        otherwise the request will be rejected.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["asset_service_stub"].SearchAllResources

    @property
    def search_all_iam_policies(self):
        """Return the gRPC stub for :meth:`AssetServiceClient.search_all_iam_policies`.

        Searches all the IAM policies within the given accessible scope (e.g., a
        project, a folder or an organization). Callers should have
        cloud.assets.SearchAllIamPolicies permission upon the requested scope,
        otherwise the request will be rejected.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["asset_service_stub"].SearchAllIamPolicies
