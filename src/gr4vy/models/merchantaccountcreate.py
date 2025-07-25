"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .cardscheme import CardScheme
from gr4vy.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from gr4vy.utils import validate_open_enum
from pydantic import model_serializer
from pydantic.functional_validators import PlainValidator
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class MerchantAccountCreateTypedDict(TypedDict):
    id: str
    r"""The ID for the merchant account."""
    display_name: str
    r"""The display name for the merchant account."""
    account_updater_enabled: NotRequired[bool]
    r"""Whether the Real-Time Account Updater service is enabled for this merchant account. The Account Updater service is used to update card details when cards are lost, stolen or expired. If the field is not set or if it's set to `false`, the Account Updater service doesn't get called if a payment fails with expired or invalid card details. If the field is set to `true`, the service is called. Please note that for this to work the other `account_updater_* fields` must be set as well."""
    account_updater_request_encryption_key: NotRequired[Nullable[str]]
    r"""The public key used to encrypt the request to the Real-Time Account Updater service. The Account Updater service is used to update card details when cards are lost, stolen or expired. If the field is not set or if it's set to `null`, the Account Updater service doesn't get called. If the field is set, the other `account_updater_*` fields must be set as well."""
    account_updater_request_encryption_key_id: NotRequired[Nullable[str]]
    r"""The ID of the key used to encrypt the request to the Real-Time Account Updater service. The Account Updater service is used to update card details when cards are lost, stolen or expired. If the field is not set or if it's set to `null`, the Account Updater service doesn't get called. If the field is set, the other `account_updater_*` fields must be set as well."""
    account_updater_response_decryption_key: NotRequired[Nullable[str]]
    r"""The key used to decrypt the response from the Real-Time Account Updater service. The Account Updater service is used to update card details when cards are lost, stolen or expired. If the field is not set or if it's set to `null`, the Account Updater service doesn't get called. If the field is set, the other `account_updater_*` fields must be set as well."""
    account_updater_response_decryption_key_id: NotRequired[Nullable[str]]
    r"""The ID of the key used to decrypt the request from the Real-Time Account Updater service. The Account Updater service is used to update card details when cards are lost, stolen or expired. If the field is not set or if it's set to `null`, the Account Updater service doesn't get called. If the field is set, the other `account_updater_*` fields must be set as well."""
    over_capture_amount: NotRequired[Nullable[int]]
    r"""The maximum monetary amount allowed for over-capture, in the smallest currency unit, for example `1299` cents to allow for an over-capture of `$12.99`."""
    over_capture_percentage: NotRequired[Nullable[int]]
    r"""The maximum percentage allowed for over-capture, for example `25` to allow for an over-capture of `25%` of the original transaction amount."""
    loon_client_key: NotRequired[Nullable[str]]
    r"""Client key provided by Pagos to authenticate to the Loon API. Loon is the Account Updater service we use and if the field is not set or if it's set to null, the Account Updater service doesn't get configured. If the field is set to `null`, the other `loon_*` fields must be set to null as well."""
    loon_secret_key: NotRequired[Nullable[str]]
    r"""Secret key provided by Pagos to authenticate to the Loon API. Loon is the Account Updater service we use and if the field is not set or if it's set to null, the Account Updater service doesn't get configured. If the field is set to `null`, the other `loon_*` fields must be set to null as well."""
    loon_accepted_schemes: NotRequired[Nullable[List[CardScheme]]]
    r"""Card schemes accepted when creating jobs using this set of Loon API keys. Loon is the Account Updater service we use and if the field is not set or if it's set to null, the Account Updater service doesn't get configured. If the field is set to `null`, the other `loon_*` fields must be set to null as well."""
    visa_network_tokens_requestor_id: NotRequired[Nullable[str]]
    r"""Requestor ID provided for Visa after onboarding to use Network Tokens."""
    visa_network_tokens_app_id: NotRequired[Nullable[str]]
    r"""Application ID provided for Visa after onboarding to use Network Tokens."""
    amex_network_tokens_requestor_id: NotRequired[Nullable[str]]
    r"""Requestor ID provided for American Express after onboarding to use Network Tokens."""
    amex_network_tokens_app_id: NotRequired[Nullable[str]]
    r"""Application ID provided for American Express after onboarding to use Network Tokens."""
    mastercard_network_tokens_requestor_id: NotRequired[Nullable[str]]
    r"""Requestor ID provided for Mastercard after onboarding to use Network Tokens."""
    mastercard_network_tokens_app_id: NotRequired[Nullable[str]]
    r"""Application ID provided for Mastercard after onboarding to use Network Tokens."""


