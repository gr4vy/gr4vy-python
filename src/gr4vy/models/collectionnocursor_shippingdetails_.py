"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .shippingdetails import ShippingDetails, ShippingDetailsTypedDict
from gr4vy.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class CollectionNoCursorShippingDetailsTypedDict(TypedDict):
    items: List[ShippingDetailsTypedDict]
    r"""A list of items returned for this request."""


class CollectionNoCursorShippingDetails(BaseModel):
    items: List[ShippingDetails]
    r"""A list of items returned for this request."""
