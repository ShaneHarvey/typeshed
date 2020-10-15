import ssl as _ssl
from socket import socket
from ssl import VERIFY_CRL_CHECK_LEAF as VERIFY_CRL_CHECK_LEAF
from typing import Any, Optional

PROTOCOL_SSLv23: Any
OP_NO_SSLv2: Any
OP_NO_SSLv3: Any
OP_NO_COMPRESSION: Any
OP_NO_RENEGOTIATION: Any
HAS_SNI: Any
IS_PYOPENSSL: bool
SSLError = _ssl.SSLError
CHECK_HOSTNAME_SAFE: Any

class SSLContext:
    def __init__(self, protocol: int) -> None: ...
    @property
    def protocol(self) -> int: ...
    verify_mode: Any = ...
    def load_cert_chain(self, certfile: Any, keyfile: Optional[Any] = ..., password: Optional[Any] = ...) -> None: ...
    def load_verify_locations(self, cafile: Optional[str] = ..., dummy: Optional[Any] = ...) -> None: ...
    def wrap_socket(
        self,
        sock: socket,
        server_side: bool = ...,
        do_handshake_on_connect: bool = ...,
        suppress_ragged_eofs: bool = ...,
        dummy: Optional[Any] = ...,
    ) -> ssl.SSLSocket: ...
