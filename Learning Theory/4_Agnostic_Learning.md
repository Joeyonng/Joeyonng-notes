# Agnostic Learning

Agnostic learning is the PAC learning in the unrealizable setting.
That is, the perfect concept cannot be realized because either one of the following events happens

- the concept that the algorithm $A$ learns is not in the hypothesis class that $A$ considers,

- any instance can have contradictory labels, amd therefore there doesn't exist a concept that can perfectly label all instances in the input space. 

## Uniform convergence property

An algorithm $A$ has the **uniform convergence property** over the hypothesis class $\mathcal{H}$ if, 

- given a set of labeled instances $\mathcal{D}^{n}$, where instances and labels are sampled from *any joint distribution* $\mathbb{P}_{\mathbf{X}, Y}$ over the instance space and the label space, and there exists a function for some $\epsilon > 0 $ and $\delta > 0$ such that 

    $$
    n \geq n_{\mathcal{H}} (\epsilon, \delta),
    $$

- $A$ returns a hypothesis $h \in \mathcal{H}$, where the *difference between its true risk and estimated risk* is no greater than $\epsilon$ with probability at least $1 - \delta$

    $$
    \mathbb{P} (\lvert R (h) - R_{n} (h) \rvert \leq \epsilon) \geq 1 - \delta.
    $$

## Empirical risk minimizer

Since there is no way for any algorithm to learn a perfect concept that works any dataset in the agnostic settings,
the best hypothesis an algorithm can learn is the one that minimizes the empirical risk 

$$
h_{n} = \argmin_{h \in \mathcal{H}} R_{n} (h).
$$

A special property of the empirical risk minimizer is that 

$$
R (h) - R (h_{n}) \leq 2 \max_{h \in \mathcal{H}} \lvert R (h) - R_{n} (h) \rvert.
$$

:::{prf:proof} Uniform convergence result
:label: uniform-convergence result
:class:dropdown

$$
\begin{aligned}
R (h) - R (h_{n}) 
& = (R (h) + R_{n} (h) - R_{n} (h)) - (R (h_{n}) + R_{n} (h_{n}) - R_{n} (h_{n}))
\\
& = (R_{n} (h) - R_{n} (h_{n})) + (R (h) - R_{n} (h)) + (R_{n} (h_{n}) - R (h_{n}))
\end{aligned}
$$

Since $h_{n}$ is the one that minimizes $R_{n}$, 
$R_{n} (h) - R_{n} (h_{n}) \geq 0$, 
and therefore

$$
\begin{aligned}
R (h) - R (h_{n}) 
& \leq (R (h) - R_{n} (h)) + (R_{n} (h_{n}) - R (h_{n}))
\\
& \leq 2 \max_{h \in \mathcal{H}} \lvert R (h) - R_{n} (h) \rvert.
\end{aligned}
$$

:::

## Agnostic PAC model

An algorithm $A$ learns the concept class $\mathcal{C}$ in the **agnostic PAC model** by the hypothesis class $\mathcal{H}$ if, 

- given a set of labeled instances $\mathcal{D}^{n}$, where instances and labels are sampled from *any joint distribution* $\mathbb{P}_{\mathbf{X}, Y}$ over the instance space and the label space, and there exists a function for some $\epsilon > 0 $ and $\delta > 0$ such that 

    $$
    n \geq n_{\mathcal{H}} (\epsilon, \delta),
    $$

- $A$ returns a hypothesis $h \in \mathcal{H}$, where the *difference between its true risk and the minimum true risk achieved by any hypothesis in $\mathcal{H}$* is no greater than $\epsilon$ with probability at least $1 - \delta$

    $$
    \mathbb{P} (\lvert R (h) - \min_{h \in \mathcal{H}} R (h)] \rvert \leq \epsilon) \geq 1 - \delta.
    $$


## Sample complexity results 

### Uniform convergence result

An $A$ has the uniform convergence property over the hypothesis class $\mathcal{H}$ with the sample complexity

$$
n_{\mathcal{H}} (\epsilon, \delta) = \frac{
    \log \lvert \mathcal{H} \rvert + \log \frac{ 2 }{ \delta } 
}{
    2 \epsilon^{2}
}.
$$

:::{prf:proof} Uniform convergence result
:label: uniform-convergence result
:class:dropdown

Since the true risk of a hypothesis is the expectation of the empirical risk with respect to the joint distribution $\mathbb{P}_{\mathbf{X}, Y}$

