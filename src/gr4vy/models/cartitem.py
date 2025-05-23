"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .producttype import ProductType
from gr4vy.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from gr4vy.utils import validate_open_enum
from pydantic import model_serializer
from pydantic.functional_validators import PlainValidator
from typing import List
from typing_extensions import Annotated, NotRequired, TypedDict


class CartItemTypedDict(TypedDict):
    name: str
    r"""The name of the cart item. The value you set for this property may be truncated if the maximum length accepted by a payment service provider is less than 255 characters."""
    quantity: int
    r"""The quantity of this item in the cart. This value cannot be negative or zero."""
    unit_amount: int
    r"""The amount for an individual item represented as a monetary amount in the smallest currency unit for the given currency, for example `1299` USD cents represents `$12.99`. The amount sent through to the payment processor as unitary amount will be calculated to include the discount and tax values sent as part of this cart item."""
    discount_amount: NotRequired[Nullable[int]]
    r"""The amount discounted for this item represented as a monetary amount in the smallest currency unit for the given currency, for example `1299` USD cents represents `$12.99`."""
    tax_amount: NotRequired[Nullable[int]]
    r"""The tax amount for this item represented as a monetary amount in the smallest currency unit for the given currency, for example `1299` USD cents represents `$12.99`."""
    external_identifier: NotRequired[Nullable[str]]
    r"""An external identifier for the cart item. This can be set to any value and is not sent to the payment service."""
    sku: NotRequired[Nullable[str]]
    r"""The SKU for the item."""
    product_url: NotRequired[Nullable[str]]
    r"""The product URL for the item."""
    image_url: NotRequired[Nullable[str]]
    r"""The URL for the image of the item."""
    categories: NotRequired[Nullable[List[str]]]
    r"""A list of strings containing product categories for the item."""
    product_type: NotRequired[Nullable[ProductType]]
    r"""The product type of the cart item."""
    seller_country: NotRequired[Nullable[str]]
    r"""The seller country of the cart item."""


class CartItem(BaseModel):
    name: str
    r"""The name of the cart item. The value you set for this property may be truncated if the maximum length accepted by a payment service provider is less than 255 characters."""

    quantity: int
    r"""The quantity of this item in the cart. This value cannot be negative or zero."""

    unit_amount: int
    r"""The amount for an individual item represented as a monetary amount in the smallest currency unit for the given currency, for example `1299` USD cents represents `$12.99`. The amount sent through to the payment processor as unitary amount will be calculated to include the discount and tax values sent as part of this cart item."""

    discount_amount: OptionalNullable[int] = UNSET
    r"""The amount discounted for this item represented as a monetary amount in the smallest currency unit for the given currency, for example `1299` USD cents represents `$12.99`."""

    tax_amount: OptionalNullable[int] = UNSET
    r"""The tax amount for this item represented as a monetary amount in the smallest currency unit for the given currency, for example `1299` USD cents represents `$12.99`."""

    external_identifier: OptionalNullable[str] = UNSET
    r"""An external identifier for the cart item. This can be set to any value and is not sent to the payment service."""

    sku: OptionalNullable[str] = UNSET
    r"""The SKU for the item."""

    product_url: OptionalNullable[str] = UNSET
    r"""The product URL for the item."""

    image_url: OptionalNullable[str] = UNSET
    r"""The URL for the image of the item."""

    categories: OptionalNullable[List[str]] = UNSET
    r"""A list of strings containing product categories for the item."""

    product_type: Annotated[
        OptionalNullable[ProductType], PlainValidator(validate_open_enum(False))
    ] = UNSET
    r"""The product type of the cart item."""

    seller_country: OptionalNullable[str] = UNSET
    r"""The seller country of the cart item."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "discount_amount",
            "tax_amount",
            "external_identifier",
            "sku",
            "product_url",
            "image_url",
            "categories",
            "product_type",
            "seller_country",
        ]
        nullable_fields = [
            "discount_amount",
            "tax_amount",
            "external_identifier",
            "sku",
            "product_url",
            "image_url",
            "categories",
            "product_type",
            "seller_country",
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
