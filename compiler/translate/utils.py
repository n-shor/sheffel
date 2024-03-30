from typing import Callable, Any


def transform_matching_attributes(obj, type_: type, transform: Callable[[Any], Any]):
    """Transforms all sub attributes of a given object conforming to a type, according to the given function."""

    for attr_name in dir(obj):
        if attr_name.startswith('__'):
            continue

        match getattr(obj, attr_name):
            case attr if attr is obj:
                pass

            case type_() as attr:
                setattr(obj, attr_name, transform(attr))

            case [*attrs]:
                setattr(obj, attr_name, tuple(transform(attr) for attr in attrs))
