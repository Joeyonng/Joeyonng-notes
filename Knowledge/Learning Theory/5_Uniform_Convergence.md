# Uniform Convergence

**Uniform convergence** means convergence with respect to the difference between the empirical error and the true error, 
which is uniform with respect to all hypotheses in the class.
That is, uniform convergence bound the difference between true and empirical error across all hypotheses in the class simultaneously.

## Uniform convergence property

The **uniform convergence property** of a given hypothesis class $\mathcal{H}$ states that 
there exists a large enough sample size such that for all hypotheses in the class $\mathcal{H}$,
the empirical risk is close to the true risk with high probability,
regardless of the underlying distribution $\mathbb{P}_{Z}$. 

:::{#def-uniform-convergence-property}

#### Uniform convergence property

A hypothesis class $\mathcal{H}$ has the **uniform convergence property** if, 

- given a set of labeled instances $\mathcal{S}$, 
    where instances and labels are sampled from *any joint distribution* $\mathbb{P}_{Z}$ over the instance space and the label space, and there exists a function for some $\epsilon > 0$ and $\delta > 0$ such that 

    $$
    n \geq n_{\mathcal{H}} (\epsilon, \delta),
    $$

- for every hypothesis $h \in \mathcal{H}$, 
    the *difference between its true risk and estimated risk* is no greater than $\epsilon$ with probability at least $1 - \delta$

    $$
    \mathbb{P}_{\mathcal{S}} (\lvert R (h) - R_{\mathcal{S}} (h) \rvert \leq \epsilon) \geq 1 - \delta.
    $$

:::

Note that this definition is stated using the **sample complexity** $n_{\mathcal{H}} (\epsilon, \delta)$,
which is the sample size that we need to supply, 
so that with an arbitrarily high probability $1 - \delta$, 
the considered event has an arbitrarily small error $\epsilon$.


## Uniform convergence results 

The following theorems state that a hypothesis class has the uniform convergence property if either it has a finite number of hypotheses or has a finite VC dimension.

:::{#thm-uniform-convergence}

#### Uniform convergence theorem

Any finite hypothesis class $\mathcal{H}$ has the uniform convergence property with the sample complexity

$$
n_{\mathcal{H}} (\epsilon, \delta) = \frac{
    \log \lvert \mathcal{H} \rvert + \log \frac{ 2 }{ \delta } 
}{
    2 \epsilon^{2}
}.
$$

:::

:::{.callout-note collapse="true" title="Proof"}

Since the true risk of a hypothesis is the expectation of the empirical risk with respect to the joint distribution $\mathbb{P}_{Z}$

$$
R(h) = \mathbb{E}_{Z} \left[
    R_{n} (h)
\right] = \mathbb{E}_{Z} \left[
    \frac{ 1 }{ n } \sum_{i = 1}^{n} L (h (z_{i}))
\right]
$$

and we can view the 0-1 loss on an instance as a bounded random variable

$$
L_{i} = L (h (\mathbf{X_{i}}), Y_{i}) = \mathbb{1} \left[
    h (\mathbf{X_{i}}) \neq Y_{i}
\right] \in [0, 1],
$$

we can apply Hoeffding's inequality on $L_{i}$ for a fixed hypothesis $h \in \mathcal{H}$, 

$$
\begin{aligned}
\mathbb{P} \left(
    \left\lvert 
        \frac{ 1 }{ n } \sum_{i = 1}^{n} L_{i} - \mathbb{E}_{Z} \left[
            \frac{ 1 }{ n } \sum_{i = 1}^{n} L_{i}
        \right] 
    \right\rvert \geq \epsilon
\right) 
& \leq 2 \exp \left[
    -\frac{ 2 n^{2} \epsilon^{2} }{ \sum_{i=1}^{n} (b_{i} - a_{i})^{2} }
\right]
\\
\mathbb{P} \left(
    \lvert R_{n} (h) - \mathbb{E}_{Z} \left[
        R_{n} (h)
    \right] \rvert \geq \epsilon
\right) 
& \leq 2 \exp \left[
    -\frac{ 2 n^{2} \epsilon^{2} }{ n }
\right]
\\
\mathbb{P} \left(
    \lvert R_{n} (h) - R (h) \rvert \geq \epsilon
\right) 
& \leq 2 \exp \left[
    - 2 n \epsilon^{2} 
\right].
\end{aligned}
$$

The above inequality only works for one $h \in \mathcal{F}$. 
we can apply union bound to extend it for all $f \in \mathcal{F}$, 

$$
\begin{aligned}
\mathbb{P} \left(
    \exist f \in \mathcal{F}, \lvert R_{n} (f) - R (f) \rvert \geq \epsilon
\right) 
& \leq \sum_{i = 1}^{\lvert \mathcal{F} \rvert} \mathbb{P} \left(
    \lvert R_{n} (f_{i}) - R (f_{i}) \rvert \geq \epsilon
\right) 
\\
& \leq 2 \lvert \mathcal{F} \rvert \exp \left[
    - 2 n \epsilon^{2} 
\right].
\end{aligned}
$$

Since $\mathbb{P} (X \geq a) = 1 - \mathbb{P} (X \leq a)$

$$
\begin{aligned}
\mathbb{P} \left(
    \exist f \in \mathcal{F}, \lvert R_{n} (f) - R (f) \rvert \leq \epsilon
\right) 
& \geq 1 - 2 \lvert \mathcal{F} \rvert \exp \left[
    - 2 n \epsilon^{2} 
\right]
\\
& \geq 1 - \delta
\end{aligned}
$$

where 

$$
\begin{aligned}
\delta 
& = 2 \lvert \mathcal{F} \rvert \exp \left[
    - 2 n \epsilon^{2} 
\right] 
\\
n
& = \frac{
    \log \lvert \mathcal{F} \rvert + \log \frac{ 2 }{ \delta }
}{
    2 \epsilon^{2}
}.
\end{aligned}
$$

:::

:::{#thm-}

Any infinite hypothesis class $\mathcal{H}$ with a finite VC dimension has the uniform convergence property with the sample complexity

$$
n_{\mathcal{H}} (\epsilon, \delta) = 8 \frac{
    \log \Pi_{\mathcal{H}} (2 n) + \log \frac{ 4 }{ \delta } 
}{
    \epsilon^{2}
}
$$

where $n$ is the number of samples in the training set.

:::

:::{.callout-note collapse="true" title="Proof"}

Let's first define 3 "bad" events that are useful in the following proof.

Given any set of labeled instances $\mathcal{S} = \{ z_{1}, \dots, z_{n} \}$,
let $B (\mathcal{S})$ denote the event that there exists a hypothesis $h \in \mathcal{H}$ such that the difference between its true risk and empirical risk on $\mathcal{S}$ is larger than $\epsilon$,

$$
B (\mathcal{S}) \coloneqq \exist h \in \mathcal{H}: \lvert R_{\mathcal{S}} (h) -  R (h) \rvert \geq \epsilon.
$$

and therefore we want to prove

$$
\mathbb{P}_{\mathcal{S}} (B (\mathcal{S})) \leq \delta.
$$

Now let's draw the "ghost samples",
which is another set of i.i.d labeled instances $\mathcal{S}' = \{ z_{1}', \dots, z_{n}' \}$ from the distribution $\mathbb{P}_{Z}$,
and define another event $B'$ as a function of $\mathcal{S}$ and $\mathcal{S}'$,
which states that there exists a hypothesis $h \in \mathcal{H}$ such that the difference between its empirical risk on $\mathcal{S}$ and empirical risk on $\mathcal{S}'$ is larger than $\frac{ \epsilon }{ 2 }$,

$$
B' (\mathcal{S}, \mathcal{S}') \coloneqq \exist h \in \mathcal{H}: \lvert R_{\mathcal{S}} (h) - R_{S'} (h) \rvert \geq \frac{ \epsilon }{ 2 }.
$$

Finally, let's define an event $B (\mathcal{S}, \mathcal{S}', \sigma)$ as a function of $\mathcal{S}, \mathcal{S}'$, and a set of independent Rademacher random variables $\sigma_{1}, \dots, \sigma_{n}$ that takes values $-1$ or $1$ with equal probabilities

$$
\begin{aligned}
B'' (\mathcal{S}, \mathcal{S}', \sigma) 
& \coloneqq \exist h \in \mathcal{H}: \lvert R_{\mathcal{S}_{\sigma}} (h) - R_{\mathcal{S}_{\sigma}'} (h) \rvert \geq \frac{ \epsilon }{ 2 }
\\
& \coloneqq \exist h \in \mathcal{H}: \left\lvert 
    \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} \left(
        \mathbb{1} \left[
            h (\mathbf{x}_{i}) \neq y_{i} 
        \right] - \mathbb{1} \left[
            h (\mathbf{x}_{i}') \neq y_{i}'
        \right]
    \right)
\right\rvert \geq \frac{ \epsilon }{ 2 },
\\
\end{aligned}
$$

where the samples $\mathcal{S}_{\sigma}, \mathcal{S}_{\sigma}'$ are created by swapping the labeled instances in $\mathcal{S}, \mathcal{S}'$ based on the values of $\sigma$

- $z_{i}$ and $z_{i}'$ are swapped if the corresponding $\sigma_{i} = 1$,

- and $z_{i}$ and $z_{i}'$ are not swapped if the corresponding $\sigma_{i} = -1$.

The event $B'' (\mathcal{S}, \mathcal{S}', \sigma)$ states that there exists a hypothesis $h \in \mathcal{H}$ such that the difference between its empirical risk on $\mathcal{S}_{\sigma}$ and empirical risk on $\mathcal{S}_{\sigma}'$ is larger than $\frac{ \epsilon }{ 2 }$,

**Claim 1**: $\mathbb{P}_{\mathcal{S}} (B (\mathcal{S}))$ is upper-bounded by $2 \mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}'))$,

$$
\mathbb{P}_{\mathcal{S}} (B (\mathcal{S})) \leq 2 \mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}')).
$$ 

Since the probability of an event cannot be larger than its conjunction with another event,

$$
\begin{aligned}
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}')) 
& \geq \mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}') \cap B (\mathcal{S}))
\\
& = \mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}') \mid B (\mathcal{S})) \mathbb{P}_{\mathcal{S}} (B (\mathcal{S}))
\end{aligned}
$$

