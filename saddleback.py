
# function invert(f, z):
#     m = max y such that f(0, y) <= z
#     n = max x such that f(x, 0) <= z
#     return find(0, m, n)


# function find(u, v, n):
#     if u > n or v < 0:
#         return []

#     t = f (u, v)
#     if t < z:
#         return find(u+1, v, n)
#     elif t > z:
#         return find(u, v-1, n)
#     else:
#         return [(u, v)] + find(u+1, v-1, n)
