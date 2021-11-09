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
from gr4vy.gr4vy_api.openapi_client.model.error400_bad_request import Error400BadRequest
from gr4vy.gr4vy_api.openapi_client.model.error401_unauthorized import Error401Unauthorized
from gr4vy.gr4vy_api.openapi_client.model.payment_options import PaymentOptions


class PaymentOptionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.list_payment_options_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentOptions,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/payment-options',
                'operation_id': 'list_payment_options',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'country',
                    'currency',
                    'environment',
                    'locale',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'environment',
                ],
                'validation': [
                    'locale',
                ]
            },
            root_map={
                'validations': {
                    ('locale',): {

                        'regex': {
                            'pattern': r'^[a-z]{2}(?:-[A-Z]{2})?$',  # noqa: E501
                        },
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
                    'country':
                        (str,),
                    'currency':
                        (str,),
                    'environment':
                        (str,),
                    'locale':
                        (str,),
                },
                'attribute_map': {
                    'country': 'country',
                    'currency': 'currency',
                    'environment': 'environment',
                    'locale': 'locale',
                },
                'location_map': {
                    'country': 'query',
                    'currency': 'query',
                    'environment': 'query',
                    'locale': 'query',
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

    def list_payment_options(
        self,
        **kwargs
    ):
        """List payment options  # noqa: E501

        Returns a list of available payment method options for a currency and country.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_payment_options(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            country (str): Filters the results to only the items which support this country code. A country is formatted as 2-letter ISO country code.. [optional]
            currency (str): Filters the results to only the items which support this currency code. A currency is formatted as 3-letter ISO currency code.. [optional]
            environment (str): Filters the results to only the items available in this environment.. [optional] if omitted the server will use the default value of "production"
            locale (str): An ISO 639-1 Language Code and optional ISO 3166 Country Code. This locale determines the language for the labels returned for every payment option.. [optional] if omitted the server will use the default value of "en-US"
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
            PaymentOptions
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
        return self.list_payment_options_endpoint.call_with_http_info(**kwargs)

