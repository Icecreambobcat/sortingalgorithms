from typing import List


if __name__ == "__main__":
    import lib.common as c

    array = c.gen_array(100, 0, 10000)

    # sort here
    def partition(arr: List[int]) -> List[List[int]]:
        # recursively partition the array
        if len(arr) < 2:
            return [arr]

        mid = len(arr) // 2
        return partition(arr[:mid]) + partition(arr[mid:])

    def merge(arr1: List[int], arr2: List[int]) -> List[int]:
        # merges 2 sorted arrays by repeated comparison
        out = []
        while len(arr1) > 0 and len(arr2) > 0:
            if arr1[0] < arr2[0]:
                out.append(arr1.pop(0))
            else:
                out.append(arr2.pop(0))
        out += arr1 + arr2
        return out

    array = partition(array)
    while len(array) > 1:
        for i in range(len(array) - 1):
            array.insert(0, merge(array.pop(0), array.pop(0)))

    print(array[0])
