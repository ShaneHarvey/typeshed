from typing import Any, Dict, FrozenSet, Optional, Sequence, Set, Tuple, Union

from bson import CodecOptions
from pymongo import common
from pymongo.client_session import ClientSession
from pymongo.cursor_manager import CursorManager
from pymongo.database import Database
from pymongo.monitoring import _EventListener
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import _ServerMode
from pymongo.write_concern import WriteConcern

class MongoClient(common.BaseObject):
    HOST: str = ...
    PORT: int = ...
    def __init__(
        self,
        host: Optional[Any] = ...,
        port: Optional[Any] = ...,
        document_class: Any = ...,
        tz_aware: Optional[Any] = ...,
        connect: Optional[Any] = ...,
        type_registry: Optional[Any] = ...,
        **kwargs: Any,
    ): ...
    def watch(
        self,
        pipeline: Optional[Any] = ...,
        full_document: Optional[Any] = ...,
        resume_after: Optional[Any] = ...,
        max_await_time_ms: Optional[Any] = ...,
        batch_size: Optional[Any] = ...,
        collation: Optional[Any] = ...,
        start_at_operation_time: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
        start_after: Optional[Any] = ...,
    ): ...
    @property
    def event_listeners(self) -> Tuple[Sequence[_EventListener]]: ...
    @property
    def address(self) -> Union[Tuple[str, int], None]: ...
    @property
    def primary(self) -> Union[Tuple[str, int], None]: ...
    @property
    def secondaries(self) -> Union[Set[str], Set[Tuple[str, int]]]: ...
    @property
    def arbiters(self) -> Union[Set[str], Set[Tuple[str, int]]]: ...
    @property
    def is_primary(self) -> bool: ...
    @property
    def is_mongos(self) -> bool: ...
    @property
    def max_pool_size(self) -> int: ...
    @property
    def min_pool_size(self) -> int: ...
    @property
    def max_idle_time_ms(self) -> int: ...
    @property
    def nodes(self) -> FrozenSet[Tuple[str, int]]: ...
    @property
    def max_bson_size(self) -> int: ...
    @property
    def max_message_size(self) -> int: ...
    @property
    def max_write_batch_size(self) -> int: ...
    @property
    def local_threshold_ms(self) -> int: ...
    @property
    def server_selection_timeout(self) -> int: ...
    @property
    def retry_writes(self): ...
    @property
    def retry_reads(self): ...
    def close(self) -> None: ...
    def set_cursor_manager(self, manager_class: CursorManager) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __getattr__(self, name: Any): ...
    def __getitem__(self, name: Any): ...
    def close_cursor(self, cursor_id: int, address: Optional[Tuple[str, int]] = ...) -> None: ...
    def kill_cursors(self, cursor_ids: Sequence[int], address: Optional[Tuple[str, int]] = ...) -> None: ...
    def start_session(self, causal_consistency: bool = ..., default_transaction_options: Optional[Any] = ...): ...
    def server_info(self, session: Optional[ClientSession] = ...): ...
    def list_databases(self, session: Optional[ClientSession] = ..., **kwargs: Any): ...
    def list_database_names(self, session: Optional[ClientSession] = ...): ...
    def database_names(self, session: Optional[ClientSession] = ...): ...
    def drop_database(self, name_or_database: Any, session: Optional[ClientSession] = ...) -> None: ...
    def get_default_database(
        self,
        default: Optional[Any] = ...,
        codec_options: Optional[Any] = ...,
        read_preference: Optional[Any] = ...,
        write_concern: Optional[Any] = ...,
        read_concern: Optional[Any] = ...,
    ): ...
    def get_database(
        self,
        name: Optional[str] = ...,
        codec_options: Optional[CodecOptions] = ...,
        read_preference: Optional[_ServerMode] = ...,
        write_concern: Optional[WriteConcern] = ...,
        read_concern: Optional[ReadConcern] = ...,
    ) -> Database: ...
    @property
    def is_locked(self) -> bool: ...
    def fsync(self, **kwargs: Any) -> Dict[str, Any]: ...
    def unlock(self, session: Optional[ClientSession] = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> None: ...
    next: Any = ...

class _MongoClientErrorHandler:
    client: Any = ...
    server_address: Any = ...
    session: Optional[ClientSession] = ...
    max_wire_version: Any = ...
    sock_generation: Any = ...
    completed_handshake: bool = ...
    def __init__(self, client: Any, server: Any, session: Optional[ClientSession]) -> None: ...
    def contribute_socket(self, sock_info: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
