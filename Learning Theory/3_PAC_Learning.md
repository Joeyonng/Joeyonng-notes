# PAC Learning

## Consistency model

Learning in the consistency model requires the algorithm to always predict correctly on the training set,
but doesn't care much about the generalization of the performance on the test set. 

We say that a concept $c$ is **consistent** with a set of labeled instances $\mathcal{S} = \{ (\mathbf{x}_{1}, y_{1}), \dots, (\mathbf{x}_{n}, y_{n}) \}$ if $c (\mathbf{x}_{i}) = y_{i}$ for all $i$.

:::{prf:definition}
:label: 

An algorithm $A$ learns the concept class $\mathcal{C}$ in the **consistency model** if

- given a set of labeled instances $\mathcal{S} = \{ \mathbf{x}_{1}, y_{1}), \dots, (\mathbf{x}_{n}, y_{n}) \}$, where instances are sampled from *any distribution* $\mathbb{P}_{\mathbf{X}}$ over the instance space, 

- $A$ can find a concept $c \in \mathcal{C}$ that is consistent with $\mathcal{S}$ if $c$ exists, or $A$ outputs False if no such concept exists.

:::

## Probably Approximately Correct (PAC) model

Learning in the PAC model is more applicable in real world,
as it emphasizes more on the generalization ability of the learned function from the algorithm. 

:::{prf:definition}
:label: 

An algorithm $A$ learns the concept class $\mathcal{C}$ in the **PAC model** by the hypothesis class $\mathcal{H} \supseteq \mathcal{C}$ if, 

- given a set of labeled instances $\mathcal{S}$, where instances are sampled from *any distribution* $\mathbb{P}_{\mathbf{X}}$ over the instance space and are labeled by *any concept* $c \in \mathcal{C}$, and there exists a function for some $\epsilon > 0 $ and $\delta > 0$ such that 

    $$
    n \geq n_{\mathcal{H}} (\epsilon, \delta),
    $$

- $A$ returns a hypothesis $h \in \mathcal{H}$, where **its true risk** is no greater than $\epsilon$ with probability at least $1 - \delta$

    $$
    \mathbb{P} (R (h) \leq \epsilon) \geq 1 - \delta.
    $$

:::

## Sample complexity results 

### PAC learnability for finite classes

If $\mathcal{C}$ is finite and learnable in the consistency model, 
then $\mathcal{C}$ is PAC learnable. 

:::{prf:theorem}
:label: 

If an algorithm $A$ learns a finite concept class $\mathcal{C}$ in the consistency model, 
then $A$ learns the concept class $\mathcal{C}$ by the hypothesis class $\mathcal{H} = \mathcal{C}$ in the PAC model with

$$
n_{\mathcal{H}} (\epsilon, \delta) = \frac{
    \log \lvert \mathcal{H} \rvert + \log \frac{ 1 }{ \delta } 
}{
    \epsilon
}.
$$

:::{prf:proof}
:label: 
:class:dropdown

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

### PAC learnability for infinite classes

:::{prf:theorem}
:label: 

If an algorithm $A$ learns an infinite concept class $\mathcal{C}$ in the consistency model, 
then $A$ learns the concept class $\mathcal{C}$ by the hypothesis class $\mathcal{H} = \mathcal{C}$ in the PAC model with

$$
n_{\mathcal{H}} (\epsilon, \delta) = \frac{
    4 \log \Pi_{\mathcal{H}} (2 n) + 2 \log \frac{ 2 }{ \delta } 
}{
    \epsilon
}.
$$

:::{prf:proof}
:label: 
:class:dropdown

Let's first define 3 "bad" events that are useful in the following proof.

Given any set of instances $\mathcal{S} = \{ \mathbf{x}_{1}, \dots, \mathbf{x}_{n} \}$,
let $B (\mathcal{S})$ denote the event that there exists a hypothesis $h \in \mathcal{H}$ that is consistent with $\mathcal{S}$ but has the true risk larger than $\epsilon$

