"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .paymentservicecreate import PaymentServiceCreate, PaymentServiceCreateTypedDict
from gr4vy.types import BaseModel
from gr4vy.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdatePaymentServiceGlobalsTypedDict(TypedDict):
    merchant_account_id: NotRequired[str]
    r"""The ID of the merchant account to use for this request."""


class UpdatePaymentServiceGlobals(BaseModel):
    merchant_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-gr4vy-merchant-account-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of the merchant account to use for this request."""


class UpdatePaymentServiceRequestTypedDict(TypedDict):
    payment_service_create: PaymentServiceCreateTypedDict
    merchant_account_id: NotRequired[str]
    r"""The ID of the merchant account to use for this request."""


class UpdatePaymentServiceRequest(BaseModel):
    payment_service_create: Annotated[
        PaymentServiceCreate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    merchant_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-gr4vy-merchant-account-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of the merchant account to use for this request."""
