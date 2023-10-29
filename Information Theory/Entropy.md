## Entropy

### Entropy

The entropy $H(X)$ of a discrete random variable $X$ is defined by

$$
H (X) = - \sum_{x} \mathbb{P}_{X} (x) \log \mathbb{P}_{X} (x),
$$

which can be written as the expectation of the random variable $\log \mathbb{P}_{X} [x]$

$$
H (X) = - \mathbb{E}_{X} \left[
    \log \mathbb{P}_{X} (x)
\right].
$$

### Joint entropy

The joint entropy $H(X, Y)$ of a pair of discrete random variables $X, Y$ with a joint distribution $\mathbb{P}_{X, Y} (x, y)$ is defined as

$$
\begin{aligned}
H (X, Y)
& = - \mathbb{E}_{X, Y} \left[
    \mathbb{P}_{X, Y} (x, y)
\right]
\\
& = - \sum_{x, y} \mathbb{P}_{X, Y} (x, y) \log \mathbb{P}_{X, Y} (x, y)
\end{aligned}
$$

### Conditional entropy

Given a joint probability $\mathbb{P}_{X, Y} (x, y)$, 
the conditional entropy $H (Y \mid X)$ is defined as 

$$
\begin{aligned}
H(Y \mid X) 
& = - \mathbb{E}_{X, Y} \left[
    \mathbb{P}_{Y \mid X} (y \mid x)
\right]
\\
& = - \sum_{x, y} \mathbb{P}_{X, Y} (x, y) \log \mathbb{P}_{Y \mid X} (y \mid x)
\\
& = - \sum_{x} \mathbb{P}_{X} (x) \sum_{y} \mathbb{P}_{Y \mid X} (y \mid x) \log \mathbb{P}_{Y \mid X} (y \mid x)
\\
& = \sum_{x} \mathbb{P}_{X} (x) H (Y \mid x)
\end{aligned}
$$

## Relative entropy

### Relative entropy (KL Divergence)

The relative entropy or Kullback–Leibler (KL) divergence between two distributions $p (x), q (x)$ for the same random variable $X$ is defined as 

$$
\begin{aligned}
D (p \Vert q) 
& = \mathbb{E}_{X} \left[
    \log \frac{ p (X) }{ q(X) }
\right]
\\
& = \sum_{x} p (x) \log \frac{ p (x) }{ q (x) }
\end{aligned}
$$

## Mutual Information

### Mutual information

The mutual information $I (X; Y)$ is the relative entropy between the joint distribution of two random variables $X, Y$ and the product distribution

$$
\begin{aligned}
I (X; Y) 
& = \mathbb{E}_{X, Y} \left[
    \frac{ 
        \mathbb{P}_{X, Y} (X, Y) 
    }{ 
        \mathbb{P}_{X} (X) \mathbb{P}_{Y} (Y) 
    }
\right]
\\
& = \sum_{x, y} \mathbb{P}_{X, Y} (x, y) \log \frac{ 
    \mathbb{P}_{X, Y} (x, y) 
}{ 
    \mathbb{P}_{X} (x) \mathbb{P}_{Y} (y) 
}
\\
& = D (\mathbb{P}_{X, Y} \Vert \mathbb{P}_{X} \mathbb{P}_{Y})
\end{aligned}
$$

Also, the mutual information can be rewritten using entropies 

$$
\begin{aligned}
I (X; Y)
& = \sum_{x, y} \mathbb{P}_{X, Y} (x, y) \log \frac{ 
    \mathbb{P}_{X, Y} (x, y) 
}{ 
    \mathbb{P}_{X} (x) \mathbb{P}_{Y} (y) 
}
\\
& = \sum_{x, y} \mathbb{P}_{X, Y} (x, y) \log \frac{ 
    \mathbb{P}_{X \mid Y} (x \mid y) \mathbb{P}_{Y} (y)
}{ 
    \mathbb{P}_{X} (x) \mathbb{P}_{Y} (y) 
}
\\
& = 
- \sum_{x, y} \mathbb{P}_{X, Y} (x, y) \log \mathbb{P}_{X} (x) 
+ \sum_{x, y} \mathbb{P}_{X, Y} (x, y) \log \mathbb{P}_{X \mid Y} (x \mid y) 
\\
& = 
- \sum_{x} \mathbb{P}_{X} (x) \log \mathbb{P}_{X} (x) 
+ \sum_{x, y} \mathbb{P}_{X, Y} (x, y) \log \mathbb{P}_{X \mid Y} (x \mid y) 
\\
& = 
H (X) - H (X \mid Y)
\end{aligned}
$$

Then according to the chain rule of entropy $H (X, Y) = H (Y) + H (X \mid Y)$,

$$
I (X; Y) = H (X) - H (X \mid Y) = H (X) + H (Y) - H (X, Y).
$$

### Conditional mutual information

