from . import Type, type_type
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
