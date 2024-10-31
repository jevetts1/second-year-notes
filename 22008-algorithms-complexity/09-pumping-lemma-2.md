# Pumping Lemma

## Proving a language isn't regular

1. Suppose the language is regular.
2. Then, by the pumping lemma, all words with length $\geq n$ can be pumped.
3. Show that for *any* $n$, ther is some word $w \in L$ of length $\geq n$ that can't be pumped.
4. Proof by contradiction. 

## Example

$$L = \set {w \in \set {0,1}^* | w \text { has an equal number of 0s and 1s}}$$

1. Suppose that $L$ is regular. Then by the pumping lemma, there is some $n > 0$ such that all words with $|w| \geq n$ can be pumped.
2. Define $w = 0^n1^n \in L$, and note that $|w| = 2n \geq n$. $n$ is an arbitrary number. 
3. If the word $w$ can be pumped, then it must be represented by $xyz$ such that:
    - $y \neq e$
    - $|xy| \leq n$
        - this means that y has to occur in the first $n$ letters, meaning in our example it is in the block of 0s. 
    - $xy^iz$ has an equal number of 0s and 1s for all $i \geq 0$

If the word is pumpable, we should be able to pump the $y$ down to 0 repetitions, to get $xz$. Since the $y$ was in the 0s, the number of 1s has remained. But now the number of 0s does not equal the number of 1s which means it is not in the language! Contradiction. 

## General Proof

1. Suppose that $L$ is regular. Then by the pumping lemma, there is some $n > 0$ such that all words with $|w| \geq n$ can be pumped.
2. Make a clever choice of $w \in L$ with $|w| \geq n$. The choice needs to work for any $n$.
3. By the pumping lemma, there is some division $w = xyz$ such that
    - $y \neq e$
    - $|xy| \leq n$
    - $xy^iz \in L$ for $i \geq 0$
4. For any such division, use the fact that $y \neq e$ or $|xy| \leq n$ to find some $i$ such that $xy^iz \notin L$.
5. Contradiction!

1,3,5 are the same for all proofs, but 2 and 4 are determined by the language we are trying to prove.

## Common mistakes

- DO NOT specify $n$ in the proof, it must be arbitrary. 
- DO NOT specify what the exact decomposition of $xyz$ is, it must be general.