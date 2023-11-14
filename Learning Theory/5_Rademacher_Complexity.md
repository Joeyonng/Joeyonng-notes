# Rademacher Complexity

## Rademacher distribution

A Rademacher distribution is a discrete probability distribution where a random variate $X$ has the equal probability of being +1 and -1.

## Rademacher complexity

Given an i.i.d sample $\mathcal{S} = \{ z_{1}, \dots, z_{n} \}$ from the distribution $\mathbb{P}_{\mathcal{Z}^{n}}$ and $n$ independent Rademacher random variables $\sigma = \{ \sigma_{1}, \dots, \sigma_{n} \}$,
the **empirical Rademacher complexity** of a class of binary function $\mathcal{F}$ is defined as

$$
\mathrm{Rad}_{\mathcal{F}} (\mathcal{S}) = \mathbb{E}_{\sigma} \left[
    \sup_{f \in \mathcal{F}} \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} f (z_{i}) 
\right],
$$

which is a function of the random variable $\mathcal{S}$ and therefore is a random variable. 

Then the **Rademacher complexity** is defined as the expectation of the empirical Rademacher complexity over all i.i.d samples of size $n$

$$
\mathrm{Rad}_{\mathcal{F}} (n) = \mathbb{E}_{\mathcal{S}} \left[
    \mathrm{Rad}_{\mathcal{F}} (\mathcal{S})
\right] = \mathbb{E}_{\mathcal{S}} \left[
    \mathbb{E}_{\sigma} \left[
        \sup_{f \in \mathcal{F}} \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} f (z_{i}) 
    \right]
\right].
$$

### Intuitions

If $\mathcal{F}$ contains so many functions such that there exists some functions in $\mathcal{F}$ that can always output the same signs with the random generated Rademacher random variables,
then $\mathcal{F}$ will have a high Rademacher complexity according to the definition. 

The empirical Rademacher complexity measures the ability of the functions in a function class $\mathcal{F}$ to fit the random noise for a fixed sample $\mathcal{S}$,
which is described by the maximum correlation over all $f \in \mathcal{F}$ between $f (z_{i})$ and $\sigma_{i}$.

Therefore,  the Rademacher complexity of $\mathcal{F}$ measures the expected noise-fitting-ability of $\mathcal{F}$ over all data sets $\mathcal{S} \in \mathcal{Z}^{n}$ that could be drawn according to the distribution $\mathbb{P}_{\mathcal{Z}^{n}}$.

### Properties

#### Non-negativity

The empirical Rademacher complexity and Rademacher complexity are non-negative.

:::{prf:proof}
:label:
:class:dropdown

$$
\begin{aligned}
\mathrm{Rad}_{\mathcal{F}} (\mathcal{S}) 
& = \mathbb{E}_{\sigma} \left[
    \sup_{f \in \mathcal{F}} \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} f (z_{i}) 
\right]
\\
& \stackrel{(1)}{\geq} \sup_{f \in \mathcal{F}} \mathbb{E}_{\sigma} \left[
     \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} f (z_{i}) 
\right]
\\
& = \sup_{f \in \mathcal{F}} \frac{ 1 }{ n } \sum_{i = 1}^{n} \mathbb{E}_{\sigma} [ \sigma_{i} ] f (z_{i}) 
\\
& \stackrel{(2)}{=} 0.
\end{aligned}
$$

Explanations in the derivations

1. Since $\sup$ is a convex function, (1) follows because of the Jensen's inequality.

1. (2) follows because of the definition of Rademacher variable.

:::

#### Scaling and translation

Given any function class $\mathcal{F}$ and constants $a, b \in \mathbb{R}$, denote the function class $ \mathcal{G} = \{g (x) = a f (x) + b \}$.

$$
\mathrm{Rad}_{\mathcal{G}} (\mathcal{S}) = \lvert a \rvert \mathrm{Rad}_{\mathcal{F}} (\mathcal{S})
$$

$$
\mathrm{Rad}_{\mathcal{G}} (n) = \lvert a \rvert \mathrm{Rad}_{\mathcal{F}} (n).
$$

:::{prf:proof}
:label:
:class:dropdown