Now consider the probability of the event

$$
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}') \mid B (\mathcal{S})),
$$

which can be written as 

$$
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} \left(
    \lvert R (h) - R_{S'} (h) \rvert \leq \frac{ \epsilon }{ 2 }
\right)
$$

because it is the same as the $\mathbb{P}_{\mathcal{S}, \mathcal{S}'} \left( \lvert R_{\mathcal{S}} (h) - R_{S'} (h) \rvert \geq \frac{ \epsilon }{ 2 } \right)$ if the event $B (\mathcal{S}) \coloneqq \lvert R_{\mathcal{S}} (h) -  R (h) \rvert \geq \epsilon$ is given.

Since $R (h)$ is the mean of $R_{\mathcal{S}'} (h)$,
the probability of the difference between $R (h)$ and $R_{\mathcal{S}'} (h)$ can be upper bounded by applying Chebyshev's inequality with $X = R_{\mathcal{S}'} (h), \mu = R (h), t = \frac{ \epsilon }{ 2 }, \sigma^{2} = \mathrm{Var} [R_{\mathcal{S}'} (h)]$

$$
\begin{aligned}
\mathbb{P}_{X} \left(
    \lvert x - \mu \rvert \geq t
\right) 
& \leq \frac{ \sigma^{2} }{ t^{2} } 
\\
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} \left(
    \lvert R_{S'} (h) - R (h) \rvert \geq \frac{ \epsilon }{ 2 }
\right) 
& \leq \frac{ 4 \mathrm{Var} [R_{\mathcal{S}'} (h)] }{\epsilon^{2}}.
\end{aligned}
$$

Note that $h (\mathbf{x}_{i}) \neq y_{i}$ is a Bernoulli random variable whose variance is less than $\frac{ 1 }{ 4 }$

$$
\mathrm{Var} [R_{\mathcal{S}'} (h)] = \mathrm{Var} \left[
    \frac{ 1 }{ n } \sum_{\mathbf{x} \in \mathcal{S}'} h (\mathbf{x}_{i}) \neq y_{i}
\right] = \frac{ 1 }{ n^{2} } \sum_{\mathbf{x_{i} \in \mathcal{S}'}} \mathrm{Var} [h (\mathbf{x}) \neq y_{i}] \leq \frac{ 1 }{ 4 n },
$$

and therefore,

$$
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} \left(
    \lvert R (h) - R_{S'} (h) \rvert \geq \frac{ \epsilon }{ 2 }
\right) \leq \frac{ 1 }{n \epsilon^{2}}.
$$

Assume that $n \epsilon^{2} \geq 2$

$$
\begin{aligned}
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} \left(
    \lvert R (h) - R_{S'} (h) \rvert \geq \frac{ \epsilon }{ 2 }
\right) 
& \leq \frac{ 1 }{ 2 }
\\
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} \left(
    \lvert R (h) - R_{S'} (h) \rvert \leq \frac{ \epsilon }{ 2 }
\right) 
& \geq \frac{ 1 }{ 2 }.
\\
\end{aligned}
$$

Then we have proved the claim

$$
\begin{aligned}
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}') \mid B (\mathcal{S})) \mathbb{P}_{\mathcal{S}} (B (\mathcal{S}))
& \leq \mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}')) 
\\
\frac{ 1 }{ 2 } \mathbb{P}_{\mathcal{S}} (B (\mathcal{S}))
& \leq \mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}')) 
\\
\mathbb{P}_{\mathcal{S}} (B (\mathcal{S}))
& \leq 2 \mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}')).
\end{aligned}
$$

**Claim 2**: the probability of event $B' (\mathcal{S}, \mathcal{S}')$ is the same as the expectation of the probability that $B'' (\mathcal{S}, \mathcal{S}', \sigma)$ happens given $\mathcal{S}, \mathcal{S}'$

$$
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}')) 
= \mathbb{E}_{\mathcal{S}, \mathcal{S}'} \left[
    \mathbb{P}_{\sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma) \mid \mathcal{S}, \mathcal{S}')
\right].
$$ 

Since the event $B' (\mathcal{S}, \mathcal{S}')$ and $B'' (\mathcal{S}, \mathcal{S}', \sigma)$ only differ on the set of instances $\mathcal{S}, \mathcal{S}'$ and $\mathcal{S}_{\sigma}, \mathcal{S}_{\sigma}'$ and they can both be seen as the set of instances i.i.d sampled from the $\mathbb{P}_{Z}$,
their probability should be the same 

$$
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}')) = \mathbb{P}_{\mathcal{S}, \mathcal{S}', \sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma)).
$$

