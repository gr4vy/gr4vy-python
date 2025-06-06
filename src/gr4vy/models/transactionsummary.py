"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .giftcardredemption import GiftCardRedemption, GiftCardRedemptionTypedDict
from .giftcardservice import GiftCardService, GiftCardServiceTypedDict
from .instrumenttype import InstrumentType
from .method import Method
from .shippingdetails import ShippingDetails, ShippingDetailsTypedDict
from .transactionbuyer import TransactionBuyer, TransactionBuyerTypedDict
from .transactionintent import TransactionIntent
from .transactionpaymentmethod import (
    TransactionPaymentMethod,
    TransactionPaymentMethodTypedDict,
)
from .transactionpaymentservice import (
    TransactionPaymentService,
    TransactionPaymentServiceTypedDict,
)
from .transactionstatus import TransactionStatus
from datetime import datetime
from gr4vy.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from gr4vy.utils import validate_const, validate_open_enum
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator, PlainValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TransactionSummaryTypedDict(TypedDict):
    r"""A transaction, summarised"""

    id: str
    r"""The ID for the transaction."""
    reconciliation_id: str
    r"""The base62 encoded transaction ID. This represents a shorter version of this transaction's `id` which is sent to payment services, anti-fraud services, and other connectors. You can use this ID to reconcile a payment service's transaction against our system. This ID is sent instead of the transaction ID because not all services support 36 digit identifiers."""
    merchant_account_id: str
    r"""The ID of the merchant account this transaction belongs to."""
    currency: str
    r"""The currency code for this transaction."""
    amount: int
    r"""The total amount for this transaction across all funding sources including gift cards."""
    status: TransactionStatus
    authorized_amount: int
    r"""The amount for this transaction that has been authorized for the `payment_method`. This can be less than the `amount` if gift cards were used."""
    captured_amount: int
    r"""The total amount captured for this transaction, in the smallest currency unit (for example, cents or pence). This can be the full value of the `authorized_amount` or less."""
    refunded_amount: int
    r"""The total amount refunded for this transaction, in the smallest currency unit (for example, cents or pence). This can be the full value of the `captured_amount` or less."""
    settled_amount: int
    r"""The net amount settled for this transaction, in the smallest currency unit (for example, cents or pence)."""
    settled: bool
    r"""Indicates whether this transaction has been settled."""
    intent: TransactionIntent
    gift_card_redemptions: List[GiftCardRedemptionTypedDict]
    r"""The gift cards redeemed for this transaction."""
    created_at: datetime
    r"""The date and time when the transaction was created, in ISO 8601 format."""
    updated_at: datetime
    r"""The date and time when the transaction was last updated, in ISO 8601 format."""
    type: Literal["transaction"]
    r"""Always `transaction`."""
    settled_currency: NotRequired[Nullable[str]]
    r"""The ISO 4217 currency code of this transaction's settlement."""
    country: NotRequired[Nullable[str]]
    r"""The 2-letter ISO 3166-1 alpha-2 country code for the transaction. Used to filter payment services for processing."""
    external_identifier: NotRequired[Nullable[str]]
    r"""An external identifier that can be used to match the transaction against your own records."""
    payment_method: NotRequired[Nullable[TransactionPaymentMethodTypedDict]]
    r"""The payment method used for this transaction."""
    method: NotRequired[Nullable[Method]]
    r"""The method used for the transaction."""
    instrument_type: NotRequired[Nullable[InstrumentType]]
    r"""The name of the instrument used to process the transaction."""
    error_code: NotRequired[Nullable[str]]
    r"""The standardized error code set by Gr4vy."""
    payment_service: NotRequired[Nullable[TransactionPaymentServiceTypedDict]]
    r"""The payment service used for this transaction."""
    pending_review: NotRequired[bool]
    r"""Whether a manual anti fraud review is pending with an anti fraud service."""
    buyer: NotRequired[Nullable[TransactionBuyerTypedDict]]
    r"""The buyer used for this transaction."""
    raw_response_code: NotRequired[Nullable[str]]
    r"""This is the response code received from the payment service. This can be set to any value and is not standardized across different payment services."""
    raw_response_description: NotRequired[Nullable[str]]
    r"""This is the response description received from the payment service. This can be set to any value and is not standardized across different payment services."""
    shipping_details: NotRequired[Nullable[ShippingDetailsTypedDict]]
    r"""The shipping details associated with the transaction."""
    checkout_session_id: NotRequired[Nullable[str]]
    r"""The identifier for the checkout session this transaction is associated with."""
    gift_card_service: NotRequired[Nullable[GiftCardServiceTypedDict]]
    r"""The gift card service used for this transaction."""


