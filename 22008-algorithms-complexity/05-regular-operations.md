# Regular Expressions

Finite automata can describe RE, and RE can describe finite automata.

## The regular operations

Definition: let $L$ and $M$ be languages over the same alphabet $\Sigma$. The regular operations are defined as follows:

1. Union: $L \cup M := \set {w | w \in L \text { or } w \in M}$
2. Concatenation: $LM := \set {uv | u \in L \text { and } v \in M}$
    - the fist part of the word $u$ is in $L$, and the second part of the word $v$ is in $M$.
    - $L$ isn't necessarily in $LM$ since $M$ may not include the empty word.
3. Kleene star: $L^* := \set {w_1,...,w_n | n \geq 0 \text { and } w_i \in L}$
    - any length of any combination of words in $L$. Since it is any length ($n \geq 0$) it also contains the empty word.
    - $L \in L^*$.
    - Another definition is $L^* = \set {L^n | \text { for } n=0 \to \infty}$ where for example $L^2 = LL$(concatenation)

### Regular languages are closed under regular operations

Theorem:

Let $L$ and $M$ be regular languages over $\Sigma$. Then:
1. $L \cup M$ 
2. $LM$
3. $L^*$

are all regular languages.

Proof:
1. Take finite automata that accept $L$ and $M$. 
2. $L \cup M$ : Use these and an OR jump to create a automaton $L \cup M$ that accepts both.
3. $LM$: Use jumps to jump from automaton $L$'s accepting states to automaton $M$'s start state to create $LM$.
4. $L^*$: Create a new start state that is also an accepting state in front of the old start state in $L$'s automaton to accept the empty word as well as $L$. Add in jumps from $L$'s accepting states to the start state. This allows as many $L^n$ as is required.
    - You can simplify further by only having the initial state as an accepting state.