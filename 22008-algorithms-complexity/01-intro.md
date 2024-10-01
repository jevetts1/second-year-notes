# Semester 1
1. Describe models of computatoion and classes of formal grammar and languages.
2. Design algorithms as automata 
3. Prove mathematically that some computations are undecidable

# Describing algorithms
## Example

A binary word $w$ is defined as a list of any number of 1s and 0s, e.g. $w = \set {001, 0110101, 01011,...}$

We want to describe the complexity of the following questions:

### Is there an even number of 0s?

This can be implemented by flipping a bit every time we encounter a 0, and if we finish reading the word and the counter is at its start state there are even number of 0s. 

#### Memory
Finite memory since it uses one bit.

#### Flowchart
Simple.

### Is there an equal number of 0s and 1s?

We can have a counter that increases on encountering a 1 and decreases on encountering a 0.

#### Memory
Unbounded - there could be an undefined string of 0s or 1s in a row meaning the counter can grow indefinitely.

#### Flowchart
Simple.

### Is there an prime number of 0s?

This would require a counter again and once all the 0s are counted to apply a prime number checking algorithm.

#### Memory
Unbounded for same reason.

#### Flowchart
More complex.