Then, we can prove the claim by using marginalization of the probability

$$
\mathbb{P}_{\mathcal{S}, \mathcal{S}', \sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma)) = \mathbb{E}_{\mathcal{S}, \mathcal{S}'} [\mathbb{P}_{\sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma) \mid \mathcal{S}, \mathcal{S}')].
$$

**Claim 3**: $\mathbb{E}_{\mathcal{S}, \mathcal{S}'} [\mathbb{P}_{\sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma) \mid \mathcal{S}, \mathcal{S}')]$ is upper-bounded by $2 \Pi_{\mathcal{H}} (2 n) \exp \left[ - \frac{ n \epsilon^{2} }{ 8 } \right]$

$$
\mathbb{E}_{\mathcal{S}, \mathcal{S}} \left[
    \mathbb{P}_{\sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma) \mid \mathcal{S}, \mathcal{S}') 
\right] \leq 2 \Pi_{\mathcal{H}} (2 n) \exp \left[ 
    - \frac{ n \epsilon^{2} }{ 8 } 
\right].
$$

Consider the following probability for a fixed $h \in \mathcal{H}$,

$$
\mathbb{P}_{\sigma} \left(
    \left\lvert 
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} \left(
            \mathbb{1} \left[
                h (\mathbf{x}_{i}) \neq y_{i} 
            \right] - \mathbb{1} \left[
                h (\mathbf{x}_{i}') \neq y_{i}'
            \right]
        \right)
    \right\rvert \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right).
