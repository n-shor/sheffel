from abc import ABCMeta, abstractmethod


class Translator[T, K](metaclass=ABCMeta):
    """Represents a compilation stage."""

    @abstractmethod
    def translate(self, source: T) -> K:
        ...
