from collections import namedtuple
from typing import Any

class _OCSPCache:
    CACHE_KEY_TYPE = namedtuple(
        "OcspResponseCacheKey", ["hash_algorithm", "issuer_name_hash", "issuer_key_hash", "serial_number"]
    )
    def __init__(self) -> None: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __getitem__(self, item: Any): ...
