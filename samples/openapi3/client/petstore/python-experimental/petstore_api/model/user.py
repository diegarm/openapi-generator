# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401

from frozendict import frozendict  # noqa: F401

from decimal import Decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from petstore_api.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    DateSchema,
    DateTimeSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    InstantiationMetadata,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    NumberBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class User(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id = Int64Schema
    username = StrSchema
    firstName = StrSchema
    lastName = StrSchema
    email = StrSchema
    password = StrSchema
    phone = StrSchema
    userStatus = Int32Schema
    objectWithNoDeclaredProps = DictSchema
    
    
    class objectWithNoDeclaredPropsNullable(
        _SchemaTypeChecker(typing.Union[frozendict, none_type, ]),
        DictBase,
        NoneBase,
        Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, None, ],
            _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
            **kwargs: typing.Type[Schema],
        ):
            return super().__new__(
                cls,
                *args,
                _instantiation_metadata=_instantiation_metadata,
                **kwargs,
            )
    anyTypeProp = AnyTypeSchema
    anyTypePropNullable = AnyTypeSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        id: typing.Union[id, Unset] = unset,
        username: typing.Union[username, Unset] = unset,
        firstName: typing.Union[firstName, Unset] = unset,
        lastName: typing.Union[lastName, Unset] = unset,
        email: typing.Union[email, Unset] = unset,
        password: typing.Union[password, Unset] = unset,
        phone: typing.Union[phone, Unset] = unset,
        userStatus: typing.Union[userStatus, Unset] = unset,
        objectWithNoDeclaredProps: typing.Union[objectWithNoDeclaredProps, Unset] = unset,
        objectWithNoDeclaredPropsNullable: typing.Union[objectWithNoDeclaredPropsNullable, Unset] = unset,
        anyTypeProp: typing.Union[anyTypeProp, Unset] = unset,
        anyTypePropNullable: typing.Union[anyTypePropNullable, Unset] = unset,
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
        **kwargs: typing.Type[Schema],
    ):
        return super().__new__(
            cls,
            *args,
            id=id,
            username=username,
            firstName=firstName,
            lastName=lastName,
            email=email,
            password=password,
            phone=phone,
            userStatus=userStatus,
            objectWithNoDeclaredProps=objectWithNoDeclaredProps,
            objectWithNoDeclaredPropsNullable=objectWithNoDeclaredPropsNullable,
            anyTypeProp=anyTypeProp,
            anyTypePropNullable=anyTypePropNullable,
            _instantiation_metadata=_instantiation_metadata,
            **kwargs,
        )
