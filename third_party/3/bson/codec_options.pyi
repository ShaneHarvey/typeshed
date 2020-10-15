import abc
import datetime
from abc import abstractmethod
from collections import namedtuple
from typing import Any, Callable, Iterable, Optional, Union

from bson.py3compat import ABC

class TypeEncoder(ABC, metaclass=abc.ABCMeta):
    def python_type(self) -> Any: ...
    @abstractmethod
    def transform_python(self, value: Any) -> Any: ...

class TypeDecoder(ABC, metaclass=abc.ABCMeta):
    def bson_type(self) -> Any: ...
    @abstractmethod
    def transform_bson(self, value: Any) -> Any: ...

class TypeCodec(TypeEncoder, TypeDecoder, metaclass=abc.ABCMeta): ...

Codec = Union[TypeEncoder, TypeDecoder, TypeCodec]
Fallback = Callable[[Any], Any]

class TypeRegistry:
    def __init__(self, type_codecs: Optional[Iterable[Codec]] = ..., fallback_encoder: Optional[Fallback] = ...) -> None: ...
    def __eq__(self, other: Any) -> Any: ...

_options_base = namedtuple(
    "CodecOptions",
    ["document_class", "tz_aware", "uuid_representation", "unicode_decode_error_handler", "tzinfo", "type_registry"],
)

class CodecOptions(_options_base):
    def __new__(
        cls: Any,
        document_class: type = ...,
        tz_aware: bool = ...,
        uuid_representation: Optional[int] = ...,
        unicode_decode_error_handler: str = ...,
        tzinfo: Optional[datetime.tzinfo] = ...,
        type_registry: Optional[TypeRegistry] = ...,
    ) -> CodecOptions: ...
    def with_options(self, **kwargs: Any) -> CodecOptions: ...

DEFAULT_CODEC_OPTIONS: Any
