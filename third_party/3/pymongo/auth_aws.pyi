from pymongo_auth_aws import AwsSaslContext
from typing import Any

class AwsSaslContext:
    def __init__(self, credentials: Any) -> None: ...

class _AwsSaslContext(AwsSaslContext):
    def binary_type(self): ...
    def bson_encode(self, doc: Any) -> Any: ...
    def bson_decode(self, data: Any) -> Any: ...