By definition of $\mathcal{G}$ and the empirical Rademacher complexity,

$$
\begin{aligned}
\mathrm{Rad}_{\mathcal{G}} (\mathcal{S}) 
& = \mathbb{E}_{\sigma} \left[
    \sup_{f \in \mathcal{F}} \left(
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} (a f (z_{i}) + b)
    \right)
\right]
\\
& = \mathbb{E}_{\sigma} \left[
    \sup_{f \in \mathcal{F}} \left(
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} a f (z_{i}) 
        + \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} b
    \right)
\right]
\\
& \stackrel{(1)}{=} \mathbb{E}_{\sigma} \left[
    \sup_{f \in \mathcal{F}} \left(
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} a f (z_{i}) 
    \right)
\right]
+ \mathbb{E}_{\sigma} \left[
    \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} b
\right]
\\
& \stackrel{(2)}{=} \mathbb{E}_{\sigma} \left[
    \sup_{f \in \mathcal{F}} \left(
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} a f (z_{i}) 
    \right)
\right]
\\
& \stackrel{(3)}{=} \lvert a \rvert \mathbb{E}_{\sigma} \left[
    \sup_{f \in \mathcal{F}} \left(
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} f (z_{i}) 
    \right)
\right]
\\
& = \lvert a \rvert \mathrm{Rad}_{\mathcal{F}} (\mathcal{S}).
\end{aligned}
$$

Explanations in the derivations

1. Since the term $\frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} b$ does not depend on $f$, it can be pulled out of $\sup_{f \in \mathcal{F}}$. 
    Then (1) follows because of the linearity of expectation.

1. (2) follows because of the linearity of expectation and $\mathbb{E}_{\sigma} [\sigma_{i}] = 0$.

1. When $a < 0$, $\sup_{f \in \mathcal{F}} \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} a f (z_{i}) = \lvert a \rvert \sup_{f \in \mathcal{F}} \frac{ 1 }{ n } \sum_{i = 1}^{n} - \sigma_{i} f (z_{i})$. Then (3) follows since $\sigma_{i}$ and $-\sigma_{i}$ have the same distribution. 

:::

## Rademacher theorem

The primary use of the Rademacher complexity is to upper bound $\mathbb{E}_{\mathcal{S}} [\phi (\mathcal{S})]$, the expectation of the maximum error in estimating the mean of any function $f \in \mathcal{F}$,

$$
\mathbb{E}_{\mathcal{S}} [\phi (\mathcal{S})] 
= \mathbb{E}_{\mathcal{S}} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        E_{\mathcal{S}} (f) - \mathbb{E}_{Z} [f (z_{i})]
    \right\rvert
\right] \leq 2 \mathrm{Rad}_{\mathcal{F}} (n)
$$

where $E_{\mathcal{S}} (f) = \frac{ 1 }{ n } \sum_{i = 1}^{n} f (z_{i})$ is the estimated expectation of $f$ on the sample $\mathcal{S}$.

:::{prf:proof} Rademacher theorem
:label: rademacher-theorem
:class:dropdown

We introduce a ghost sample $\mathcal{S}' = \{ z_{1}', \dots, z_{n}' \}$ that is also i.i.d drawn from $\mathbb{P}_{\mathcal{Z}^{n}}$,
which means

$$
\mathbb{E}_{\mathcal{S}'} \left[ 
    E_{\mathcal{S}'} (f)
\right] = \mathbb{E}_{Z} [f (z_{i})].
$$

Therefore, we can get the following results

$$
\begin{aligned}
\mathbb{E}_{\mathcal{S}} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        E_{\mathcal{S}} (f) - \mathbb{E}_{Z} [f (z_{i})]
    \right\rvert
\right] 
& = \mathbb{E}_{\mathcal{S}} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        \frac{ 1 }{ n } \sum_{i = 1}^{n} f (z_{i}) 
        - \mathbb{E}_{\mathcal{S}'} \left[
            \frac{ 1 }{ n } \sum_{z_{i}' \in \hat{\mathcal{S}}} f (z_{i}')
        \right]
    \right\rvert
