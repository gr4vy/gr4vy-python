"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gr4vy.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class WpayPaytoSimulationOptionsTypedDict(TypedDict):
    simulate: NotRequired[Nullable[str]]
    r"""The simulation being requested. Please refer to the developer guide for a list of all available simulations."""
    delay: NotRequired[Nullable[int]]
    r"""The delay in seconds before the requested simulation is executed."""


class WpayPaytoSimulationOptions(BaseModel):
    simulate: OptionalNullable[str] = UNSET
    r"""The simulation being requested. Please refer to the developer guide for a list of all available simulations."""

    delay: OptionalNullable[int] = UNSET
    r"""The delay in seconds before the requested simulation is executed."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["simulate", "delay"]
        nullable_fields = ["simulate", "delay"]
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
