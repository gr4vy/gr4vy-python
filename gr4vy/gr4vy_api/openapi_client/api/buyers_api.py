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
from gr4vy.gr4vy_api.openapi_client.model.buyer import Buyer
from gr4vy.gr4vy_api.openapi_client.model.buyer_request import BuyerRequest
from gr4vy.gr4vy_api.openapi_client.model.buyer_update import BuyerUpdate
from gr4vy.gr4vy_api.openapi_client.model.buyers import Buyers
from gr4vy.gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from gr4vy.gr4vy_api.openapi_client.model.error404_not_found import Error404NotFound
from gr4vy.gr4vy_api.openapi_client.model.error409_duplicate_record import Error409DuplicateRecord
from gr4vy.gr4vy_api.openapi_client.model.error_generic import ErrorGeneric


class BuyersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __add_buyer(
            self,
            **kwargs
        ):
            """New buyer  # noqa: E501

            Adds a buyer, allowing for payment methods and transactions to be associated to this buyer.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.add_buyer(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                buyer_request (BuyerRequest): [optional]
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
                Buyer
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

        self.add_buyer = _Endpoint(
            settings={
                'response_type': (Buyer,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/buyers',
                'operation_id': 'add_buyer',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'buyer_request',
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
                    'buyer_request':
                        (BuyerRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'buyer_request': 'body',
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
            callable=__add_buyer
        )

        def __delete_buyer(
            self,
            buyer_id,
            **kwargs
        ):
            """Delete buyer  # noqa: E501

            Deletes a buyer record. Any associated tokenized payment methods will remain in the system but no longer associated to the buyer.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_buyer(buyer_id, async_req=True)
            >>> result = thread.get()

            Args:
                buyer_id (str): The unique ID for a buyer.

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
            kwargs['buyer_id'] = \
                buyer_id
            return self.call_with_http_info(**kwargs)

        self.delete_buyer = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/buyers/{buyer_id}',
                'operation_id': 'delete_buyer',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'buyer_id',
                ],
                'required': [
                    'buyer_id',
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
                    'buyer_id':
                        (str,),
                },
                'attribute_map': {
                    'buyer_id': 'buyer_id',
                },
                'location_map': {
                    'buyer_id': 'path',
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
            callable=__delete_buyer
        )

        def __get_buyer(
            self,
            buyer_id,
            **kwargs
        ):
            """Get buyer  # noqa: E501

            Gets the information about a buyer.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_buyer(buyer_id, async_req=True)
            >>> result = thread.get()

            Args:
                buyer_id (str): The unique ID for a buyer.

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
                Buyer
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
            kwargs['buyer_id'] = \
                buyer_id
            return self.call_with_http_info(**kwargs)

        self.get_buyer = _Endpoint(
            settings={
                'response_type': (Buyer,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/buyers/{buyer_id}',
                'operation_id': 'get_buyer',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'buyer_id',
                ],
                'required': [
                    'buyer_id',
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
                    'buyer_id':
                        (str,),
                },
                'attribute_map': {
                    'buyer_id': 'buyer_id',
                },
                'location_map': {
                    'buyer_id': 'path',
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
            callable=__get_buyer
        )

        def __list_buyers(
            self,
            **kwargs
        ):
            """List buyers  # noqa: E501

            Returns a list of buyers.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_buyers(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                search (str): Filters the results to only the buyers for which the `display_name` or `external_identifier` matches this value. This field allows for a partial match, matching any buyer for which either of the fields partially or completely matches.. [optional]
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
                Buyers
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

        self.list_buyers = _Endpoint(
            settings={
                'response_type': (Buyers,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/buyers',
                'operation_id': 'list_buyers',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'search',
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
                    'search':
                        (str,),
                    'limit':
                        (int,),
                    'cursor':
                        (str,),
                },
                'attribute_map': {
                    'search': 'search',
                    'limit': 'limit',
                    'cursor': 'cursor',
                },
                'location_map': {
                    'search': 'query',
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
            callable=__list_buyers
        )

        def __update_buyer(
            self,
            buyer_id,
            **kwargs
        ):
            """Update buyer  # noqa: E501

            Updates a buyer's details.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_buyer(buyer_id, async_req=True)
            >>> result = thread.get()

            Args:
                buyer_id (str): The unique ID for a buyer.

            Keyword Args:
                buyer_update (BuyerUpdate): [optional]
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
                Buyer
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
            kwargs['buyer_id'] = \
                buyer_id
            return self.call_with_http_info(**kwargs)

        self.update_buyer = _Endpoint(
            settings={
                'response_type': (Buyer,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/buyers/{buyer_id}',
                'operation_id': 'update_buyer',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'buyer_id',
                    'buyer_update',
                ],
                'required': [
                    'buyer_id',
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
                    'buyer_id':
                        (str,),
                    'buyer_update':
                        (BuyerUpdate,),
                },
                'attribute_map': {
                    'buyer_id': 'buyer_id',
                },
                'location_map': {
                    'buyer_id': 'path',
                    'buyer_update': 'body',
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
            callable=__update_buyer
        )