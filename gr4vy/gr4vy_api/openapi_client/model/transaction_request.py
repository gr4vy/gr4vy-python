"""
    Gr4vy API

    Welcome to the Gr4vy API reference documentation. Our API is still very much a work in product and subject to change.  # noqa: E501

    The version of the OpenAPI document: 1.1.0-beta
    Contact: code@gr4vy.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gr4vy.gr4vy_api.openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from gr4vy.gr4vy_api.openapi_client.exceptions import ApiAttributeError


def lazy_import():
    from gr4vy.gr4vy_api.openapi_client.model.three_d_secure_data_v1_v2 import ThreeDSecureDataV1V2
    from gr4vy.gr4vy_api.openapi_client.model.transaction_payment_method_request import TransactionPaymentMethodRequest
    globals()['ThreeDSecureDataV1V2'] = ThreeDSecureDataV1V2
    globals()['TransactionPaymentMethodRequest'] = TransactionPaymentMethodRequest


class TransactionRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('intent',): {
            'AUTHORIZE': "authorize",
            'CAPTURE': "capture",
        },
        ('environment',): {
            'DEVELOPMENT': "development",
            'STAGING': "staging",
            'PRODUCTION': "production",
        },
    }

    validations = {
        ('amount',): {
            'inclusive_maximum': 99999999,
            'inclusive_minimum': 0,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'amount': (int,),  # noqa: E501
            'currency': (str,),  # noqa: E501
            'payment_method': (TransactionPaymentMethodRequest,),  # noqa: E501
            'store': (bool,),  # noqa: E501
            'intent': (str,),  # noqa: E501
            'external_identifier': (str, none_type,),  # noqa: E501
            'environment': (str,),  # noqa: E501
            'three_d_secure_data': (ThreeDSecureDataV1V2,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'amount': 'amount',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'payment_method': 'payment_method',  # noqa: E501
        'store': 'store',  # noqa: E501
        'intent': 'intent',  # noqa: E501
        'external_identifier': 'external_identifier',  # noqa: E501
        'environment': 'environment',  # noqa: E501
        'three_d_secure_data': 'three_d_secure_data',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, amount, currency, payment_method, *args, **kwargs):  # noqa: E501
        """TransactionRequest - a model defined in OpenAPI

        Args:
            amount (int): The monetary amount to create an authorization for, in the smallest currency unit for the given currency, for example `1299` cents to create an authorization for `$12.99`.
            currency (str): A supported ISO-4217 currency code.
            payment_method (TransactionPaymentMethodRequest):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            store (bool): Whether or not to also try and store the payment method with us so that it can be used again for future use. This is only supported for payment methods that support this feature.. [optional] if omitted the server will use the default value of False  # noqa: E501
            intent (str): Defines the intent of this API call. This determines the desired initial state of the transaction.  * `authorize` - (Default) Optionally approves and then authorizes a transaction but does not capture the funds. * `capture` - Optionally approves and then authorizes and captures the funds of the transaction.. [optional] if omitted the server will use the default value of "authorize"  # noqa: E501
            external_identifier (str, none_type): An external identifier that can be used to match the transaction against your own records.. [optional]  # noqa: E501
            environment (str): Defines the environment to create this transaction in. Setting this to anything other than `production` will force Gr4vy to use the payment a service configured for that environment.. [optional]  # noqa: E501
            three_d_secure_data (ThreeDSecureDataV1V2): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.amount = amount
        self.currency = currency
        self.payment_method = payment_method
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, amount, currency, payment_method, *args, **kwargs):  # noqa: E501
        """TransactionRequest - a model defined in OpenAPI

        Args:
            amount (int): The monetary amount to create an authorization for, in the smallest currency unit for the given currency, for example `1299` cents to create an authorization for `$12.99`.
            currency (str): A supported ISO-4217 currency code.
            payment_method (TransactionPaymentMethodRequest):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            store (bool): Whether or not to also try and store the payment method with us so that it can be used again for future use. This is only supported for payment methods that support this feature.. [optional] if omitted the server will use the default value of False  # noqa: E501
            intent (str): Defines the intent of this API call. This determines the desired initial state of the transaction.  * `authorize` - (Default) Optionally approves and then authorizes a transaction but does not capture the funds. * `capture` - Optionally approves and then authorizes and captures the funds of the transaction.. [optional] if omitted the server will use the default value of "authorize"  # noqa: E501
            external_identifier (str, none_type): An external identifier that can be used to match the transaction against your own records.. [optional]  # noqa: E501
            environment (str): Defines the environment to create this transaction in. Setting this to anything other than `production` will force Gr4vy to use the payment a service configured for that environment.. [optional]  # noqa: E501
            three_d_secure_data (ThreeDSecureDataV1V2): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.amount = amount
        self.currency = currency
        self.payment_method = payment_method
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
