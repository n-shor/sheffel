from .. import base


class Node(base.Node):
    pass


class Block(base.block(Node)):
    pass


class _Undetermined(Node):
    def __repr__(self):
        return 'undetermined'


undetermined = _Undetermined()
