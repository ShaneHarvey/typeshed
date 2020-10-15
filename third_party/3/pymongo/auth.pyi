from collections import namedtuple
from pymongo.pool import SocketInfo
from typing import Any

HAVE_KERBEROS: bool
MECHANISMS: Any

class _Cache:
    data: Any = ...
    def __init__(self) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...

MongoCredential = namedtuple('MongoCredential', ['mechanism', 'source', 'username', 'password', 'mechanism_properties', 'cache'])

GSSAPIProperties = namedtuple('GSSAPIProperties', ['service_name', 'canonicalize_host_name', 'service_realm'])

_AWSProperties = namedtuple('AWSProperties', ['aws_session_token'])

class _AuthContext:
    credentials: Any = ...
    speculative_authenticate: Any = ...
    def __init__(self, credentials: Any) -> None: ...
    @staticmethod
    def from_credentials(creds: Any): ...
    def speculate_command(self) -> None: ...
    def parse_response(self, ismaster: Any) -> None: ...
    def speculate_succeeded(self): ...

class _ScramContext(_AuthContext):
    scram_data: Any = ...
    mechanism: Any = ...
    def __init__(self, credentials: Any, mechanism: Any) -> None: ...
    def speculate_command(self): ...

class _X509Context(_AuthContext):
    def speculate_command(self): ...

def authenticate(credentials: MongoCredential, sock_info: SocketInfo) -> None: ...
def logout(source: str, sock_info: SocketInfo) -> None: ...
