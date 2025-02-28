# Deep Neural Networks

- Networks with more than one hidden layer
- Intuition becomes more difficult!

## Composing two Shallow NNs

![](assets/2025-02-26-10-08-18.png)

Stacking these two networks end to end looks like this:

![](assets/2025-02-26-10-09-01.png)

Composing the two functions creates a much more complex line:

![](assets/2025-02-26-10-09-59.png)

## Combining two NNs

Skip out the $y$ connection and connect all $h$ neurons to all $h'$ neurons. 

![](assets/2025-02-26-10-32-49.png)

We change our notation to represent the network as matrices and vectors. 

![](assets/2025-02-26-10-36-44.png)

And we can represent the vectors and matrices by using different greek letters:

![](assets/2025-02-26-10-39-31.png)