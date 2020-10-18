from typing import Text

HAVE_STRINGPREP: bool

def saslprep(data: Text, prohibit_unassigned_code_points: bool = ...) -> Text: ...