$$
\begin{aligned}
I (X; Y \mid Z) 
& = \sum_{x, y, z} \mathbb{P}_{X, Y, Z} \log \frac{
    \mathbb{P}_{X, Y \mid Z}
}{
    \mathbb{P}_{X \mid Z} \mathbb{P}_{Y \mid Z}
}
\\
& = - \sum_{x, y, z} \mathbb{P}_{X, Y, Z} \log \left[
    \mathbb{P}_{X \mid Z} \mathbb{P}_{Y \mid Z}
\right]
+ \sum_{x, y, z} \mathbb{P}_{X, Y, Z} \log \mathbb{P}_{X \mid Y, Z}
\\
& = - \sum_{x, z} \mathbb{P}_{X, Z} \log \mathbb{P}_{X \mid Z} 
+ \sum_{x, y, z} \mathbb{P}_{X, Y, Z} \log \mathbb{P}_{X \mid Y, Z}
\\
& = H (X \mid Z) - H (X \mid Y, Z)
\end{aligned}
$$

## Chain rule 

### Chain rule for entropy

The joint entropy between 2 variables can be decomposed into an entropy and a conditional entropy 

$$
\begin{aligned}
H (X, Y) 
& = - \sum_{x} \sum_{y} \mathbb{P}_{X, Y} (x, y) \log \mathbb{P}_{X, Y} (x, y)
\\
& = - \sum_{x} \sum_{y} \mathbb{P}_{X, Y} (x, y) \log \left[
    \mathbb{P}_{X \mid Y} (x \mid y) \mathbb{P}_{Y} (y)
\right]
\\
& = - \sum_{x} \sum_{y} \mathbb{P}_{X, Y} (x, y) \log \mathbb{P}_{X \mid Y} (x \mid y)
- \sum_{x} \sum_{y} \mathbb{P}_{X, Y} (x, y) \log \mathbb{P}_{Y} (y)
\\
& = - \sum_{x} \sum_{y} \mathbb{P}_{X, Y} (x, y) \log \mathbb{P}_{X \mid Y} (x \mid y)
- \sum_{y} \mathbb{P}_{Y} (y) \log \mathbb{P}_{Y} (y)
\\
& = H(X \mid Y) + H (Y).
\end{aligned}
$$

The chain rule can also be applied to conditional entropy.

$$
\begin{aligned}
H (X, Y \mid Z) 
& = - \sum_{x} \sum_{y} \sum_{z} \mathbb{P}_{X, Y} (x, y, z) \log \mathbb{P}_{X, Y, \mid Z} (x, y \mid z)
\\
& = - \sum_{x} \sum_{y} \sum_{z} \mathbb{P}_{X, Y, Z} (x, y, z) \log \left[
    \mathbb{P}_{X \mid Y, Z} (x \mid y, z) \mathbb{P}_{Y \mid Z} (y \mid z) 
\right]
\\
& = - \sum_{x} \sum_{y} \sum_{z} \mathbb{P}_{X, Y, Z} (x, y, z) \log \mathbb{P}_{X \mid Y, Z} (x \mid y, z)
- \sum_{x} \sum_{y} \sum_{z} \mathbb{P}_{X, Y, Z} (x, y, z) \log \mathbb{P}_{Y \mid Z} (y \mid z)
\\
& = - \sum_{x} \sum_{y} \sum_{z} \mathbb{P}_{X, Y, Z} (x, y, z) \log \mathbb{P}_{X \mid Y, Z} (x \mid y, z)
- \sum_{y} \sum_{z} \mathbb{P}_{Y, Z} (y, z) \log \mathbb{P}_{Y \mid Z} (y \mid z)
\\
& = H(X \mid Y, Z) + H (Y \mid Z).
\end{aligned}
$$

By treating $X_{2}, \dots, X_{n}$ as one joint variable, the chain rule for joint entropy with multiple variables $X_{1}, \dots, X_{n}$ can be derived

$$
\begin{aligned}
H (X_{1}, \dots, X_{n}) 
& = H (X_{1}) + H (X_{2}, \dots, X_{n} \mid X_{1})
\\
& = H (X_{1}) + H (X_{2} \mid X_{1}) + H (X_{3}, \dots, X_{n} \mid X_{2}, X_{1})
\\
& = H (X_{1}) + H (X_{2} \mid X_{1}) +, \dots, + H (X_{n} \mid X_{n - 1}, \dots, X_{1})
\\
& = \sum_{i = 1}^{n} H (X_{i} \mid X_{i - 1}, \dots, X_{1})
\end{aligned}
$$

### Chain rule for mutual information

$$
\begin{aligned}
I (X_{1}, \dots, X_{n}; Y) 
& = H (X_{1}, \dots, X_{n}) - H (X_{1}, \dots, X_{n} \mid Y)
\\
& = \sum_{i = 1}^{n} H (X_{i} \mid X_{i - 1}, \dots, X_{1})
- \sum_{i = 1}^{n} H (X_{i} \mid Y, X_{i - 1}, \dots, X_{1})
\\
& = \sum_{i = 1}^{n} \left[
    H (X_{i} \mid X_{i - 1}, \dots, X_{1}) 
    - H (X_{i} \mid Y, X_{i - 1}, \dots, X_{1}) 
\right]
\\
& = \sum_{i = 1}^{n} I (X_{i}; Y \mid X_{i - 1}, \dots, X_{1})
\end{aligned}
$$