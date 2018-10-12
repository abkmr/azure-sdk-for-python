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

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling

from .. import models


class ServicesOperations(object):
    """ServicesOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version to use for each request. The current version is 2015-08-19. Constant value: "2015-08-19".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2015-08-19"

        self.config = config


    def _create_or_update_initial(
            self, resource_group_name, search_service_name, service, search_management_request_options=None, custom_headers=None, raw=False, **operation_config):
        client_request_id = None
        if search_management_request_options is not None:
            client_request_id = search_management_request_options.client_request_id

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'searchServiceName': self._serialize.url("search_service_name", search_service_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')

        # Construct body
        body_content = self._serialize.body(service, 'SearchService')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SearchService', response)
        if response.status_code == 201:
            deserialized = self._deserialize('SearchService', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create_or_update(
            self, resource_group_name, search_service_name, service, search_management_request_options=None, custom_headers=None, raw=False, polling=True, **operation_config):
        """Creates or updates a Search service in the given resource group. If the
        Search service already exists, all properties will be updated with the
        given values.

        :param resource_group_name: The name of the resource group within the
         current subscription. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param search_service_name: The name of the Azure Search service to
         create or update. Search service names must only contain lowercase
         letters, digits or dashes, cannot use dash as the first two or last
         one characters, cannot contain consecutive dashes, and must be between
         2 and 60 characters in length. Search service names must be globally
         unique since they are part of the service URI
         (https://<name>.search.windows.net). You cannot change the service
         name after the service is created.
        :type search_service_name: str
        :param service: The definition of the Search service to create or
         update.
        :type service: ~azure.mgmt.search.models.SearchService
        :param search_management_request_options: Additional parameters for
         the operation
        :type search_management_request_options:
         ~azure.mgmt.search.models.SearchManagementRequestOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns SearchService or
         ClientRawResponse<SearchService> if raw==True
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~azure.mgmt.search.models.SearchService]
         or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[~azure.mgmt.search.models.SearchService]]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = self._create_or_update_initial(
            resource_group_name=resource_group_name,
            search_service_name=search_service_name,
            service=service,
            search_management_request_options=search_management_request_options,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('SearchService', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}'}

    def update(
            self, resource_group_name, search_service_name, service, search_management_request_options=None, custom_headers=None, raw=False, **operation_config):
        """Updates an existing Search service in the given resource group.

        :param resource_group_name: The name of the resource group within the
         current subscription. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param search_service_name: The name of the Azure Search service to
         update.
        :type search_service_name: str
        :param service: The definition of the Search service to update.
        :type service: ~azure.mgmt.search.models.SearchService
        :param search_management_request_options: Additional parameters for
         the operation
        :type search_management_request_options:
         ~azure.mgmt.search.models.SearchManagementRequestOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SearchService or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.search.models.SearchService or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        client_request_id = None
        if search_management_request_options is not None:
            client_request_id = search_management_request_options.client_request_id

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'searchServiceName': self._serialize.url("search_service_name", search_service_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')

        # Construct body
        body_content = self._serialize.body(service, 'SearchService')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SearchService', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}'}

    def get(
            self, resource_group_name, search_service_name, search_management_request_options=None, custom_headers=None, raw=False, **operation_config):
        """Gets the Search service with the given name in the given resource
        group.

        :param resource_group_name: The name of the resource group within the
         current subscription. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param search_service_name: The name of the Azure Search service
         associated with the specified resource group.
        :type search_service_name: str
        :param search_management_request_options: Additional parameters for
         the operation
        :type search_management_request_options:
         ~azure.mgmt.search.models.SearchManagementRequestOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SearchService or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.search.models.SearchService or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        client_request_id = None
        if search_management_request_options is not None:
            client_request_id = search_management_request_options.client_request_id

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'searchServiceName': self._serialize.url("search_service_name", search_service_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SearchService', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}'}

    def delete(
            self, resource_group_name, search_service_name, search_management_request_options=None, custom_headers=None, raw=False, **operation_config):
        """Deletes a Search service in the given resource group, along with its
        associated resources.

        :param resource_group_name: The name of the resource group within the
         current subscription. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param search_service_name: The name of the Azure Search service
         associated with the specified resource group.
        :type search_service_name: str
        :param search_management_request_options: Additional parameters for
         the operation
        :type search_management_request_options:
         ~azure.mgmt.search.models.SearchManagementRequestOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        client_request_id = None
        if search_management_request_options is not None:
            client_request_id = search_management_request_options.client_request_id

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'searchServiceName': self._serialize.url("search_service_name", search_service_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 204, 404]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}'}

    def list_by_resource_group(
            self, resource_group_name, search_management_request_options=None, custom_headers=None, raw=False, **operation_config):
        """Gets a list of all Search services in the given resource group.

        :param resource_group_name: The name of the resource group within the
         current subscription. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param search_management_request_options: Additional parameters for
         the operation
        :type search_management_request_options:
         ~azure.mgmt.search.models.SearchManagementRequestOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of SearchService
        :rtype:
         ~azure.mgmt.search.models.SearchServicePaged[~azure.mgmt.search.models.SearchService]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        client_request_id = None
        if search_management_request_options is not None:
            client_request_id = search_management_request_options.client_request_id

        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
            if client_request_id is not None:
                header_parameters['x-ms-client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.SearchServicePaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.SearchServicePaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices'}

    def check_name_availability(
            self, name, search_management_request_options=None, custom_headers=None, raw=False, **operation_config):
        """Checks whether or not the given Search service name is available for
        use. Search service names must be globally unique since they are part
        of the service URI (https://<name>.search.windows.net).

        :param name: The Search service name to validate. Search service names
         must only contain lowercase letters, digits or dashes, cannot use dash
         as the first two or last one characters, cannot contain consecutive
         dashes, and must be between 2 and 60 characters in length.
        :type name: str
        :param search_management_request_options: Additional parameters for
         the operation
        :type search_management_request_options:
         ~azure.mgmt.search.models.SearchManagementRequestOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CheckNameAvailabilityOutput or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.search.models.CheckNameAvailabilityOutput or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        client_request_id = None
        if search_management_request_options is not None:
            client_request_id = search_management_request_options.client_request_id
        check_name_availability_input = models.CheckNameAvailabilityInput(name=name)

        # Construct URL
        url = self.check_name_availability.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')

        # Construct body
        body_content = self._serialize.body(check_name_availability_input, 'CheckNameAvailabilityInput')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CheckNameAvailabilityOutput', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    check_name_availability.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Search/checkNameAvailability'}
