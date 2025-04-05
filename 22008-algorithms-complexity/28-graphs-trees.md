# Graph and Tree Algorithms

## Graphs

Every graph has:

- Set of vertices $V$
- Set of edges $E$
- A function $s: E \to V$ telling us the source of each edge
- A function $t: E \to V$ telling us the target of each edge

A **path** is a sequence of edges, where the target of each edge is the source of the next.

An undirected graph is **connected** if there is a path from any node to any other node. 

Cycles are paths that are made of distinct edges that start and end at the same node. 
- A graph is acyclic if it contains no cycles.

## Trees

A tree is an undirected graph which is connected and acyclic. However, normally we consider a tree to have a **heirarchy**.

If we define a **root** of a tree, then each node has a well defined distance from the root, which is its **level**. 

## Traversal

If your collection of nodes is a stack when looping over neighbours, the produced algorithm is **depth first search**. If the collection is a queue, the produced algorithm is a **breadth first search**.

### Preorder

1. Process current node
2. Process left subtree
3. Process right subtree

### Postorder

1. Process left subtree
2. Process right subtree
3. Process current node

### Inorder

1. Process left subtree
2. Process current node
3. Process right subtree