"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gr4vy.types import BaseModel
from gr4vy.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetTransactionGlobalsTypedDict(TypedDict):
    merchant_account_id: NotRequired[str]
    r"""The ID of the merchant account to use for this request."""


class GetTransactionGlobals(BaseModel):
    merchant_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-gr4vy-merchant-account-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of the merchant account to use for this request."""


class GetTransactionRequestTypedDict(TypedDict):
    transaction_id: str
    r"""The ID of the transaction"""
    merchant_account_id: NotRequired[str]
    r"""The ID of the merchant account to use for this request."""


class GetTransactionRequest(BaseModel):
    transaction_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the transaction"""

    merchant_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-gr4vy-merchant-account-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of the merchant account to use for this request."""
