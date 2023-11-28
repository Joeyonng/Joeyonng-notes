# PAC Learning

Probably approximately correct (PAC) learning is a statistical learning objective that requires that the algorithm learns a hypothesis $h$ from a hypothesis class $\mathcal{H}$ using a given sample set $\mathcal{S}$ with the following properties.

- Correct: $h$ should achieve low true risk $R (h)$.

- Approximately: $R (h)$ should be approximately closed to the lowest true risk that any hypothesis can achieve $R (h) \approx \min_{\hat{h}} R (\hat{h})$.

- Probably: the event $R (h) \approx \min_{\hat{h}} R (\hat{h})$ should have high probability.

## Realizable case

Under the realizable assumption, 
it is assumed that there exists a perfect concept from a concept class $c \in \mathcal{C}$ such that all labels of the instances are labeled according to $c$ and 
the hypothesis class that our algorithm ERM considers is the concept class $\mathcal{H} = \mathcal{C}$.

:::{#def-consistent}

#### Consistent

We say that a hypothesis $h$ is **consistent** with a set of labeled instances $\mathcal{S} = \{ (\mathbf{x}_{1}, y_{1}), \dots, (\mathbf{x}_{n}, y_{n}) \}$ if $h (\mathbf{x}_{i}) = y_{i}$ for all $i$.

:::

Therefore, under the realizable assumption, 
ERM can always find a hypothesis that is consistent with any given training set,
and therefore we say that ERM learns in the consistency model.

### Consistency model

Learning in the consistency model requires the algorithm to always predict correctly on the training set,
but doesn't care much about the generalization of the performance on the test set. 

:::{#def-consistency-model}

#### Consistency model

An algorithm $A$ learns the hypothesis class $\mathcal{H} = \mathcal{C}$ in the **consistency model** if

- given any set of labeled instances $\mathcal{S} = \{ z_{1}, \dots, z_{n} \}$, where instances are sampled from *any distribution* $\mathbb{P}_{\mathbf{X}}$ over the instance space and are labeled by *any concept* $c \in \mathcal{C}$, 

- $A$ can find a concept $h \in \mathcal{H}$ that is consistent with $\mathcal{S}$ if $h$ exists, or $A$ outputs False if no such concept exists.

:::

### Probably Approximately Correct (PAC) model

Learning in the PAC model is more applicable in real world,
as it emphasizes more on the generalization ability of the learned function from the algorithm. 

:::{#def-pac-model}

#### PAC model

An algorithm $A$ learns the concept class $\mathcal{C}$ in the **PAC model** by the hypothesis class $\mathcal{H} = \mathcal{C}$ if, 

- given a set of labeled instances $\mathcal{S} = \{ z_{1}, \dots, z_{n} \}$, where instances are sampled from *any distribution* $\mathbb{P}_{\mathbf{X}}$ over the instance space and are labeled by *any concept* $c \in \mathcal{C}$, and there exists a function for some $\epsilon > 0 $ and $\delta > 0$ such that 

    $$
    n \geq n_{\mathcal{H}} (\epsilon, \delta),
    $$

- $A$ returns a hypothesis $h \in \mathcal{H}$, where **its true risk** is no greater than $\epsilon$ with probability at least $1 - \delta$

    $$
    \mathbb{P} (R (h) \leq \epsilon) \geq 1 - \delta.
    $$

:::

### ERM as a PAC learner

Here we present some results about the generalization error of the algorithms using the definitions of consistency model and PAC model. 
Since ERM learns the hypothesis class in the consistency model, the following theorems naturally apply to it.

The following theorem states that a **finite concept class** $\mathcal{C}$ is PAC learnable by the same hypothesis class $\mathcal{H} = \mathcal{C}$ if $\mathcal{C}$ is learnable in the consistency model,
and proves its sample complexity as a function of the size of the hypothesis class.

:::{#thm-}

If an algorithm $A$ learns a finite concept class $\mathcal{C}$ in the consistency model, 
then $A$ learns the concept class $\mathcal{C}$ by the hypothesis class $\mathcal{H} = \mathcal{C}$ in the PAC model with

$$
n_{\mathcal{H}} (\epsilon, \delta) = \frac{
    \log \lvert \mathcal{H} \rvert + \log \frac{ 1 }{ \delta } 
}{
    \epsilon
}.
$$

:::

:::{.callout-note collapse="true" title="Proof"}

Another way to state the PAC learnability with the consistency model is

$$
\mathbb{P}_{\mathcal{S}} (\exist h \in \mathcal{H}: R_{\mathcal{S}} (h) = 0, R (h) \geq \epsilon) \leq \delta
$$

when $n \geq n_{\mathcal{H}} (\epsilon, \delta)$. 

Given $h \in \mathcal{H}$, 
by definition of the empirical risk we can write the probability that $h$ is consistent with $\mathcal{S}$ as 

$$
\begin{aligned}
\mathbb{P}_{\mathcal{S}} (R_{\mathcal{S}} (h) = 0)
& = \mathbb{P}_{\mathcal{S}} (h (\mathbf{x_{i}}) = y_{i}, \forall (\mathbf{x}_{i}, y_{i}) \in \mathcal{S})
\\
& \stackrel{(1)}{=} \prod_{i = 1}^{n} \mathbb{P}_{\mathbf{X}} (h (\mathbf{x}_{i}) = y_{i})
\\
& = \prod_{i = 1}^{n} 1 - \mathbb{P}_{\mathbf{X}} (h (\mathbf{x}_{i}) \neq y_{i})
\\
& \stackrel{(2)}{=} \prod_{i = 1}^{n} 1 - R (h)
\\
& = (1 - R (h))^{n}.
\end{aligned}
$$

1. (1) follows because the labeled instances in $\mathcal{S}$ are independent.

1. (2) follows because the true risk of $h$ is the probability of $h$ makes a mistake on a given labeled instance when the loss function is the 0-1 loss.

If we add the fact that $R (h) \geq \epsilon$, 

$$
\begin{aligned}
\mathbb{P}_{\mathcal{S}} (R_{\mathcal{S}} (h) = 0, R (h) \geq \epsilon)
& \leq (1 - \epsilon)^{n} 
\\
& \leq e^{- n \epsilon}
\end{aligned}
$$

where the last inequality uses the fact that 

$$
1 - x < e^{-x}, \forall x \in [0, 1].
$$

We can add the part $\exists h \in \mathcal{H}$ by applying the union bound 

$$
\mathbb{P}_{\mathcal{S}} (\exists h \in \mathcal{H}: R_{\mathcal{S}} (h) = 0, R (h) \geq \epsilon)
\leq \lvert \mathcal{H} \rvert e^{- n \epsilon},
$$

and make $\delta = \lvert \mathcal{H} \rvert e^{- n \epsilon}$,
we can derive

$$
n \geq \frac{
    \log \lvert \mathcal{H} \rvert + \log \frac{ 1 }{ \delta } 
}{
    \epsilon
}.
$$

:::

The following theorem states a similar results as above: an **infinite concept class** $\mathcal{C}$ it is PAC learnable by the same hypothesis class $\mathcal{H} = \mathcal{C}$ if $\mathcal{H}$ is learnable in the consistency model,
and proves the sample complexity as a function of the growth function of $\mathcal{H}$. 

:::{#thm-}

If an algorithm $A$ learns an infinite concept class $\mathcal{C}$ in the consistency model, 
then $A$ learns the concept class $\mathcal{C}$ by the hypothesis class $\mathcal{H} = \mathcal{C}$ in the PAC model with

$$
n_{\mathcal{H}} (\epsilon, \delta) = 2 \frac{
    \log \Pi_{\mathcal{H}} (2 n) + \log \frac{ 2 }{ \delta } 
}{
    \epsilon
}.
$$

:::

:::{.callout-note collapse="true" title="Proof"}

Let's first define 3 "bad" events that are useful in the following proof.

Given any set of labeled instances $\mathcal{S} = \{ z_{1}, \dots, z_{n} \}$,
the difference between its true risk and empirical risk on $\mathcal{S}$ is larger than $\epsilon$,
let $B (\mathcal{S})$ denote the event that there exists a hypothesis $h \in \mathcal{H}$ that is consistent with $\mathcal{S}$ but has the true risk larger than $\epsilon$

$$
B (\mathcal{S}) \coloneqq \exist h \in \mathcal{H}: R_{\mathcal{S}} (h) = 0,  R (h) \geq \epsilon.
$$

and therefore we want to prove

$$
\mathbb{P}_{\mathcal{S}} (B (\mathcal{S})) \leq \delta.
$$

Now let's draw the "ghost samples",
which is another set of i.i.d labeled instances $\mathcal{S}' = \{ z_{1}', \dots, z_{n}' \}$ from the distribution $\mathbb{P}_{Z}$,
and define another event $B'$ as a function of $\mathcal{S}$ and $\mathcal{S}'$,
which states that there exists a hypothesis $h \in \mathcal{H}$ that is consistent with $\mathcal{S}$ but has empirical risk on $\mathcal{S}'$ larger than $\frac{ \epsilon }{ 2 }$

$$
B' (\mathcal{S}, \mathcal{S}') \coloneqq \exist h \in \mathcal{H}: R_{\mathcal{S}} (h) = 0,  R_{S'} (h) \geq \frac{ \epsilon }{ 2 }.
$$

Finally, let's define an event $B (\mathcal{S}, \mathcal{S}', \sigma)$ as a function of $\mathcal{S}, \mathcal{S}'$, and a set of independent Rademacher random variables $\sigma_{1}, \dots, \sigma_{n}$ that takes values $-1$ or $1$ with equal probabilities

$$
B'' (\mathcal{S}, \mathcal{S}', \sigma) \coloneqq \exist h \in \mathcal{H}: R_{\mathcal{S}_{\sigma}} (h) = 0, R_{\mathcal{S}_{\sigma}'} (h) \geq \frac{ \epsilon }{ 2 }.
$$

where the samples $\mathcal{S}_{\sigma}, \mathcal{S}_{\sigma}'$ are created by swapping the labeled instances in $\mathcal{S}, \mathcal{S}'$ based on the values of $\sigma$

- $z_{i}$ and $z_{i}'$ are swapped if the corresponding $\sigma_{i} = 1$,

- and $z_{i}$ and $z_{i}'$ are not swapped if the corresponding $\sigma_{i} = -1$.

The event $B'' (\mathcal{S}, \mathcal{S}', \sigma)$ states that there exists a hypothesis $h \in \mathcal{H}$ such that the difference between its empirical risk on $\mathcal{S}_{\sigma}$ and empirical risk on $\mathcal{S}_{\sigma}'$ is larger than $\frac{ \epsilon }{ 2 }$.

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
    R_{\mathcal{S}'} (h) \geq \frac{ \epsilon }{ 2 }
\right)
$$

because the event $B' (\mathcal{S}, \mathcal{S}')$ is the event $R_{\mathcal{S}'} (h) \geq \frac{ \epsilon }{ 2 }$ if the event $B (\mathcal{S})$ is given.

Since $R (h)$ is the mean of $R_{\mathcal{S}'} (h)$,
we can apply the lower tail case of the Chernoff bound for the average of Bernoulli variables and set $X = R_{\mathcal{S}'} (h), \mu = R (h), \delta = \frac{ 1 }{ 2 }$

$$
\begin{aligned}
\mathbb{P}_{X} (X \leq (1 - \delta) \mu) 
& \leq \exp \left[
    -\frac{ n \delta^{2} \mu }{ 2 }
\right]
\\
\mathbb{P} \left(
    R_{\mathcal{S}'} (h) \leq \frac{ R (h) }{ 2 }
\right) 
& \leq \exp \left[
    -\frac{ n R (h) }{ 8 }
\right].
\end{aligned}
$$

Since $R (h) \geq \epsilon$ and the assumption states that $n > \frac{ 8 }{ \epsilon }$

$$
\mathbb{P} \left(
    R_{\mathcal{S}'} (h) \leq \frac{ \epsilon }{ 2 }
\right) \leq \mathbb{P} \left(
    R_{\mathcal{S}'} (h) \leq \frac{ R (h) }{ 2 }
\right) \leq \exp \left[
    \frac{ - n R(h) }{ 8 }
\right] \leq \exp \left[
    \frac{ - R(h) }{ \epsilon } 
\right] \leq \frac{ 1 }{ e } \leq \frac{ 1 }{ 2 }
\\
\mathbb{P} \left(
    R_{\mathcal{S}'} (h) \geq \frac{ \epsilon }{ 2 }
\right) \geq \frac{ 1 }{ 2 }
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

**Claim 3**: $\mathbb{E}_{\mathcal{S}, \mathcal{S}'} [\mathbb{P}_{\sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma) \mid \mathcal{S}, \mathcal{S}')]$ is upper-bounded by $\Pi_{\mathcal{H}} (2 n) \exp \left[ - \frac{ n \epsilon }{ 2 } \right]$

$$
\mathbb{E}_{\mathcal{S}, \mathcal{S}} \left[
    \mathbb{P}_{\sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma) \mid \mathcal{S}, \mathcal{S}') 
\right] \leq \Pi_{\mathcal{H}} (2 n) \exp \left[ 
    - \frac{ n \epsilon }{ 2 } 
\right].
$$

Remember that $\mathcal{S}, \mathcal{S}'$ all have $n$ instances and therefore there are $n$ pairs of instances $(\mathbf{x}_{1}, \mathbf{x}_{1}'), \dots, (\mathbf{x}_{n}, \mathbf{x}_{n}')$.
There are 3 cases for the corrections of the predictions made by $h$ for each pair $(h (\mathbf{x}_{i}), h (\mathbf{x}_{i}'))$. 

1. Both $h (\mathbf{x}_{i}), h (\mathbf{x}_{i}')$ are incorrect.

1. Either $h (\mathbf{x}_{i})$ or $h (\mathbf{x}_{i}')$ is incorrect (correct).

1. Both $h (\mathbf{x}_{i}), h (\mathbf{x}_{i}')$ are correct.

First if there is a pair in $\mathcal{S}, \mathcal{S}'$ with case 1, then

$$
\mathbb{P}_{\sigma} \left(
    R_{\mathcal{S}_{\sigma}} (h) = 0, R_{\mathcal{S}_{\sigma}'} (h) \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) = 0
$$

because $R_{\mathcal{S}_{\sigma}} (h) > 0$ no matter how to generate $\mathcal{S}_{\sigma}$ by swapping instances in $\mathcal{S}, \mathcal{S}'$. 

Then denoted by $r$ the number of pairs in $\mathcal{S}, \mathcal{S}'$ that case 2 is true, 
if $r < \frac{ \epsilon n }{ 2 }$, 

$$
\mathbb{P}_{\sigma} \left(
    R_{\mathcal{S}_{\sigma}} (h) = 0, R_{\mathcal{S}_{\sigma}'} (h) \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) = 0
$$

because $R_{\mathcal{S}_{\sigma}'} (h) < \frac{ \epsilon }{2}$ no matter how to generate $\mathcal{S}_{\sigma}'$ by swapping instances in $\mathcal{S}, \mathcal{S}'$.

When $r \geq \frac{ \epsilon n }{ 2 }$, 
the event $R_{\mathcal{S}_{\sigma}} (h) = 0, R_{\mathcal{S}_{\sigma}'} (h) \geq \frac{ \epsilon }{ 2 }$ is possible and its possibility is 

$$
\mathbb{P}_{\sigma} \left(
    R_{\mathcal{S}_{\sigma}} (h) = 0, R_{\mathcal{S}_{\sigma}'} (h) \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) = \left(
    \frac{ 1 }{ 2 }
\right)^{r} \leq 2^{- \frac{ \epsilon n }{ 2 }}
$$

because the independent Rademacher random variables in $\sigma$ must take $1$ with probability $\frac{ 1 }{ 2 }$ for all $r'$ mistakes that were in $\mathcal{S}$ and swapped to be in $\mathcal{S}_{\sigma}'$,
and take $-1$ with probability $\frac{ 1 }{ 2 }$ for the $r - r'$ mistakes that were in $\mathcal{S}'$ and are stayed in $\mathcal{S}_{\sigma}'$.

Since the probability of the case 3 is already included in the calculation of the above probabilities,
we can prove the claim by adding probabilities for all cases

$$
\mathbb{P}_{\sigma} \left(
    R_{\mathcal{S}_{\sigma}} (h) = 0, R_{\mathcal{S}_{\sigma}'} (h) \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) \leq 2^{- \frac{ \epsilon n }{ 2 }}.
$$

To get the probability for any $h \in \mathcal{H}$, 
we apply union bound on all possible label assignments that $\mathcal{H}$ can make over the set $\mathcal{S} \cup \mathcal{S}'$,

$$
\begin{aligned}
\mathbb{P}_{\sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma) \mid \mathcal{S}, \mathcal{S}') 
& = \mathbb{P}_{\sigma} \left(
    \exist h \in \mathcal{H}: R_{\mathcal{S}_{\sigma}} (h) = 0, R_{\mathcal{S}_{\sigma}'} (h) \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) 
\\
& = \mathbb{P}_{\sigma} \left(
    \exist h \in \mathcal{H} (\mathcal{S} \cup \mathcal{S}'): R_{\mathcal{S}_{\sigma}} (h) = 0, R_{\mathcal{S}_{\sigma}'} (h) \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) 
\\
& \leq \sum_{h \in \mathcal{H} (\mathcal{S} \cup \mathcal{S}')} \mathbb{P}_{\sigma} \left(
    R_{\mathcal{S}_{\sigma}} (h) = 0, R_{\mathcal{S}_{\sigma}'} (h) \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) 
\\
& \leq \Pi_{\mathcal{H}} (2 n) 2^{- \frac{ \epsilon n }{ 2 }},
\\
\end{aligned}
$$

where the last inequality is because of the definition of the growth function states that 

$$
\lvert \mathcal{H} (\mathcal{S} \cup \mathcal{S}') \rvert \leq \Pi_{H} (\lvert \mathcal{S} \rvert + \lvert \mathcal{S}' \rvert) = \Pi_{\mathcal{H}} (2 n).
$$

Note that the term $\Pi_{\mathcal{H}} (2 n) 2^{- \frac{ n \epsilon }{ 2 }}$ doesn't depend on $\mathcal{S}, \mathcal{S}'$.
Since the expectation of a constant is that constant,
we have proved the claim

$$
\mathbb{E}_{\mathcal{S}, \mathcal{S}} \left[
    \mathbb{P}_{\sigma} (B'' (\mathcal{S}, \mathcal{S}', \sigma) \mid \mathcal{S}, \mathcal{S}') 
\right] \leq \mathbb{E}_{\mathcal{S}, \mathcal{S}} \left[
    \Pi_{\mathcal{H}} (2 n) \exp \left[ 
        - \frac{ n \epsilon }{ 2 } 
    \right]
\right] \leq \Pi_{\mathcal{H}} (2 n) \exp \left[ 
    - \frac{ n \epsilon }{ 2 } 
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
& \leq 2 \Pi_{\mathcal{H}} (2 n) 2^{- \frac{ n \epsilon }{ 2 }}.
\end{aligned}
$$ 

By setting $\delta = 2 \Pi_{\mathcal{H}} (2 n) 2^{- \frac{ n \epsilon }{ 2 }}$,

$$
\begin{aligned}
\delta
& = 2 \Pi_{\mathcal{H}} (2 n) 2^{- \frac{ n \epsilon }{ 2 }}
\\
n
& = 2 \frac{ 
    \log \Pi_{\mathcal{H}} (2 n) + \log \frac{ 2 }{ \delta }
}{
    \epsilon
}.
\end{aligned}
$$

:::

Now we can use the Sauer’s lemma to get a nice closed form expression on sample complexity result for the infinite class. 

:::{#thm-}

If an algorithm $A$ learns an infinite concept class $\mathcal{C}$ in the consistency model, 
then $A$ learns the concept class $\mathcal{C}$ by the hypothesis class $\mathcal{H} = \mathcal{C}$ in the PAC model with

$$
n_{\mathcal{H}} (\epsilon, \delta) = \frac{
    8 d \log \frac{ 16 }{ \epsilon} + 4 \log \frac{ 2 }{ \delta } 
}{
    \epsilon
},
$$

where $d = \mathrm{VC} (\mathcal{H})$. 

:::

:::{.callout-note collapse="true" title="Proof"}

By applying Sauer's lemma to the sample complexity results for the infinite classes

$$
\begin{aligned}
\frac{
    4 \log \Pi_{\mathcal{H}} (2 n) + 2 \log \frac{ 2 }{ \delta } 
}{
    \epsilon
} 
& \leq \frac{
    4 \log \left(
        \frac{ 2 e n }{ d }
    \right)^{d} + 2 \log \frac { 2 }{ \delta }
}{
    \epsilon
}
\\
& = \frac{ 4 d }{ \epsilon } \log n 
+ \frac{ 4 d  }{ \epsilon } \log \frac{ 2 e }{ d } 
+ \frac { 2 }{ \epsilon }\log \frac { 2 }{ \delta }
\end{aligned}
$$

Since $\log x \leq a x - \log a - 1$ for $a, x > 0$, 
we can show that 

$$
\begin{aligned}
\log n 
& \leq \frac{ \epsilon n }{ 8 d } - \log \frac{ \epsilon }{ 8 d  } - 1
\\
\frac{ 4 d }{ \epsilon } \log n
& \leq \frac{ 4 d }{ \epsilon } \left(
    \frac{ \epsilon n }{ 8 d } + \log \frac{ 8 d }{ \epsilon } - 1
\right)
\\
& = \frac{ n }{ 2 } + \frac{ 4 d }{ \epsilon } \log \frac{ 8 d }{\epsilon e }.
\end{aligned}
$$

By combining the results above,

$$
\begin{aligned}
\frac{
    4 \log \Pi_{\mathcal{H}} (2 n) + 2 \log \frac{ 2 }{ \delta } 
}{
    \epsilon
} 
& \leq \frac{ 4 d }{ \epsilon } \log n 
+ \frac{ 4 d }{ \epsilon } \log \frac{ 2 e }{ d } 
+ \frac { 2 }{ \epsilon }\log \frac { 2 }{ \delta }
\\
& \leq \frac{ n }{ 2 } 
+ \frac{ 4 d }{ \epsilon } \log \frac{ 8 d }{\epsilon e }
+ \frac{ 4 d }{ \epsilon } \log \frac{ 2 e }{ d } 
+ \frac { 2 }{ \epsilon }\log \frac { 2 }{ \delta }
\\
& \leq \frac{ n }{ 2 } 
+ \frac{ 4 d }{ \epsilon } \log \frac{ 16 }{\epsilon }
+ \frac { 2 }{ \epsilon }\log \frac { 2 }{ \delta }.
\end{aligned}
$$

Therefore, if we have a training set that has a number of instances 

$$
\begin{aligned}
n 
& \geq \frac{ n }{ 2 } 
+ \frac{ 4 d }{ \epsilon } \log \frac{ 16 }{\epsilon }
+ \frac { 2 }{ \epsilon }\log \frac { 2 }{ \delta }
\\
\frac{ n }{ 2 } 
& \geq \frac{ 4 d }{ \epsilon } \log \frac{ 16 }{\epsilon }
+ \frac { 2 }{ \epsilon }\log \frac { 2 }{ \delta }
\\
n 
& \geq \frac{
    8 d \log \frac{ 16 }{ \epsilon} + 4 \log \frac{ 2 }{ \delta } 
}{
    \epsilon
}.
\end{aligned}
$$

:::

## Unrealizable case

The PAC learning in the unrealizable setting is also called agnostic PAC learning
where the perfect concept cannot be realized because either one of the following events happens

- the concept that the algorithm $A$ learns is not in the hypothesis class that $A$ considers,

- any instance can have contradictory labels, amd therefore there doesn't exist a concept that can perfectly label all instances in the input space. 

### Agnostic PAC model

:::{#def-}

An algorithm $A$ learns the concept class $\mathcal{C}$ in the **agnostic PAC model** by the hypothesis class $\mathcal{H}$ if, 

- given a set of labeled instances $\mathcal{S}$, where instances and labels are sampled from *any joint distribution* $\mathbb{P}_{Z}$ over the instance space and the label space, and there exists a function for some $\epsilon > 0 $ and $\delta > 0$ such that 

    $$
    n \geq n_{\mathcal{H}} (\epsilon, \delta),
    $$

- $A$ returns a hypothesis $h \in \mathcal{H}$, where the *difference between its true risk and the minimum true risk achieved by any hypothesis in $\mathcal{H}$* is no greater than $\epsilon$ with probability at least $1 - \delta$

    $$
    \mathbb{P} (\lvert R (h) - \min_{h \in \mathcal{H}} R (h) \rvert \leq \epsilon) \geq 1 - \delta.
    $$

:::

### Uniform convergence implies agnostic PAC of ERM

The uniform convergence result guarantees the agnostic PAC learnability of ERM.

:::{#lem-uc-pac-erm}

If $A$ is the ERM algorithm that learns the hypothesis class $\mathcal{H}$,
which satisfies uniform convergence with sample complexity $n_{\mathcal{H}}^{u}$,
then $A$ learns $\mathcal{H}$ in the agnostic PAC model with the sample complexity

$$
n_{\mathcal{H}} (\epsilon, \delta) = n_{\mathcal{H}}^{u} (\frac{ \epsilon }{ 2 }, \delta).
$$

:::

:::{.callout-note collapse="true" title="Proof"}

Let $h_{n}$ be the hypothesis learned by ERM. 
According the property of the ERM, we have

$$
R (h) - R (h_{n}) \leq 2 \max_{h \in \mathcal{H}} \lvert R (h) - R_{n} (h) \rvert.
$$

Since $\mathcal{H}$ has @def:uniform-convergence-property,
if $n \geq n_{\mathcal{H}}^{u} (\hat{\epsilon}, \delta)$,
then

$$
\forall h \in \mathcal{H}, \mathbb{P} (\lvert R (h) - R_{n} (h) \rvert \leq \hat{\epsilon}) \geq 1 - \delta,
$$

which is equivalent of 

$$
\begin{aligned}
\mathbb{P} (\max_{h \in \mathcal{H}} \lvert R (h) - R_{n} (h) \rvert \leq \hat{\epsilon}) 
& \geq 1 - \delta
\\
\mathbb{P} (R (h) - R (h_{n}) \leq 2 \hat{\epsilon}) 
& \geq 1 - \delta.
\end{aligned}
$$

By setting $\epsilon = 2 \hat{\epsilon}$,
we have the conclusion that if $n \geq n_{\mathcal{H}}^{u} (\frac{ \epsilon }{ 2 }, \delta)$,
then

$$
\mathbb{P} (R (h) - R (h_{n}) \leq \epsilon) \geq 1 - \delta,
$$

which is the definition of agonistic PAC learning.

:::

By the lemma @lem-uc-pac-erm, 
we can easily derive the sample complexity results for agnostic PAC by plugging $ \epsilon = \frac{ \epsilon }{ 2 }$ to the sample complexity results of the uniform convergence.