class BehaviorQualifier:
    """The base for all behavior qualifiers."""


class EmptyBehaviorQualifier(BehaviorQualifier):
    """The state of variable assigned with this qualifier does not change whatsoever."""


class ConstBehaviorQualifier(BehaviorQualifier):
    """The value of a variable assigned with this qualifier is determined before runtime of the program."""


class NoWriteBehaviorQualifier(BehaviorQualifier):
    """The state of variable assigned with this qualifier cannot be changed after instantiation."""


class NoReadBehaviorQualifier(BehaviorQualifier):
    """The state of variable assigned with this qualifier cannot be read."""
