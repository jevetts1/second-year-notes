# Random Forests

An ensemble model, uses many different models together to produce an output.

They are a collection of decision trees which can learn. 

The main idea is to overcome the main weakness of decision trees, which is that they are very reliant on training data. This makes them overfit to it.
- Intuition is that if there are lots of trees, the average overfitting makes a more general pattern.

The RF picks the modal class of all the decision trees.

For regression, we could pick:
- the mean
- the median


## Creating a RF

The two key steps are:

1. Create a bootstrapped dataset.
    - select a random row from the training dataset.
    - append it to a new dataset.
    - repeat until the new set is the size of the training set.
    - this results in repeated rows and some missing rows, so it is different to the training set. 
2. Use this to create a decision tree.
    - at each node, only consider a random set of features. 

Repeat these steps $n$ times. Usually at least 100.

## Overfitting

Overfitting can be limited by setting a maximum question depth. This stops the tree from splitting every single sample into its own leaf node, generalising better.

This can cause issues with *underfitting* on other parts of the data though. 
- For example, if there a three distinct groups, a max depth of 1 may classify the first group well but leave the other 2 as part of the same classification. 
- One circumvention is to stop when a certain number of samples are left at a node, for example when 3 samples are left. This prevents the underfitting at the hard cap max depth.

These methods help to reduce computation in a RF as well.

## Limitations

- You don't have to store all the different datasets for each tree, only the leaf node values
- You have to store all the trees themselves
- Computation can be high with lots of trees
- Bootstrapping may result in some training data not (or barely) being used. 

### Pros

1. No complex hyperparameters
2. Does not overfit
3. Not sensitive to outliers

### Cons

1. Computationally inefficient
2. Reliant on number of trees
3. Difficult to explain results