class TransactionSummary(BaseModel):
    r"""A transaction, summarised"""

    id: str
    r"""The ID for the transaction."""

    reconciliation_id: str
    r"""The base62 encoded transaction ID. This represents a shorter version of this transaction's `id` which is sent to payment services, anti-fraud services, and other connectors. You can use this ID to reconcile a payment service's transaction against our system. This ID is sent instead of the transaction ID because not all services support 36 digit identifiers."""

    merchant_account_id: str
    r"""The ID of the merchant account this transaction belongs to."""

    currency: str
    r"""The currency code for this transaction."""

    amount: int
    r"""The total amount for this transaction across all funding sources including gift cards."""

    status: Annotated[TransactionStatus, PlainValidator(validate_open_enum(False))]

    authorized_amount: int
    r"""The amount for this transaction that has been authorized for the `payment_method`. This can be less than the `amount` if gift cards were used."""

    captured_amount: int
    r"""The total amount captured for this transaction, in the smallest currency unit (for example, cents or pence). This can be the full value of the `authorized_amount` or less."""

    refunded_amount: int
    r"""The total amount refunded for this transaction, in the smallest currency unit (for example, cents or pence). This can be the full value of the `captured_amount` or less."""

    settled_amount: int
    r"""The net amount settled for this transaction, in the smallest currency unit (for example, cents or pence)."""

    settled: bool
    r"""Indicates whether this transaction has been settled."""

    intent: Annotated[TransactionIntent, PlainValidator(validate_open_enum(False))]

    gift_card_redemptions: List[GiftCardRedemption]
    r"""The gift cards redeemed for this transaction."""

    created_at: datetime
    r"""The date and time when the transaction was created, in ISO 8601 format."""

    updated_at: datetime
    r"""The date and time when the transaction was last updated, in ISO 8601 format."""

    TYPE: Annotated[
        Annotated[
            Optional[Literal["transaction"]],
            AfterValidator(validate_const("transaction")),
        ],
        pydantic.Field(alias="type"),
    ] = "transaction"
    r"""Always `transaction`."""

    settled_currency: OptionalNullable[str] = UNSET
    r"""The ISO 4217 currency code of this transaction's settlement."""

    country: OptionalNullable[str] = UNSET
    r"""The 2-letter ISO 3166-1 alpha-2 country code for the transaction. Used to filter payment services for processing."""

    external_identifier: OptionalNullable[str] = UNSET
    r"""An external identifier that can be used to match the transaction against your own records."""

    payment_method: OptionalNullable[TransactionPaymentMethod] = UNSET
    r"""The payment method used for this transaction."""

    method: Annotated[
        OptionalNullable[Method], PlainValidator(validate_open_enum(False))
    ] = UNSET
    r"""The method used for the transaction."""

    instrument_type: Annotated[
        OptionalNullable[InstrumentType], PlainValidator(validate_open_enum(False))
    ] = UNSET
    r"""The name of the instrument used to process the transaction."""

    error_code: OptionalNullable[str] = UNSET
    r"""The standardized error code set by Gr4vy."""

    payment_service: OptionalNullable[TransactionPaymentService] = UNSET
    r"""The payment service used for this transaction."""

    pending_review: Optional[bool] = False
    r"""Whether a manual anti fraud review is pending with an anti fraud service."""

    buyer: OptionalNullable[TransactionBuyer] = UNSET
    r"""The buyer used for this transaction."""

    raw_response_code: OptionalNullable[str] = UNSET
    r"""This is the response code received from the payment service. This can be set to any value and is not standardized across different payment services."""

    raw_response_description: OptionalNullable[str] = UNSET
    r"""This is the response description received from the payment service. This can be set to any value and is not standardized across different payment services."""

    shipping_details: OptionalNullable[ShippingDetails] = UNSET
    r"""The shipping details associated with the transaction."""

    checkout_session_id: OptionalNullable[str] = UNSET
    r"""The identifier for the checkout session this transaction is associated with."""

    gift_card_service: OptionalNullable[GiftCardService] = UNSET
    r"""The gift card service used for this transaction."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "type",
            "settled_currency",
            "country",
            "external_identifier",
            "payment_method",
            "method",
            "instrument_type",
            "error_code",
            "payment_service",
            "pending_review",
            "buyer",
            "raw_response_code",
            "raw_response_description",
            "shipping_details",
            "checkout_session_id",
            "gift_card_service",
        ]
        nullable_fields = [
            "settled_currency",
            "country",
            "external_identifier",
            "payment_method",
            "method",
            "instrument_type",
            "error_code",
            "payment_service",
            "buyer",
            "raw_response_code",
            "raw_response_description",
            "shipping_details",
            "checkout_session_id",
            "gift_card_service",
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
