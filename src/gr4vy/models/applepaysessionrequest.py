"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gr4vy.types import BaseModel
from typing_extensions import TypedDict


class ApplePaySessionRequestTypedDict(TypedDict):
    validation_url: str
    r"""The validation URL as provided by the Apple SDK when processing a payment."""
    domain_name: str
    r"""The domain on which Apple Pay is being loaded."""


class ApplePaySessionRequest(BaseModel):
    validation_url: str
    r"""The validation URL as provided by the Apple SDK when processing a payment."""

    domain_name: str
    r"""The domain on which Apple Pay is being loaded."""
