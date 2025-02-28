# Master Theorem

General formula to find complexity of recurrences:

$$
T(1) = \text {constant}\\
T(n) = aT\left(\frac{n}{b}\right) + f(n)
$$

**Theorem**:

Let $c = \log_b a$.

1. If $f(n)$ is smaller than $O(n^c)$ then $T(n) = \Theta (n^c)$
2. If $f(n)$ is $\Theta(n^c)$ then $T(n) = \Theta (n^c \log n)$
3. If $f(n)$ is bigger than $\Omega(n^c)$ then $T(n) = \Theta (f(n))$

$n^c$ is the critical polynomial. 

Might have to prove case 2, and also remember the epsilon thing.