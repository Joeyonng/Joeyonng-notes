# Bayesian Decision Theory

## Bayes classifier

**Bayes classifier** is the particular hypothesis $h^{*} (x)$ that minimizes the risk

$$ 
h^{*} = \argmin_{h} R (h)
$$

and the risk that Bayes decision rule achieves is called **Bayes Risk**, 

$$
R^{*} = R (h^{*})
$$

which is the minimum risk that any hypothesis can achieve if we know the true probabilities $\mathbb{P}_{X, Y}$.

### MAP rule

Since the true risk $R (h)$ does not depend on $X$ and @lem-risk shows that $R(h) = \mathbb{E}_{X} \left[ \mathbb{E}_{Y \mid X} \left[ L (h (X), Y) \right] \right]$,
the Bayes classifier can also be written as the hypothesis that minimizes the conditional expectation

$$ 
h^{*} = \argmin_{h} \mathbb{E}_{Y \mid X} \left[
    L (h (X), Y)
\right],
$$

which can be further simplied to **maximum a-posteriori probability (MAP) rule** if the loss function is 0-1 loss and there are $m$ labels $y \in [1, m]$

$$
h^{*} (x) = \argmax_{y \in [1, m]} \mathbb{P}_{Y \mid X} (y \mid x)
$$

::: {.callout-note collapse="true" title="Proof"}

According to the definition of Bayes classifier,

$$
\begin{aligned}
h^{*}
& = \argmin_{h} \mathbb{E}_{Y \mid X} \left[
    L (h (X), Y)
\right]
\\
& = \argmin_{h} \sum_{y=1}^{m} \mathbb{P}_{Y \mid X} (y \mid x) L (h, y) 
& [\text{def of } \mathbb{E}_{Y \mid X}] 
\\
& = \argmin_{h} \sum_{y = h (x)}^{m} \mathbb{P}_{Y \mid X} (y \mid x) \times 0 
+ 
\sum_{y \neq h (x)}^{m} \mathbb{P}_{Y \mid X}(y \mid x) \times 1 
& [\text{def of 0-1 loss}] 
\\
& = \argmin_{h} \sum_{y \neq h (x)}^{m} \mathbb{P}_{Y \mid X} (y \mid x) 
\\
& = \argmin_{h} \left[
    1 - \mathbb{P}_{Y \mid X} (h (x) \mid x) 
\right]
& [\sum_{x \neq \alpha} \mathbb{P}_{X} (x) = 1 - \mathbb{P}_{X} (\alpha) ]
\\
& = \argmax_{h} \mathbb{P}_{Y \mid X} (h (x) \mid x) 
& [\argmin_{x} (1 - f(x)) = \arg\max_{x} (f(x))].
\end{aligned}
$$

where the last line can be simplied to 

$$
h^{*} (x) = \argmax_{y \in [1, m]} \mathbb{P}_{Y \mid X} (y \mid x)
$$

since $h (x) \in [1, m]$.

:::

According to Bayes Theorem, 