\right]
\\
& \stackrel{(1)}{=} \mathbb{E}_{\mathcal{S}} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        \mathbb{E}_{\mathcal{S}'} \left[
            \frac{ 1 }{ n } \sum_{i = 1}^{n} (f (z_{i}) - f (z_{i}'))
        \right]
    \right\rvert
\right]
\\
& \stackrel{(2)}{\leq} \mathbb{E}_{\mathcal{S}, \mathcal{S}'} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        \frac{ 1 }{ n } \sum_{i = 1}^{n} (f (z_{i}) - f (z_{i}'))
    \right\rvert
\right]
\end{aligned}
$$

Explanations in the derivations

1. (1) uses the linearity of expectation and $\frac{ 1 }{ n } \sum_{z_{i} \in \mathcal{S} f (z_{i})}$ is a constant.

1. (2) uses Jensen's inequality since $\sup$ is a convex operator.


Since $f (z_{i}) - f (z_{i}')$ is invariant of sign change,
we get

$$
\begin{aligned}
\mathbb{E}_{\mathcal{S}, \mathcal{S}'} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        \frac{ 1 }{ n } \sum_{i = 1}^{n} (f (z_{i}) - f (z_{i}'))
    \right\rvert
\right]
& = \mathbb{E}_{\mathcal{S}, \mathcal{S}', \sigma} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} (f (z_{i}) - f (z_{i}'))
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
        \frac{ 1 }{ n } \sum_{i = 1}^{n} - \sigma_{i} f (z_{i}')
    \right\rvert
\right]
\\
& \stackrel{(2)}{=} 2 \mathrm{Rad}_{\mathcal{F}} (n).
\end{aligned}
$$

Explanations in the derivations

1. (1) follows because of the $\sup_{f \in \mathcal{F}}$ operator,

1. (2) follows because $\sigma_{i} = - \sigma_{i}$ by the definition of Rademacher variable.

Therefore we have reached our conclusion

$$
\mathbb{E}_{\mathcal{S}} \left[
    \sup_{f \in \mathcal{F}} \left\lvert
        E_{\mathcal{S}} (f) - \mathbb{E}_{Z} [f (z_{i})]
    \right\rvert
\right] 
\leq 2 \mathrm{Rad}_{\mathcal{F}} (n).
$$

:::

## Rademacher-based uniform convergence

### General results for all classes

Given a sample $\mathcal{S}$ that is drawn i.i.d from any distribution $\mathbb{P}_{\mathcal{Z}^{n}}$,
if the function class $\mathcal{F}$ only contains the functions $f$ such that $f (x) \in [a, a + 1]$,
then for every $f \in \mathcal{F}$, the *difference between its true expectation and estimated expectation* is no greater than the error $\epsilon$ with probability at least $1 - \delta$

$$
\mathbb{P} (\lvert \mathbb{E}_{\mathcal{Z}} [f (z_{i})] - E_{\mathcal{S}} (f) \rvert \leq \epsilon) \geq 1 - \delta, 
\quad \forall f \in \mathcal{F}
$$

where the error $\epsilon$ is

$$
\epsilon = 2 \mathrm{Rad}_{\mathcal{F}} (n) + \sqrt{\frac{ \log \frac{ 1 }{ \delta }}{ 2 n }}.
$$

:::{prf:proof} 
:label: 
:class:dropdown

Given a function $f \in \mathcal{F}$, 
the difference between its true expectation and estimated expectation on a sample $\mathcal{S} = \{ z_{1}, \dots, z_{n} \}$ is less than the maximum difference of the expectations among all functions in $\mathcal{F}$, 
which is denoted by $\phi (\mathcal{S})$

$$
\lvert \mathbb{E}_{\mathcal{Z}} [f (z_{i})] - E_{\mathcal{S}} (f) \rvert  \leq \sup_{\hat{f} \in \mathcal{F}} [\lvert \mathbb{E}_{\mathcal{Z}} [\hat{f} (z_{i})] - E_{\mathcal{S}} (\hat{f}) \rvert] = \phi (\mathcal{S}).
$$

First we will prove the following property so that we can use McDiarmid's inequality on $\phi (\mathcal{S})$

