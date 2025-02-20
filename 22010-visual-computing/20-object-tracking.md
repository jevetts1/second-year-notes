# Object Tracking

## Change Detection

Given a static camera, we want to find meaningful changes: moving objects, people, etc. 
- Real time classification of foreground vs. background pixels.

### Challenges

We want to ignore uninteresting changes:
- Background fluctuations
- Image noise
- Weather changes
- Illumination changes and shadows
- Camera shake

### Different Foreground detection methods

1. Difference in frames > threshold
2. Difference in averages frames
3. Difference in median frames
4. The other one
5. Gaussian Mixture Model
- Higher dimensional - not just 1D features like the others (only pixel intensity)

### GMM

1. Compute pixel colour histogram for $N$ frames
2. Normalise $\hat H := H / \| H \|$
3. Model $\hat H$ as a mixture of $K$ guassians (usually 3-5)
4. For each subsequent frame:
    1. The pixel values $\textbf X$ belongs to Gaussian $k$ for which $\| \textbf {X} - \mu _k \|$ is minimum and $\| \textbf {X} - \mu _k \| < 2.5 \sigma _k$
    2. If $\omega_k / \sigma _k$ is large then classify as background pixel, otherwise it is foreground.
    3. Update histogram using the new pixel intensity.
    4. If $\hat H$ is very different to $H / \|H\|$ then $\hat H := H / \|H\|$ refit GMM.

## Template Matching

Two methods:
1. Take an image of the object and match the image to later frames to track it. 
    - Not robust to scale, changes in illumination or occlusion. 
    - Uses three metrics:
        1. Sum of absolute differences
        2. Sum of square differences
        3. Minimum normalised cross correlation
2. Histogram based tracking
    - Epanechnikov kernel
3. Feature Detection
    - Run through SIFT detector
    - For the points that lie in the bounding box, add them to the object model features.
    - Algorithm:
        1. Compute SIFT for each 