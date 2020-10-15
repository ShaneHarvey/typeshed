from typing import Any, Dict, Iterable, Iterator, Mapping, Optional, Tuple, TypeVar, Union

RE_TYPE: Any
_Key = TypeVar('_Key')
_Value = TypeVar('_Value')

class SON(Dict[_Key, _Value]):
    def __init__(self, data: Optional[Union[Mapping[_Key, _Value], Iterable[Tuple[_Key, _Value]]]]=..., **kwargs: _Value) -> None: ...
    def __new__(cls: Any, *args: Any, **kwargs: Any) -> SON[_Key, _Value]: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def keys(self): ...
    def copy(self) -> SON[_Key, _Value]: ...
    def __iter__(self) -> Any: ...
    def has_key(self, key: _Key) -> bool: ...
    def iteritems(self) -> Iterator[Tuple[_Key, _Value]]: ...
    def iterkeys(self) -> Iterator[_Key]: ...
    def itervalues(self) -> Iterator[_Value]: ...
    def values(self): ...
    def items(self): ...
    def clear(self) -> None: ...
    def setdefault(self, key: _Key, default: Optional[_Value]=...) -> _Value: ...
    def pop(self, key: Any, *args: Any): ...
    def popitem(self) -> Tuple[_Key, _Value]: ...
    def update(self, other: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def get(self, key: Any, default: Optional[Any] = ...): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __len__(self): ...
    def to_dict(self) -> Dict[_Key, _Value]: ...
    def __deepcopy__(self, memo: Any): ...
