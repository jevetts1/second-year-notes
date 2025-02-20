# Gradient Descent

**Step 1.** Compute the derivatives of the loss with respect to the parameters:

$$
\frac{\partial L}{\partial\phi} =
\left [
\begin {array} {}
\frac{\partial L}{\partial\phi_0}\\
\frac{\partial L}{\partial\phi_1}\\
...\\
\frac{\partial L}{\partial\phi_N}\\
\end {array} 
\right ]
$$

**Step 2.** Then update the parameters with a scalar $\alpha$ to scale the change.

$$\phi := \phi - \alpha \frac{\partial L}{\partial\phi}$$

# Stochastic Gradient Descent

Compute gradient based on only a subset of points - a mini batch. Instead of summing all the gradients for all the points to update parameters, update parameters using a **subset of the dataset**. Across an epoch, all the datapoints are used, so the mini-batches add up to the dataset. 
- The loss function is slightly different for every mini batch, so gradients are (almost) always different. This adds a level of randomness that helps avoid local optima.