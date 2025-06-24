from typing import List
from collections import deque


if __name__ == "__main__":
    import lib.common as c

    array = c.gen_array(10000, 0, 10000)

    # sort here
    def sort(array: List[int]) -> List[int]:
        if len(array) < 2:
            return array

        mid = len(array) // 2
        return merge(sort(array[:mid]), sort(array[mid:]))

    def merge(arr1: List[int], arr2: List[int]) -> List[int]:
        out = []
        a1, a2 = deque(arr1), deque(arr2)
        while len(a1) > 0 and len(a2) > 0:
            if a1[0] < a2[0]:
                out.append(a1.popleft())
            else:
                out.append(a2.popleft())
        out += list(a1 + a2)
        return out

    print(sort(array))
