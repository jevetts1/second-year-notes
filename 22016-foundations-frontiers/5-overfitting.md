# Lecture 5

## Measurement Theory

In ML, if you can't measure it, you can't improve it

## Bad Data

- Insufficient - not enough data
- Spurious correlation
    - "correctly" finding correlation through the wrong proxy in the training set
- No correlation
    - using features that have no correlation to the output
- Imbalanced data
    - more truths than falses for example
- Selection bias
    - e.g. survivorship bias
- Runtime mismatch
    - Extrapolation instead of interpolation
- Missing context
    - Need to check answers before deploying
- Bias
- Data poisoning
    - Hacking by changing the data - malicious

# Feature Importance

- Correlation is "information" between variables
- Feature importance is "information" between variables *in the context of others*

## Ablation studies

- Removing a feature and seeing how performance changes
- Very expensive to keep training over and over

## Permutation test

- Testing if randomly swapping elements in the group changes the performance
- Permutation Feature Importance
    - How does performance change if you shuffle the values of a feature?

## Shapley Values for feature importance