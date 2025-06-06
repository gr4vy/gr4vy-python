"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gr4vy.types import BaseModel
from typing_extensions import TypedDict


class FieldTTypedDict(TypedDict):
    r"""A field used in a payment service"""

    key: str
    r"""The ID of the configured field."""
    value: str
    r"""The value of the configured field."""


class FieldT(BaseModel):
    r"""A field used in a payment service"""

    key: str
    r"""The ID of the configured field."""

    value: str
    r"""The value of the configured field."""
