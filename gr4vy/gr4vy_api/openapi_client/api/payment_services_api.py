"""
    Gr4vy API

    Welcome to the Gr4vy API reference documentation. Our API is still very much a work in product and subject to change.  # noqa: E501

    The version of the OpenAPI document: 1.1.0-beta
    Contact: code@gr4vy.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gr4vy.gr4vy_api.openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from gr4vy.gr4vy_api.openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from gr4vy.gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from gr4vy.gr4vy_api.openapi_client.model.error404_not_found import Error404NotFound
from gr4vy.gr4vy_api.openapi_client.model.error_generic import ErrorGeneric
from gr4vy.gr4vy_api.openapi_client.model.payment_service import PaymentService
from gr4vy.gr4vy_api.openapi_client.model.payment_service_request import PaymentServiceRequest
from gr4vy.gr4vy_api.openapi_client.model.payment_service_update import PaymentServiceUpdate
from gr4vy.gr4vy_api.openapi_client.model.payment_services import PaymentServices


class PaymentServicesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __add_payment_service(
            self,
            **kwargs
        ):
            """New payment service  # noqa: E501

            Adds a new payment service by providing a custom name and a value for each of the required fields.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.add_payment_service(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                payment_service_request (PaymentServiceRequest): [optional]
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
                PaymentService
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

        self.add_payment_service = _Endpoint(
            settings={
                'response_type': (PaymentService,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/payment-services',
                'operation_id': 'add_payment_service',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_service_request',
                ],
                'required': [],
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
                    'payment_service_request':
                        (PaymentServiceRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'payment_service_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__add_payment_service
        )

        def __delete_payment_service(
            self,
            payment_service_id,
            **kwargs
        ):
            """Delete payment service  # noqa: E501

            Deletes a specific active payment service.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_payment_service(payment_service_id, async_req=True)
            >>> result = thread.get()

            Args:
                payment_service_id (str): The ID of the payment service.

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
                None
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
            kwargs['payment_service_id'] = \
                payment_service_id
            return self.call_with_http_info(**kwargs)

        self.delete_payment_service = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/payment-services/{payment_service_id}',
                'operation_id': 'delete_payment_service',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_service_id',
                ],
                'required': [
                    'payment_service_id',
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
                    'payment_service_id':
                        (str,),
                },
                'attribute_map': {
                    'payment_service_id': 'payment_service_id',
                },
                'location_map': {
                    'payment_service_id': 'path',
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
            callable=__delete_payment_service
        )

        def __get_payment_service(
            self,
            payment_service_id,
            **kwargs
        ):
            """Get payment service  # noqa: E501

            Retrieves the details of a single configured payment service.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_payment_service(payment_service_id, async_req=True)
            >>> result = thread.get()

            Args:
                payment_service_id (str): The ID of the payment service.

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
                PaymentService
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
            kwargs['payment_service_id'] = \
                payment_service_id
            return self.call_with_http_info(**kwargs)

        self.get_payment_service = _Endpoint(
            settings={
                'response_type': (PaymentService,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/payment-services/{payment_service_id}',
                'operation_id': 'get_payment_service',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_service_id',
                ],
                'required': [
                    'payment_service_id',
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
                    'payment_service_id':
                        (str,),
                },
                'attribute_map': {
                    'payment_service_id': 'payment_service_id',
                },
                'location_map': {
                    'payment_service_id': 'path',
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
            callable=__get_payment_service
        )

        def __list_payment_services(
            self,
            **kwargs
        ):
            """List payment services  # noqa: E501

            Lists the currently configured and activated payment services.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_payment_services(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                limit (int): Defines the maximum number of items to return for this request.. [optional] if omitted the server will use the default value of 20
                cursor (str): A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list.. [optional]
                method (str): Filters the results to only the items for which the `method` has been set to this value.. [optional]
                environment (str): Filters the results to only the items available in this environment.. [optional] if omitted the server will use the default value of "production"
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
                PaymentServices
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

        self.list_payment_services = _Endpoint(
            settings={
                'response_type': (PaymentServices,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/payment-services',
                'operation_id': 'list_payment_services',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'limit',
                    'cursor',
                    'method',
                    'environment',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'method',
                    'environment',
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
                    ('method',): {

                        "CARD": "card",
                        "PAYPAL": "paypal",
                        "BANKED": "banked",
                        "GOCARDLESS": "gocardless",
                        "STRIPEDD": "stripedd",
                        "APPLEPAY": "applepay"
                    },
                    ('environment',): {

                        "DEVELOPMENT": "development",
                        "STAGING": "staging",
                        "PRODUCTION": "production"
                    },
                },
                'openapi_types': {
                    'limit':
                        (int,),
                    'cursor':
                        (str,),
                    'method':
                        (str,),
                    'environment':
                        (str,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'cursor': 'cursor',
                    'method': 'method',
                    'environment': 'environment',
                },
                'location_map': {
                    'limit': 'query',
                    'cursor': 'query',
                    'method': 'query',
                    'environment': 'query',
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
            callable=__list_payment_services
        )

        def __update_payment_service(
            self,
            payment_service_id,
            **kwargs
        ):
            """Update payment service  # noqa: E501

            Updates an existing payment service. Allows all fields to be changed except for the service ID.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_payment_service(payment_service_id, async_req=True)
            >>> result = thread.get()

            Args:
                payment_service_id (str): The ID of the payment service.

            Keyword Args:
                payment_service_update (PaymentServiceUpdate): [optional]
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
                PaymentService
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
            kwargs['payment_service_id'] = \
                payment_service_id
            return self.call_with_http_info(**kwargs)

        self.update_payment_service = _Endpoint(
            settings={
                'response_type': (PaymentService,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/payment-services/{payment_service_id}',
                'operation_id': 'update_payment_service',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_service_id',
                    'payment_service_update',
                ],
                'required': [
                    'payment_service_id',
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
                    'payment_service_id':
                        (str,),
                    'payment_service_update':
                        (PaymentServiceUpdate,),
                },
                'attribute_map': {
                    'payment_service_id': 'payment_service_id',
                },
                'location_map': {
                    'payment_service_id': 'path',
                    'payment_service_update': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_payment_service
        )
