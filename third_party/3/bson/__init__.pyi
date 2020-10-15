from typing import Any, BinaryIO, ByteString, Iterator, List, Mapping, MutableMapping, Sequence

from bson.binary import CSHARP_LEGACY as CSHARP_LEGACY, JAVA_LEGACY as JAVA_LEGACY, OLD_UUID_SUBTYPE as OLD_UUID_SUBTYPE
from bson.codec_options import CodecOptions as CodecOptions

EPOCH_AWARE: Any
EPOCH_NAIVE: Any
BSONNUM: bytes
BSONSTR: bytes
BSONOBJ: bytes
BSONARR: bytes
BSONBIN: bytes
BSONUND: bytes
BSONOID: bytes
BSONBOO: bytes
BSONDAT: bytes
BSONNUL: bytes
BSONRGX: bytes
BSONREF: bytes
BSONCOD: bytes
BSONSYM: bytes
BSONCWS: bytes
BSONINT: bytes
BSONTIM: bytes
BSONLON: bytes
BSONDEC: bytes
BSONMIN: bytes
BSONMAX: bytes

def get_data_and_view(data: Any): ...
def gen_list_name() -> Iterator[bytes]: ...
def encode(document: Mapping, check_keys: bool = ..., codec_options: CodecOptions = ...) -> bytes: ...
def decode(data: ByteString, codec_options: CodecOptions = ...) -> Mapping[str, Any]: ...
def decode_all(data: ByteString, codec_options: CodecOptions = ...) -> List[Mapping[str, Any]]: ...
def decode_iter(data: ByteString, codec_options: CodecOptions = ...) -> Iterator[Mapping[str, Any]]: ...
def decode_file_iter(file_obj: BinaryIO, codec_options: CodecOptions = ...) -> Iterator[Mapping[str, Any]]: ...
def is_valid(bson: bytes) -> bool: ...

class BSON(bytes):
    @classmethod
    def encode(cls: Any, document: Mapping[str, Any], check_keys: bool = ..., codec_options: CodecOptions = ...) -> BSON: ...
    def decode(self, codec_options: CodecOptions = ...) -> MutableMapping[str, Any]: ...

def has_c() -> bool: ...
