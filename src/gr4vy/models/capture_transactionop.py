"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .transactioncapture import TransactionCapture, TransactionCaptureTypedDict
from gr4vy.types import BaseModel
from gr4vy.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CaptureTransactionGlobalsTypedDict(TypedDict):
    merchant_account_id: NotRequired[str]
    r"""The ID of the merchant account to use for this request."""


class CaptureTransactionGlobals(BaseModel):
    merchant_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-gr4vy-merchant-account-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of the merchant account to use for this request."""


class CaptureTransactionRequestTypedDict(TypedDict):
    transaction_id: str
    transaction_capture: TransactionCaptureTypedDict
    timeout_in_seconds: NotRequired[float]
    merchant_account_id: NotRequired[str]
    r"""The ID of the merchant account to use for this request."""


class CaptureTransactionRequest(BaseModel):
    transaction_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    transaction_capture: Annotated[
        TransactionCapture,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    timeout_in_seconds: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1

    merchant_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-gr4vy-merchant-account-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of the merchant account to use for this request."""
