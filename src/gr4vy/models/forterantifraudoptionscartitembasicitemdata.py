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
from gr4vy.utils import validate_open_enum
from pydantic import model_serializer
from pydantic.functional_validators import PlainValidator
from typing import Literal, Union
from typing_extensions import Annotated, NotRequired, TypedDict


Type = Union[Literal["TANGIBLE", "NON_TANGIBLE"], UnrecognizedStr]


class ForterAntiFraudOptionsCartItemBasicItemDataTypedDict(TypedDict):
    type: NotRequired[Nullable[Type]]
    r"""Indicates whether the item is a physical good or a service/digital item."""


class ForterAntiFraudOptionsCartItemBasicItemData(BaseModel):
    type: Annotated[
        OptionalNullable[Type], PlainValidator(validate_open_enum(False))
    ] = UNSET
    r"""Indicates whether the item is a physical good or a service/digital item."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["type"]
        nullable_fields = ["type"]
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
