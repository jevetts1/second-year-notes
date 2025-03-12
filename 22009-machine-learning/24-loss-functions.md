# Loss Functions

- Training datasets consist of $I$ pairs of input/output examples: $L[\phi]$
    - This function returns a smaller scalar when the model performs better

## Log Likelihood

We want to find the parameters $\phi$ that maxmimise the likelihood of predicting $\bf{y}$ given $\bf{x}$:

$$\hat \phi =  \argmax _\phi \left[\prod \limits _{i=1} ^I P(\mathbf{y}_i|\mathbf{x}_i)\right]$$

Since this product goes to zero, we use $\log$ to make the product into addition and keep machine precision.

$$
\hat \phi =  \argmax _\phi \sum \limits _{i=1} ^I \log \left[  P(\mathbf{y}_i|\mathbf{x}_i)\right] \\
\hat \phi = \argmin_\phi - \sum \limits _{i=1} ^I \log \left[  P(\mathbf{y}_i|\mathbf{x}_i)\right]\\
= \argmin_\phi L[\phi]
$$

Changing to $\argmin$ makes the problem a minimisation problem instead of maximisation.

## Recipe for a Loss function

1. Choose a probability distribution $P(\mathbf{y}_i|\mathbf{x}_i)$