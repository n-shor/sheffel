from abc import ABCMeta, abstractmethod


class ITranslator[T, K](metaclass=ABCMeta):
    """Represents a compilation stage."""

    @abstractmethod
    def translate(self, source: T) -> K:
        ...
