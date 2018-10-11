# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ServiceTopologyProperties(Model):
    """The properties of a service topology.

    :param artifact_source_id: The resource Id of the artifact source that
     contains the artifacts that can be referenced in the service units.
    :type artifact_source_id: str
    """

    _attribute_map = {
        'artifact_source_id': {'key': 'artifactSourceId', 'type': 'str'},
    }

    def __init__(self, *, artifact_source_id: str=None, **kwargs) -> None:
        super(ServiceTopologyProperties, self).__init__(**kwargs)
        self.artifact_source_id = artifact_source_id
