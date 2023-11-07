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
then $A$ learns the concept class $\mathcal{C}$ by the hypothesis class $\mathcal{H}$ in the agnostic PAC model with the sample complexity

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