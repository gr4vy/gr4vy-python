"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .transactionstatus import TransactionStatus
from gr4vy.types import BaseModel
from gr4vy.utils import validate_const, validate_open_enum
import pydantic
from pydantic.functional_validators import AfterValidator, PlainValidator
from typing import Literal, Optional
from typing_extensions import Annotated, TypedDict


class TransactionStatusSummaryTypedDict(TypedDict):
    id: str
    r"""The ID for the transaction."""
    status: TransactionStatus
    type: Literal["transaction"]
    r"""Always `transaction`."""


class TransactionStatusSummary(BaseModel):
    id: str
    r"""The ID for the transaction."""

    status: Annotated[TransactionStatus, PlainValidator(validate_open_enum(False))]

    TYPE: Annotated[
        Annotated[
            Optional[Literal["transaction"]],
            AfterValidator(validate_const("transaction")),
        ],
        pydantic.Field(alias="type"),
    ] = "transaction"
    r"""Always `transaction`."""
