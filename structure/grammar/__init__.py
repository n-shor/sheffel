try:
    from .generated import *
except ModuleNotFoundError:
    print("Missing grammar files.")
from .utils import regenerate
