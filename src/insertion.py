if __name__ == "__main__":
    import lib.common as c

    array = c.gen_array(10000, 0, 10000)

    # sort here
    tmp = [array.pop(0)]
    for _ in range(len(array)):
        tmp.append(array.pop(0))
        for i in range(len(tmp) - 1, 0, -1):
            if tmp[i - 1] > tmp[i]:
                tmp[i - 1], tmp[i] = tmp[i], tmp[i - 1]
            else:
                break

    array = tmp
    print(array)
