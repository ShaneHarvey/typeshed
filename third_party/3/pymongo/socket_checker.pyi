from typing import Any

class SocketChecker:
    def __init__(self) -> None: ...
    def select(self, sock: Any, read: bool=..., write: bool=..., timeout: int=...) -> Any: ...
    def socket_closed(self, sock: Any) -> Any: ...
