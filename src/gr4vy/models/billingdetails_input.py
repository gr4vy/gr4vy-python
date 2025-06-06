"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .taxid import TaxID, TaxIDTypedDict
from gr4vy.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class BillingDetailsInputTypedDict(TypedDict):
    first_name: NotRequired[Nullable[str]]
    r"""The first name(s) or given name for the buyer."""
    last_name: NotRequired[Nullable[str]]
    r"""The last name, or family name, of the buyer."""
    email_address: NotRequired[Nullable[str]]
    r"""The email address for the buyer."""
    phone_number: NotRequired[Nullable[str]]
    r"""The phone number for the buyer which should be formatted according to the E164 number standard."""
    address: NotRequired[Nullable[AddressTypedDict]]
    r"""The billing address for the buyer."""
    tax_id: NotRequired[Nullable[TaxIDTypedDict]]
    r"""The tax ID information associated with the billing details."""


class BillingDetailsInput(BaseModel):
    first_name: OptionalNullable[str] = UNSET
    r"""The first name(s) or given name for the buyer."""

    last_name: OptionalNullable[str] = UNSET
    r"""The last name, or family name, of the buyer."""

    email_address: OptionalNullable[str] = UNSET
    r"""The email address for the buyer."""

    phone_number: OptionalNullable[str] = UNSET
    r"""The phone number for the buyer which should be formatted according to the E164 number standard."""

    address: OptionalNullable[Address] = UNSET
    r"""The billing address for the buyer."""

    tax_id: OptionalNullable[TaxID] = UNSET
    r"""The tax ID information associated with the billing details."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "first_name",
            "last_name",
            "email_address",
            "phone_number",
            "address",
            "tax_id",
        ]
        nullable_fields = [
            "first_name",
            "last_name",
            "email_address",
            "phone_number",
            "address",
            "tax_id",
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