$$
R(h) = \mathbb{E}_{\mathbf{X}, Y} \left[
    R_{n} (h)
\right] = \mathbb{E}_{\mathbf{X}, Y} \left[
    \frac{ 1 }{ n } \sum_{i = 1}^{n} L (h (x_{i}), y_{i})
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
        \frac{ 1 }{ n } \sum_{i = 1}^{n} L_{i} - \mathbb{E}_{\mathbf{X}, Y} \left[
            \frac{ 1 }{ n } \sum_{i = 1}^{n} L_{i}
        \right] 
    \right\rvert \geq \epsilon
\right) 
& \leq 2 \exp \left[
    -\frac{ 2 n^{2} \epsilon^{2} }{ \sum_{i=1}^{n} (b_{i} - a_{i})^{2} }
\right]
\\
\mathbb{P} \left(
    \lvert R_{n} (h) - \mathbb{E}_{\mathbf{X}, Y} \left[
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

### Agnostic PAC learnability for finite hypothesis class

If $A$ learns the concept by minimizing the empirical risk, 
then $A$ learns the concept class $\mathcal{C}$ by the finite hypothesis class $\mathcal{H}$ in the agnostic PAC model with the sample complexity

$$
n_{\mathcal{H}} (\epsilon, \delta) = \frac{
    2 \log \lvert \mathcal{H} \rvert + \log \frac{ 2 }{ \delta } 
}{
    \epsilon^{2}
}.
$$

:::{prf:proof} 
:label: 
:class:dropdown

We can prove this by applying the uniform convergence result and the property of the empirical risk minimizer

$$
R (h) - R (h_{n}) \leq 2 \max_{h \in \mathcal{H}} \lvert R (h) - R_{n} (h) \rvert,
$$

we can have if $A$ learns a hypothesis with the number of training instances

$$
n \geq \frac{
    \log \lvert \mathcal{H} \rvert + \log \frac{ 2 }{ \delta } 
}{
    2 \hat{\epsilon}^{2}
},
$$

then for any $h \in \mathcal{H}$ we have

$$
\begin{aligned}
\mathbb{P} (\lvert R (h) - R_{n} (h) \rvert \leq \hat{\epsilon})
& \geq 1 - \delta
\\
\mathbb{P} (\lvert R (h) - R (h_{n}) \rvert \leq 2 \hat{\epsilon})
& \geq 1 - \delta.
\end{aligned}
$$

Rewriting the statement by replacing $\hat{\epsilon} = \frac{ \epsilon }{ 2 }$,
we have the statement that if

$$
n \geq \frac{
    \log \lvert \mathcal{H} \rvert + \log \frac{ 2 }{ \delta } 
}{
    2 \hat{\epsilon}^{2}
} = 
\frac{
    \log \lvert \mathcal{H} \rvert + \log \frac{ 2 }{ \delta } 
}{
    2 \left(
        \frac{ 1 }{ 2 } \epsilon
    \right)^{2}
} = 
\frac{
    2 \left(
        \log \lvert \mathcal{H} \rvert + \log \frac{ 2 }{ \delta } 
    \right)
}{
    \epsilon^{2}
},
$$

then the hypothesis learned by minimizing the empirical risk $h_{n}$ has the following property for any $h \in \mathcal{H}$

$$
\mathbb{P} (\lvert R (h_{n}) - R(h) \rvert \leq \epsilon) \geq 1 - \delta.
$$

:::

### Agnostic PAC learnability for infinite hypothesis class

:::{prf:proof} 
:label: 
:class:dropdown

Let's first define 3 "bad" events that are useful in the following proof.

Given any set of instances $\mathcal{S} = \{ \mathbf{x}_{1}, \dots, \mathbf{x}_{n} \}$,
let $B (\mathcal{S})$ denote the event that there exists a hypothesis $h \in \mathcal{H}$ such that the difference between its true risk and empirical risk on $\mathcal{S}$ is larger than $\epsilon$,

$$
B (\mathcal{S}) \coloneqq \exist h \in \mathcal{H}: \lvert R_{\mathcal{S}} (h) -  R (h) \rvert \geq \epsilon.
$$

and therefore we want to prove

$$
\mathbb{P}_{\mathcal{S}} (B (\mathcal{S})) \leq \delta.
$$

Now let's draw the "ghost samples",
which is another set of i.i.d instances $\mathcal{S}' = \{ \mathbf{x}_{1}', \dots, \mathbf{x}_{n} \}$ from the distribution $\mathbb{P}_{\mathbf{X}}$,
and define another event $B'$ as a function of $\mathcal{S}$ and $\mathcal{S}'$,
which states that there exists a hypothesis $h \in \mathcal{H}$ such that the difference between its empirical risk on $\mathcal{S}$ and empirical risk on $\mathcal{S}'$ is larger than $\frac{ \epsilon }{ 2 }$,

$$
B (\mathcal{S}, \mathcal{S}') \coloneqq \exist h \in \mathcal{H}: \lvert R_{\mathcal{S}} (h) - R_{S'} (h) \rvert \geq \frac{ \epsilon }{ 2 }.
$$

Finally, let's define an event $B (\mathcal{S}, \mathcal{S}', \sigma)$ as a function of $\mathcal{S}, \mathcal{S}'$ and a set of independent Rademacher random variables $\sigma_{1}, \dots, \sigma_{n}$ that takes values $-1$ or $1$ with equal probabilities

