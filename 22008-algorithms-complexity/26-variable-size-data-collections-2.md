# Variable-size Data Collections 2

## Fixed resize strategy

- If we simply create a new array 1 size bigger than the last (stupid idea) then we get a amortized complexity of $O(n)$.

## Proportionally resize strategy

- What if we double (or multiply by some other factor) the size of the array every time it gets full?

This has an amortized of $O(1)$.

- When the array is 25% full, we can halve its size to save memory. This is also $O(1)$.

Space usage is $O(n)$.

## Doubly linked list

Each node points to previous and next elements, and there is a pointer at the beginning and the end of the list.

$O(1)$ add and get operations, and no wasted memory (other than the two sets of pointers)