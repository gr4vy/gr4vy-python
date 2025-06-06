"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .paymentserviceupdate import PaymentServiceUpdate, PaymentServiceUpdateTypedDict
from gr4vy.types import BaseModel
from gr4vy.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreatePaymentServiceGlobalsTypedDict(TypedDict):
    merchant_account_id: NotRequired[str]
    r"""The ID of the merchant account to use for this request."""


class CreatePaymentServiceGlobals(BaseModel):
    merchant_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-gr4vy-merchant-account-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of the merchant account to use for this request."""


class CreatePaymentServiceRequestTypedDict(TypedDict):
    payment_service_id: str
    r"""the ID of the payment service"""
    payment_service_update: PaymentServiceUpdateTypedDict
    merchant_account_id: NotRequired[str]
    r"""The ID of the merchant account to use for this request."""


class CreatePaymentServiceRequest(BaseModel):
    payment_service_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""the ID of the payment service"""

    payment_service_update: Annotated[
        PaymentServiceUpdate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    merchant_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-gr4vy-merchant-account-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of the merchant account to use for this request."""
