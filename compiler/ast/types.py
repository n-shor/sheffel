from dataclasses import dataclass


@dataclass
class LiteralType:
    """A type for literal values."""
    type_qualifier: str


@dataclass
class CompleteType:
    """A type for complete variables."""
    behavior_qualifiers: list[str]
    type_qualifier: str
    memory_qualifier: str
