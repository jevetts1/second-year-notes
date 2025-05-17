# Hash Tables 

- Store items, each associated with a key
- They are dictionaries - and many other names
- Store: $O(1)$, search: $O(1)$ (on average, under certain assumptions)

## Hashing Functions

- Use a function $h(x)$ to compute the index of the array from the key.
- Problem - hashing functions are not injective
    - So there are two keys that cause a hashing collision, for any hashing function

### Chaining

- Having multiple items in each hash when a collision happens
- Have pointers in the index to find the correct entry
- Slower than constant time, since you have to search through the other datastructure 

1. Go to address with hash
2. Search down the linked list for the item with the correct key

For adding, just add the element at the start of the list.

Storage: $O(n)$.
Assuming hashing in uniform:
- each slot should hold $n/M$ items. This is called the load factor, and is denoted $\alpha$
- so a typical list can be searched in $O(\alpha)$
- average case of `get`, `contains`, and `delete` is $\Theta (1 + \alpha)$

#### Resizing

If your hash table gets too full (over the limit $\alpha$ that you want to set, e.g. 0.75) then you have to resize
- New hashing function to address all indices in the new array
- Create new array
- Rehash every item in the old array

Amortized complexity doesn't change, when using strategies like the doubling size strategy.

## Open Addressing

- If you find a slot that is taken, move to the next available slot. Linear Probing
    - Or multiply the index by some factor.

Probe sequence:
- Check the availability of the hashes in some predefined order: $h(k,0), h(k,1), h(k,2),...$

Easiest sequence is just to check the next slots sequentially until an empty one is found, wrapping back to the start when required.

### Getting

Search for the key until an empty slot is found.

### Deleting

- Delete the item but replace it with a tombstone, so you know that an item used to be there
- Or rehash everything as if the deleted item was never there
    - Since the clusters are *ideally* not too big, doing this shuffling method should not take too long.

### Complexity of put

Linear probing has a complexity of $\frac{1}{1 - \alpha}$. 

So it has complexity $\Theta (1 + \frac{1}{1 - \alpha})$.

On average, all the operations have constant time.

### Primary clustering

This is an issue; as the clusters grow, more keys are hashed into the same cluster which causes it to grow more.

Solutions:
- quadratic probing: $h(k,i) = h(h(k) + c_1i + c_2i^2) \mod M$
- double hashing: $h_1(k,i) = h_1(k) + ih_2(k) \mod M$