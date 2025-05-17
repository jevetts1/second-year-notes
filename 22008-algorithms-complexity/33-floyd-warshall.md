# Floyd-Warshall

Computes shortest paths between all pairs of nodes in the graph.

## Dynamic Programming

- Often applies to problems that can be broken apart in some way.

## The problem

Given a finite directed graph with weighted edges, such that no cycle has a negative total weight, determine the function 

$$\delta(u,v)$$ 

for all vertex pairs $u, v$.

### Divide and Conquer

Shortest paths have the Bellman Optimality property:
- if a shortest path from $u$ to $v$ goes through $w$, then:
    - $uw$ is optimally short
    - and $wv$ is optimally short

Suppose there are $n$ vertices $1,..,n$. Define $\delta$ with three arguments $\delta(i,j,k)$ which gives the shortest path from $i$ to $j$, only passing through nodes $1,...,k$ as intermediate nodes. 
- $\delta(i,j,0)$ is a direct edge
- $\delta(i,j,n)$ is the ultimate shortest path what we want

The new recurrence:

$$\delta(i,j,k) = \min(\delta(i,j,k-1), \delta(i,j,k-1) + \delta(k,j,k-1)$$

Since the third argument gets smaller each recursion, it terminates at $k=0$.

But it has terrible complexity! 3 sub calls from each call, so $O(3^n)$. 

If we avoid duplicate calls in the tree, we can reduce complexity. Using Dynamic Programming.

### Dynamic Programming Solution

Idea: keep a table of previously computed solutions. 
- The new complexity is now $i \cdot j \cdot k$ which is $\Theta (|V|^3)$.
- Once a larger $k$ in $\delta(i,j,k)$ has been calculated, discard all the calculations from the lower $k$. So instead keep everything in a 2D array, indexing $i$ and $j$. 

This uses dynamic programming because the sub problems in the recursions overlap. 