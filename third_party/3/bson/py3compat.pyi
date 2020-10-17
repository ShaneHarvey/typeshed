import _thread as thread
import codecs as codecs
from abc import ABC as ABC, abstractmethod as abstractmethod
from collections import abc as abc
from io import BytesIO as StringIO
from typing import Any, Iterable, Mapping, Optional, Tuple

PY3: bool

def abstractproperty(func: Any) -> Any: ...

MAXSIZE: int
imap = map

def b(s: Any) -> bytes: ...
def bytes_from_hex(h: Any) -> bytes: ...
def iteritems(d: Mapping) -> Iterable[Tuple[Any, Any]]: ...
def itervalues(d: Mapping) -> Iterable[Any]: ...
def reraise(exctype: Any, value: Any, trace: Optional[Any] = ...) -> None: ...
def reraise_instance(exc_instance: Any, trace: Optional[Any] = ...) -> None: ...

text_type = str
string_type = str
integer_types = int
