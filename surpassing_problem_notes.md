# Surpassing Problem (Pearl 2) - Core Idea + Pseudocode

## Core idea (succinct)
Use divide-and-conquer with a merge step on **sorted halves**. During merge, when a left element is smaller than the current right element, **all remaining right elements are greater**, so you can add that count in O(1). This yields O(n log n).

## The trick
Turn a global "greater elements to the right" count into a **local merge step** by keeping halves sorted.

## Pseudocode (max surpasser count)

```
function maxSurpasser(xs):
    pairs = [(x, 0) for x in xs]
    sortedPairs = countAndSort(pairs)
    return max(count for (_, count) in sortedPairs)

function countAndSort(pairs):
    if length(pairs) <= 1:
        return pairs
    (L, R) = split(pairs)
    L = countAndSort(L)
    R = countAndSort(R)
    return mergeCount(L, R)

function mergeCount(L, R):
    i = 0; j = 0
    remR = length(R)
    result = []
    while i < length(L) and j < length(R):
        (x, cx) = L[i]
        (y, cy) = R[j]
        if x < y:
            result.append((x, cx + remR))
            i += 1
        else:
            result.append((y, cy))
            j += 1
            remR -= 1
    append remaining L to result
    append remaining R to result
    return result
```

## Complexity (one sentence)
Naive is O(n^2), divide-and-conquer merge is O(n log n).

## Test cases (Python assert style)

```python
assert maxSurpasser([]) == 0
assert maxSurpasser([5]) == 0
assert maxSurpasser([1,2,3,4]) == 3
assert maxSurpasser([4,3,2,1]) == 0
assert maxSurpasser([2,1,3]) == 1
assert maxSurpasser([3,1,2,5,4]) == 3  # counts: 2,3,2,0,0
assert maxSurpasser([1,1,2]) == 1
assert maxSurpasser(list("GENERATING")) == 6
```