$$ 
\begin{aligned}
\arg\max_{y} \mathbb{P}_{Y \mid \mathbf{X}}(y \mid \mathbf{x}) 
& = \arg\max_{y} \frac{\mathbb{P}_{\mathbf{X} \mid Y}(\mathbf{x} \mid y) \mathbb{P}_{Y}(y)}{\mathbb{P}_{\mathbf{X}}(\mathbf{x})} 
\\
& = \arg\max_{y} \mathbb{P}_{\mathbf{X} \mid Y}(\mathbf{x} \mid y) \mathbb{P}_{Y}(y) & [\mathbb{P}_{\mathbf{X}}(\mathbf{x}) \text{ doesn't depend on } y], 
\\
\end{aligned}
$$

MAP rule can thus be computed using the class conditional probability (likelihood) and the class probability (prior),
which is more practical since the class conditional probability and class probability can be more easily obtained from the data than the posterior probability. 

Using the log trick, the BDR for 0-1 loss is often calculated using: 

$$ 
\begin{aligned}
\arg\max_{y} \ln \mathbb{P}_{Y \mid \mathbf{X}}(y \mid \mathbf{x}) 
& = \arg\max_{y} \ln \mathbb{P}_{\mathbf{X} \mid Y}(\mathbf{x} \mid y) \mathbb{P}_{Y}(y) 
\\
& = \arg\max_{y} \ln \mathbb{P}_{\mathbf{X} \mid Y}(\mathbf{x} \mid y) + \ln \mathbb{P}_{Y}(y).
\\
\end{aligned}
$$

## MAP rule for binary classification

Since there are only 2 labels in the binary classification problem,
the MAP rule for binary classification is simplied to

$$
\begin{aligned}
h^{*} (x) 
& = \argmax_{y \in [0, 1]} \mathbb{P}_{Y \mid X} (y \mid x) 
\\
& = \mathbb{1} \left[
    \mathbb{P}_{Y \mid X} (1 \mid x) > \mathbb{P}_{Y \mid X} (0 \mid x)
\right]
\\
& = \begin{cases}
    1, \quad \mathbb{P}_{Y \mid X} (1 \mid x) > \frac{ 1 }{ 2 }  \\
    0, \quad \mathbb{P}_{Y \mid X} (1 \mid x) < \frac{ 1 }{ 2 }.
\end{cases}
\end{aligned}
$$

### Regression function

The conditional distribution $\mathbb{P}_{Y \mid X}$ can be modeled with a Bernoulli distribution $\mathbb{P}_{Y \mid X} (y \mid x) = \mathrm{Ber} (\eta (x))$,
where $\eta (x)$ is the **regression function**  

$$
\eta (x) = \mathbb{P}_{Y \mid X} (1 \mid x) = \mathbb{E}_{Y \mid X} (Y).
$$

:::{#lem-bayes-risk}

For any hypothesis $h$,
we can write its risk function with 0-1 loss for binary classification as

$$
R (h) = \mathbb{E}_{X} \left[
    \eta (X) (1 - h (X))
    + 
    (1 - \eta (X)) h (X)
\right].
$$

:::

::: {.callout-note collapse="true" title="Proof"}

According to the definition of the risk function

$$
R (h) = \mathbb{E}_{X} \left[
    \mathbb{E}_{Y \mid X} \left[
        L (h (X), Y)
    \right]
\right].
$$

Since the 0-1 loss for binary classification problem can be written as 

$$
L (h (x), y) = \mathbb{1} \left[
    h (x) \neq y
\right] = y (1 - h (x)) + (1 - y) h (x)
$$

we have

$$
\begin{aligned}
R (h) 
& = \mathbb{E}_{X} \left[
    \mathbb{E}_{Y \mid X} \left[
        L (h (X), Y)
    \right]
\right]
\\
& = \mathbb{E}_{X} \left[
    \mathbb{E}_{Y \mid X} \left[
        y (1 - h (x)) + (1 - y) h (x)
    \right]
\right]
\\
& = \mathbb{E}_{X} \left[
    \mathbb{E}_{Y \mid X} [y](1 - h (x)) 
    + 
    \mathbb{E}_{Y \mid X} [1 - y] h (x)
\right]
\\
& = \mathbb{E}_{X} \left[
    \eta (X) (1 - h (X))
    + 
    (1 - \eta (X)) h (X)
\right].
\end{aligned}
$$

:::

:::{#thm-bayes-risk}

The risk of the Bayes classifier for binary classification with 0-1 loss is the expectation of the minimum of $\eta (X)$ and $1 - \eta (X)$

$$
R (h^{*}) = \mathbb{E}_{X} \left[
    \min \left[ 
        \eta (X), 1 - \eta (X)
    \right]
\right]
$$

and is less than $\frac{ 1 }{ 2 }$ 

$$
\mathbb{E}_{X} \left[
    \min \left[ 
        \eta (X), 1 - \eta (X)
    \right]
\right] \leq \frac{ 1 }{ 2 }.
$$

:::

::: {.callout-note collapse="true" title="Proof"}

By applying @lem-bayes-risk and replacing $h$ with the Bayes classifier $h^{*}$,
we have

$$
\begin{aligned}
R (h^{*})
& = \mathbb{E}_{X} \left[
    \eta (X) (1 - h^{*} (X))
    + 
    (1 - \eta (X)) h^{*} (X)
\right]
\\
& = \mathbb{E}_{X} \left[
    \eta (X) \mathbb{1} \left[
        \eta (X) < \frac{ 1 }{ 2 }
    \right]
    + 
    (1 - \eta (X)) \mathbb{1} \left[
        \eta (X) > \frac{ 1 }{ 2 }
    \right]
\right]
\\
& = \mathbb{E}_{X} \left[
    \min \left[
        \eta (X), 1 - \eta (X)
    \right]
\right]
\end{aligned}
$$

where the last inequality follows because 


$$
R (h^{*}) = \mathbb{E}_{X} [\eta (X)] = \mathbb{E}_{X} [\min [\eta (X), 1 - \eta (X)]], \quad \text{ if } \eta (X) < \frac{ 1 }{ 2 } \\
R (h^{*}) = \mathbb{E}_{X} [1 - \eta (X)] = \mathbb{E}_{X} [\min [\eta (X), 1 - \eta (X)]], \quad \text{ if } \eta (X) > \frac{ 1 }{ 2 }.
$$

Since $\min [\eta (X), 1 - \eta (X)] < \frac{ 1 }{ 2 }$,
its expectation is also less than $\frac{ 1 }{ 2 }$

$$
\mathbb{E}_{X} [\min [\eta (X), 1 - \eta (X)]] < \frac{ 1 }{ 2 }.
$$

:::

### Excess risk

For any hypothesis $h$, we are interested in the difference between its risk $R (h)$ and Bayes risk $R (h^{*})$,
which is called **excess risk** of $h$ 

$$
\mathcal{E} (h) = R (h) - R (h^{*}).
$$

:::{#thm-excess-risk}

For any hypothesis $h$,
the excess risk satisfies 

$$
\mathcal{E} (h) = \mathbb{E}_{X} \left[
    \lvert 2 \eta (X) - 1 \rvert \times \mathbb{1} \left[
        h (X) \neq h^{*} (X)
    \right]
\right]
$$

:::

::: {.callout-note collapse="true" title="Proof"}

By applying @lem-bayes-risk for $R (h)$ and $R (h^{*})$ and linearity of expectation,
we have

$$
\begin{aligned}
R (h) - R(h^{*}) 
& = \mathbb{E}_{X} \left[
    \eta (X) (h^{*} (X) - h (X))
    + 
    (1 - \eta (X)) (h (X) - h^{*} (X))
\right]
\\
& = \mathbb{E}_{X} \left[
    (2 \eta (X) - 1) (h^{*} (X) - h (X))
\right].
\end{aligned}
$$

Note that

$$
h^{*} (X) - h (X) =  \mathrm{sgn} [2 \eta (X) - 1] \times \mathbb{1} [h^{*} \neq h (X)],
$$

because it combines all 3 cases for the results of $h^{*} (X) - h (X)$.

1. If $h^{*} (X) = h (X)$, 

    $$
    h^{*} (X) - h (X) = 0.
    $$

1. Since $\eta (X) > \frac{ 1 }{ 2 } \implies h^{*} (X) = 1$, 
    if $h^{*} (X) = 1, h (X) = 0$, 

    $$
    h^{*} (X) - h (X) = 1 = \mathrm{sgn} [2 \eta (X) - 1].
    $$

1. Since $\eta (X) < \frac{ 1 }{ 2 } \implies h^{*} (X) = 0$, 
    if $h^{*} (X) = 0, h (X) = 1$, 

    $$
    h^{*} (X) - h (X) = -1 = \mathrm{sgn} [2 \eta (X) - 1].
    $$

Therefore,

$$
\begin{aligned}
R (h) - R(h^{*}) 
& = \mathbb{E}_{X} \left[
    (2 \eta (X) - 1) \mathrm{sgn} [2 \eta (X) - 1] \times \mathbb{1} [h^{*} \neq h (X)],
\right]
\\
& = \mathbb{E}_{X} \left[
    \lvert 2 \eta (X) - 1 \rvert \times \mathbb{1} [h^{*} \neq h (X)]
\right].
\end{aligned}
$$

where the last equality holds since $x \times \mathrm{sgn} [x] = \lvert x \rvert$.

:::