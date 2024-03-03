from enum import Enum


class MemoryQualifier(Enum):
    CONST = 0,
    VALUE = 1,
    REF = 2


class Passer(Enum):
    IMPLICIT = 0
    COPY = 1
    VIEW = 2
    EVAL = 3
