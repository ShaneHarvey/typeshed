from typing import Any, Optional, Union

HAVE_SSL: bool
HAVE_CERTIFI: bool
HAVE_WINCERTSTORE: bool
HAS_SNI: Any
IPADDR_SAFE: Any
SSLError: Any

def validate_cert_reqs(option: str, value: Optional[Union[str, int]]) -> Any: ...
def validate_allow_invalid_certs(option: Any, value: Any): ...
def get_ssl_context(*args: Any) -> Any: ...

class SSLError(Exception): ...
