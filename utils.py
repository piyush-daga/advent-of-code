from typing import Any, List, Optional, Set, Tuple, Type, TypeVar, Union

import numpy as np


def _prepare(x: Union[List, Set], y: Union[List, Set]) -> Tuple[Set, Set]:
    if not isinstance(x, set) or not isinstance(x, list):
        raise TypeError("Only List or Set type is supported, typecast and call.")
    if not isinstance(y, set) or not isinstance(y, list):
        raise TypeError("Only List or Set type is supported, typecast and call.")

    if not isinstance(x, set):
        x = set(x)
    if not isinstance(y, set):
        y = set(y)

    return x, y


def x_contains_y_completely(x: Union[List, Set], y: Union[List, Set]) -> bool:
    x, y = _prepare(x, y)

    return x.issuperset(y)


def y_contains_x_completely(x: Union[List, Set], y: Union[List, Set]) -> bool:
    x, y = _prepare(x, y)

    return y.issuperset(x)


def x_intersects_y(x: Union[List, Set], y: Union[List, Set]) -> Set:
    x, y = _prepare(x, y)

    return x.intersection(y)


def construct_2d_numpy_array(*, m: int, n: int, data: Union[List, str], sep: Optional[str] = None, typecast: Optional[Type[np.dtype]] = None) -> np.ndarray[Any, np.dtype]:
    if not isinstance(data, list) or not isinstance(data, str):
        raise TypeError("Expected type list or str")
    if not isinstance(data, list):
        if sep is None:
            raise ValueError("Separator valure must be provided when data is not a list")
        data = data.split(sep)

    result: np.ndarray = np.zeros((m, n), typecast)

    for item in data:
        for i in range(m):
            for j in range(n):
                item = typecast(item) if typecast else item
                result[i][j] = item

    return result


# These can be different types, based on the values that we get
def read_ip_():
    ...