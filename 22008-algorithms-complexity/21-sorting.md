# Sorting Algorithms

Loop invariant
- the loop invariant holds each time we enter the loop
- executing the loop restores the invariant

## Loop Invariant

```
...
setup_code();
...
while (guard) {
    ...
    loop_body();
    ...
}
```

Given a predicate $P$ is true in the setup, and the guard is true, $P \land \text{guard} = 1$, then $P$ must be true at the end of the loop body.

For any number of loops, $P$ is always true at the start of the loop and at the end of the loop body.

After the loop, $P \land \lnot \text{guard} = 1$. 