$$

Since $\mathcal{S}, \mathcal{S}'$ are given, 
the value $\alpha_{i} = \mathbb{1} \left[ h (\mathbf{x}_{i}) \neq y_{i} \right] - \mathbb{1} \left[ h (\mathbf{x}_{i}') \neq y_{i}' \right]$ is a fixed value and therefore

$$
\frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} \left(
    \mathbb{1} \left[
        h (\mathbf{x}_{i}) \neq y_{i} 
    \right] - \mathbb{1} \left[
        h (\mathbf{x}_{i}') \neq y_{i}'
    \right]
\right) = \frac{ 1 }{ n } \sum_{i = 1}^{n} \alpha_{i} \sigma_{i} 
$$

is a random variable with

$$
\mathbb{E}_{\sigma} \left[
    \frac{ 1 }{ n } \sum_{i = 1}^{n} \alpha_{i} \sigma_{i} 
\right] = \frac{ 1 }{ n } \sum_{i = 1}^{n} \alpha_{i} \mathbb{E}_{\sigma} [\sigma_{i}] = 0.
$$

Applying Hoeffding's inequality with $X_{i} = \alpha_{i} \sigma_{i}, \mu = 0, t = \frac{ \epsilon }{ 2 }$,

$$
\begin{aligned}
\mathbb{P} \left(
    \left\lvert 
        \frac{ 1 }{ n } \sum_{i = 1}^{n} X_{i} - \mathbb{E} \left[
            \frac{ 1 }{ n } \sum_{i = 1}^{n} X_{i}
        \right] 
    \right\rvert \geq t
\right) 
& \leq 2 \exp \left[
    -\frac{ 2 n^{2} t^{2} }{ \sum_{i=1}^{n} (b_{i} - a_{i})^{2} }
\right]
\\
\mathbb{P}_{\sigma} \left(
    \left\lvert 
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \alpha_{i} \sigma_{i} - 0
    \right\rvert \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) 
& \leq 2 \exp \left[
    - \frac{ 2 n^{2} \frac{ \epsilon^{2} }{ 4 } }{ 4 n }
\right]
\\
\mathbb{P}_{\sigma} \left(
    \left\lvert 
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \alpha_{i} \sigma_{i}
    \right\rvert \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) 
& \leq 2 \exp \left[
    - \frac{ n \epsilon^{2} }{ 8 }
\right].
\end{aligned}
$$

To get the probability for any $h \in \mathcal{H}$, 
we apply union bound on all possible label assignments that $\mathcal{H}$ can make over the set $\mathcal{S} \cup \mathcal{S}'$,

$$
\begin{aligned}
\mathbb{P}_{\sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma) \mid \mathcal{S}, \mathcal{S}')
& =
\mathbb{P}_{\sigma} \left(
    \exist h \in \mathcal{H}: \left\lvert 
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \alpha_{i} \sigma_{i}
    \right\rvert \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) 
\\
& = \mathbb{P}_{\sigma} \left(
    \exist h \in \mathcal{H} (\mathcal{S} \cup \mathcal{S}'): \left\lvert 
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \alpha_{i} \sigma_{i}
    \right\rvert \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) 
\\
& \leq \sum_{h \in \mathcal{H} (\mathcal{S} \cup \mathcal{S}')} \mathbb{P}_{\sigma} \left(
    \left\lvert 
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \alpha_{i} \sigma_{i}
    \right\rvert \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) 
\\
& \leq 2 \Pi_{\mathcal{H}} (2 n) \exp \left[
    - \frac{ n \epsilon^{2} }{ 8 }
\right].
\\
\end{aligned}
$$

Note that the term $2 \Pi_{\mathcal{H}} (2 n) \exp \left[ - \frac{ n \epsilon^{2} }{ 8 } \right]$ doesn't depend on $\mathcal{S}, \mathcal{S}'$.
Since the expectation of a constant is that constant,
we have proved the claim

$$
\mathbb{E}_{\mathcal{S}, \mathcal{S}} \left[
    \mathbb{P}_{\sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma) \mid \mathcal{S}, \mathcal{S}') 
\right] \leq \mathbb{E}_{\mathcal{S}, \mathcal{S}} \left[
    2 \Pi_{\mathcal{H}} (2 n) \exp \left[ 
        - \frac{ n \epsilon^{2} }{ 8 } 
    \right]
\right] \leq 2 \Pi_{\mathcal{H}} (2 n) \exp \left[ 
    - \frac{ n \epsilon^{2} }{ 8 } 
\right].
$$

Finally we can prove the theorem by using all of the claims above

$$
\begin{aligned}
\mathbb{P}_{\mathcal{S}} (B (\mathcal{S})) 
& \leq 2 \mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}'))
\\
& = 2 \mathbb{E}_{\mathcal{S}, \mathcal{S}'} \left[
    \mathbb{P}_{\sigma} (B' (\mathcal{S}, \mathcal{S}', \sigma) \mid \mathcal{S}, \mathcal{S}')
\right]
\\
& \leq 4 \Pi_{\mathcal{H}} (2 n) \exp \left[ 
    - \frac{ n \epsilon^{2} }{ 8 } 
\right].
\end{aligned}
$$ 

By setting $\delta = 4 \Pi_{\mathcal{H}} (2 n) \exp \left[ - \frac{ n \epsilon^{2} }{ 8 } \right]$,

$$
\begin{aligned}
\delta
& = 4 \Pi_{\mathcal{H}} (2 n) \exp \left[ 
    - \frac{ n \epsilon^{2} }{ 8 } 
\right]
\\
n
& = 8 \frac{ 
    \log \Pi_{\mathcal{H}} (2 n) + \log \frac{ 4 }{ \delta }
}{
    \epsilon^{2}   
}.
\end{aligned}
$$

:::