"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .paymentmethodstatus import PaymentMethodStatus
from datetime import datetime
from gr4vy.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from gr4vy.utils import validate_const, validate_open_enum
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator, PlainValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PaymentServiceTokenTypedDict(TypedDict):
    id: str
    r"""The ID for the payment service token."""
    payment_method_id: str
    r"""The ID of the payment method used to generate this token"""
    payment_service_id: str
    r"""The ID of the payment method used to generate this token."""
    status: PaymentMethodStatus
    created_at: datetime
    r"""The date and time when this payment service token was first created in our system."""
    updated_at: datetime
    r"""The date and time when this payment service token was last updated in our system."""
    type: Literal["payment-service-token"]
    r"""Always `payment-service-token`."""
    approval_url: NotRequired[Nullable[str]]
    r"""The optional URL that the buyer needs to be redirected to to further authorize the token creation."""
    token: NotRequired[Nullable[str]]
    r"""The token value. Will be present if succeeded."""


class PaymentServiceToken(BaseModel):
    id: str
    r"""The ID for the payment service token."""

    payment_method_id: str
    r"""The ID of the payment method used to generate this token"""

    payment_service_id: str
    r"""The ID of the payment method used to generate this token."""

    status: Annotated[PaymentMethodStatus, PlainValidator(validate_open_enum(False))]

    created_at: datetime
    r"""The date and time when this payment service token was first created in our system."""

    updated_at: datetime
    r"""The date and time when this payment service token was last updated in our system."""

    TYPE: Annotated[
        Annotated[
            Optional[Literal["payment-service-token"]],
            AfterValidator(validate_const("payment-service-token")),
        ],
        pydantic.Field(alias="type"),
    ] = "payment-service-token"
    r"""Always `payment-service-token`."""

    approval_url: OptionalNullable[str] = UNSET
    r"""The optional URL that the buyer needs to be redirected to to further authorize the token creation."""

    token: OptionalNullable[str] = UNSET
    r"""The token value. Will be present if succeeded."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["type", "approval_url", "token"]
        nullable_fields = ["approval_url", "token"]
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
