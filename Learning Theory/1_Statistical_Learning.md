# Statistical Learning

## Learning problem

The goal of machine learning is to use algorithms to learn from the data.
The data here refers to labeled instances $(\mathbf{x}, y) \in \mathcal{X} \times \mathcal{Y}$, 
where

- The instance $\mathbf{x}$ is usually a vector that belongs to an instance space $\mathcal{X}$;

- The label $y$ is usualy a scalar that belongs to a label space $\mathcal{Y}$. 

For simplicity, we will write the labeled instances $z \coloneqq (\mathbf{x}, y)$ and the space of labeled instances as $\mathcal{Z} \coloneqq \mathcal{X} \times \mathcal{Z}$.

Machine learning problems usually have two sets of data:

- Training set: the training set consists of a finite number of labeled instances from which the algorithms can learn. 

- Test set: the test set may consist of an infinite number of labeled instances that are used to evaluate the performance of the algorithm in a real-world setting. 

### Decision function

A decision function is a function $f: \mathcal{X} \to \mathcal{Y}$ whose domain is $\mathcal{X}$ and the range is $\mathcal{Y}$ 

$$
\hat{y} = f (\mathbf{x})
$$

that maps each input instance $\mathbf{x} \in \mathcal{X}$ to a label $y \in \mathcal{Y}$. 

Here we have two types of decision functions that have slightly different meanings in the context of machine learning

- Concept $c$ and concept class $C$: a concept from a concept class $c \in \mathcal{C}$ is the decision function that the algorithm wants to learn, which assigns all correct labels for given instances.

- Hypothesis $h$ and hypothesis class $H$: a hypothesis from a hypothesis class $h \in \mathcal{H}$ is the decision function that the algorithm actually learns from the hypothesis class. 

### Loss function

The way we evaluate a function $f$ on a labeled instance $(\mathbf{x}, y)$ is determined by a loss function $L: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}^{+}$ 

$$
L (z) = L (f (\mathbf{x}), y)
$$

which calculates some notion of discrepancy between the true label $y$ and the predicated label $\hat{y} = f (\mathbf{x})$. 

All the loss functions used in this note are 0-1 loss for binary classification problem

$$
L (z) = L (f (\mathbf{x}), y) = \mathbb{1} \left[
    f (\mathbf{x}) \neq y
\right],
$$

which incurs a loss of 1 if the predicated label is the same as the true label and 0 if they are the same.

## Learning in a probability setting

In a statistical learning problem, 
each labeled instance is an **independent and identically distributed** (i.i.d.) draw from some fixed but unknown joint distribution $\mathbb{P}_{\mathbf{X}, Y}$ over $\mathcal{X} \times \mathcal{Y}$ that describes the probability that both $\mathbf{x}$ and $y$ happens in the real world.

This means that there is always a probability associated with each term:

- the distribution $\mathbb{P}_{\mathbf{X}}$ for a multivariate random variable $\mathbf{X}$ that describes the probability of an instance $\mathbf{x}$

- the distribution $\mathbb{P}_{Y}$ for a random variable $Y$ that describes the probability of a label $y$.

We can decompose the joint probability according to the chain rule:

$$ 
\mathbb{P}_{\mathbf{X}, Y}(\mathbf{x}, y) = \mathbb{P}_{\mathbf{X} \mid Y}(\mathbf{x} \mid y) \mathbb{P}_{Y}(y), 
$$

where $\mathbb{P}_{\mathbf{X} \mid Y}(\mathbf{x} \mid y)$ is called class conditional probability, which gives the probability of the instance if we know the label is $y$.

For simplicity, sometimes we will write $\mathbb{P}_{Z} \coloneqq \mathbb{P}_{\mathbf{X}, Y}$ to denote the probability of the labeled instance. 

### True risk

The **true risk** of the hypothesis $h$ is defined as the expectation of the loss function over the joint probability

$$
R (f) = \mathbb{E}_{Z} [L (z)] $$

which is the probability that $h$ makes a mistake if the loss function is 0-1 loss

$$
R (f) = \mathbb{P}_{\mathbf{X}, Y} \left[
    \mathbb{1} \left[
        h (\mathbf{x}) \neq y
    \right]
\right].
$$

### Empirical risk

Since $\mathbb{P}_{Z}$ is unknown,
the risk of the decision function cannot be evaluated. 
Instead, the **empirical risk** function is used with the past data of $n$ labeled instances $\mathcal{S} = \{ z_{1}, \dots, z_{n} \}$ as a surrogate function for the risk function

$$
R_{\mathcal{S}} (f) = \frac{ 1 }{ n } \sum_{i = 1}^{n} L (z_{i}),
$$

which is the average number of mistakes $f$ made in $\mathcal{D}^{n}$ if the loss is 0-1 loss

$$
R_{\mathcal{S}} (f) = \frac{ 1 }{ n } \sum_{i = 1}^{n} \mathbb{1} \left[
    h (\mathbf{x}_{i}) \neq y_{i}
\right].
$$

The idea is that if the past data we have is representative of the actual distribution, 
then it will be the case that the empirical risk will be close to the true risk.

Note that the expectation of the empirical risk over all samples is the true risk

$$
\begin{aligned}
\mathbb{E}_{\mathcal{S}} \left[
    R_{\mathcal{S}} (f)
\right] 
& = \mathbb{E}_{Z} \left[
    \frac{ 1 }{ n } \sum_{i = 1}^{n} L (z_{i})
\right]
\\
& = \frac{ 1 }{ n } \sum_{i = 1}^{n} \mathbb{E}_{Z} [L (z_{i})]
\\
& = \frac{ 1 }{ n } \sum_{i = 1}^{n} R (f)
\\
& = R (f).
\end{aligned}
$$