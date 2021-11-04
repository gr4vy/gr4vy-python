"""
    Gr4vy API

    Welcome to the Gr4vy API reference documentation. Our API is still very much a work in product and subject to change.  # noqa: E501

    The version of the OpenAPI document: 1.1.0-beta
    Contact: code@gr4vy.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gr4vy_python.gr4vy_api.openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from gr4vy_python.gr4vy_api.openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from gr4vy_python.gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from gr4vy_python.gr4vy_api.openapi_client.model.error404_not_found import Error404NotFound
from gr4vy_python.gr4vy_api.openapi_client.model.payment_service_definition import PaymentServiceDefinition
from gr4vy_python.gr4vy_api.openapi_client.model.payment_service_definitions import PaymentServiceDefinitions


class PaymentServiceDefinitionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_payment_service_definition(
            self,
            payment_service_definition_id,
            **kwargs
        ):
            """Get payment service definition  # noqa: E501

            Gets the definition for a payment service.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_payment_service_definition(payment_service_definition_id, async_req=True)
            >>> result = thread.get()

            Args:
                payment_service_definition_id (str): The unique ID of the payment service definition.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PaymentServiceDefinition
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['payment_service_definition_id'] = \
                payment_service_definition_id
            return self.call_with_http_info(**kwargs)

        self.get_payment_service_definition = _Endpoint(
            settings={
                'response_type': (PaymentServiceDefinition,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/payment-service-definitions/{payment_service_definition_id}',
                'operation_id': 'get_payment_service_definition',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_service_definition_id',
                ],
                'required': [
                    'payment_service_definition_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'payment_service_definition_id':
                        (str,),
                },
                'attribute_map': {
                    'payment_service_definition_id': 'payment_service_definition_id',
                },
                'location_map': {
                    'payment_service_definition_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_payment_service_definition
        )

        def __list_payment_service_definitions(
            self,
            **kwargs
        ):
            """List payment service definitions  # noqa: E501

            Returns a list of all available payment service definitions.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_payment_service_definitions(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                limit (int): Defines the maximum number of items to return for this request.. [optional] if omitted the server will use the default value of 20
                cursor (str): A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PaymentServiceDefinitions
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.list_payment_service_definitions = _Endpoint(
            settings={
                'response_type': (PaymentServiceDefinitions,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/payment-service-definitions',
                'operation_id': 'list_payment_service_definitions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'limit',
                    'cursor',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'limit':
                        (int,),
                    'cursor':
                        (str,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'cursor': 'cursor',
                },
                'location_map': {
                    'limit': 'query',
                    'cursor': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_payment_service_definitions
        )