$$
\sup_{\mathcal{S}, \mathcal{S}'} \lvert \phi (\mathcal{S}) - \phi (\mathcal{S}') \rvert \leq \frac{ 1 }{ n }
$$

where $\mathcal{S}' = \{ z_{1}, \dots, z_{j}', \dots, z_{n} \}$ has $z_{j}'$ different from $z_{j}$ in $\mathcal{S}$. 

Let $f^{*} \in \mathcal{F}$ be the function that maximizes $\phi (\mathcal{S})$ 

$$
\lvert \mathbb{E}_{\mathcal{Z}} [f^{*} (z_{i})] - E_{\mathcal{S}} (f^{*}) \rvert 
= \sup_{\hat{f} \in \mathcal{F}} [\lvert \mathbb{E}_{\mathcal{Z}} [\hat{f} (z_{i})] - E_{\mathcal{S}} (\hat{f}) \rvert] 
= \phi (\mathcal{S})
$$

and by definition 

$$
\lvert \mathbb{E}_{\mathcal{Z}} [f^{*} (z_{i})] - E_{\mathcal{S}'} (f^{*}) \rvert 
\leq \sup_{\hat{f} \in \mathcal{F}} [\lvert \mathbb{E}_{\mathcal{Z}} [\hat{f} (z_{i})] - E_{\mathcal{S}'} (\hat{f}) \rvert] 
= \phi (\mathcal{S}').
$$

Therefore, 

$$
\begin{aligned}
\lvert \phi (\mathcal{S}) - \phi (\mathcal{S}') \rvert 
& \leq \lvert \lvert \mathbb{E}_{\mathcal{Z}} [f^{*} (z_{i})] - E_{\mathcal{S}} (f^{*}) \rvert
- \lvert \mathbb{E}_{\mathcal{Z}} [f^{*} (z_{i})] - E_{\mathcal{S}'} (f^{*}) \rvert \rvert
\\
& = \lvert E_{\mathcal{S}'} (f^{*}) - E_{\mathcal{S}} (f^{*}) \rvert
\\
& = \left\lvert 
    \frac{ 1 }{ n } \sum_{i = 1}^{n} f^{*} (z_{i}) - \frac{ 1 }{ n } \sum_{i = 1}^{n} f^{*} (z_{i}')
\right\rvert.
\end{aligned}
$$

Since $\mathcal{S}$ and $\mathcal{S}'$ only differ on two elements $z_{j}, z_{j}'$,
this becomes

$$
\begin{aligned}
\lvert \phi (\mathcal{S}) - \phi (\mathcal{S}') \rvert 
& \leq \left\lvert 
    \frac{ 1 }{ n } \sum_{i = 1}^{n} f^{*} (z_{i}) - \frac{ 1 }{ n } \sum_{i = 1}^{n} f^{*} (z_{i}')
\right\rvert
\\
& = \frac{ 1 }{ n } \left\lvert \left(
        \sum_{i \neq j} f^{*} (z_{i}) + f^{*} (z_{j})
    \right) - \left(
        \sum_{i \neq j} f^{*} (z_{i}) + f^{*} (z_{j}')
    \right)
\right\rvert
\\
& = \frac{ 1 }{ n } \left\lvert f^{*} (z_{j}) - f^{*} (z_{j}') \right\rvert
\\
& \leq \frac{ 1 }{ n }.
\end{aligned}
$$

This results show that the function $\phi$ follows the bounded difference property,
so we can apply the McDiarmid's inequality on $\phi$,

$$
\begin{aligned}
\mathbb{P}_{\mathcal{S}} (\phi (\mathcal{S}) - \mathbb{E}_{\mathcal{S}} [\phi (\mathcal{S})] \geq t) 
& \leq \exp \left[
    \frac{ - 2 t^{2} }{ \sum_{i = 1}^{n} \left(
        \frac{ 1 }{ n }
    \right)^{2} }
\right] 
\\
& \leq e^{- 2 m t^{2}}.
\end{aligned}
$$

By setting $\delta = e^{-2 n t^{2}}$, 
we can derive that $t = \sqrt{\frac{ \log{\frac{ 1 }{ \delta }} }{ 2 n }}$,
so

$$
\begin{aligned}
\mathbb{P}_{\mathcal{S}} \left(
    \phi (\mathcal{S}) - \mathbb{E}_{\mathcal{S}} [\phi (\mathcal{S})] \geq 
    \sqrt{\frac{ \log{\frac{ 1 }{ \delta }} }{ 2 n }}
\right) 
& \leq \delta
\\
\mathbb{P}_{\mathcal{S}} \left(
    \phi (\mathcal{S}) - \mathbb{E}_{\mathcal{S}} [\phi (\mathcal{S})] \leq 
    \sqrt{\frac{ \log{\frac{ 1 }{ \delta }} }{ 2 n }}
\right) 
& \geq 1 - \delta.
\end{aligned}
$$

which means we have the following fact with the probability larger than $1 - \delta$, 

$$
\phi (\mathcal{S}) \leq \mathbb{E}_{\mathcal{S}} [\phi (\mathcal{S})]
+ \sqrt{\frac{ \log{\frac{ 1 }{ \delta }} }{ 2 n }}.
$$

By plugging back the result to the equation that we want to prove,
we have the final results

$$
\begin{aligned}
\lvert \mathbb{E}_{\mathcal{Z}} [f (z_{i})] - E_{\mathcal{S}} (f)] \rvert
& \leq \phi (\mathcal{S})
\\
& \leq \mathbb{E}_{\mathcal{S}} [\phi (\mathcal{S})]
+ \sqrt{\frac{ \log{\frac{ 1 }{ \delta }} }{ 2 n }}
\\
& \leq 2 \mathrm{Rad}_{\mathcal{F}} (n)
+ \sqrt{\frac{ \log{\frac{ 1 }{ \delta }} }{ 2 n }}
\end{aligned}
$$

with the probability larger than $1 - \delta$. 

:::

### Results for risks 

Given a hypothesis class $\mathcal{H}$, a corresponding 0-1 loss class can be defined as 

$$
\mathcal{L} = \{ l_{h} \mid l_{h} (z) = L (h (\mathbf{x}), y), h \in \mathcal{H}, z \sim \mathcal{Z} \}
$$

and therefore the empirical risk and true risk can be defined as 

$$
R_{\mathcal{S}} (h) = E_{\mathcal{S}} (l_{h}), R (h) = \mathbb{E}_{\mathcal{Z}} [l_{h} (z)].
$$

Since all the loss functions $l_{h} \in \mathcal{L}$ have output range $[0, 1]$,
we can apply the uniform theorem above to the loss class $\mathcal{L}$ to derive the uniform convergence results for risks.


:::{prf:theorem}

Given a sample $\mathcal{S}$ that is drawn i.i.d from any distribution $\mathbb{P}_{\mathcal{Z}^{n}}$,
for every hypothesis $h \in \mathcal{H}$, the *difference between its true risk and estimated risk* is no greater than the error $\epsilon$ with probability at least $1 - \delta$

$$
\mathbb{P} (\lvert R_{\mathcal{S}} (h) - R (h) \rvert \leq \epsilon) \geq 1 - \delta, 
\quad \forall h \in \mathcal{H}
$$

where the error $\epsilon$ is

$$
\epsilon = 2 \mathrm{Rad}_{\mathcal{L}} (n) + \sqrt{\frac{ \log \frac{ 1 }{ \delta }}{ 2 n }}.
$$

Since the 0-1 loss can be written as 

:::

## Bounding Rademacher complexity

### Massart’s lemma

Given any finite function class $\mathcal{F}$ and a sample $\mathcal{S} = \{ z_{1}, \dots, z_{n} \}$,
the empirical Rademacher complexity is upper-bounded 

$$
\mathrm{Rad}_{\mathcal{F}} (\mathcal{S}) \leq \frac{ R \sqrt{2 \log \lvert \mathcal{F} \rvert} }{ n }
$$

where $R = \sup_{f \in \mathcal{F}} \sqrt{\sum_{i = 1}^{n} f^{2} (z_{i})}$.

:::{prf:proof} 
:label: 
:class:dropdown

By Jensen's inequality, 
the following quantity can be upper-bounded

$$
\begin{aligned}
\exp \left[
    s \mathbb{E}_{\sigma} \left[
        \sup_{f \in \mathcal{F}} \sum_{i = 1}^{n} \sigma_{i} f (z_{i})
    \right]
\right]
& \leq \mathbb{E}_{\sigma} \left[ 
    \exp \left[
        s \sup_{f \in \mathcal{F}} \sum_{i = 1}^{n} \sigma_{i} f (z_{i})
    \right]
\right]
\\
& = \mathbb{E}_{\sigma} \left[ 
    \sup_{f \in \mathcal{F}} \exp \left[
        s \sum_{i = 1}^{n} \sigma_{i} f (z_{i})
    \right]
\right]
\\
& \stackrel{(1)}{\leq} \mathbb{E}_{\sigma} \left[ 
    \sum_{f \in \mathcal{F}} \exp \left[
        s \sum_{i = 1}^{n} \sigma_{i} f (z_{i})
    \right]
\right]
\\
& = \sum_{f \in \mathcal{F}} \mathbb{E}_{\sigma} \left[ 
    \prod_{i = 1}^{n} \exp \left[
        s \sigma_{i} f (z_{i})
    \right]
\right]
\\
& \stackrel{(2)}{=} \sum_{f \in \mathcal{F}} \prod_{i = 1}^{n} \mathbb{E}_{\sigma} \left[ 
    \exp \left[
        s \sigma_{i} f (z_{i})
    \right]
\right]
\end{aligned}
$$

Explanations in the derivations

1. (1) follows since $\exp$ is non-negative and therefore $\sup \leq \sum$.

1. (2) follows because of the independence between $\sigma_{i}$. 

Since $\mathbb{E}_{\sigma_{i} f (z_{i})} = 0$, 
we can apply Hoeffding's lemma with $\mu = 0$ 

$$
\begin{aligned}
\exp \left[
    s \sigma_{i} f (z_{i})
\right]
& \leq \exp \left[
    \frac{ s^{2} (2 f (z_{i}))^{2}}{ 8 }
\right]
\\
& = \exp \left[
    \frac{ s^{2} f^{2} (z_{i}) }{ 2 }
\right],
\end{aligned}
$$

and therefore

$$
\begin{aligned}
\sum_{f \in \mathcal{F}} \prod_{i = 1}^{n} \mathbb{E}_{\sigma} \left[ 
    \exp \left[
        s \sigma_{i} f (z_{i})
    \right]
\right] 
& \leq \sum_{f \in \mathcal{F}} \prod_{i = 1}^{n} \exp \left[
    \frac{ s^{2} f^{2} (z_{i}) }{ 2 }
\right]
\\
& = \sum_{f \in \mathcal{F}} \exp \left[
    \frac{ s^{2} }{ 2 } \sum_{i = 1}^{n} f^{2} (z_{i})
\right]
\\
& \stackrel{(1)}{\leq} \lvert \mathcal{F} \rvert \exp \left[
    \frac{ s^{2} }{ 2 } \sup_{f \in \mathcal{F}} \sum_{i = 1}^{n} f^{2} (z_{i})
\right].
\end{aligned}
$$

Explanations in the derivations

1. (1) follows since $\sum_{i = 1}^{n} f (a_{i}) \leq n \sup_{a_{i}} f (a_{i})$.

Combining all pieces together,

$$
\begin{aligned}
\exp \left[
    s \mathbb{E}_{\sigma} \left[
        \sup_{f \in \mathcal{F}} \sum_{i = 1}^{n} \sigma_{i} f (z_{i})
    \right]
\right]
& \leq \lvert \mathcal{F} \rvert \exp \left[
    \frac{ s^{2} }{ 2 } \sup_{f \in \mathcal{F}} \sum_{i = 1}^{n} f^{2} (z_{i})
\right]
\\
\mathbb{E}_{\sigma} \left[
    \sup_{f \in \mathcal{F}} \sum_{i = 1}^{n} \sigma_{i} f (z_{i})
\right]
& \leq \frac{ \log \lvert \mathcal{F} \rvert }{ s } + \frac{ s R^{2} }{ 2 } 
\end{aligned}
$$

where $R^{2} = \sup_{f \in \mathcal{F}} \sum_{i = 1}^{n} f^{2} (z_{i})$.

Since $\log \frac{ \lvert \mathcal{F} \rvert }{ s } + \frac{ s R^{2} }{ 2 }$ is a convex function, 
we can minimize it with respect to $s$ 

$$
\begin{aligned}
\frac{ d }{ d s } \frac{ \log \lvert \mathcal{F} \rvert }{ s } + \frac{ s R^{2} }{ 2 } 
& = 0
\\
- \frac{ \log \lvert \mathcal{F} \rvert }{ s^{2} } + \frac{ R^{2} }{ 2 } 
& = 0
\\
s 
& = \frac{ \sqrt{ 2 \log \lvert \mathcal{F} \rvert } }{ R }. 
\end{aligned}
$$

Plugging it back 

$$
\begin{aligned}
\mathbb{E}_{\sigma} \left[
    \sup_{f \in \mathcal{F}} \sum_{i = 1}^{n} \sigma_{i} f (z_{i})
\right]
& \leq \frac{ \log \lvert \mathcal{F} \rvert }{ s } + \frac{ s R^{2} }{ 2 } 
\\
& = \frac{ 
    \log \lvert \mathcal{F} \rvert 
}{ 
    \frac{ \sqrt{ 2 \log \lvert \mathcal{F} \rvert } }{ R }
} + \frac{ 
    \frac{ \sqrt{ 2 \log \lvert \mathcal{F} \rvert } }{ R } R^{2} 
}{ 
    2 
} 
\\
& = R \sqrt{ 2 \log \lvert \mathcal{F} \rvert }
\\
\mathbb{E}_{\sigma} \left[
    \sup_{f \in \mathcal{F}} \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} f (z_{i})
\right]
& \leq \frac{ R \sqrt{ 2 \log \lvert \mathcal{F} \rvert } }{ n },
\end{aligned}
$$

where the last equation is derived by dividing both sides by $n$.

:::

### Connection with VC theory

If $\mathcal{F}$ in Massart’s lemma is a finite hypothesis class $\mathcal{H}$,
then $R = \sup_{h \in \mathcal{H}} \sqrt{\sum_{i = 1}^{n} h^{2} (z_{i})} = \sqrt{n}$ since $h^{2} (z_{i}) = 1, \forall z_{i}$. Therefore, 

$$
\mathrm{Rad}_{\mathcal{H}} (\mathcal{S}) \leq \frac{ \sqrt{n} \sqrt{2 \log \lvert \mathcal{H} \rvert} }{ n } = \sqrt{\frac{ 2 \log \lvert \mathcal{H} \rvert }{ n }}.
$$

When $\mathcal{H}$ is an infinite class, 
$\log \lvert \mathcal{H} \rvert$ can be replaced with $\log \lvert \mathcal{H} (\mathcal{S}) \rvert$, 
the number of projections of $\mathcal{H}$ on the sample $\mathcal{S}$, 
so we have 

$$
\mathrm{Rad}_{\mathcal{H}} (\mathcal{S}) 
\leq \sqrt{\frac{ 2 \log \lvert \mathcal{H} (\mathcal{S}) \rvert }{ n }}.
$$

By the definition of growth function and Sauer's lemma $\lvert \mathcal{H} (\mathcal{S}) \rvert \leq \Pi_{\mathcal{H}} (\mathcal{S}) \leq \left( \frac{ e }{ d } n \right)^{d}$,
where $d$ is the VC dimension of $\mathcal{H}$,
we can derive

$$
\mathrm{Rad}_{\mathcal{H}} (\mathcal{S}) \leq \sqrt{\frac{ 2 \log \lvert \mathcal{H} (\mathcal{S}) \rvert }{ n }} 
\leq \sqrt{\frac{ 2 \log \Pi_{\mathcal{H}} (\mathcal{S}) }{ n }} 
\leq \sqrt{\frac{ 2 d \log \frac{ e n }{ d } }{ n }}.
$$