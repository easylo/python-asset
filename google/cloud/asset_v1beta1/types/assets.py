# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.iam.v1 import policy_pb2 as policy  # type: ignore
from google.protobuf import struct_pb2 as struct  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.asset.v1beta1",
    manifest={"TemporalAsset", "TimeWindow", "Asset", "Resource",},
)


class TemporalAsset(proto.Message):
    r"""Temporal asset. In addition to the asset, the temporal asset
    includes the status of the asset and valid from and to time of
    it.

    Attributes:
        window (~.assets.TimeWindow):
            The time window when the asset data and state
            was observed.
        deleted (bool):
            If the asset is deleted or not.
        asset (~.assets.Asset):
            Asset.
    """

    window = proto.Field(proto.MESSAGE, number=1, message="TimeWindow",)

    deleted = proto.Field(proto.BOOL, number=2)

    asset = proto.Field(proto.MESSAGE, number=3, message="Asset",)


class TimeWindow(proto.Message):
    r"""A time window of (start_time, end_time].

    Attributes:
        start_time (~.timestamp.Timestamp):
            Start time of the time window (exclusive).
        end_time (~.timestamp.Timestamp):
            End time of the time window (inclusive).
            Current timestamp if not specified.
    """

    start_time = proto.Field(proto.MESSAGE, number=1, message=timestamp.Timestamp,)

    end_time = proto.Field(proto.MESSAGE, number=2, message=timestamp.Timestamp,)


class Asset(proto.Message):
    r"""Cloud asset. This includes all Google Cloud Platform
    resources, Cloud IAM policies, and other non-GCP assets.

    Attributes:
        name (str):
            The full name of the asset. For example:
            ``//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1``.
            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__
            for more information.
        asset_type (str):
            Type of the asset. Example:
            "google.compute.Disk".
        resource (~.assets.Resource):
            Representation of the resource.
        iam_policy (~.policy.Policy):
            Representation of the actual Cloud IAM policy
            set on a cloud resource. For each resource,
            there must be at most one Cloud IAM policy set
            on it.
    """

    name = proto.Field(proto.STRING, number=1)

    asset_type = proto.Field(proto.STRING, number=2)

    resource = proto.Field(proto.MESSAGE, number=3, message="Resource",)

    iam_policy = proto.Field(proto.MESSAGE, number=4, message=policy.Policy,)


class Resource(proto.Message):
    r"""Representation of a cloud resource.

    Attributes:
        version (str):
            The API version. Example: "v1".
        discovery_document_uri (str):
            The URL of the discovery document containing the resource's
            JSON schema. For example:
            ``"https://www.googleapis.com/discovery/v1/apis/compute/v1/rest"``.
            It will be left unspecified for resources without a
            discovery-based API, such as Cloud Bigtable.
        discovery_name (str):
            The JSON schema name listed in the discovery
            document. Example: "Project". It will be left
            unspecified for resources (such as Cloud
            Bigtable) without a discovery-based API.
        resource_url (str):
            The REST URL for accessing the resource. An HTTP GET
            operation using this URL returns the resource itself.
            Example:
            ``https://cloudresourcemanager.googleapis.com/v1/projects/my-project-123``.
            It will be left unspecified for resources without a REST
            API.
        parent (str):
            The full name of the immediate parent of this resource. See
            `Resource
            Names <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__
            for more information.

            For GCP assets, it is the parent resource defined in the
            `Cloud IAM policy
            hierarchy <https://cloud.google.com/iam/docs/overview#policy_hierarchy>`__.
            For example:
            ``"//cloudresourcemanager.googleapis.com/projects/my_project_123"``.

            For third-party assets, it is up to the users to define.
        data (~.struct.Struct):
            The content of the resource, in which some
            sensitive fields are scrubbed away and may not
            be present.
    """

    version = proto.Field(proto.STRING, number=1)

    discovery_document_uri = proto.Field(proto.STRING, number=2)

    discovery_name = proto.Field(proto.STRING, number=3)

    resource_url = proto.Field(proto.STRING, number=4)

    parent = proto.Field(proto.STRING, number=5)

    data = proto.Field(proto.MESSAGE, number=6, message=struct.Struct,)


__all__ = tuple(sorted(__protobuf__.manifest))