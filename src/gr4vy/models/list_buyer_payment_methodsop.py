"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gr4vy.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
    UnrecognizedStr,
)
from gr4vy.utils import (
    FieldMetadata,
    HeaderMetadata,
    QueryParamMetadata,
    validate_const,
    validate_open_enum,
)
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator, PlainValidator
from typing import Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class ListBuyerPaymentMethodsGlobalsTypedDict(TypedDict):
    merchant_account_id: NotRequired[str]
    r"""The ID of the merchant account to use for this request."""


class ListBuyerPaymentMethodsGlobals(BaseModel):
    merchant_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-gr4vy-merchant-account-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of the merchant account to use for this request."""


OrderBy = Union[Literal["asc", "desc"], UnrecognizedStr]
r"""The direction to sort the payment methods in."""


class ListBuyerPaymentMethodsRequestTypedDict(TypedDict):
    buyer_id: NotRequired[Nullable[str]]
    r"""The ID of the buyer to query payment methods for."""
    buyer_external_identifier: NotRequired[Nullable[str]]
    r"""The external identifier of the buyer to query payment methods for."""
    sort_by: Nullable[Literal["last_used_at"]]
    r"""The field to sort the payment methods by."""
    order_by: NotRequired[OrderBy]
    r"""The direction to sort the payment methods in."""
    country: NotRequired[Nullable[str]]
    r"""The country code to filter payment methods by. This only applies to payment methods with a `country` value."""
    currency: NotRequired[Nullable[str]]
    r"""The currency code to filter payment methods by. This only applies to payment methods with a `currency` value."""
    merchant_account_id: NotRequired[str]
    r"""The ID of the merchant account to use for this request."""


class ListBuyerPaymentMethodsRequest(BaseModel):
    buyer_id: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""The ID of the buyer to query payment methods for."""

    buyer_external_identifier: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""The external identifier of the buyer to query payment methods for."""

    SORT_BY: Annotated[
        Annotated[
            OptionalNullable[Literal["last_used_at"]],
            AfterValidator(validate_const("last_used_at")),
        ],
        pydantic.Field(alias="sort_by"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "last_used_at"
    r"""The field to sort the payment methods by."""

    order_by: Annotated[
        Annotated[Optional[OrderBy], PlainValidator(validate_open_enum(False))],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "desc"
    r"""The direction to sort the payment methods in."""

    country: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""The country code to filter payment methods by. This only applies to payment methods with a `country` value."""

    currency: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""The currency code to filter payment methods by. This only applies to payment methods with a `currency` value."""

    merchant_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-gr4vy-merchant-account-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of the merchant account to use for this request."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "buyer_id",
            "buyer_external_identifier",
            "sort_by",
            "order_by",
            "country",
            "currency",
            "merchant_account_id",
        ]
        nullable_fields = [
            "buyer_id",
            "buyer_external_identifier",
            "sort_by",
            "country",
            "currency",
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
