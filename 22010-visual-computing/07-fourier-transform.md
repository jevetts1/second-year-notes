# Fourier Transform

## Periodic Functions

A function $f(x)$ is periodic if:
- it is defined for all real $x$
- it has some positive number $T$, the period, such that $f(x) = f(x+T)$

## Fourier Series

If a function $f(x)$ is periodic with a period of $2\pi$, the function can be represented by the fourier series:

$$f(x) = \frac {a_0} {2} + \sum \limits _{n=1} ^\infty a_n \cos(nx) + \sum \limits _{n=1} ^\infty b_n \sin(nx)$$

### Using integration to determine $a_n$ and $b_n$ 

#### Product of sines

$$n \neq m: \int \limits _{-\pi} ^{\pi} \sin(nx) \sin(mx) dx=0$$

$$n = m: \int \limits _{-\pi} ^{\pi} \sin(nx) \sin(mx) dx=\pi$$

#### Product of cosines

$$n \neq m: \int \limits _{-\pi} ^{\pi} \cos(nx) \cos(mx) dx=0$$

$$n = m: \int \limits _{-\pi} ^{\pi} \cos(nx) \cos(mx) dx=\pi$$

#### Product of sine and cosine

$$\forall n,m: \int \limits _{-\pi} ^{\pi} \sin(nx) \cos(mx) dx=0$$

### Computing $a_0$

$$\int \limits _{-\pi} ^{\pi} f(x) dx$$

$$ = \int \limits _{-\pi} ^{\pi} \left [ \frac {a_0} {2} + \sum \limits _{n=1} ^\infty a_n \cos(nx) + \sum \limits _{n=1} ^\infty b_n \sin(nx) \right ] dx$$

$$ = \pi a_0 + \sum \limits _{n=1} ^\infty a_n \int \limits _{-\pi} ^{\pi} \cos(nx) dx + \sum \limits _{n=1} ^\infty b_n \int \limits _{-\pi} ^{\pi} \sin(nx) dx$$

Since $n \neq 0$, all of the cosine and sine integrals are 0.

$$= \pi a_0 + \sum \limits _{n=1} ^\infty a_n \cdot 0 + \sum \limits _{n=1} ^\infty b_n \cdot 0 = \pi a_0$$

$$a_0 = \frac {1} {\pi} \int \limits _{-\pi} ^{\pi} f(x) dx$$

### Computing $a_n$

Multiply $f(x)$ by $\cos(mx)$ for $m > 0$.

$$\int \limits _{-\pi} ^{\pi} f(x) \cos(mx) dx$$

$$ = \int \limits _{-\pi} ^{\pi} \left [ \frac {a_0} {2} + \sum \limits _{n=1} ^\infty a_n \cos(nx) + \sum \limits _{n=1} ^\infty b_n \sin(nx) \right ]\cos(mx) dx$$

1st term: $\int \limits _{-\pi} ^{\pi} \frac {a_0} {2} \cos(mx) dx = 0$
**2nd term**: $\sum \limits _{n=1} ^\infty a_n \int \limits _{-\pi} ^{\pi} \cos(nx) \cos(mx) dx = \pi a_m$
- since the the only non-zero term is when $n=m$

3rd term: $\sum \limits _{n=1} ^\infty b_n \int \limits _{-\pi} ^{\pi} \sin(nx) \cos(mx) dx = 0$

So

$$a_n = \frac {1} {\pi} \int \limits _{-\pi} ^{\pi} f(x) \cos(nx) dx$$

So in this example, we have found the coefficient for the frequency with period $n$.

We can apply this method for $n=0,1,2,3,...$

### Computing $b_n$

We use the same method but with sine:

$$\int \limits _{-\pi} ^{\pi} f(x) \sin(mx) dx$$

$$b_n = \frac {1} {\pi} \int \limits _{-\pi} ^{\pi} f(x) \sin(nx) dx$$

