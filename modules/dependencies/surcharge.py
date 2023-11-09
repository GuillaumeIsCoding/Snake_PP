from typing import (
    Any
)
from collections.abc import Callable

class surcharge:
    fset: Callable[[Any, Any], None] | None
    def __init__(
        self, 
        fset: Callable[[Any, Any], None] | None = ...,
    ) -> None: ...
    def __add__(self, __fset: Callable[[Any, Any], None]) -> Any: ...
    def __sub__(self, __fset: Callable[[Any, Any], None]) -> Any: ...
        