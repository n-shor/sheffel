class Node:

    def syntax(self):
        """Returns the syntax representation as string."""
        return repr(self)

    def __repr__(self):
        return f'{type(self).__name__}({', '.join(f'{name}={value}' for name, value in self.__dict__.items())})'
