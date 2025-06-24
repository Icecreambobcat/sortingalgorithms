import random as _r
from typing import List


def gen_array(n: int, min: int, max: int) -> List[int]:
    return [_r.randint(min, max) for _ in range(n)]
