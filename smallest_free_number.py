# find the smallest number


# function minfree_array(xs):
def minfree_array(xs):
    L = len(xs)

    array = [0] * (L+1)
    for x in xs:
        if 0 <= x <= L:
            array[x] = 1

    for i, each in enumerate(array):
        if not each:
            return i


if __name__ == '__main__':
    print(minfree_array([8, 23, 9, 0, 12, 11, 1, 10, 13, 7, 41, 4, 14, 21, 5, 17, 3, 19, 2, 6]))
