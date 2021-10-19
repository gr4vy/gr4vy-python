"""
    Gr4vy API

    Welcome to the Gr4vy API reference documentation. Our API is still very much a work in product and subject to change.  # noqa: E501

    The version of the OpenAPI document: 1.1.0-beta
    Contact: code@gr4vy.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.error401_unauthorized import Error401Unauthorized
from openapi_client.model.error404_not_found import Error404NotFound
from openapi_client.model.payment_method import PaymentMethod
from openapi_client.model.payment_methods import PaymentMethods
from openapi_client.model.payment_methods_tokenized import PaymentMethodsTokenized
from openapi_client.model.unknownbasetype import UNKNOWNBASETYPE


class PaymentMethodsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.approve_payment_method_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/payment-methods/{payment_method_id}/approve',
                'operation_id': 'approve_payment_method',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_method_id',
                ],
                'required': [
                    'payment_method_id',
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
                    'payment_method_id':
                        (str,),
                },
                'attribute_map': {
                    'payment_method_id': 'payment_method_id',
                },
                'location_map': {
                    'payment_method_id': 'path',
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
            api_client=api_client
        )
        self.delete_payment_method_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/payment-methods/{payment_method_id}',
                'operation_id': 'delete_payment_method',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_method_id',
                ],
                'required': [
                    'payment_method_id',
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
                    'payment_method_id':
                        (str,),
                },
                'attribute_map': {
                    'payment_method_id': 'payment_method_id',
                },
                'location_map': {
                    'payment_method_id': 'path',
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
            api_client=api_client
        )
        self.get_payment_method_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentMethod,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/payment-methods/{payment_method_id}',
                'operation_id': 'get_payment_method',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_method_id',
                ],
                'required': [
                    'payment_method_id',
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
                    'payment_method_id':
                        (str,),
                },
                'attribute_map': {
                    'payment_method_id': 'payment_method_id',
                },
                'location_map': {
                    'payment_method_id': 'path',
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
            api_client=api_client
        )
        self.list_buyer_payment_methods_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentMethodsTokenized,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/buyers/payment-methods',
                'operation_id': 'list_buyer_payment_methods',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'buyer_id',
                    'buyer_external_identifier',
                    'country',
                    'currency',
                    'environment',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'environment',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('environment',): {

                        "DEVELOPMENT": "development",
                        "STAGING": "staging",
                        "PRODUCTION": "production"
                    },
                },
                'openapi_types': {
                    'buyer_id':
                        (str,),
                    'buyer_external_identifier':
                        (str,),
                    'country':
                        (str,),
                    'currency':
                        (str,),
                    'environment':
                        (str,),
                },
                'attribute_map': {
                    'buyer_id': 'buyer_id',
                    'buyer_external_identifier': 'buyer_external_identifier',
                    'country': 'country',
                    'currency': 'currency',
                    'environment': 'environment',
                },
                'location_map': {
                    'buyer_id': 'query',
                    'buyer_external_identifier': 'query',
                    'country': 'query',
                    'currency': 'query',
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
            api_client=api_client
        )
        self.list_payment_methods_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentMethods,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/payment-methods',
                'operation_id': 'list_payment_methods',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment',
                    'buyer_id',
                    'buyer_external_identifier',
                    'limit',
                    'cursor',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
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
                    ('environment',): {

                        "DEVELOPMENT": "development",
                        "STAGING": "staging",
                        "PRODUCTION": "production"
                    },
                },
                'openapi_types': {
                    'environment':
                        (str,),
                    'buyer_id':
                        (str,),
                    'buyer_external_identifier':
                        (str,),
                    'limit':
                        (int,),
                    'cursor':
                        (str,),
                },
                'attribute_map': {
                    'environment': 'environment',
                    'buyer_id': 'buyer_id',
                    'buyer_external_identifier': 'buyer_external_identifier',
                    'limit': 'limit',
                    'cursor': 'cursor',
                },
                'location_map': {
                    'environment': 'query',
                    'buyer_id': 'query',
                    'buyer_external_identifier': 'query',
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
            api_client=api_client
        )
        self.redirect_payment_method_approval_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/payment-methods/approvals/{payment_method_approval_token}',
                'operation_id': 'redirect_payment_method_approval',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_method_approval_token',
                ],
                'required': [
                    'payment_method_approval_token',
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
                    'payment_method_approval_token':
                        (str,),
                },
                'attribute_map': {
                    'payment_method_approval_token': 'payment_method_approval_token',
                },
                'location_map': {
                    'payment_method_approval_token': 'path',
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
            api_client=api_client
        )
        self.store_payment_method_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentMethod,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/payment-methods',
                'operation_id': 'store_payment_method',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'unknown_base_type',
                ],
                'required': [],
                'nullable': [
                    'unknown_base_type',
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
                    'unknown_base_type':
                        (UNKNOWN_BASE_TYPE,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'unknown_base_type': 'body',
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
            api_client=api_client
        )

    def approve_payment_method(
        self,
        payment_method_id,
        **kwargs
    ):
        """Buyer approval callback  # noqa: E501

        Internal API used as a redirect endpoint for payment methods that require buyer authorization.  For example, when a buyer tries to add a GoCardless payment method, the buyer needs to be sent to them, after which they are sent back to this endpoint upon completion.  This API applies any required updates for the payment method based on its query parameters and then redirects the browser back to the `redirect_url` specified when the payment method was first created.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.approve_payment_method(payment_method_id, async_req=True)
        >>> result = thread.get()

        Args:
            payment_method_id (str): The ID of the payment method.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
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
        kwargs['payment_method_id'] = \
            payment_method_id
        return self.approve_payment_method_endpoint.call_with_http_info(**kwargs)

    def delete_payment_method(
        self,
        payment_method_id,
        **kwargs
    ):
        """Delete payment method  # noqa: E501

        Removes a stored payment method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_payment_method(payment_method_id, async_req=True)
        >>> result = thread.get()

        Args:
            payment_method_id (str): The ID of the payment method.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
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
        kwargs['payment_method_id'] = \
            payment_method_id
        return self.delete_payment_method_endpoint.call_with_http_info(**kwargs)

    def get_payment_method(
        self,
        payment_method_id,
        **kwargs
    ):
        """Get stored payment method  # noqa: E501

        Gets the details for a stored payment method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_payment_method(payment_method_id, async_req=True)
        >>> result = thread.get()

        Args:
            payment_method_id (str): The ID of the payment method.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
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
            PaymentMethod
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
        kwargs['payment_method_id'] = \
            payment_method_id
        return self.get_payment_method_endpoint.call_with_http_info(**kwargs)

    def list_buyer_payment_methods(
        self,
        **kwargs
    ):
        """List stored payment methods for a buyer  # noqa: E501

        Returns a list of stored (tokenized) payment methods for a buyer in a short tokenized format. Only payment methods that are compatible with at least one active payment service in that region are shown.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_buyer_payment_methods(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            buyer_id (str): Filters the results to only the items for which the `buyer` has an `id` that matches this value.. [optional]
            buyer_external_identifier (str): Filters the results to only the items for which the `buyer` has an `external_identifier` that matches this value.. [optional]
            country (str): Filters the results to only the items which support this country code. A country is formatted as 2-letter ISO country code.. [optional]
            currency (str): Filters the results to only the items which support this currency code. A currency is formatted as 3-letter ISO currency code.. [optional]
            environment (str): Filters the results to only the items available in this environment.. [optional] if omitted the server will use the default value of "production"
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
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
            PaymentMethodsTokenized
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
        return self.list_buyer_payment_methods_endpoint.call_with_http_info(**kwargs)

    def list_payment_methods(
        self,
        **kwargs
    ):
        """List payment methods  # noqa: E501

        Returns a list of stored (tokenized) payment methods.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_payment_methods(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            environment (str): Filters the results to only the items available in this environment.. [optional] if omitted the server will use the default value of "production"
            buyer_id (str): Filters the results to only the items for which the `buyer` has an `id` that matches this value.. [optional]
            buyer_external_identifier (str): Filters the results to only the items for which the `buyer` has an `external_identifier` that matches this value.. [optional]
            limit (int): Defines the maximum number of items to return for this request.. [optional] if omitted the server will use the default value of 20
            cursor (str): A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
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
            PaymentMethods
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
        return self.list_payment_methods_endpoint.call_with_http_info(**kwargs)

    def redirect_payment_method_approval(
        self,
        payment_method_approval_token,
        **kwargs
    ):
        """Redirect buyer to service  # noqa: E501

        Redirect a buyer to an alternative payment provider to approve their payment method. This is mainly used with providers like GoCardless and Klarna to redirect a buyer to their sites.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.redirect_payment_method_approval(payment_method_approval_token, async_req=True)
        >>> result = thread.get()

        Args:
            payment_method_approval_token (str): The token used to redirect the buyer for approval of the payment method setup. This token does not represent anything to the consumer and no value should be derived from it except for internal use.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
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
        kwargs['payment_method_approval_token'] = \
            payment_method_approval_token
        return self.redirect_payment_method_approval_endpoint.call_with_http_info(**kwargs)

    def store_payment_method(
        self,
        **kwargs
    ):
        """New payment method  # noqa: E501

        Stores and tokenizes a new payment method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.store_payment_method(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            unknown_base_type (UNKNOWN_BASE_TYPE): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
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
            PaymentMethod
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
        return self.store_payment_method_endpoint.call_with_http_info(**kwargs)

