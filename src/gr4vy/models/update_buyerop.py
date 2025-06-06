"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .buyerupdate import BuyerUpdate, BuyerUpdateTypedDict
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


class UpdateBuyerGlobalsTypedDict(TypedDict):
    merchant_account_id: NotRequired[str]
    r"""The ID of the merchant account to use for this request."""


class UpdateBuyerGlobals(BaseModel):
    merchant_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-gr4vy-merchant-account-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of the merchant account to use for this request."""


class UpdateBuyerRequestTypedDict(TypedDict):
    buyer_id: str
    r"""The ID of the buyer to edit."""
    buyer_update: BuyerUpdateTypedDict
    merchant_account_id: NotRequired[str]
    r"""The ID of the merchant account to use for this request."""


class UpdateBuyerRequest(BaseModel):
    buyer_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the buyer to edit."""

    buyer_update: Annotated[
        BuyerUpdate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    merchant_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-gr4vy-merchant-account-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of the merchant account to use for this request."""
