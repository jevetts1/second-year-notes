# Reducing Overfitting

## Generalisation

- Training data only covers a subset of the expected input domain.
- All the data is never available in the real world.

Models overfit when the training loss decreases at the cost of testing and validation increasing.

## Early Stopping

- Allow the model to train, evaluating at every epoch checking validation performance
- Stop training until validation starts worsening.
- Or use the last $n$ time steps, using momentum to keep moving over small increases in validation loss. 
- Checkpointing - store the model with best validation, so that when validation loss increases, revert to the best model. 

## Data Augmentation

- Expanding the dataset to include more examples
    - for images:
        - flip, scale, rotate
        - colours
        - crop
        - add noise
    - this could change the input distribution such that it no longer models the real distribution
    - for audio:
        - pitch
        - gauss noise
        - the speed
    - for text: 
        - add typos
        - substitute words for synonyms
        - add in noise - random words
        - sentence shuffling

This risks overfitting to augmented data, so it shouldn't always be used. 

## Dropout

Reduces over reliance on certain features.
- Every training iteration, drop a certain proportion of nodes, training the rest. 
- Makes training take longer
- If a specific feature is extremely important, dropout may prevent it from being utilised
- Turn off dropout for deployment.
- This is regularisation, and does not improve training set. The only reason to use these methods is to prevent overfitting

## Explicit Regularisation

- L1
    - applies a penalty term to loss - the sum of magnitude of each weight. Keeps weights closer to zero. Reduces exploding gradients and weights.
- L2
    - Same as L1 but square instead of absolute.
- Elastic
    - Use both, mixed with some parameter.