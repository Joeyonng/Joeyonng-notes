# Rademacher Complexity

## Rademacher distribution

A Rademacher distribution is a discrete probability distribution where a random variate $X$ has the equal probability of being +1 and -1.

## Rademacher complexity

### Definitions

Given an i.i.d sample $\mathcal{S} = \{ z_{1}, \dots, z_{n} \}$ from the distribution $\mathbb{P}_{\mathcal{Z}^{n}}$ and $n$ independent Rademacher random variables $\sigma = \{ \sigma_{1}, \dots, \sigma_{n} \}$,
the **empirical Rademacher complexity** of a class of binary function $\mathcal{F}$ is defined as

$$
\mathrm{Rad}_{\mathcal{F}} (\mathcal{S}) = \mathbb{E}_{\sigma} \left[
    \sup_{f \in \mathcal{F}} \left\lvert 
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} f (z_{i}) 
    \right\rvert
\right],
$$

which is a function of the random variable $\mathcal{S}$ and therefore is a random variable. 

Then the **Rademacher complexity** is defined as the expectation of the empirical Rademacher complexity over all i.i.d samples of size $n$

$$
\mathrm{Rad}_{\mathcal{F}} (n) = \mathbb{E}_{\mathcal{S}} \left[
    \mathrm{Rad}_{\mathcal{F}} (\mathcal{S})
\right] = \mathbb{E}_{\mathcal{S}} \left[
    \mathbb{E}_{\sigma} \left[
        \sup_{f \in \mathcal{F}} \left\lvert 
            \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} f (z_{i}) 
        \right\rvert
    \right]
\right].
$$

### Intuitions

If $\mathcal{F}$ contains so many functions such that there exists some functions in $\mathcal{F}$ that can always output the same signs with the random generated Rademacher random variables,
then $\mathcal{F}$ will have a high Rademacher complexity according to the definition. 

The empirical Rademacher complexity measures the ability of the functions in a function class $\mathcal{F}$ to fit the random noise for a fixed sample $\mathcal{S}$,
which is described by the maximum correlation over all $f \in \mathcal{F}$ between $f (z_{i})$ and $\sigma_{i}$.

Therefore,  the Rademacher complexity of $\mathcal{F}$ measures the expected noise-fitting-ability of $\mathcal{F}$ over all data sets $\mathcal{S} \in \mathcal{Z}^{n}$ that could be drawn according to the distribution $\mathbb{P}_{\mathcal{Z}^{n}}$.

## Rademacher theorem

The primary use of the Rademacher complexity is to upper bound the following quantity 

$$
\mathbb{E}_{\mathcal{S}} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        \frac{ 1 }{ n } \sum_{i = 1}^{n} f (z_{i}) - \mathbb{E}_{Z} [f (z_{i})]
    \right\rvert
\right] \leq 2 \mathrm{Rad}_{\mathcal{F}} (n).
$$

:::{prf:proof} Rademacher theorem
:label: rademacher-theorem
:class:dropdown

We introduce a ghost sample $\mathcal{S}' = \{ \hat{z}_{1}, \dots, \hat{z}^{n} \}$ that is also i.i.d drawn from $\mathbb{P}_{\mathcal{Z}^{n}}$,
which means

$$
\mathbb{E}_{\mathcal{S}'} \left[ 
    \frac{ 1 }{ n } \sum_{\hat{z}_{i} \in \hat{\mathcal{S}}} f (\hat{z}_{i}) 
\right] = \mathbb{E}_{Z} [f (z_{i})].
$$

Therefore, we can get the following results

$$
\begin{aligned}
\mathbb{E}_{\mathcal{S}} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        \frac{ 1 }{ n } \sum_{i = 1}^{n} f (z_{i}) - \mathbb{E}_{Z} [f (z_{i})]
    \right\rvert
\right]
& = \mathbb{E}_{\mathcal{S}} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        \frac{ 1 }{ n } \sum_{i = 1}^{n} f (z_{i}) 
        - \mathbb{E}_{\mathcal{S}'} \left[
            \frac{ 1 }{ n } \sum_{\hat{z}_{i} \in \hat{\mathcal{S}}} f (\hat{z}_{i})
        \right]
    \right\rvert
\right]
\\
& \stackrel{(1)}{=} \mathbb{E}_{\mathcal{S}} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        \mathbb{E}_{\mathcal{S}'} \left[
            \frac{ 1 }{ n } \sum_{i = 1}^{n} (f (z_{i}) - f (\hat{z}_{i}))
        \right]
    \right\rvert
\right]
\\
& \stackrel{(2)}{\leq} \mathbb{E}_{\mathcal{S}, \mathcal{S}'} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        \frac{ 1 }{ n } \sum_{i = 1}^{n} (f (z_{i}) - f (\hat{z}_{i}))
    \right\rvert
\right]
\end{aligned}
$$

where 

- (1) uses the linearity of expectation and $\frac{ 1 }{ n } \sum_{z_{i} \in \mathcal{S} f (z_{i})}$ is a constant,

- (2) uses Jensen's inequality since $\sup$ is a convex operator.


Since $f (z_{i}) - f (\hat{z}_{i})$ is invariant of sign change

$$
\begin{aligned}
\mathbb{E}_{\mathcal{S}, \mathcal{S}'} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        \frac{ 1 }{ n } \sum_{i = 1}^{n} (f (z_{i}) - f (\hat{z}_{i}))
    \right\rvert
\right]
& = \mathbb{E}_{\mathcal{S}, \mathcal{S}', \sigma} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} (f (z_{i}) - f (\hat{z}_{i}))
    \right\rvert
\right]
\\
& \stackrel{(1)}{\leq} \mathbb{E}_{\mathcal{S}, \sigma} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} f (z_{i}) 
    \right\rvert
\right] 
+ \mathbb{E}_{\hat{\mathcal{S}}, \sigma} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} f (\hat{z}_{i})
    \right\rvert
\right]
\\
& \stackrel{(2)}{=} 2 \mathrm{Rad}_{\mathcal{F}} (n).
\end{aligned}
$$

Therefore we have reached our conclusion

$$
\mathbb{E}_{\mathcal{S}} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        \frac{ 1 }{ n } \sum_{i = 1}^{n} f (z_{i}) - \mathbb{E}_{Z} [f (z_{i})]
    \right\rvert
\right] \leq 2 \mathrm{Rad}_{\mathcal{F}} (n).
$$

:::

## Rademacher-based uniform convergence

It turns out that the Rademacher theorem can be applied to derive a uniform convergence result.

Given a sample $\mathcal{S}$ that is drawn i.i.d from any distribution $\mathbb{P}_{\mathcal{Z}^{n}}$,
for every function $f \in \mathcal{F}$, 
the *difference between its true risk and estimated risk* is no greater than the error $\epsilon$ with probability at least $1 - \delta$

$$
\mathbb{P} (\lvert R (h) - R_{n} (h) \rvert \leq \epsilon) \geq 1 - \delta.
$$

where the error $\epsilon$ is

$$
\epsilon = 2 \mathrm{Rad}_{\mathcal{F}} (n) + \sqrt{\frac{ \log \frac{ 1 }{ \delta }}{ n }}
$$

:::{prf:proof} 
:label: 
:class:dropdown
:::