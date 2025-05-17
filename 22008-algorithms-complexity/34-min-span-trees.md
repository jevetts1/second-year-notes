# Minimum Spanning Trees

For a graph $G$ with $V$ and $E$, removing edges and or vertices results in a subgraph $G'$. 
- A subgraph $G'$ is spanning if it contains all the nodes in $G$ and is connected.
- A spanning tree is a subgraph that is spanning and is a tree (connected and acyclic)
- If $G$ is weighted, then a minimum spanning tree is a spanning tree whose total edge weight is minimised

Every connected graph has a MST.
- If it is acyclic, it is already a spanning tree of itself
    - If not, throw away an edge to break the cycle
    - Repeat this until all cycles are broken
- Find the minimum of these trees, and an MST is found.

## Kruskal's Algorithm

A greedy algorithm.

Steps:
1. Find the smallest weight and add it to the graph
2. Find the next smallest weight and add it, unless it creates a cycle, in which case do not. 
3. Repeat until the graph is connected.

### The Invariant

*A graph $T$ us acyclic and can be extended to a minimum spanning tree of $G$.*

In one loop body execution, we add edge $e$ to $T$. If $T'$ is the MST, then if $T'$ does contain $e$, then the loop invariant holds. If it doesn't contain $e$:
- adding $e$ must create a cycle
- $e'$ is the highest weight edge in the cycle that is not $e$.
- $e'$ must be at least as high as that of $e$. This is because we added $e'$ to $T'$ during its creation (it is an MST).
- Remove $e'$ from $T \cup \set{e}$ to break the cycle, leaving us with an MST.