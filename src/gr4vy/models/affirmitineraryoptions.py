"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gr4vy.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class AffirmItineraryOptionsTypedDict(TypedDict):
    type: NotRequired[Nullable[str]]
    r"""The type of itinerary object."""
    sku: NotRequired[Nullable[str]]
    r"""The booking/itinerary number (if applicable)."""
    display_name: NotRequired[Nullable[str]]
    r"""Readable description of the itinerary item."""
    venue: NotRequired[Nullable[str]]
    r"""The name of the venue where the event is hosted."""
    location: NotRequired[Nullable[str]]
    r"""The address object that can be parsed."""
    date_start: NotRequired[Nullable[str]]
    r"""The start date of this itinerary item."""
    management: NotRequired[Nullable[str]]
    r"""The corporation."""


class AffirmItineraryOptions(BaseModel):
    type: OptionalNullable[str] = UNSET
    r"""The type of itinerary object."""

    sku: OptionalNullable[str] = UNSET
    r"""The booking/itinerary number (if applicable)."""

    display_name: OptionalNullable[str] = UNSET
    r"""Readable description of the itinerary item."""

    venue: OptionalNullable[str] = UNSET
    r"""The name of the venue where the event is hosted."""

    location: OptionalNullable[str] = UNSET
    r"""The address object that can be parsed."""

    date_start: OptionalNullable[str] = UNSET
    r"""The start date of this itinerary item."""

    management: OptionalNullable[str] = UNSET
    r"""The corporation."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "type",
            "sku",
            "display_name",
            "venue",
            "location",
            "date_start",
            "management",
        ]
        nullable_fields = [
            "type",
            "sku",
            "display_name",
            "venue",
            "location",
            "date_start",
            "management",
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
