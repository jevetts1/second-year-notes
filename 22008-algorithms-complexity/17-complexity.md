# Complexity

The complexity of an algorithm is how many steps it takes to obtain an output. It is also the number of steps the corresponding TM would take to halt. But it may not halt - this causes problems. 
- We restrict our attention to decidable functions - where all inputs halt. 

Another problem is machines that halt at different steps for inputs of the same size. 
- We can take the maximum steps for an input of a given length and call that the complexity. 

Focusing on tiny details of the TM (like whether you start on the start symbol or not) is not useful. So focus on the *order of growth* instead.

For a function $f(n)$ that has lots of little details, we choose a function $g(n)$ such that there exists a constant $c$ such that $f(n) \leq cg(n)$ for all $n$. This means that at some value $c$, the $g$ function is larger than $f$. For example:

$$f(n) = 2n + 1$$

We choose $g(n) = n$, because we can select $c=3$ such that $f(n) < cg(n)$ for all $n$. So the complexity of $f$ is $O(g(n)) = O(n)$. 

You can also choose to look at the average time complexity, and the space complexity, for memory. 