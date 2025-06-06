"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gr4vy.types import BaseModel
from gr4vy.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Any, Dict
from typing_extensions import Annotated, TypedDict


class CreatePaymentServiceDefinitionSessionRequestTypedDict(TypedDict):
    payment_service_definition_id: str
    request_body: Dict[str, Any]


class CreatePaymentServiceDefinitionSessionRequest(BaseModel):
    payment_service_definition_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        Dict[str, Any],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
