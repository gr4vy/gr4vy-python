"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .networktokenstatus import NetworkTokenStatus
from datetime import datetime
from gr4vy.types import BaseModel
from gr4vy.utils import validate_const, validate_open_enum
import pydantic
from pydantic.functional_validators import AfterValidator, PlainValidator
from typing import Literal, Optional
from typing_extensions import Annotated, TypedDict


class NetworkTokenTypedDict(TypedDict):
    id: str
    r"""The ID for the network token."""
    expiration_date: str
    r"""The expiration date for the network token."""
    payment_method_id: str
    r"""The ID of the payment method used to generate this token"""
    status: NetworkTokenStatus
    token: str
    r"""The token value. Will be present if succeeded."""
    created_at: datetime
    r"""The date and time when this network token was first created in our system."""
    updated_at: datetime
    r"""The date and time when this network token was last updated in our system."""
    type: Literal["network-token"]
    r"""Always `network-token`."""


class NetworkToken(BaseModel):
    id: str
    r"""The ID for the network token."""

    expiration_date: str
    r"""The expiration date for the network token."""

    payment_method_id: str
    r"""The ID of the payment method used to generate this token"""

    status: Annotated[NetworkTokenStatus, PlainValidator(validate_open_enum(False))]

    token: str
    r"""The token value. Will be present if succeeded."""

    created_at: datetime
    r"""The date and time when this network token was first created in our system."""

    updated_at: datetime
    r"""The date and time when this network token was last updated in our system."""

    TYPE: Annotated[
        Annotated[
            Optional[Literal["network-token"]],
            AfterValidator(validate_const("network-token")),
        ],
        pydantic.Field(alias="type"),
    ] = "network-token"
    r"""Always `network-token`."""
