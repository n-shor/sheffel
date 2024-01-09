from llvmlite import ir

from . import UnqualifiedType, DirectUnqualifiedType, VariableType


class FunctionType(UnqualifiedType):
    """The unqualified type information of a function as it is declared."""
    def __init__(self, *, parameter_types: tuple[VariableType] = (), return_type: VariableType = None):
        super().__init__()

        self.parameter_types = parameter_types
        self.return_type = return_type

    def get_direct_unqualified_type(self):
        """Gets the direct unqualified type of this function (llvmlite.ir correspondant)
        if all of its subtypes can be represented in the same way."""
        subtypes = self.return_type, *self.parameter_types

        if all(isinstance(vt.base_type, DirectUnqualifiedType) for vt in subtypes):
            pass

        return DirectUnqualifiedType(
            ir.FunctionType(
                self.return_type.base_type.type_,
                (vt.base_type.type_ for vt in self.parameter_types)
            )
        )
