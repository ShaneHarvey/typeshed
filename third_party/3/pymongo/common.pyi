import datetime
from typing import Any, Callable, Dict, List, Mapping, MutableMapping, Optional, Sequence, Tuple, Type, Union

from bson.codec_options import CodecOptions, TypeRegistry
from bson.py3compat import abc
from bson.raw_bson import RawBSONDocument
from pymongo.driver_info import DriverInfo
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import _ServerMode
from pymongo.write_concern import WriteConcern

ORDERED_TYPES: Tuple[Type[MutableMapping]]
MAX_BSON_SIZE: int
MAX_MESSAGE_SIZE: int
MIN_WIRE_VERSION: int
MAX_WIRE_VERSION: int
MAX_WRITE_BATCH_SIZE: int
MIN_SUPPORTED_SERVER_VERSION: str
MIN_SUPPORTED_WIRE_VERSION: int
MAX_SUPPORTED_WIRE_VERSION: int
HEARTBEAT_FREQUENCY: int
KILL_CURSOR_FREQUENCY: int
EVENTS_QUEUE_FREQUENCY: int
SERVER_SELECTION_TIMEOUT: int
MIN_HEARTBEAT_INTERVAL: float
MIN_SRV_RESCAN_INTERVAL: int
CONNECT_TIMEOUT: float
MAX_POOL_SIZE: int
MIN_POOL_SIZE: int
MAX_IDLE_TIME_MS: Optional[int]
MAX_IDLE_TIME_SEC: Optional[int]
WAIT_QUEUE_TIMEOUT: Optional[int]
LOCAL_THRESHOLD_MS: int
RETRY_WRITES: bool
RETRY_READS: bool
COMMAND_NOT_FOUND_CODES: Sequence[int]
UNAUTHORIZED_CODES: Sequence[int]

def partition_node(node: str) -> Tuple[str, int]: ...
def clean_node(node: str) -> Tuple[str, int]: ...
def raise_config_error(key: str, dummy: Any) -> None: ...
def validate_boolean(option: str, value: Any) -> bool: ...
def validate_boolean_or_string(option: str, value: Any) -> bool: ...
def validate_integer(option: str, value: Any) -> int: ...
def validate_positive_integer(option: str, value: Any) -> int: ...
def validate_non_negative_integer(option: str, value: Any) -> int: ...
def validate_readable(option: str, value: Any) -> Optional[str]: ...
def validate_positive_integer_or_none(option: str, value: Any) -> Optional[int]: ...
def validate_non_negative_integer_or_none(option: str, value: Any) -> Optional[int]: ...
def validate_string(option: str, value: Any) -> str: ...
def validate_string_or_none(option: str, value: Any) -> Optional[str]: ...
def validate_int_or_basestring(option: str, value: Any) -> Union[int, str]: ...
def validate_non_negative_int_or_basestring(option: Any, value: Any) -> Union[int, str]: ...
def validate_positive_float(option: str, value: Any) -> float: ...
def validate_positive_float_or_zero(option: str, value: Any) -> float: ...
def validate_timeout_or_none(option: str, value: Any) -> Optional[float]: ...
def validate_timeout_or_zero(option: str, value: Any) -> float: ...
def validate_timeout_or_none_or_zero(option: Any, value: Any) -> Optional[float]: ...
def validate_max_staleness(option: str, value: Any) -> int: ...
def validate_read_preference(dummy: Any, value: Any) -> _ServerMode: ...
def validate_read_preference_mode(dummy: Any, value: Any) -> _ServerMode: ...
def validate_auth_mechanism(option: str, value: Any) -> str: ...
def validate_uuid_representation(dummy: Any, value: Any) -> int: ...
def validate_read_preference_tags(name: str, value: Any) -> List[Dict[str, str]]: ...
def validate_auth_mechanism_properties(option: str, value: Any) -> Dict[str, Union[bool, str]]: ...
def validate_document_class(option: str, value: Any) -> Union[MutableMapping, RawBSONDocument]: ...
def validate_type_registry(option: Any, value: Any) -> TypeRegistry: ...
def validate_list(option: str, value: Any) -> List[Any]: ...
def validate_list_or_none(option: Any, value: Any) -> Optional[List[Any]]: ...
def validate_list_or_mapping(option: Any, value: Any) -> None: ...
def validate_is_mapping(option: str, value: Any) -> Dict[Any, Any]: ...
def validate_is_document_type(option: str, value: Any) -> None: ...
def validate_appname_or_none(option: str, value: Any) -> Optional[str]: ...
def validate_driver_or_none(option: Any, value: Any) -> Optional[DriverInfo]: ...
def validate_is_callable_or_none(option: Any, value: Any) -> Optional[Callable]: ...
def validate_ok_for_replace(replacement: Any) -> None: ...
def validate_ok_for_update(update: Any) -> None: ...
def validate_unicode_decode_error_handler(dummy: Any, value: str) -> str: ...
def validate_tzinfo(dummy: Any, value: Any) -> Optional[datetime.tzinfo]: ...

URI_OPTIONS_ALIAS_MAP: Any
URI_OPTIONS_VALIDATOR_MAP: Any
NONSPEC_OPTIONS_VALIDATOR_MAP: Any
KW_VALIDATORS: Any
INTERNAL_URI_OPTION_NAME_MAP: Any
URI_OPTIONS_DEPRECATION_MAP: Any
VALIDATORS: Any
TIMEOUT_OPTIONS: Any

def validate_auth_option(option: str, value: Any) -> Tuple[str, Any]: ...
def validate(option: str, value: Any) -> Tuple[str, Any]: ...
def get_validated_options(options: Mapping[str, Any], warn: bool = ...) -> Dict[str, Any]: ...

WRITE_CONCERN_OPTIONS: Any

class BaseObject:
    def __init__(
        self, codec_options: CodecOptions, read_preference: _ServerMode, write_concern: WriteConcern, read_concern: ReadConcern
    ) -> None: ...
    @property
    def codec_options(self) -> CodecOptions: ...
    @property
    def write_concern(self) -> WriteConcern: ...
    @property
    def read_preference(self) -> _ServerMode: ...
    @property
    def read_concern(self) -> ReadConcern: ...

class _CaseInsensitiveDictionary(abc.MutableMapping):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __contains__(self, key: Any): ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __getitem__(self, key: Any): ...
    def __delitem__(self, key: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def get(self, key: Any, default: Optional[Any] = ...): ...
    def pop(self, key: Any, *args: Any, **kwargs: Any): ...
    def popitem(self): ...
    def clear(self) -> None: ...
    def setdefault(self, key: Any, default: Optional[Any] = ...): ...
    def update(self, other: Any) -> None: ...
    def cased_key(self, key: Any): ...
