from typing import Optional, NamedTuple

"""
Python 2 compatible

def square(x): # type: (float) -> float
    return x * x
"""

# PEP 484 -- Type Hints
# added in Python 3.x
def square(x: float) -> float:
    return x * x


# typing module was added in python3.5
def log(s: str, filename: Optional[str] = None) -> None:
    pass


# added in python3.6
x: int = 10


class NT(NamedTuple):
    x: int
    y: int


# added in python3.9
# def print_items(dct: Dict[str, str]) -> None:
def print_items(dct: dict[str, str]) -> None:
    pass


# mypy will generate error with type of NT.y
reveal_type(NT(1, 2).y)
