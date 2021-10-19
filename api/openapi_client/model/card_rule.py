"""
    Gr4vy API

    Welcome to the Gr4vy API reference documentation. Our API is still very much a work in product and subject to change.  # noqa: E501

    The version of the OpenAPI document: 1.1.0-beta
    Contact: code@gr4vy.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
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
from openapi_client.exceptions import ApiAttributeError



class CardRule(ModelNormal):
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
        ('type',): {
            'CARD-RULE': "card-rule",
        },
        ('environment',): {
            'DEVELOPMENT': "development",
            'STAGING': "staging",
            'PRODUCTION': "production",
        },
        ('unprocessable_fallback_strategy',): {
            'USE_ALL_PROVIDERS': "use_all_providers",
            'DECLINE': "decline",
        },
        ('invalid_rule_fallback_strategy',): {
            'USE_ALL_PROVIDERS': "use_all_providers",
            'SKIP': "skip",
            'DECLINE': "decline",
        },
    }

    validations = {
        ('conditions',): {
            'min_items': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
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
        return {
            'type': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'active': (bool,),  # noqa: E501
            'environment': (str,),  # noqa: E501
            'conditions': ([bool, date, datetime, dict, float, int, list, str, none_type],),  # noqa: E501
            'payment_service_ids': ([str],),  # noqa: E501
            'position': (float,),  # noqa: E501
            'unprocessable_fallback_strategy': (str,),  # noqa: E501
            'invalid_rule_fallback_strategy': (str,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'type': 'type',  # noqa: E501
        'id': 'id',  # noqa: E501
        'active': 'active',  # noqa: E501
        'environment': 'environment',  # noqa: E501
        'conditions': 'conditions',  # noqa: E501
        'payment_service_ids': 'payment_service_ids',  # noqa: E501
        'position': 'position',  # noqa: E501
        'unprocessable_fallback_strategy': 'unprocessable_fallback_strategy',  # noqa: E501
        'invalid_rule_fallback_strategy': 'invalid_rule_fallback_strategy',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """CardRule - a model defined in OpenAPI

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
            type (str): `card-rule`.. [optional] if omitted the server will use the default value of "card-rule"  # noqa: E501
            id (str): The ID of the rule.. [optional]  # noqa: E501
            active (bool): Whether this rule is currently in use. Rules can be deactivated to allow for them to be kept around and re-activated at a later date.. [optional]  # noqa: E501
            environment (str): The environment to use this rule in. This rule will only be used for transactions created in that environment.. [optional] if omitted the server will use the default value of "production"  # noqa: E501
            conditions ([bool, date, datetime, dict, float, int, list, str, none_type]): One or more conditions that apply for this rule. Each condition needs to match for this rule to go into effect.. [optional]  # noqa: E501
            payment_service_ids ([str]): A list of IDs for the payment services to use, in order of priority. The payment services all need to process cards.. [optional]  # noqa: E501
            position (float): The numeric rank of a rule. Rules with a lower position value are processed first.. [optional]  # noqa: E501
            unprocessable_fallback_strategy (str): Defines what strategy to use when all of the payment services defined in this rule declined or otherwise were not able to process the card.  * `use_all_providers` - Try all payment services enabled for this currency in order of priority, even if they are not listed in this rule. This is the default behaviour for a rule. * `decline` - Decline the transaction.. [optional] if omitted the server will use the default value of "use_all_providers"  # noqa: E501
            invalid_rule_fallback_strategy (str): Defines what strategy to use when this rule is not valid. This can happen when the rule has triggered for a certain transaction but none of the listed payment services are eligible to process that transaction currency.  * `use_all_providers` - Try all payment services enabled for this currency in order of priority, even if they are not listed in this rule. This is the default behaviour for a rule. * `skip` - Skip this rule and instead move on to the next highest priority rule. * `decline` - Decline the transaction.. [optional] if omitted the server will use the default value of "use_all_providers"  # noqa: E501
            created_at (datetime): The date and time when this rule was created.. [optional]  # noqa: E501
            updated_at (datetime): The date and time when this rule was last updated.. [optional]  # noqa: E501
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
    def __init__(self, *args, **kwargs):  # noqa: E501
        """CardRule - a model defined in OpenAPI

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
            type (str): `card-rule`.. [optional] if omitted the server will use the default value of "card-rule"  # noqa: E501
            id (str): The ID of the rule.. [optional]  # noqa: E501
            active (bool): Whether this rule is currently in use. Rules can be deactivated to allow for them to be kept around and re-activated at a later date.. [optional]  # noqa: E501
            environment (str): The environment to use this rule in. This rule will only be used for transactions created in that environment.. [optional] if omitted the server will use the default value of "production"  # noqa: E501
            conditions ([bool, date, datetime, dict, float, int, list, str, none_type]): One or more conditions that apply for this rule. Each condition needs to match for this rule to go into effect.. [optional]  # noqa: E501
            payment_service_ids ([str]): A list of IDs for the payment services to use, in order of priority. The payment services all need to process cards.. [optional]  # noqa: E501
            position (float): The numeric rank of a rule. Rules with a lower position value are processed first.. [optional]  # noqa: E501
            unprocessable_fallback_strategy (str): Defines what strategy to use when all of the payment services defined in this rule declined or otherwise were not able to process the card.  * `use_all_providers` - Try all payment services enabled for this currency in order of priority, even if they are not listed in this rule. This is the default behaviour for a rule. * `decline` - Decline the transaction.. [optional] if omitted the server will use the default value of "use_all_providers"  # noqa: E501
            invalid_rule_fallback_strategy (str): Defines what strategy to use when this rule is not valid. This can happen when the rule has triggered for a certain transaction but none of the listed payment services are eligible to process that transaction currency.  * `use_all_providers` - Try all payment services enabled for this currency in order of priority, even if they are not listed in this rule. This is the default behaviour for a rule. * `skip` - Skip this rule and instead move on to the next highest priority rule. * `decline` - Decline the transaction.. [optional] if omitted the server will use the default value of "use_all_providers"  # noqa: E501
            created_at (datetime): The date and time when this rule was created.. [optional]  # noqa: E501
            updated_at (datetime): The date and time when this rule was last updated.. [optional]  # noqa: E501
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
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
