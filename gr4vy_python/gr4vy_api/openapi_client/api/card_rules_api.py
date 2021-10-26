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
from gr4vy_python.gr4vy_api.openapi_client.model.card_rule import CardRule
from gr4vy_python.gr4vy_api.openapi_client.model.card_rule_request import CardRuleRequest
from gr4vy_python.gr4vy_api.openapi_client.model.card_rule_update import CardRuleUpdate
from gr4vy_python.gr4vy_api.openapi_client.model.card_rules import CardRules
from gr4vy_python.gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from gr4vy_python.gr4vy_api.openapi_client.model.error404_not_found import Error404NotFound
from gr4vy_python.gr4vy_api.openapi_client.model.error_generic import ErrorGeneric


class CardRulesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.add_card_rule_endpoint = _Endpoint(
            settings={
                'response_type': (CardRule,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/card-rules',
                'operation_id': 'add_card_rule',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'card_rule_request',
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
                    'card_rule_request':
                        (CardRuleRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'card_rule_request': 'body',
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
        self.delete_card_rule_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/card-rules/{card_rule_id}',
                'operation_id': 'delete_card_rule',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'card_rule_id',
                ],
                'required': [
                    'card_rule_id',
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
                    'card_rule_id':
                        (str,),
                },
                'attribute_map': {
                    'card_rule_id': 'card_rule_id',
                },
                'location_map': {
                    'card_rule_id': 'path',
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
        self.get_card_rule_endpoint = _Endpoint(
            settings={
                'response_type': (CardRule,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/card-rules/{card_rule_id}',
                'operation_id': 'get_card_rule',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'card_rule_id',
                ],
                'required': [
                    'card_rule_id',
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
                    'card_rule_id':
                        (str,),
                },
                'attribute_map': {
                    'card_rule_id': 'card_rule_id',
                },
                'location_map': {
                    'card_rule_id': 'path',
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
        self.list_cards_rules_endpoint = _Endpoint(
            settings={
                'response_type': (CardRules,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/card-rules',
                'operation_id': 'list_cards_rules',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'limit',
                    'cursor',
                    'environment',
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
                    'limit':
                        (int,),
                    'cursor':
                        (str,),
                    'environment':
                        (str,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'cursor': 'cursor',
                    'environment': 'environment',
                },
                'location_map': {
                    'limit': 'query',
                    'cursor': 'query',
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
        self.update_card_rule_endpoint = _Endpoint(
            settings={
                'response_type': (CardRule,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/card-rules/{card_rule_id}',
                'operation_id': 'update_card_rule',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'card_rule_id',
                    'card_rule_update',
                ],
                'required': [
                    'card_rule_id',
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
                    'card_rule_id':
                        (str,),
                    'card_rule_update':
                        (CardRuleUpdate,),
                },
                'attribute_map': {
                    'card_rule_id': 'card_rule_id',
                },
                'location_map': {
                    'card_rule_id': 'path',
                    'card_rule_update': 'body',
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

    def add_card_rule(
        self,
        **kwargs
    ):
        """Create card rule  # noqa: E501

        Creates a new rule that is used for card transactions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_card_rule(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            card_rule_request (CardRuleRequest): [optional]
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
            CardRule
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
        return self.add_card_rule_endpoint.call_with_http_info(**kwargs)

    def delete_card_rule(
        self,
        card_rule_id,
        **kwargs
    ):
        """Delete card rule  # noqa: E501

        Deletes a specific card rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_card_rule(card_rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            card_rule_id (str): The unique ID for a card rule.

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
        kwargs['card_rule_id'] = \
            card_rule_id
        return self.delete_card_rule_endpoint.call_with_http_info(**kwargs)

    def get_card_rule(
        self,
        card_rule_id,
        **kwargs
    ):
        """Get card rule  # noqa: E501

        Returns a rule that can be used for card transactions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_card_rule(card_rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            card_rule_id (str): The unique ID for a card rule.

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
            CardRule
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
        kwargs['card_rule_id'] = \
            card_rule_id
        return self.get_card_rule_endpoint.call_with_http_info(**kwargs)

    def list_cards_rules(
        self,
        **kwargs
    ):
        """List card rules  # noqa: E501

        Returns a list of rules for card transactions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_cards_rules(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            limit (int): Defines the maximum number of items to return for this request.. [optional] if omitted the server will use the default value of 20
            cursor (str): A cursor that identifies the page of results to return. This is used to paginate the results of this API.  For the first page of results, this parameter can be left out. For additional pages, use the value returned by the API in the `next_cursor` field. Similarly the `previous_cursor` can be used to reverse backwards in the list.. [optional]
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
            CardRules
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
        return self.list_cards_rules_endpoint.call_with_http_info(**kwargs)

    def update_card_rule(
        self,
        card_rule_id,
        **kwargs
    ):
        """Update card rule  # noqa: E501

        Updates a rule that can be used for card transactions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_card_rule(card_rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            card_rule_id (str): The unique ID for a card rule.

        Keyword Args:
            card_rule_update (CardRuleUpdate): [optional]
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
            CardRule
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
        kwargs['card_rule_id'] = \
            card_rule_id
        return self.update_card_rule_endpoint.call_with_http_info(**kwargs)

