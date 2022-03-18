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
    from gr4vy.gr4vy_api.openapi_client.model.cart_item import CartItem
    globals()['CartItem'] = CartItem


from gr4vy.gr4vy_api.openapi_client.model.payment_service import PaymentService
from gr4vy.gr4vy_api.openapi_client.model.payment_method import PaymentMethod
from gr4vy.gr4vy_api.openapi_client.model.buyer import Buyer
class Transaction(ModelNormal):
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
            'TRANSACTION': "transaction",
        },
        ('status',): {
            'PROCESSING': "processing",
            'PROCESSING_FAILED': "processing_failed",
            'CAPTURE_SUCCEEDED': "capture_succeeded",
            'CAPTURE_PENDING': "capture_pending",
            'CAPTURE_DECLINED': "capture_declined",
            'CAPTURE_FAILED': "capture_failed",
            'AUTHORIZATION_SUCCEEDED': "authorization_succeeded",
            'AUTHORIZATION_PENDING': "authorization_pending",
            'AUTHORIZATION_DECLINED': "authorization_declined",
            'AUTHORIZATION_FAILED': "authorization_failed",
            'AUTHORIZATION_EXPIRED': "authorization_expired",
            'AUTHORIZATION_VOIDED': "authorization_voided",
            'AUTHORIZATION_VOID_PENDING': "authorization_void_pending",
            'AUTHORIZATION_VOID_DECLINED': "authorization_void_declined",
            'AUTHORIZATION_VOID_FAILED': "authorization_void_failed",
            'REFUND_SUCCEEDED': "refund_succeeded",
            'REFUND_PENDING': "refund_pending",
            'REFUND_DECLINED': "refund_declined",
            'REFUND_FAILED': "refund_failed",
            'BUYER_APPROVAL_SUCCEEDED': "buyer_approval_succeeded",
            'BUYER_APPROVAL_PENDING': "buyer_approval_pending",
            'BUYER_APPROVAL_DECLINED': "buyer_approval_declined",
            'BUYER_APPROVAL_FAILED': "buyer_approval_failed",
            'BUYER_APPROVAL_TIMEDOUT': "buyer_approval_timedout",
        },
        ('payment_source',): {
            'ECOMMERCE': "ecommerce",
            'MOTO': "moto",
            'RECURRING': "recurring",
            'INSTALLMENT': "installment",
            'CARD_ON_FILE': "card_on_file",
        },
    }

    validations = {
        ('amount',): {
            'inclusive_maximum': 99999999,
            'inclusive_minimum': 0,
        },
        ('captured_amount',): {
            'inclusive_maximum': 99999999,
            'inclusive_minimum': 0,
        },
        ('refunded_amount',): {
            'inclusive_maximum': 99999999,
            'inclusive_minimum': 0,
        },
        ('cart_items',): {
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
            'type': (str,),  # noqa: E501
            'id': (str, none_type),  # noqa: E501
            'status': (str,),  # noqa: E501
            'amount': (int,),  # noqa: E501
            'captured_amount': (int,),  # noqa: E501
            'refunded_amount': (int,),  # noqa: E501
            'currency': (str,),  # noqa: E501
            'payment_method': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'buyer': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'external_identifier': (str, none_type,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'payment_service': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'merchant_initiated': (bool,),  # noqa: E501
            'payment_source': (str,),  # noqa: E501
            'is_subsequent_payment': (bool,),  # noqa: E501
            'statement_descriptor': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'cart_items': ([CartItem],),  # noqa: E501
            'scheme_transaction_id': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'type': 'type',  # noqa: E501
        'id': 'id',  # noqa: E501
        'status': 'status',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'captured_amount': 'captured_amount',  # noqa: E501
        'refunded_amount': 'refunded_amount',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'payment_method': 'payment_method',  # noqa: E501
        'buyer': 'buyer',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'external_identifier': 'external_identifier',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'payment_service': 'payment_service',  # noqa: E501
        'merchant_initiated': 'merchant_initiated',  # noqa: E501
        'payment_source': 'payment_source',  # noqa: E501
        'is_subsequent_payment': 'is_subsequent_payment',  # noqa: E501
        'statement_descriptor': 'statement_descriptor',  # noqa: E501
        'cart_items': 'cart_items',  # noqa: E501
        'scheme_transaction_id': 'scheme_transaction_id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Transaction - a model defined in OpenAPI

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
            type (str): The type of this resource. Is always `transaction`.. [optional] if omitted the server will use the default value of "transaction"  # noqa: E501
            id (str): The unique identifier for this transaction.. [optional]  # noqa: E501
            status (str): The status of the transaction. The status may change over time as asynchronous  processing events occur.. [optional]  # noqa: E501
            amount (int): The authorized amount for this transaction. This can be different than the actual captured amount and part of this amount may be refunded.. [optional]  # noqa: E501
            captured_amount (int): The captured amount for this transaction. This can be a part and in some cases even more than the authorized amount.. [optional]  # noqa: E501
            refunded_amount (int): The refunded amount for this transaction. This can be a part or all of the captured amount.. [optional]  # noqa: E501
            currency (str): The currency code for this transaction.. [optional]  # noqa: E501
            payment_method (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            buyer (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            created_at (datetime): The date and time when this transaction was created in our system.. [optional]  # noqa: E501
            external_identifier (str, none_type): An external identifier that can be used to match the transaction against your own records.. [optional]  # noqa: E501
            updated_at (datetime): Defines when the transaction was last updated.. [optional]  # noqa: E501
            payment_service (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            merchant_initiated (bool): Indicates whether the transaction was initiated by the merchant (true) or customer (false).. [optional] if omitted the server will use the default value of False  # noqa: E501
            payment_source (str): The source of the transaction. Defaults to `ecommerce`.. [optional]  # noqa: E501
            is_subsequent_payment (bool): Indicates whether the transaction represents a subsequent payment coming from a setup recurring payment. Please note this flag is only compatible with `payment_source` set to `recurring`, `installment`, or `card_on_file` and will be ignored for other values or if `payment_source` is not present.. [optional] if omitted the server will use the default value of False  # noqa: E501
            statement_descriptor (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            cart_items ([CartItem]): An array of cart items that represents the line items of a transaction.. [optional]  # noqa: E501
            scheme_transaction_id (str, none_type): An identifier for the transaction used by the scheme itself, when available.  e.g. the Visa Transaction Identifier, or Mastercard Trace ID.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
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
        """Transaction - a model defined in OpenAPI

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
            type (str): The type of this resource. Is always `transaction`.. [optional] if omitted the server will use the default value of "transaction"  # noqa: E501
            id (str): The unique identifier for this transaction.. [optional]  # noqa: E501
            status (str): The status of the transaction. The status may change over time as asynchronous  processing events occur.. [optional]  # noqa: E501
            amount (int): The authorized amount for this transaction. This can be different than the actual captured amount and part of this amount may be refunded.. [optional]  # noqa: E501
            captured_amount (int): The captured amount for this transaction. This can be a part and in some cases even more than the authorized amount.. [optional]  # noqa: E501
            refunded_amount (int): The refunded amount for this transaction. This can be a part or all of the captured amount.. [optional]  # noqa: E501
            currency (str): The currency code for this transaction.. [optional]  # noqa: E501
            payment_method (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            buyer (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            created_at (datetime): The date and time when this transaction was created in our system.. [optional]  # noqa: E501
            external_identifier (str, none_type): An external identifier that can be used to match the transaction against your own records.. [optional]  # noqa: E501
            updated_at (datetime): Defines when the transaction was last updated.. [optional]  # noqa: E501
            payment_service (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            merchant_initiated (bool): Indicates whether the transaction was initiated by the merchant (true) or customer (false).. [optional] if omitted the server will use the default value of False  # noqa: E501
            payment_source (str): The source of the transaction. Defaults to `ecommerce`.. [optional]  # noqa: E501
            is_subsequent_payment (bool): Indicates whether the transaction represents a subsequent payment coming from a setup recurring payment. Please note this flag is only compatible with `payment_source` set to `recurring`, `installment`, or `card_on_file` and will be ignored for other values or if `payment_source` is not present.. [optional] if omitted the server will use the default value of False  # noqa: E501
            statement_descriptor (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            cart_items ([CartItem]): An array of cart items that represents the line items of a transaction.. [optional]  # noqa: E501
            scheme_transaction_id (str, none_type): An identifier for the transaction used by the scheme itself, when available.  e.g. the Visa Transaction Identifier, or Mastercard Trace ID.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
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
