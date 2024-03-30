from ..abstract import Node, Block, Value, type_type, unsigned_int_type, double_type


class _Static:
    current = None


class ScopeBase:
    def __init__(self):
        self.parent = _Static.current

    def __enter__(self):
        _Static.current = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _Static.current = self.parent


class Scope(ScopeBase):
    def __init__(self):
        super().__init__()
        self.variables: dict[str, Value] = {}

    @classmethod
    def register(cls, name: str, value: Value):
        s = _Static.current

        if s is None:
            raise AssertionError(f"Call to register was made outside of a scope.")

        if name in s.variables:
            raise KeyError(f'Variable "{name}" already registered.')

        s.variables[name] = value

    @classmethod
    def access(cls, name: str):
        s = _Static.current

        while s is not None:

            if name in s.variables:
                return s.variables[name]

            s = s.parent

        raise KeyError(f'Variable "{name}" is not registered.')


class PredefinedScope(Scope):
    def __init__(self):
        super().__init__()

    def _register_all(self):
        self.register('Type', type_type)
        self.register('Int', unsigned_int_type)
        self.register('Double', double_type)

    @classmethod
    def apply(cls):
        _Static.current = PredefinedScope()
        _Static.current._register_all()
