"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .merchantaccountupdate import MerchantAccountUpdate, MerchantAccountUpdateTypedDict
from gr4vy.types import BaseModel
from gr4vy.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class UpdateMerchantAccountRequestTypedDict(TypedDict):
    merchant_account_id: str
    r"""The ID of the merchant account"""
    merchant_account_update: MerchantAccountUpdateTypedDict


class UpdateMerchantAccountRequest(BaseModel):
    merchant_account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the merchant account"""

    merchant_account_update: Annotated[
        MerchantAccountUpdate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
