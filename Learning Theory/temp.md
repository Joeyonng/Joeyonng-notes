## Uniform convergence result

Let $\mathcal{F}$ be a finite set of hypotheses and $\mathbb{P}_{\mathbf{X}, Y}$ be a fixed distribution over $\mathcal{X} \times \mathcal{Y}$.
For any $\epsilon > 0$ and any $0 < \delta < 1$, 
if the dataset $\mathcal{D}^{n}$ is drawn i.i.d from $\mathbb{P}_{\mathbf{X}, Y}$ with 

$$
n \geq \frac{
    \log \lvert \mathcal{F} \rvert + \log \frac{ 2 }{ \delta }
}{
    2 \epsilon^{2}
},
$$

then with probability at least $1 - \delta$

$$
\lvert R_{n} (f) - R (f) \rvert \leq \epsilon 
$$

for all $f \in \mathcal{F}$. 

That is, if the number of instances in the dataset $\mathcal{D}^{n}$ is larger than 

$$
n \geq \frac{
    \log \lvert \mathcal{F} \rvert + \log \frac{ 2 }{ \delta }
}{
    2 \epsilon^{2}
},
$$

we have 

$$
\mathbb{P} \left(
    \sup_{f \in \mathcal{F}} \lvert R_{n} (f) - R (f) \rvert \leq \epsilon 
\right) \geq 1 - \delta.
$$


:::{prf:proof} Uniform convergence result
:label: uniform-convergence result
:class:dropdown

First note that the true risk is the expectation of the empirical risk with respect to the joint distribution $\mathbb{P}_{\mathbf{X}, Y}$

$$
R(f) = \mathbb{E}_{\mathbf{X}, Y} \left[
    R_{n} (f)
\right] = \mathbb{E}_{\mathbf{X}, Y} \left[
    \frac{ 1 }{ n } \sum_{i = 1}^{n} L (f (x_{i}), y_{i})
\right].
$$

Then we can view the 0-1 loss on an instance as a bounded random variable

$$
L_{i} = L (f (\mathbf{X_{i}}), Y_{i}) = \mathbb{1} \left[
    f (\mathbf{X_{i}}) \neq Y_{i}
\right] \in [0, 1]
$$ 
    
and apply Hoeffding's inequality on $L_{i}$

$$
\begin{aligned}
\mathbb{P} \left(
    \left\lvert 
        \frac{ 1 }{ n } \sum_{i = 1}^{n} L_{i} - \mathbb{E}_{\mathbf{X}, Y} \left[
            \frac{ 1 }{ n } \sum_{i = 1}^{n} L_{i}
        \right] \geq \epsilon
    \right\rvert 
\right) 
& \leq 2 \exp \left[
    -\frac{ 2 n^{2} \epsilon^{2} }{ \sum_{i=1}^{n} (b_{i} - a_{i})^{2} }
\right]
\\
\mathbb{P} \left(
    \lvert R_{n} (f) - \mathbb{E}_{\mathbf{X}, Y} \left[
        R_{n} (f)
    \right] \rvert \geq \epsilon
\right) 
& \leq 2 \exp \left[
    -\frac{ 2 n^{2} \epsilon^{2} }{ n }
\right]
\\
\mathbb{P} \left(
    \lvert R_{n} (f) - R (f) \rvert \geq \epsilon
\right) 
& \leq 2 \exp \left[
    - 2 n \epsilon^{2} 
\right].
\end{aligned}
$$

The above inequality only works for one $f \in \mathcal{F}$. 
we can apply union bound to extend it for all $f \in \mathcal{F}$, 

$$
\begin{aligned}
\mathbb{P} \left(
    \sup_{f \in \mathcal{F}} \lvert R_{n} (f) - R (f) \rvert \geq \epsilon
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
    \sup_{f \in \mathcal{F}} \lvert R_{n} (f) - R (f) \rvert \leq \epsilon
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

--- 

If there is an infinite number of possible hypotheses in a hypothesis class,
all the bounds that are positively related to the size of the hypothesis class will be infinite as well, 
which provides no information and therefore become useless. 