$$
B (\mathcal{S}) \coloneqq \exist h \in \mathcal{H}: R_{\mathcal{S}} (h) = 0,  R (h) \geq \epsilon.
$$

and therefore we want to prove

$$
\mathbb{P}_{\mathcal{S}} (B (\mathcal{S})) \leq \delta.
$$

Now let's draw another set of i.i.d instances $\mathcal{S}' = \{ \mathbf{x}_{1}', \dots, \mathbf{x}_{n} \}$ from the distribution $\mathbb{P}_{\mathbf{X}}$,
and define another event $B'$ as a function of $\mathcal{S}$ and $\mathcal{S}'$ that there exists a hypothesis $h \in \mathcal{H}$ that is consistent with $\mathcal{S}$, but has empirical risk on $\mathcal{S}'$ larger than $\frac{ \epsilon }{ 2 }$

$$
B (\mathcal{S}, \mathcal{S}') \coloneqq \exist h \in \mathcal{H}: R_{\mathcal{S}} (h) = 0,  R_{S'} (h) \geq \frac{ \epsilon }{ 2 }.
$$

Finally, consider a binary vector $\mathbf{b}$ of $n$ independent Bernoulli random variables $\mathrm{Ber} (0.5)$ that indicates whether the instances in $\mathcal{S}$ and $\mathcal{S}'$ are swapped.
That is, we use $\mathbf{b}$ to create two more sets $\mathcal{T} = \{ \mathbf{t}_{1}, \dots, \mathbf{t}_{n} \}$ and $\mathcal{T}' = \{ t_{1}', \dots, t_{n}' \}$,
where $t_{i}' = x_{i}, t_{i} = x_{i}'$ if $b_{i} = 1$ and $t_{i} = x_{i}, t_{i}' = x_{i}'$ if $b_{i} = 0$. 
Then we define another event $B'' (\mathcal{S}, \mathcal{S}', \mathbf{b})$ as

$$
B'' (\mathcal{S}, \mathcal{S}', \mathbf{b}) \coloneqq \exist h \in \mathcal{H}: R_{\mathcal{T}} (h) = 0, R_{\mathcal{T}'} (h) \geq \frac{ \epsilon }{ 2 }.
$$

Then we will prove the theorem with following 5 steps. 

**Claim 1**: if $n > \frac{ 8 }{ \epsilon }$,

$$
\mathbb{P}_{\mathbf{X}} (B' (S, S') \mid B (S)) \geq \frac{ 1 }{ 2 }.
$$

Suppose $B (S)$ holds, and therefore we have a hypothesis $h \in \mathcal{H}$ such that $R (h) \geq \epsilon$.

Since the instances in $\mathcal{S}'$ are i.i.d sampled,
each 0-1 loss in the empirical risk on $\mathcal{S}'$ is an i.i.d Bernoulli random variable 

$$
R_{\mathcal{S}'} (h) = \frac{ 1 }{ n } \sum_{i = 1}^{n} \left[
    h (\mathbf{x}_{i}') \neq y_{i}'
\right]
$$

and therefore the empirical risk $R_{\mathcal{S}'} (h)$ is an estimated average of these random variables. 

Also note that the true average of $R_{\mathcal{S}'} (h)$ with respect to the all instances is the true risk $R (h)$

$$
\mathbb{E}_{\mathcal{S}'} \left[
    R_{\mathcal{S}'} (h)
\right] = R (h).
$$

Therefore, we can apply the lower tail case of the Chernoff bound for the average of Bernoulli variables and set $X = R_{\mathcal{S}'} (h), \mu = R (h), \delta = \frac{ 1 }{ 2 }$

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
\right]
\end{aligned}
$$

Since $R (h) \geq \epsilon$ and the assumption states that $n > \frac{ 8 }{ \epsilon }$

$$
\begin{aligned}
\mathbb{P} \left(
    R_{\mathcal{S}'} (h) \leq \frac{ \epsilon }{ 2 }
\right) \leq \mathbb{P} \left(
    R_{\mathcal{S}'} (h) \leq \frac{ R (h) }{ 2 }
\right) \leq \exp \left[
    \frac{ - n R(h) }{ 8 }
\right] \leq \exp \left[
    \frac{ - R(h) }{ \epsilon } 
\right] \leq \frac{ 1 }{ e } \leq \frac{ 1 }{ 2 },
\end{aligned}
$$

and therefore given that $B (\mathcal{S})$ holds we have

$$
\mathbb{P} \left(
    R_{\mathcal{S}'} (h) \geq \frac{ \epsilon }{ 2 }
\right) \geq \frac{ 1 }{ 2 }.
$$

Therefore, when $n > \frac{ 8 }{ \epsilon }$

$$
\mathbb{P} (B' (\mathcal{S}, \mathcal{S}') \mid B (\mathcal{S})) \geq \frac{ 1 }{ 2 }.
$$

**Claim 2**: we have

$$
\mathbb{P}_{\mathcal{S}} (B (\mathcal{S})) \leq 2 \mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B (\mathcal{S}, \mathcal{S}'))
$$ 

because

$$
\begin{aligned}
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}')) 
& \geq \mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}') \cap B (\mathcal{S}))
\\
& = \mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}') \mid B (\mathcal{S})) \mathbb{P}_{\mathcal{S}} (B (\mathcal{S}))
\\
& \geq \frac{ 1 }{ 2 } \mathbb{P}_{\mathcal{S}} (B (\mathcal{S})).
\end{aligned}
$$

**Claim 3**: we have

$$
\mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}')) = \mathbb{P}_{\mathcal{S}, \mathcal{S}', \mathbf{b}} (B'' (\mathcal{S}, \mathcal{S}', \mathbf{b}))
$$

because the event $B' (\mathcal{S}, \mathcal{S}')$ and $B'' (\mathcal{S}, \mathcal{S}', \mathbf{b}) = B'' (\mathcal{T}, \mathcal{T}')$ only differ on the set of instances $\mathcal{S}, \mathcal{S}'$ and $\mathcal{T}, \mathcal{T}'$ and they can be seen as the set of instances i.i.d sampled from the $\mathcal{X}^{d}$. 

**Claim 4**: given any $\mathcal{S}, \mathcal{S}'$, we have the following for any fixed $h \in \mathcal{H}$

$$
\mathbb{P}_{\mathbf{b}} \left(
    R_{\mathcal{T}} (h) = 0, R_{\mathcal{T}'} (h) \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) \leq 2^{- \frac{ n \epsilon }{ 2 }}.
$$

Remember that $\mathcal{S}, \mathcal{S}'$ all have $n$ instances and therefore there are $n$ pairs of instances $(\mathbf{x}_{1}, \mathbf{x}_{1}'), \dots, (\mathbf{x}_{n}, \mathbf{x}_{n}')$.
There are 3 cases for the corrections of the predictions made by $h$ for each pair $(h (\mathbf{x}_{i}), h (\mathbf{x}_{i}'))$. 

1. Both $h (\mathbf{x}_{i}), h (\mathbf{x}_{i}')$ are incorrect.

1. Either $h (\mathbf{x}_{i})$ or $h (\mathbf{x}_{i}')$ is incorrect (correct).

1. Both $h (\mathbf{x}_{i}), h (\mathbf{x}_{i}')$ are correct.

First if there is a pair in $\mathcal{S}, \mathcal{S}'$ with case 1, then

$$
\mathbb{P}_{\mathbf{b}} \left(
    R_{\mathcal{T}} (h) = 0, R_{\mathcal{T}'} (h) \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) = 0
$$

because $R_{\mathcal{T}} (h) > 0$ no matter how to generate $\mathcal{T}$ by swapping instances in $\mathcal{S}, \mathcal{S}'$. 

Then denoted by $r$ the number of pairs in $\mathcal{S}, \mathcal{S}'$ that case 2 is true, 
if $r < \frac{ \epsilon n }{ 2 }$, 

$$
\mathbb{P}_{\mathbf{b}} \left(
    R_{\mathcal{T}} (h) = 0, R_{\mathcal{T}'} (h) \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) = 0
$$

because $R_{\mathcal{T}'} (h) < \frac{ \epsilon }{2}$ no matter how to generate $\mathcal{T}'$ by swapping instances in $\mathcal{S}, \mathcal{S}'$.

When $r \geq \frac{ \epsilon n }{ 2 }$, 
the event $R_{\mathcal{T}} (h) = 0, R_{\mathcal{T}'} (h) \geq \frac{ \epsilon }{ 2 }$ is possible and its possibility is 

$$
\mathbb{P}_{\mathbf{b}} \left(
    R_{\mathcal{T}} (h) = 0, R_{\mathcal{T}'} (h) \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) = \left(
    \frac{ 1 }{ 2 }
\right)^{r} \leq 2^{- \frac{ \epsilon n }{ 2 }}
$$

because the independent binary values in $\mathbf{b}$ must take $1$ with probability 0.5 for all $r'$ mistakes that were in $\mathcal{S}$ and swapped to be in $\mathcal{T}'$,
and take $0$ with probability 0.5 for the $r - r'$ mistakes that were in $\mathcal{S}'$ and are stayed in $\mathcal{T}'$.

Since the probability of the case 3 is already included in the calculation of the above probabilities,
we can prove the claim 4 by adding probabilities for all cases

$$
\mathbb{P}_{\mathbf{b}} \left(
    R_{\mathcal{T}} (h) = 0, R_{\mathcal{T}'} (h) \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) \leq 2^{- \frac{ \epsilon n }{ 2 }}.
$$

**Claim 5**: given any $\mathcal{S}, \mathcal{S}'$, 

$$
\mathbb{P}_{\mathbf{b}} \left(
    B (\mathcal{S}, \mathcal{S}', \mathbf{b}) \mid \mathcal{S}, \mathcal{S}'
\right) = \mathbb{P}_{\mathbf{b}} \left(
    \exist h \in \mathcal{H}: R_{\mathcal{T}} (h) = 0, R_{\mathcal{T}'} (h) \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) \leq \Pi_{\mathcal{H}} (2 n) 2^{- \frac{ \epsilon n }{ 2 }}.
$$

Since $\mathcal{H} (\mathcal{S} \cup \mathcal{S}')$ contains all the label assignments for the event $\exist h \in \mathcal{H}: R_{\mathcal{T}} (h) = 0, R_{\mathcal{T}'} (h) \geq \frac{ \epsilon }{ 2 }$,
$\mathcal{H}$ can be replaced with $\mathcal{H} (\mathcal{S} \cup \mathcal{S}')$ 

$$
\begin{aligned}
& \mathbb{P}_{\mathbf{b}} \left(
    \exist h \in \mathcal{H}: R_{\mathcal{T}} (h) = 0, R_{\mathcal{T}'} (h) \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) 
\\
& = \mathbb{P}_{\mathbf{b}} \left(
    \exist h \in \mathcal{H} (\mathcal{S} \cup \mathcal{S}'): R_{\mathcal{T}} (h) = 0, R_{\mathcal{T}'} (h) \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) 
\\
& \leq \sum_{h \in \mathcal{H} (\mathcal{S} \cup \mathcal{S}')} \mathbb{P}_{\mathbf{b}} \left(
    R_{\mathcal{T}} (h) = 0, R_{\mathcal{T}'} (h) \geq \frac{ \epsilon }{ 2 } \mid \mathcal{S}, \mathcal{S}'
\right) 
\\
& \leq \sum_{h \in \mathcal{H} (\mathcal{S} \cup \mathcal{S}')} (2 n) 2^{- \frac{ \epsilon n }{ 2 }}.
\\
& \leq \Pi_{\mathcal{H}} (2 n) 2^{- \frac{ \epsilon n }{ 2 }}.
\\
\end{aligned}
$$

where the first inequality is because of union bound, 
the second inequality is because the claim 4, 
and the last inequality is because the definition of the growth function states that 

$$
\lvert \mathcal{H} (\mathcal{S} \cup \mathcal{S}') \rvert \leq \Pi_{H} (\lvert \mathcal{S} \rvert + \lvert \mathcal{S}' \rvert) = \Pi_{\mathcal{H}} (2 n).
$$

**Claim 6**: $\mathbb{P}_{\mathcal{S}, \mathcal{S}', \mathbf{b}} (B'' (\mathcal{S}, \mathcal{S}', \mathbf{b}))$ has the same upper bound as $\mathbb{P}_{\mathbf{b}} (B'' (\mathcal{S}, \mathcal{S}', \mathbf{b}) \mid \mathcal{S}, \mathcal{S}')$

$$
\mathbb{P}_{\mathcal{S}, \mathcal{S}', \mathbf{b}} (B'' (\mathcal{S}, \mathcal{S}', \mathbf{b})) \leq \Pi_{\mathcal{H}} (2 n) 2^{- \frac{ \epsilon n }{ 2 }}.
$$

Since $\Pi_{\mathcal{H}} (2 n) 2^{- \frac{ \epsilon n }{ 2 }}$ is a function that only depends on $n, \epsilon, \mathcal{H}$ and doesn't depend on the choice of $\mathcal{S}, \mathcal{S}'$

$$
\mathbb{E}_{\mathcal{S}, \mathcal{S}'} \left[
    \mathbb{P}_{\mathbf{b}} (B'' (\mathcal{S}, \mathcal{S}', \mathbf{b}) \mid \mathcal{S}, \mathcal{S}') 
\right] = \mathbb{P}_{\mathbf{b}} (B'' (\mathcal{S}, \mathcal{S}', \mathbf{b}) \mid \mathcal{S}, \mathcal{S}') \leq \Pi_{\mathcal{H}} (2 n) 2^{- \frac{ \epsilon n }{ 2 }},
$$

and by marginalization, 

$$
\mathbb{P}_{\mathcal{S}, \mathcal{S}', \mathbf{b}} (B'' (\mathcal{S}, \mathcal{S}', \mathbf{b})) = \mathbb{E}_{\mathcal{S}, \mathcal{S}'} \left[
    \mathbb{P}_{\mathbf{b}} (B'' (\mathcal{S}, \mathcal{S}', \mathbf{b}) \mid \mathcal{S}, \mathcal{S}') 
\right] \leq \Pi_{\mathcal{H}} (2 n) 2^{- \frac{ \epsilon n }{ 2 }}.
$$

Finally, by combining some of the claims above,

$$
\begin{aligned}
\mathbb{P}_{\mathcal{S}} (B (\mathcal{S})) 
& \leq 2 \mathbb{P}_{\mathcal{S}, \mathcal{S}'} (B' (\mathcal{S}, \mathcal{S}'))
& [\text{claim 2}]
\\
& = 2 \mathbb{P}_{\mathcal{S}, \mathcal{S}', \mathbf{b}} (B'' (\mathcal{S}, \mathcal{S}', \mathbf{b}))
& [\text{claim 3}]
\\
& \leq 2 \Pi_{\mathcal{H}} (2 n) 2^{- \frac{ \epsilon n }{ 2 }}
& [\text{claim 6}]
\end{aligned}
$$

and setting $\delta$, we can get the threshold for $n$

$$
\begin{aligned}
\delta 
& = 2 \Pi_{\mathcal{H}} (2 n) 2^{- \frac{ \epsilon n }{ 2 }}
\\
n
&  = \frac{
    4 \log \Pi_{\mathcal{H}} (2 n) + 2 \log \frac{ 2 }{ \delta } 
}{
    \epsilon
}.
\end{aligned}
$$

:::

### More general results using Sauer’s lemma

Now we can use the Sauer’s lemma to get a nice closed form expression on sample complexity result for the infinite class. 

:::{prf:theorem}
:label: 

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

:::{prf:proof}
:label: 
:class:dropdown

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