from . import Node, Value, Type, type_type
from .utils import make_declarations_block


class _MemTypeBase(Type):
    def __init__(self):
        super().__init__(
            type_type,
            make_declarations_block(t=type_type)
        )


class _CopyType(_MemTypeBase):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'copy_type'


class _RefType(_MemTypeBase):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'ref_type'


class _EvalType(_MemTypeBase):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'eval_type'


copy_type = _CopyType()
ref_type = _RefType()
eval_type = _EvalType()


class MemoryComposition(Node):
    def __init__(self, memory_type: _MemTypeBase, value_type: Value):
        self.memory_type = memory_type
        self.value_type = value_type

    _symbol_dict = {'&': copy_type, '*': ref_type, '^': eval_type}

    @classmethod
    def from_symbol(cls, symbol: str, value_type: Value):
        return cls(cls._symbol_dict[symbol], value_type)

    def syntax(self):
        return f'{self.value_type.syntax()}:{self.memory_type.syntax()}'
