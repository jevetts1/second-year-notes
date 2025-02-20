# Interesting Sorting Algorithms

## Shell Sorts

Insertion sort is slow when items are in reverse order. Shell sort improves this by beginning with longer jumps. 

### Algorithm

1. Pick a jump size, e.g. 7
2. Check all elements that are 7 apart, and use the usual insertion sort on them.
3. Choose another number and repeat
4. Repeat until jump size = 1, then after this you are done.

A sort with stride length 7 is called 7-sorting. A regular insertion sort is called 1-sorting.

Since shell sorting always ends in 1-sorting, and we proved that it is correct, shell sorting is also correct.

**Theorem.** If a list is already $p$-sorted, and then you $q$-sort it, then the result is still $p$-sorted: you never lose sortedness, only stay the same or increase!

- Works in place
- No recursion
- So doesn't take up any extra space!

## Mergesort

The complexity of mergesort is defined recursively:
- $T(1) = 0$
- $T(n) = 2T(\frac{n}{2}) + n$
- So: $T(2^k) = 2^kT(1) + k \cdot 2^k = k \cdot 2^k$
- $n = 2^k \implies T(n) = n \log_2 n$

- Mergesort is much faster
- Doesn't sort in place
- Recursive, so uses more memory