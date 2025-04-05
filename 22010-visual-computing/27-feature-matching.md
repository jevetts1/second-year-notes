# Feature Matching

How do we match points with descriptors to align two images?

A simple approach is using SSD between two features' descriptors. However this can give good scores to bad matches. 

Choosing correspondences only based on descriptor will produce some wrong matches.

## Choosing Correct Correspondences - RANSAC

"Random sample consensus". 

1. Sample the number of data points required to fit the model.
2. Compute model parameters using the ampled data points
3. Score by the fraction of inliers within a preset threshold of the model

Repeat 1-3 until the best model is found.