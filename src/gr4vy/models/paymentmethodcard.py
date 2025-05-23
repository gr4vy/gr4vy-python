"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .cardscheme import CardScheme
from gr4vy.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from gr4vy.utils import validate_const, validate_open_enum
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator, PlainValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PaymentMethodCardTypedDict(TypedDict):
    number: str
    r"""The 13-19 digit number for this card as it can be found on the front of the card."""
    expiration_date: str
    r"""The expiration date of the card, formatted `MM/YY`."""
    method: Literal["card"]
    r"""Set to `card` to use a new card."""
    card_scheme: NotRequired[Nullable[CardScheme]]
    r"""The optional card's network scheme."""
    external_identifier: NotRequired[Nullable[str]]
    r"""The merchant identifier for this card."""


class PaymentMethodCard(BaseModel):
    number: str
    r"""The 13-19 digit number for this card as it can be found on the front of the card."""

    expiration_date: str
    r"""The expiration date of the card, formatted `MM/YY`."""

    METHOD: Annotated[
        Annotated[Optional[Literal["card"]], AfterValidator(validate_const("card"))],
        pydantic.Field(alias="method"),
    ] = "card"
    r"""Set to `card` to use a new card."""

    card_scheme: Annotated[
        OptionalNullable[CardScheme], PlainValidator(validate_open_enum(False))
    ] = UNSET
    r"""The optional card's network scheme."""

    external_identifier: OptionalNullable[str] = UNSET
    r"""The merchant identifier for this card."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["method", "card_scheme", "external_identifier"]
        nullable_fields = ["card_scheme", "external_identifier"]
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
