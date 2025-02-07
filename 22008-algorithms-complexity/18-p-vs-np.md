# P vs NP

## Complexity Class P

A yes or no problem belongs to $P$ if there exists a TM that decides the problem in polynomial time: $O(n^d)$.

## Non deterministic TMs

An NTM is defined by the same objects as a TM but computations are interpreted differently. 

1. Write the problem as word $w$ on the tape.
2. Write the guess as word $v$ next to $w$.
3. Check whether the guess satisfies the problem.

The language accepted by a NTM is defined by:
- $w$ is accepted if there is SOME guess $v$ such that in the verification stage, the NTM halts in the yes state.
- $M$ solves the decision problem $L \in \Sigma _0 ^*$ if $w$ is accepted by $M$ iff $w \in L$

### Complexity of NTM

The running time is defined to be:
- the length of the shortest verifcation among all guesses if $w \in L$
- 1 if $w \notin L$.

A yes no problem belongs to NP if there exists NTM $M$ that decides it in complexity $O(n^d)$.

## Relationship between P and NP

- P: a solution can be found in polynomial time (if one exists)
- NP: a proposed solution can be verified in polynomial time

Theorem: $P \subseteq NP$.

Theorem: for any $L \in NP$ there is a TM that decides $L$ in complexity $O(2^{p(n)})$, where $p(n)$ is a polynomial. 