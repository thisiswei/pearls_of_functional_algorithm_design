# Pearl 3 — Improving on Saddleback Search

## Problem
Given a function `f(x, y)` that is **strictly increasing in each argument**, and a target value `z`, compute **all pairs** `(x, y)` such that `f(x, y) = z`.

## Main concept (saddleback search)
Instead of brute‑forcing all pairs, search the grid from the **top‑left corner** of a rectangle and eliminate a **row or column** each step:

- Start at `(u, v)` (top‑left).
- If `f(u, v) < z`: discard column `u` and move **right**.
- If `f(u, v) > z`: discard row `v` and move **down**.
- If `f(u, v) = z`: record `(u, v)` and move **diagonally** (discard both row and column).

This visits at most the perimeter of the rectangle: **O(m + n)** evaluations for an `m×n` rectangle.

## Key improvement (tight bounds)
The naive rectangle `[0..z] × [0..z]` is too large. Compute tighter bounds:

```
m = max y such that f(0, y) ≤ z
n = max x such that f(x, 0) ≤ z
```

Use **binary search** on `f(0, y)` and `f(x, 0)` to find `m` and `n` in **O(log z)** each. Then saddleback search only on the `(m+1) × (n+1)` rectangle.

## Complexity
- Naive search: **O(z²)** evaluations
- Saddleback on full square: **O(z)**
- Saddleback with tight bounds: **O(log z + m + n)**, often much smaller

## Takeaway
Exploit monotonicity to **eliminate entire rows/columns**, and shrink the search region before you start.
