"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .reportspecmodel import ReportSpecModel
from gr4vy.types import BaseModel
from gr4vy.utils import validate_open_enum
from pydantic.functional_validators import PlainValidator
from typing import Any, Dict
from typing_extensions import Annotated, TypedDict


class ReportSpecTypedDict(TypedDict):
    model: ReportSpecModel
    params: Dict[str, Any]
    r"""The parameters for the report model."""


class ReportSpec(BaseModel):
    model: Annotated[ReportSpecModel, PlainValidator(validate_open_enum(False))]

    params: Dict[str, Any]
    r"""The parameters for the report model."""
