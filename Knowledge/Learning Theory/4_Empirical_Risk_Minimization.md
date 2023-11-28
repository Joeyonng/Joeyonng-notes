# Empirical Risk Minimization

Since the underlying distribution $\mathbb{P}_{X, Y}$ is unknown,
the true risk cannot be calculated and therefore Bayesian decision theory can not be applied in practice.

Instead, we use the **empirical risk minimization** (ERM) algorithm in practice,
which produces the empirical risk minimizer that is similar to Bayer's classifier as it minimizes the empirical risk instead of the unknown true risk.

## No free lunch theorem

The **no-free-lunch** (NFL) theorem for machine learning states that there is no algorithm that can generate perfect hypothesis for any distribution using a finite training set.

:::{#thm-nfl}

TODO

:::

Another interpretation of the NFL theorem is that any two algorithms are equivalent when their performance is averaged across all possible distributions.
Therefore, one must make some biased assumptions about the underlying distribution about the targeted problems,
so that the algorithm can be designed to have good performance on the interested problem but having bad performance on the problems that we don't care.

## ERM with inductive bias

To apply the NFL theorem to ERM, 
we make assumptions about the underlying distribution by adding **inductive bias** to the ERM algorithm. 
The inductive bias implies that we have a predetermined preference for some hypotheses over other hypotheses. 
One reasonable approach to inductive bias is to restrict the hypothesis class that ERM considers.
Therefore, instead of looking for the best hypothesis over all possible functions, 
ERM method minimizes the risk over a selected hypothesis class $\mathcal{H}$ to derive the empirical risk minimizer $h_{n}$

$$
h_{n} = \argmin_{h \in \mathcal{H}} R_{n} (h).
$$

:::{#lem-ERM}

A special property of the ERM over any hypothesis class $\mathcal{H}$ is that 

$$
\forall h \in \mathcal{H}: R (h) - R (h_{n}) \leq 2 \max_{\hat{h} \in \mathcal{H}} \lvert R (\hat{h}) - R_{n} (\hat{h}) \rvert.
$$

:::

:::{.callout-note collapse="true" title="Proof"}

By definition, for all $h \in \mathcal{H}$,

$$
\begin{aligned}
R (h) - R (h_{n}) 
& = (R (h) + R_{n} (h) - R_{n} (h)) - (R (h_{n}) + R_{n} (h_{n}) - R_{n} (h_{n}))
\\
& = (R_{n} (h) - R_{n} (h_{n})) + (R (h) - R_{n} (h)) + (R_{n} (h_{n}) - R (h_{n}))
\end{aligned}
$$

Since $h_{n}$ is the one that minimizes $R_{n}$, 

$$
R_{n} (h) - R_{n} (h_{n}) \geq 0,
$$ 

so

$$
R (h) - R (h_{n}) \leq (R (h) - R_{n} (h)) + (R_{n} (h_{n}) - R (h_{n}))
$$

Since both $h, h_{n} \in \mathcal{H}$, 

$$
R (h) - R_{n} (h) \leq \max_{\hat{h} \in \mathcal{H}} \lvert R (\hat{h}) - R_{n} (\hat{h}) \rvert
\\
R_{n} (h_{n}) - R (h_{n}) \leq \max_{\hat{h} \in \mathcal{H}} \lvert R (\hat{h}) - R_{n} (\hat{h}) \rvert,
$$

so

$$
R (h) - R (h_{n}) \leq (R (h) - R_{n} (h)) + (R_{n} (h_{n}) - R (h_{n}))
\leq 2 \max_{h \in \mathcal{H}} \lvert R (h) - R_{n} (h) \rvert.
$$

:::