class MerchantAccountCreate(BaseModel):
    id: str
    r"""The ID for the merchant account."""

    display_name: str
    r"""The display name for the merchant account."""

    account_updater_enabled: Optional[bool] = False
    r"""Whether the Real-Time Account Updater service is enabled for this merchant account. The Account Updater service is used to update card details when cards are lost, stolen or expired. If the field is not set or if it's set to `false`, the Account Updater service doesn't get called if a payment fails with expired or invalid card details. If the field is set to `true`, the service is called. Please note that for this to work the other `account_updater_* fields` must be set as well."""

    account_updater_request_encryption_key: OptionalNullable[str] = UNSET
    r"""The public key used to encrypt the request to the Real-Time Account Updater service. The Account Updater service is used to update card details when cards are lost, stolen or expired. If the field is not set or if it's set to `null`, the Account Updater service doesn't get called. If the field is set, the other `account_updater_*` fields must be set as well."""

    account_updater_request_encryption_key_id: OptionalNullable[str] = UNSET
    r"""The ID of the key used to encrypt the request to the Real-Time Account Updater service. The Account Updater service is used to update card details when cards are lost, stolen or expired. If the field is not set or if it's set to `null`, the Account Updater service doesn't get called. If the field is set, the other `account_updater_*` fields must be set as well."""

    account_updater_response_decryption_key: OptionalNullable[str] = UNSET
    r"""The key used to decrypt the response from the Real-Time Account Updater service. The Account Updater service is used to update card details when cards are lost, stolen or expired. If the field is not set or if it's set to `null`, the Account Updater service doesn't get called. If the field is set, the other `account_updater_*` fields must be set as well."""

    account_updater_response_decryption_key_id: OptionalNullable[str] = UNSET
    r"""The ID of the key used to decrypt the request from the Real-Time Account Updater service. The Account Updater service is used to update card details when cards are lost, stolen or expired. If the field is not set or if it's set to `null`, the Account Updater service doesn't get called. If the field is set, the other `account_updater_*` fields must be set as well."""

    over_capture_amount: OptionalNullable[int] = UNSET
    r"""The maximum monetary amount allowed for over-capture, in the smallest currency unit, for example `1299` cents to allow for an over-capture of `$12.99`."""

    over_capture_percentage: OptionalNullable[int] = UNSET
    r"""The maximum percentage allowed for over-capture, for example `25` to allow for an over-capture of `25%` of the original transaction amount."""

    loon_client_key: OptionalNullable[str] = UNSET
    r"""Client key provided by Pagos to authenticate to the Loon API. Loon is the Account Updater service we use and if the field is not set or if it's set to null, the Account Updater service doesn't get configured. If the field is set to `null`, the other `loon_*` fields must be set to null as well."""

    loon_secret_key: OptionalNullable[str] = UNSET
    r"""Secret key provided by Pagos to authenticate to the Loon API. Loon is the Account Updater service we use and if the field is not set or if it's set to null, the Account Updater service doesn't get configured. If the field is set to `null`, the other `loon_*` fields must be set to null as well."""

    loon_accepted_schemes: OptionalNullable[
        List[Annotated[CardScheme, PlainValidator(validate_open_enum(False))]]
    ] = UNSET
    r"""Card schemes accepted when creating jobs using this set of Loon API keys. Loon is the Account Updater service we use and if the field is not set or if it's set to null, the Account Updater service doesn't get configured. If the field is set to `null`, the other `loon_*` fields must be set to null as well."""

    visa_network_tokens_requestor_id: OptionalNullable[str] = UNSET
    r"""Requestor ID provided for Visa after onboarding to use Network Tokens."""

    visa_network_tokens_app_id: OptionalNullable[str] = UNSET
    r"""Application ID provided for Visa after onboarding to use Network Tokens."""

    amex_network_tokens_requestor_id: OptionalNullable[str] = UNSET
    r"""Requestor ID provided for American Express after onboarding to use Network Tokens."""

    amex_network_tokens_app_id: OptionalNullable[str] = UNSET
    r"""Application ID provided for American Express after onboarding to use Network Tokens."""

    mastercard_network_tokens_requestor_id: OptionalNullable[str] = UNSET
    r"""Requestor ID provided for Mastercard after onboarding to use Network Tokens."""

    mastercard_network_tokens_app_id: OptionalNullable[str] = UNSET
    r"""Application ID provided for Mastercard after onboarding to use Network Tokens."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "account_updater_enabled",
            "account_updater_request_encryption_key",
            "account_updater_request_encryption_key_id",
            "account_updater_response_decryption_key",
            "account_updater_response_decryption_key_id",
            "over_capture_amount",
            "over_capture_percentage",
            "loon_client_key",
            "loon_secret_key",
            "loon_accepted_schemes",
            "visa_network_tokens_requestor_id",
            "visa_network_tokens_app_id",
            "amex_network_tokens_requestor_id",
            "amex_network_tokens_app_id",
            "mastercard_network_tokens_requestor_id",
            "mastercard_network_tokens_app_id",
        ]
        nullable_fields = [
            "account_updater_request_encryption_key",
            "account_updater_request_encryption_key_id",
            "account_updater_response_decryption_key",
            "account_updater_response_decryption_key_id",
            "over_capture_amount",
            "over_capture_percentage",
            "loon_client_key",
            "loon_secret_key",
            "loon_accepted_schemes",
            "visa_network_tokens_requestor_id",
            "visa_network_tokens_app_id",
            "amex_network_tokens_requestor_id",
            "amex_network_tokens_app_id",
            "mastercard_network_tokens_requestor_id",
            "mastercard_network_tokens_app_id",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
