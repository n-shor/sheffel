class MemoryQualifier:
    """The base for all memory qualifiers."""


class ValueMemoryQualifier(MemoryQualifier):
    """A variable assigned with this qualifier is kept by-value."""


class ReferenceMemoryQualifier(MemoryQualifier):
    """A variable assigned with this qualifier is kept by-reference."""
