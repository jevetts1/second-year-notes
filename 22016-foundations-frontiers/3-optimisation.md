# Optimisation

- Optimisation is fitting the model to data. 
- It doesn't always provide the best answer - usually just a good answer
- It fails if:
    - It produces bad answers
    - It doesn't converge
    - There are no gradients

## Algorithms that don't need gradients

1. Meat Sack
    - Manually doing optimisation
2. Analytic
    - Do maths to solve the problem directly
3. Brute Force
    - Try all combinations of parameters
    - Only works if discrete
4. Grid search
    - Nested loop
    - Explodes in higher dimensions
5. Random search
    - Sample dimensions with a uniform distribution
    - Works with higher dimensions
6. Hill climbing - gradient ascent
    - Take a random step. If its better, accept and repeat, if worse, go another direction.
    - Hyperparameters - step size. Scheduling, reducing step size as time goes on.
7. Shotgun Hill climbing
    - Do it a random number of times to avoid bad starting points.
8. Genetic Algorithm
    - Parameters, loss function, and crossover (breeding)
    - After crossover, draw the "survivors" with probability proportional to fitness

Optimisation needs a smooth objective - it won't work on fractals for example.