"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gr4vy.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Dict
from typing_extensions import NotRequired, TypedDict


class CybersourceOptionsTypedDict(TypedDict):
    meta_key_merchant_id: NotRequired[Nullable[str]]
    r"""The merchant ID to use for this transaction. This requires a meta key to be set up for use with Cybersource, and this overrides the connector configuration."""
    merchant_defined_information: NotRequired[Nullable[Dict[str, str]]]
    r"""A list of merchant defined data to be passed to the Cybersource. Each key needs to be a numeric string."""
    ship_to_method: NotRequired[Nullable[str]]
    r"""The shipping method for this transaction."""


class CybersourceOptions(BaseModel):
    meta_key_merchant_id: OptionalNullable[str] = UNSET
    r"""The merchant ID to use for this transaction. This requires a meta key to be set up for use with Cybersource, and this overrides the connector configuration."""

    merchant_defined_information: OptionalNullable[Dict[str, str]] = UNSET
    r"""A list of merchant defined data to be passed to the Cybersource. Each key needs to be a numeric string."""

    ship_to_method: OptionalNullable[str] = UNSET
    r"""The shipping method for this transaction."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "meta_key_merchant_id",
            "merchant_defined_information",
            "ship_to_method",
        ]
        nullable_fields = [
            "meta_key_merchant_id",
            "merchant_defined_information",
            "ship_to_method",
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
