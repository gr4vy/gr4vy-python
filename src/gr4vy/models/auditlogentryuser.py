"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .userstatus import UserStatus
from gr4vy.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from gr4vy.utils import validate_const, validate_open_enum
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator, PlainValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AuditLogEntryUserTypedDict(TypedDict):
    name: str
    r"""The name of the user."""
    is_staff: bool
    r"""Whether this is a Gr4vy staff user."""
    status: UserStatus
    type: Literal["user"]
    r"""Always `user`."""
    id: NotRequired[Nullable[str]]
    r"""The ID of the user."""
    email_address: NotRequired[Nullable[str]]
    r"""The email address for this user."""


class AuditLogEntryUser(BaseModel):
    name: str
    r"""The name of the user."""

    is_staff: bool
    r"""Whether this is a Gr4vy staff user."""

    status: Annotated[UserStatus, PlainValidator(validate_open_enum(False))]

    TYPE: Annotated[
        Annotated[Optional[Literal["user"]], AfterValidator(validate_const("user"))],
        pydantic.Field(alias="type"),
    ] = "user"
    r"""Always `user`."""

    id: OptionalNullable[str] = UNSET
    r"""The ID of the user."""

    email_address: OptionalNullable[str] = UNSET
    r"""The email address for this user."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["type", "id", "email_address"]
        nullable_fields = ["id", "email_address"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
