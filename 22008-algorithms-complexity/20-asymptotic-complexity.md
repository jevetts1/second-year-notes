# Asymptotic Complexity

$$0 \leq f(n) \leq cg(n)$$

implies that the function $f$ has complexity $O(g(n))$.

$\log$ functions are asymptotically equivalent complexity, no matter their base.

# Big Omega and Big Theta

Big O is an upper bound for a function's complexity.

Big Omega is the same as Big O but the lower bound, so $\Omega(g(n))$ has some multiple $c$ such that the function is always less than $cg(n)$. 

Big Theta is a function such that two constants $c_1, c_2$ show both the upper and the lower bound of the function. 