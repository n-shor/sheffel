from __future__ import annotations

from typing import Generator, Self, Any

class Expression:
    
    def __init__(self, value: str, direct_children: list[Expression] = []) -> None:
        self.value = value
        self.direct_children = direct_children
    
    def __iter__(self) -> Generator[Self, Any, None]:
        yield self
        
        for child in self.direct_children:
            yield from child