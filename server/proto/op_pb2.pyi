from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RegUserRequest(_message.Message):
    __slots__ = ("email", "ticker", "requestId")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    email: str
    ticker: str
    requestId: str
    def __init__(self, email: _Optional[str] = ..., ticker: _Optional[str] = ..., requestId: _Optional[str] = ...) -> None: ...

class RegUserResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("email", "ticker", "requestId")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    email: str
    ticker: str
    requestId: str
    def __init__(self, email: _Optional[str] = ..., ticker: _Optional[str] = ..., requestId: _Optional[str] = ...) -> None: ...

class UpdateUserResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("email", "requestId")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    email: str
    requestId: str
    def __init__(self, email: _Optional[str] = ..., requestId: _Optional[str] = ...) -> None: ...

class DeleteUserResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class GetLatestValueRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class GetLatestValueResponse(_message.Message):
    __slots__ = ("email", "ticker", "value", "timestamp")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    email: str
    ticker: str
    value: float
    timestamp: str
    def __init__(self, email: _Optional[str] = ..., ticker: _Optional[str] = ..., value: _Optional[float] = ..., timestamp: _Optional[str] = ...) -> None: ...

class CalcAvarageValueRequest(_message.Message):
    __slots__ = ("email", "count")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    email: str
    count: int
    def __init__(self, email: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class CalcAvarageValueResponse(_message.Message):
    __slots__ = ("email", "ticker", "averageValue")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    AVERAGEVALUE_FIELD_NUMBER: _ClassVar[int]
    email: str
    ticker: str
    averageValue: float
    def __init__(self, email: _Optional[str] = ..., ticker: _Optional[str] = ..., averageValue: _Optional[float] = ...) -> None: ...
