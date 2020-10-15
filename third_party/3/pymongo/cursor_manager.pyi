from pymongo import MongoClient
from typing import Tuple

class CursorManager:
    def __init__(self, client: MongoClient) -> None: ...
    def close(self, cursor_id: int, address: Tuple[str, int]) -> None: ...
