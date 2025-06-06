"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountupdaterjobcreate import (
    AccountUpdaterJobCreate,
    AccountUpdaterJobCreateTypedDict,
)
from gr4vy.types import BaseModel
from gr4vy.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateAccountUpdaterJobGlobalsTypedDict(TypedDict):
    merchant_account_id: NotRequired[str]
    r"""The ID of the merchant account to use for this request."""


class CreateAccountUpdaterJobGlobals(BaseModel):
    merchant_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-gr4vy-merchant-account-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of the merchant account to use for this request."""


class CreateAccountUpdaterJobRequestTypedDict(TypedDict):
    account_updater_job_create: AccountUpdaterJobCreateTypedDict
    merchant_account_id: NotRequired[str]
    r"""The ID of the merchant account to use for this request."""


class CreateAccountUpdaterJobRequest(BaseModel):
    account_updater_job_create: Annotated[
        AccountUpdaterJobCreate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    merchant_account_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-gr4vy-merchant-account-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of the merchant account to use for this request."""
