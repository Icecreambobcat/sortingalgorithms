if __name__ == "__main__":
    import lib.common as c

    array = c.gen_array(10000, 0, 10000)
    end = False

    # sort here
    while not end:
        end = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                end = False
                array[i], array[i + 1] = array[i + 1], array[i]

    print(array)
