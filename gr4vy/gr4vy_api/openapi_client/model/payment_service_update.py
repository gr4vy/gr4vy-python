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

def lazy_import():
    from gr4vy.gr4vy_api.openapi_client.model.payment_service_update_fields import PaymentServiceUpdateFields
    globals()['PaymentServiceUpdateFields'] = PaymentServiceUpdateFields


class PaymentServiceUpdate(ModelNormal):
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
    }

    validations = {
        ('display_name',): {
            'max_length': 50,
            'min_length': 1,
        },
        ('accepted_countries',): {
            'min_items': 1,
        },
        ('accepted_currencies',): {
            'min_items': 1,
        },
        ('acquirer_bin_visa',): {
            'max_length': 11,
        },
        ('acquirer_bin_mastercard',): {
            'max_length': 11,
        },
        ('acquirer_bin_amex',): {
            'max_length': 11,
        },
        ('acquirer_bin_discover',): {
            'max_length': 11,
        },
        ('acquirer_merchant_id',): {
            'max_length': 35,
        },
        ('merchant_name',): {
            'max_length': 40,
        },
        ('merchant_country_code',): {
            'regex': {
                'pattern': r'^\d{3}$',  # noqa: E501
            },
        },
        ('merchant_category_code',): {
            'max_length': 4,
            'min_length': 4,
        },
        ('merchant_url',): {
            'max_length': 2048,
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
        lazy_import()
        return {
            'display_name': (str,),  # noqa: E501
            'fields': ([PaymentServiceUpdateFields],),  # noqa: E501
            'accepted_countries': ([str],),  # noqa: E501
            'accepted_currencies': ([str],),  # noqa: E501
            'three_d_secure_enabled': (bool,),  # noqa: E501
            'acquirer_bin_visa': (str, none_type,),  # noqa: E501
            'acquirer_bin_mastercard': (str, none_type,),  # noqa: E501
            'acquirer_bin_amex': (str, none_type,),  # noqa: E501
            'acquirer_bin_discover': (str, none_type,),  # noqa: E501
            'acquirer_merchant_id': (str, none_type,),  # noqa: E501
            'merchant_name': (str, none_type,),  # noqa: E501
            'merchant_country_code': (str, none_type,),  # noqa: E501
            'merchant_category_code': (str, none_type,),  # noqa: E501
            'merchant_url': (str, none_type,),  # noqa: E501
            'active': (bool,),  # noqa: E501
            'position': (float,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'display_name': 'display_name',  # noqa: E501
        'fields': 'fields',  # noqa: E501
        'accepted_countries': 'accepted_countries',  # noqa: E501
        'accepted_currencies': 'accepted_currencies',  # noqa: E501
        'three_d_secure_enabled': 'three_d_secure_enabled',  # noqa: E501
        'acquirer_bin_visa': 'acquirer_bin_visa',  # noqa: E501
        'acquirer_bin_mastercard': 'acquirer_bin_mastercard',  # noqa: E501
        'acquirer_bin_amex': 'acquirer_bin_amex',  # noqa: E501
        'acquirer_bin_discover': 'acquirer_bin_discover',  # noqa: E501
        'acquirer_merchant_id': 'acquirer_merchant_id',  # noqa: E501
        'merchant_name': 'merchant_name',  # noqa: E501
        'merchant_country_code': 'merchant_country_code',  # noqa: E501
        'merchant_category_code': 'merchant_category_code',  # noqa: E501
        'merchant_url': 'merchant_url',  # noqa: E501
        'active': 'active',  # noqa: E501
        'position': 'position',  # noqa: E501
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
    def __init__(self, *args, **kwargs):  # noqa: E501
        """PaymentServiceUpdate - a model defined in OpenAPI

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
            display_name (str): A custom name for the payment service. This will be shown in the Admin UI.. [optional]  # noqa: E501
            fields ([PaymentServiceUpdateFields]): A list of fields, each containing a key-value pair for each field defined by the definition for this payment service e.g. for stripe-card `secret_key` is required and so must be sent with in this field.. [optional]  # noqa: E501
            accepted_countries ([str]): A list of countries that this payment service needs to support in ISO two-letter code format.. [optional]  # noqa: E501
            accepted_currencies ([str]): A list of currencies that this payment service needs to support in ISO 4217 three-letter code format.. [optional]  # noqa: E501
            three_d_secure_enabled (bool): Defines if 3-D Secure is enabled for the service (can only be enabled if the payment service definition supports the `three_d_secure_hosted` feature). This does not affect pass through 3-D Secure data.. [optional] if omitted the server will use the default value of False  # noqa: E501
            acquirer_bin_visa (str, none_type): Acquiring institution identification code for VISA.. [optional]  # noqa: E501
            acquirer_bin_mastercard (str, none_type): Acquiring institution identification code for Mastercard.. [optional]  # noqa: E501
            acquirer_bin_amex (str, none_type): Acquiring institution identification code for Amex.. [optional]  # noqa: E501
            acquirer_bin_discover (str, none_type): Acquiring institution identification code for Discover.. [optional]  # noqa: E501
            acquirer_merchant_id (str, none_type): Merchant identifier used in authorisation requests (assigned by the acquirer).. [optional]  # noqa: E501
            merchant_name (str, none_type): Merchant name (assigned by the acquirer).. [optional]  # noqa: E501
            merchant_country_code (str, none_type): ISO 3166-1 numeric three-digit country code.. [optional]  # noqa: E501
            merchant_category_code (str, none_type): Merchant category code that describes the business.. [optional]  # noqa: E501
            merchant_url (str, none_type): Fully qualified URL of 3-D Secure requestor website or customer care site.. [optional]  # noqa: E501
            active (bool): Defines if this service is currently active or not.. [optional] if omitted the server will use the default value of True  # noqa: E501
            position (float): The numeric rank of a payment service. Payment services with a lower position value are processed first. When a payment services is inserted at a position, any payment services with the the same value or higher are shifted down a position accordingly. When left out, the payment service is inserted at the end of the list.. [optional]  # noqa: E501
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

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
