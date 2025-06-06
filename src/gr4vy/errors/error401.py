"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gr4vy import utils
from gr4vy.models import errordetail as models_errordetail
from gr4vy.types import BaseModel
from gr4vy.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated


class Error401Data(BaseModel):
    TYPE: Annotated[
        Annotated[Optional[Literal["error"]], AfterValidator(validate_const("error"))],
        pydantic.Field(alias="type"),
    ] = "error"
    r"""Always `error`."""

    code: Optional[str] = "unauthorized"
    r"""Always `unauthorized`"""

    status: Optional[int] = 401
    r"""Always `401`."""

    message: Optional[str] = "No valid API authentication found"
    r"""A human readable message that provides more context to the error."""

    details: Optional[List[models_errordetail.ErrorDetail]] = None
    r"""A list of details that further ellaborate on the error."""


class Error401(Exception):
    data: Error401Data

    def __init__(self, data: Error401Data):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, Error401Data)