$$
\begin{aligned}
B (\mathcal{S}, \mathcal{S}', \sigma) 
& \coloneqq \exist h \in \mathcal{H}: \lvert R_{\mathcal{\sigma S}} (h) - R_{\sigma S'} (h) \rvert \geq \frac{ \epsilon }{ 2 }.
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

which states that there exists a hypothesis $h \in \mathcal{H}$ such that the difference between its empirical risk on $\mathcal{S}$ and empirical risk on $\mathcal{S}'$ is larger than $\frac{ \epsilon }{ 2 }$,

**Claim 1**: $\mathbb{P}_{\mathcal{S}} (B (\mathcal{S}))$ is bounded by $\mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B (\mathcal{S}, \mathcal{S}'))$,

$$
\mathbb{P}_{\mathcal{S}} (B (\mathcal{S})) \leq 2 \mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B (\mathcal{S}, \mathcal{S}')).
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
the probability of the difference between $R (h)$ and $R_{\mathcal{S}'} (h)$ can be upper bounded by applying Chebyshev's inequality with $X = R'(h), \mu = R (h), t = \frac{ \epsilon }{ 2 }, \sigma^{2} = \mathrm{Var} [R_{\mathcal{S}'} (h)]$

$$
\begin{aligned}
\mathbb{P}_{X} \left(
    \lvert x - \mu \rvert \geq t
\right) 
& \leq \frac{ \sigma^{2} }{ t^{2} } 
\\
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} \left(
    \lvert R (h) - R_{S'} (h) \rvert \geq \frac{ \epsilon }{ 2 }
\right) 
& \leq \frac{ 4 \mathrm{Var} [R_{\mathcal{S}'} (h)] }{\epsilon^{2}}.
\end{aligned}
$$

Note that $h (\mathbf{x}_{i}) \neq y_{i}$ is a Bernoulli random variable whose variance is less than $0.25$

$$
\mathrm{Var} [R_{\mathcal{S}'} (h)] = \mathrm{Var} \left[
    \frac{ 1 }{ n } \sum_{\mathbf{x} \in \mathcal{S}'} h (\mathbf{x}_{i}) \neq y_{i}
\right] = \frac{ 1 }{ n^{2} } \sum_{\mathbf{x_{i} \in \mathcal{S}'}} \mathrm{Var} [h (\mathbf{x}) \neq y_{i}] \leq \frac{ 0.25 }{ n },
$$

and therefore,

$$
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} \left(
    \lvert R (h) - R_{S'} (h) \rvert \geq \frac{ \epsilon }{ 2 }
\right) \leq \frac{ 1 }{n \epsilon^{2}}.
$$

Assume that $n \epsilon^{2} \geq 2$

$$
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} \left(
    \lvert R (h) - R_{S'} (h) \rvert \geq \frac{ \epsilon }{ 2 }
\right) \leq \frac{ 1 }{ 2 }
$$

and take the inversion,

$$
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} \left(
    \lvert R (h) - R_{S'} (h) \rvert \leq \frac{ \epsilon }{ 2 }
\right) \geq \frac{ 1 }{ 2 }.
$$

Finally we have

$$
\begin{aligned}
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}') \mid B (\mathcal{S})) \mathbb{P}_{\mathcal{S}} (B (\mathcal{S}))
& \leq \mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}')) 
\\
\mathbb{P}_{\mathcal{S}} (B (\mathcal{S}))
& \leq 2 \mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}')).
\end{aligned}
$$

**Claim 2**: $\mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}')) = \mathbb{P}_{\mathcal{S}, \mathcal{S}', \sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma)) = \mathbb{E}_{\mathcal{S}, \mathcal{S}'} [\mathbb{P}_{\mathcal{S}, \mathcal{S}', \sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma) \mid \mathcal{S}, \mathcal{S}')]$, 

Since the event $B' (\mathcal{S}, \mathcal{S}')$ and $B'' (\mathcal{S}, \mathcal{S}', \sigma)$ only differ on the set of instances $\mathcal{S}, \mathcal{S}'$ and $\sigma \mathcal{S}, \sigma \mathcal{S}'$ and they can be seen as the set of instances i.i.d sampled from the $\mathcal{X}^{d}$,
their probability should be the same 

$$
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}')) = \mathbb{P}_{\mathcal{S}, \mathcal{S}', \sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma)).
$$

Also, by marginlization

$$
\mathbb{P}_{\mathcal{S}, \mathcal{S}', \sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma)) = \mathbb{E}_{\mathcal{S}, \mathcal{S}'} [\mathbb{P}_{\mathcal{S}, \mathcal{S}', \sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma) \mid \mathcal{S}, \mathcal{S}')].
$$

**Claim 3**: $\mathbb{P}_{\mathcal{S}, \mathcal{S}', \sigma} (B (\mathcal{S}, \mathcal{S}', \sigma), \mid \mathcal{S}, \mathcal{S}')$ is bounded by $2 \Pi_{\mathcal{H}} (2 n) \exp \left[ - \frac{ n \epsilon^{2} }{ 8 } \right]$.

Consider the probability for a fixed $h \in \mathcal{H}$,

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
the value $ \mathbb{1} \left[ h (\mathbf{x}_{i}) \neq y_{i} \right] - \mathbb{1} \left[ h (\mathbf{x}_{i}') \neq y_{i}' \right]$ is a fixed value and therefore

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

Applying Hoeffding's inequality with $X = \frac{ 1 }{ n } \sum_{i = 1}^{n} \alpha_{i} \sigma_{i}, \mu = 0, t = \frac{ \epsilon }{ 2 }$,

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
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} \left(
            \mathbb{1} \left[
                h (\mathbf{x}_{i}) \neq y_{i} 
            \right] - \mathbb{1} \left[
                h (\mathbf{x}_{i}') \neq y_{i}'
            \right]
        \right) - 0
    \right\rvert \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) 
& \leq 2 \exp \left[
    - \frac{ 2 n^{2} \frac{ \epsilon^{2} }{ 4 } }{ 4 n }
\right]
\\
& \leq 2 \exp \left[
    - \frac{ n \epsilon^{2} }{ 8 }
\right].
\end{aligned}
$$

To get the probability for any $h \in \mathcal{H}$, 
we apply union bound on all possible label assignments that $\mathcal{H}$ can make over the set $\mathcal{S} \cup \mathcal{S}'$,

$$
\begin{aligned}
& \mathbb{P}_{\sigma} \left(
    \exist h \in \mathcal{H}: \left\lvert 
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} \left(
            \mathbb{1} \left[
                h (\mathbf{x}_{i}) \neq y_{i} 
            \right] - \mathbb{1} \left[
                h (\mathbf{x}_{i}') \neq y_{i}'
            \right]
        \right) - 0
    \right\rvert \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) 
\\
& = \mathbb{P}_{\sigma} \left(
    \exist h \in \mathcal{H} (\mathcal{S} \cup \mathcal{S}'): \left\lvert 
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} \left(
            \mathbb{1} \left[
                h (\mathbf{x}_{i}) \neq y_{i} 
            \right] - \mathbb{1} \left[
                h (\mathbf{x}_{i}') \neq y_{i}'
            \right]
        \right) - 0
    \right\rvert \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) 
\\
& \leq \sum_{h \in \mathcal{H} (\mathcal{S} \cup \mathcal{S}')} \mathbb{P}_{\sigma} \left(
    \left\lvert 
        \frac{ 1 }{ n } \sum_{i = 1}^{n} \sigma_{i} \left(
            \mathbb{1} \left[
                h (\mathbf{x}_{i}) \neq y_{i} 
            \right] - \mathbb{1} \left[
                h (\mathbf{x}_{i}') \neq y_{i}'
            \right]
        \right) - 0
    \right\rvert \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) 
\\
& \leq 2 \Pi_{\mathcal{H}} (2 n) \exp \left[
    - \frac{ n \epsilon^{2} }{ 8 }
\right]
\\
\end{aligned}
$$

:::