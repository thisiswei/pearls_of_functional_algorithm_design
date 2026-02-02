
# function maxSurpasser(xs):
#   pairs = [(x, 0) for x in xs]
#   sortedPairs = countAndSort(pairs)
#   return max(count for (_, count) in sortedPairs)


# function countAndSort(pairs):
#   if length(pairs) <= 1:
#       return pairs
#   (L, R) = split(pairs)
#   L = countAndSort(L)
#   R = countAndSort(R)
#   return mergeCount(L, R)


# function mergeCount(L, R):
#   i = 0; j = 0
#   remR = length(R)
#   result = []

#   while i < length(L) and j < length(R):
#       (x, cx) = L[i]
#       (y, cy) = R[j]
#       if x < y:
#           result.append((x, cx + remR))
#           i++
#       else:
#           result.append((y, cy))
#           j++
#           remR--

#   append remaining L to result
#   append remaining R to result
#   return result


# # [1,2,3,4] → 3
# # Counts: 3,2,1,0 → max = 3


def maxSurpasser(xs):
    if not xs:
        return 0

    pairs = [(x, 0) for x in xs]
    sortedPairs = countAndSort(pairs)
    return max(count for (_, count) in sortedPairs)


def countAndSort(pairs):
    if len(pairs) <= 1:
        return pairs

    len_pairs = len(pairs)
    mid = len_pairs // 2
    L, R = pairs[:mid], pairs[mid:]

    L = countAndSort(L)
    R = countAndSort(R)
    return mergeCount(L, R)


def mergeCount(L, R):
    i = 0; j = 0
    len_l = len(L)
    len_r = len(R)

    ret = []
    while i < len_l and j < len_r:
        x, xc = L[i]
        y, yc = R[j]

        if x < y:
            ret.append((x, xc + len_r))
            i = i + 1
        else:
            ret.append((y, yc))
            j = j + 1
            len_r = len_r - 1

    ret = ret + L[i:]
    ret = ret + R[j:]
    return ret

if __name__ == '__main__':
    assert maxSurpasser([]) == 0
    assert maxSurpasser([5]) == 0
    assert maxSurpasser([1,2,3,4]) == 3
    assert maxSurpasser([4,3,2,1]) == 0
    assert maxSurpasser([2,1,3]) == 1
    assert maxSurpasser([3,1,2,5,4]) == 3  # counts: 2,3,2,0,0
    assert maxSurpasser([1,1,2]) == 1
    assert maxSurpasser(list("GENERATING")) == 6
