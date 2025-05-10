# Dijkstra's Algorithm

## Graphs

- Adjacency list - a variable sized collection storing all nodes that are adjacent to it.
- Adjacency matrix - a square matrix of 0s and 1s. A one is stored at the column and row where there is an edge.
    - For adjacency matrix $A$, $A \times A$ produces all paths of length two!
    - $A^3$ gives 3 length paths, etc.
    - For sparse graphs, this is not efficient storage for lots of nodes.


### Weighted Graphs

- For list, store tuples of nodes and weights
- For matrix, store the weight instead of a 1.

## Shortest Paths

The setup:
- a directed graph with vertices $V$ and edges $E$
- a weight function $w(u,v)$ that gives the weight between $u$ and $v$.

A path from $u$ to $v$:
- $u, v_1, v_2, ..., v_n, v$
- $w(u, v_1), w(v_1, v_2), ..., w(v_n, v)$

Dijkstra is an extension of the breadth first search. It uses a priority queue to look at shortest paths first.

## Dijkstra Setup

- Source $s$ - fixed
- $\delta (u)$ is the shortest path - truth.
- $d (u)$ is the shortest estimate for the path. 

There are a set $S$ of settled vertices - the paths whose shortest path we know. 

The algorithm is extended one of the nodes in $S$ to all the nodes it is connected to not in $S$ - the shortest of which is then settled. 

## The algorithm

1. Start at $d(s) = 0$
2. Use a priority queue $Q$. They are sorted by $d(u)$, with shortest first. 
3. Grab highest priority $u$ from $Q$, then explore all nodes $v$ it is connected to.
4. If the path through $u$ plus $w(u,v)$ is shorter than $d(v)$, set $d(v)$ to this new shortest path. 
5. Change the priority in $Q$ of $v$

## Loop invariant

At the start, $S$ contains only settled vertices: $\forall u \in S, \delta(u) = d(u)$.

## Complexity

$$\Theta ((|E| + |V|) \log |V|)$$

If the number of edges are close to $|V|^2$, then:
- keep vertices in an array with their $d(u)$
- use linear seach instead of priority queue.

This has complexity $\Theta(|V|^2)$

Using bucket queues instead of heaps (when weights are integers for example)