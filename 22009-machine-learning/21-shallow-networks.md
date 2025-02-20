# Shallow Networks

![](assets/2025-02-12-15-43-59.png)

Example of a shallow network, with activation functions $a$.

ReLU: Rectified linear unit. 
- Activation functions allow some of the parameters to be active while others are not, which adds complexity to the function the network can model. 

We abstract away some detail with hidden units:

![](assets/2025-02-12-15-46-04.png)

Graphical representation:

![](assets/2025-02-12-15-48-31.png)

Biases are usually omitted from the graph.

*with enough hidden units, a shallow network can describe any continuous function to arbitrary accuracy.*

The number of regions that a shallow neural network can separate the inputs into is:

![](assets/2025-02-12-15-59-43.png)