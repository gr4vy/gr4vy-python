"""
    Gr4vy API

    Welcome to the Gr4vy API reference documentation. Our API is still very much a work in product and subject to change.  # noqa: E501

    The version of the OpenAPI document: 1.1.0-beta
    Contact: code@gr4vy.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gr4vy_python.gr4vy_api.openapi_client.model_utils import (  # noqa: F401
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


class PaymentMethodRequest(ModelNormal):
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
        ('method',): {
            'CARD': "card",
            'PAYPAL': "paypal",
            'BANKED': "banked",
            'GOCARDLESS': "gocardless",
            'STRIPEDD': "stripedd",
            'TOKEN': "token",
        },
        ('environment',): {
            'DEVELOPMENT': "development",
            'STAGING': "staging",
            'PRODUCTION': "production",
        },
    }

    validations = {
        ('number',): {
            'max_length': 16,
            'min_length': 14,
            'regex': {
                'pattern': r'^[0-9]{14,16}$',  # noqa: E501
            },
        },
        ('expiration_date',): {
            'max_length': 5,
            'min_length': 5,
            'regex': {
                'pattern': r'^\d\d\/\d\d$',  # noqa: E501
            },
        },
        ('security_code',): {
            'max_length': 4,
            'min_length': 3,
            'regex': {
                'pattern': r'^\d{3,4}$',  # noqa: E501
            },
        },
    }

    additional_properties_type = None

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
        return {
            'method': (str,),  # noqa: E501
            'number': (str,),  # noqa: E501
            'expiration_date': (str,),  # noqa: E501
            'security_code': (str,),  # noqa: E501
            'external_identifier': (str, none_type,),  # noqa: E501
            'buyer_id': (str,),  # noqa: E501
            'buyer_external_identifier': (str,),  # noqa: E501
            'redirect_url': (str,),  # noqa: E501
            'currency': (str,),  # noqa: E501
            'country': (str,),  # noqa: E501
            'environment': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'method': 'method',  # noqa: E501
        'number': 'number',  # noqa: E501
        'expiration_date': 'expiration_date',  # noqa: E501
        'security_code': 'security_code',  # noqa: E501
        'external_identifier': 'external_identifier',  # noqa: E501
        'buyer_id': 'buyer_id',  # noqa: E501
        'buyer_external_identifier': 'buyer_external_identifier',  # noqa: E501
        'redirect_url': 'redirect_url',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'country': 'country',  # noqa: E501
        'environment': 'environment',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, method, *args, **kwargs):  # noqa: E501
        """PaymentMethodRequest - a model defined in OpenAPI

        Args:
            method (str): The method to use for this request.

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
            number (str): The 15-16 digit number for this credit card as it can be found on the front of the card.  If a card has been stored with us previously, this number will represent the unique tokenized card ID provided via our API.. [optional]  # noqa: E501
            expiration_date (str): The expiration date of the card, formatted `MM/YY`. If a card has been previously stored with us this value is optional.  If the `number` of this card represents a tokenized card, then this value is ignored.. [optional]  # noqa: E501
            security_code (str): The 3 or 4 digit security code often found on the card. This often referred to as the CVV or CVD.  If the `number` of this card represents a tokenized card, then this value is ignored.. [optional]  # noqa: E501
            external_identifier (str, none_type): An external identifier that can be used to match the card against your own records.. [optional]  # noqa: E501
            buyer_id (str): The ID of the buyer to associate this payment method to. If this field is provided then the `buyer_external_identifier` field needs to be unset.. [optional]  # noqa: E501
            buyer_external_identifier (str): The `external_identifier` of the buyer to associate this payment method to. If this field is provided then the `buyer_id` field needs to be unset.. [optional]  # noqa: E501
            redirect_url (str): The redirect URL to redirect a buyer to after they have authorized their transaction or payment method. This only applies to payment methods that require buyer approval.. [optional]  # noqa: E501
            currency (str): The ISO-4217 currency code to store this payment method for. This is used to select the payment service to use.  This only applies to `redirect` mode payment methods like `gocardless`.. [optional]  # noqa: E501
            country (str): The 2-letter ISO code of the country to store this payment method for. This is used to select the payment service to use.  This only applies to `redirect` mode payment methods like `gocardless`.. [optional]  # noqa: E501
            environment (str): Defines the environment to store this payment method in. Setting this to anything other than `production` will force Gr4vy to use a payment a service configured for that environment.. [optional]  # noqa: E501
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

        self.method = method
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
