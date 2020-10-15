from pymongo import mongo_client
from typing import Any

class MongoReplicaSetClient(mongo_client.MongoClient):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
