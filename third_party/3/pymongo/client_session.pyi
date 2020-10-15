import collections
from typing import Any, Dict, Mapping, Optional

from bson.binary import Binary
from bson.timestamp import Timestamp
from pymongo.mongo_client import MongoClient
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import _ServerMode
from pymongo.write_concern import WriteConcern

class SessionOptions:
    def __init__(
        self, causal_consistency: bool = ..., default_transaction_options: Optional[TransactionOptions] = ...
    ) -> None: ...
    @property
    def causal_consistency(self) -> bool: ...
    @property
    def default_transaction_options(self) -> Optional[TransactionOptions]: ...

class TransactionOptions:
    def __init__(
        self,
        read_concern: Optional[Any] = ...,
        write_concern: Optional[Any] = ...,
        read_preference: Optional[Any] = ...,
        max_commit_time_ms: Optional[Any] = ...,
    ) -> None: ...
    @property
    def read_concern(self) -> ReadConcern: ...
    @property
    def write_concern(self) -> WriteConcern: ...
    @property
    def read_preference(self) -> _ServerMode: ...
    @property
    def max_commit_time_ms(self): ...

class _TransactionContext:
    def __init__(self, session: ClientSession) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...

class _TxnState:
    NONE: int = ...
    STARTING: int = ...
    IN_PROGRESS: int = ...
    COMMITTED: int = ...
    COMMITTED_EMPTY: int = ...
    ABORTED: int = ...

class _Transaction:
    opts: Any = ...
    state: Any = ...
    sharded: bool = ...
    pinned_address: Any = ...
    recovery_token: Any = ...
    attempt: int = ...
    def __init__(self, opts: Any) -> None: ...
    def active(self): ...
    def reset(self) -> None: ...

class ClientSession:
    def __init__(self, client: MongoClient, server_session: ServerSession, options: Any, authset: Any, implicit: Any) -> None: ...
    def end_session(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    @property
    def client(self) -> MongoClient: ...
    @property
    def options(self) -> SessionOptions: ...
    @property
    def session_id(self) -> Dict[str, Binary]: ...
    @property
    def cluster_time(self) -> Mapping[str, Timestamp]: ...
    @property
    def operation_time(self) -> Timestamp: ...
    def with_transaction(
        self,
        callback: Any,
        read_concern: Optional[Any] = ...,
        write_concern: Optional[Any] = ...,
        read_preference: Optional[Any] = ...,
        max_commit_time_ms: Optional[Any] = ...,
    ): ...
    def start_transaction(
        self,
        read_concern: Optional[Any] = ...,
        write_concern: Optional[Any] = ...,
        read_preference: Optional[Any] = ...,
        max_commit_time_ms: Optional[Any] = ...,
    ): ...
    def commit_transaction(self) -> None: ...
    def abort_transaction(self) -> None: ...
    def advance_cluster_time(self, cluster_time: Mapping[str, Timestamp]) -> None: ...
    def advance_operation_time(self, operation_time: Timestamp) -> None: ...
    @property
    def has_ended(self) -> bool: ...
    @property
    def in_transaction(self): ...
    def __copy__(self) -> None: ...

class _ServerSession:
    session_id: Any = ...
    last_use: Any = ...
    dirty: bool = ...
    generation: Any = ...
    def __init__(self, generation: Any) -> None: ...
    def mark_dirty(self) -> None: ...
    def timed_out(self, session_timeout_minutes: Any): ...
    @property
    def transaction_id(self): ...
    def inc_transaction_id(self) -> None: ...

class _ServerSessionPool(collections.deque):
    generation: int = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def reset(self) -> None: ...
    def pop_all(self): ...
    def get_server_session(self, session_timeout_minutes: Any): ...
    def return_server_session(self, server_session: Any, session_timeout_minutes: Any) -> None: ...
    def return_server_session_no_lock(self, server_session: Any) -> None: ...
