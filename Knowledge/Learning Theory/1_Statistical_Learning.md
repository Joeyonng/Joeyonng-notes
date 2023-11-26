# Statistical Learning Framework

## Learning problem

The goal of machine learning is to use algorithms to learn from the data.
The data here refers to labeled instances $(x, y) \in \mathcal{X} \times \mathcal{Y}$, 
where

- The instance $x$ is usually a vector that belongs to an instance space $\mathcal{X}$;

- The label $y$ is usually a scalar that belongs to a label space $\mathcal{Y}$. 

For simplicity, we will write the labeled instances $z \coloneqq (x, y)$ and the space of labeled instances as $\mathcal{Z} \coloneqq \mathcal{X} \times \mathcal{Z}$.

Machine learning problems usually have two sets of data:

- Training set: the training set consists of a finite number of labeled instances from which the algorithms can learn. 

- Test set: the test set may consist of an infinite number of labeled instances that are used to evaluate the performance of the algorithm in a real-world setting. 

### Decision function

A decision function is a function $f: \mathcal{X} \to \mathcal{Y}$ whose domain is $\mathcal{X}$ and the range is $\mathcal{Y}$ 

$$
\hat{y} = f (x)
$$

that maps each input instance $x \in \mathcal{X}$ to a label $y \in \mathcal{Y}$. 

Here we have two types of decision functions that have slightly different meanings in the context of machine learning

- Concept $c$ and concept class $C$: a concept from a concept class $c \in \mathcal{C}$ is the decision function that the algorithm wants to learn, which assigns all correct labels for given instances.

- Hypothesis $h$ and hypothesis class $H$: a hypothesis from a hypothesis class $h \in \mathcal{H}$ is the decision function that the algorithm actually learns from the hypothesis class. 

### Loss function

The way we evaluate a function $f$ on a labeled instance $(x, y)$ is determined by a loss function $L: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}^{+}$ 

$$
L (z) = L (f (x), y)
$$

which calculates some notion of discrepancy between the true label $y$ and the predicated label $\hat{y} = f (x)$. 

All the loss functions used in this note are 0-1 loss 

$$
L (z) = L (f (x), y) = \mathbb{1} \left[
    f (x) \neq y
\right],
$$

which incurs a loss of 1 if the predicated label is the same as the true label and 0 if they are the same.

## Learning in a probability setting

In a statistical learning problem, 
each labeled instance is an **independent and identically distributed** (i.i.d.) draw from some fixed but unknown joint distribution $\mathbb{P}_{X, Y}$ over $\mathcal{X} \times \mathcal{Y}$ that describes the probability that both $x$ and $y$ happens in the real world.

This means that there is always a probability associated with each term:

- the distribution $\mathbb{P}_{X}$ for a multivariate random variable $X$ that describes the probability of an instance $x$

- the distribution $\mathbb{P}_{Y}$ for a random variable $Y$ that describes the probability of a label $y$.

We can decompose the joint probability according to the chain rule:

$$ 
\mathbb{P}_{X, Y}(x, y) = \mathbb{P}_{X \mid Y}(x \mid y) \mathbb{P}_{Y}(y), 
$$

where $\mathbb{P}_{X \mid Y}(x \mid y)$ is called class conditional probability, which gives the probability of the instance if we know the label is $y$.

For simplicity, sometimes we will write $\mathbb{P}_{Z} \coloneqq \mathbb{P}_{X, Y}$ to denote the probability of the labeled instance. 

### True risk

The **true risk** of the hypothesis $h$ is defined as the expectation of the loss function over the joint probability

$$
R (h) =  \mathbb{E}_{X, Y} [L (h (X), Y)] = \mathbb{E}_{Z} [L (Z)] 
$$

which is the probability that $h$ makes a mistake if the loss function is 0-1 loss

$$
R (h) = \mathbb{P}_{X, Y} \left[
    \mathbb{1} \left[
        h (x) \neq y
    \right]
\right].
$$


::: {#lem-risk}

Apart from the expectation with respect to the join probability of $\mathbb{P}_{X, Y}$, 
the true risk of any hypothesis $h$ can also be written as the expectation of the conditional expectation of the loss function

$$
R(h) = \mathbb{E}_{X} \left[
    \mathbb{E}_{Y \mid X} \left[
        L (h (X), Y)
    \right]
\right].
$$

:::

::: {.callout-note collapse="true" title="Proof"}

The proof is based on the definition of the expectation and the chain rules of the probability 

$$
\begin{aligned}
R(h) 
& = \mathbb{E}_{X, Y} [L (h (X), Y)]
\\
& = \int \int \mathbb{P}_{X, Y} (x, y) L (h (x), y) \mathop{d x} \mathop{dy}
& [\text{definition of } \mathbb{E} [\cdot]]
\\
& = \int \int \mathbb{P}_{Y \mid X} (y \mid x) \mathbb{P}_{X} (x) L (g(x), y) \mathop{d x} \mathop{dy}
& [\text{probability chain rule}]
\\
& = \int \mathbb{P}_{X} (x) \int \mathbb{P}_{Y \mid X} (y \mid x) L (g(x), y) \mathop{dy} \mathop{d x}
\\
& = \mathbb{E}_{X} \left[
    \mathbb{E}_{Y \mid X} \left[
        L (h (X), Y)
    \right]
\right].
\end{aligned}
$$

:::

### Empirical risk

The **empirical risk** function is used with the past data of $n$ labeled instances $\mathcal{S} = \{ z_{1}, \dots, z_{n} \}$ as a surrogate function for the risk function

$$
R_{\mathcal{S}} (h) = \frac{ 1 }{ n } \sum_{i = 1}^{n} L (h (x_{i}), y) = \frac{ 1 }{ n } \sum_{i = 1}^{n} L (z_{i}),
$$

which is the average number of mistakes $h$ made in $\mathcal{D}^{n}$ if the loss is 0-1 loss

$$
R_{\mathcal{S}} (h) = \frac{ 1 }{ n } \sum_{i = 1}^{n} \mathbb{1} \left[
    h (x_{i}) \neq y_{i}
\right].
$$

The idea is that if the past data we have is representative of the actual distribution, 
then it will be the case that the empirical risk will be close to the true risk.

### Empirical risk as a unbiased estimator

The empirical risk is an **unbiased estimator** of the true risk. 
That is, the expectation of the empirical risk over all samples is the true risk

$$
\mathbb{E}_{\mathcal{S}} \left[
    R_{\mathcal{S}} (h)
\right] = R (h).
$$

::: {.callout-note collapse="true" title="Proof"}

$$
\begin{aligned}
\mathbb{E}_{\mathcal{S}} \left[
    R_{\mathcal{S}} (h)
\right] 
& = \mathbb{E}_{Z} \left[
    \frac{ 1 }{ n } \sum_{i = 1}^{n} L (z_{i})
\right]
\\
& = \frac{ 1 }{ n } \sum_{i = 1}^{n} \mathbb{E}_{Z} [L (z_{i})]
\\
& = \frac{ 1 }{ n } \sum_{i = 1}^{n} R (h)
\\
& = R (h).
\end{aligned}
$$

:::

Also, by the law of large numbers, we have $R_{n} (h) \to R(h)$ as $n \to \infty$, almost surely, 
which means the empirical risk is closed to the true risk if the sample size is large enough.

## Some probability facts

### Basics

- Complement rule

$$
\mathbb{P} (A > t) < \delta \implies \mathbb{P} (A \leq t) \geq 1 - \delta
$$