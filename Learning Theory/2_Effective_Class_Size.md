# Effective Class Size

If there is an infinite number of possible hypotheses in a hypothesis class,
all the bounds that are positively related to the size of the hypothesis class will be infinite as well, 
which provides no information and therefore become useless. 

However, even if a hypothesis class $\mathcal{H}$ can contain an infinite number of hypotheses,
the number of unique ways that the hypotheses in $\mathcal{H}$ can label any finite set of instances is finite, 
which is at most $2^{n}$ if the set has $n$ instances.

## Growth function (shattering coefficient)

Given a set of instances $\mathcal{S} = \{ \mathbf{x}_{1}, \dots, \mathbf{x}_{n} \}$, 
the **projection** of a hypothesis class $\mathcal{H}$ onto $\mathcal{S}$ is the set of all distinct labels that $\mathcal{H}$ can produce onto $\mathcal{S}$

$$
\mathcal{H} (\mathcal{S}) = \{ \{ h (x_{1}), \dots, h (x_{n}) \}, \forall h \in \mathcal{H} \}.
$$


The concept of the growth function (shattering coefficient) is to measure the richness of the decisions that a hypothesis class can make with respect to a dataset of size $n$.

:::{prf:definition}

The **growth function** of a hypothesis class $\mathcal{H}$ is defined as the maximum number of unique ways that the hypotheses in $\mathcal{H}$ can label any set of $n$ instances

$$
\Pi_{\mathcal{H}} (n) = \sup_{\mathcal{S}: \lvert \mathcal{S} \rvert = n} \lvert \mathcal{H} (\mathcal{S}) \rvert.
$$

:::

Note that $\Pi_{\mathcal{H}} (n) \leq 2^{n}$ for any $\mathcal{H}$ with binary labels.

## Vapnik-Chervonenkis (VC) dimension

We say that $\mathcal{X}^{n}$ is **shattered** by $\mathcal{H}$ if a hypothesis class $\mathcal{H}$ can label a set of instances $\mathcal{X}^{n}$ in every possible way, that is, $\mathcal{X}^{n}$ is shattered by $\mathcal{H}$ if

$$
\mathcal{H} (\mathcal{X}^{n}) = 2^{n}.
$$

:::{prf:definition}

The **Vapnik-Chervonenkis (VC) dimension** of $\mathcal{H}$ is the size
of the largest set that is shattered by $\mathcal{H}$

$$
\mathrm{VC} (\mathcal{H}) = \max_{n: \mathcal{H} (\mathcal{X}^{n}) = 2^{n}} n.
$$

:::

## Sauer's lemma

Sauer's lemma shows that the growth function of any hypothesis class $\mathcal{H}$ is upper-bounded by a function of its VC dimension.

:::{prf:theorem} Sauer's lemma

For any hypothesis class $\mathcal{H}$ and any dataset size $n$,
we have

$$
\Pi_{\mathcal{H}} (n) \leq \sum_{i = 0}^{\mathrm{VC} (\mathcal{H})} {n \choose i}.
$$

:::{prf:proof} 
:class: dropdown

We will prove the lemma for any set of $n$ instances and any hypothesis class $\mathcal{H}$ with $\mathrm{VC} (\mathcal{H}) = d$ using induction on $n$ and $d$. 

That is, we will prove 

- the lemma is correct under the base cases where $(n, d) = (0, d)$ and $(n, d) = (n, 0)$,

- the lemma is correct under general case for $(n ,d)$ by assuming the lemma is true under the previous cases $(m, c)$ where $m < n$ and $c < d$.

First the base case $(n, d) = (0, d)$ implies that 

$$
\Pi_{\mathcal{H}} (0) = 1 = {0 \choose 0} = \sum_{i = 0}^{\mathrm{VC} (\mathcal{H})} {0 \choose i}
$$

because any hypothesis class can have at most 1 distinct label on an empty set ($n = 0$).

Then the base case $(n, d) = (n, 0)$ means that $\mathcal{H}$ can only shatter the empty set $\empty$ and therefore according to the definition of shattering

$$
\Pi_{\mathcal{H}} (n) = \mathcal{H} (\empty) = 2^{0} = 1 = {n \choose 0} = \sum_{i = 0}^{0} {n \choose i}.
$$

Therefore we have proven the lemma is true in the base case, that is,

$$
\Pi_{\mathcal{H}} (n) = \sum_{i = 0}^{\mathrm{VC} (\mathcal{H})} {n \choose i}
$$ 

is true when $(n, d) = (0, d)$ and $(n, d) = (n, 0)$.

To prove the general case of the lemma,
take any set $\mathcal{S} = \{\mathbf{x}_{1} \dots, \mathbf{x}_{n} \}$ with $n$ instances and any hypothesis class $\mathcal{H}$,
we can classify each unique way of the label assignment $\pi \in \mathcal{H} (\mathcal{S})$ into 2 groups $\mathcal{G}_{1}$ and $\mathcal{G}_{2}$ based on whether $\pi$ can form a pair in $\mathcal{H} (\mathcal{S})$.

- $(\pi, \pi')$ form a pair if  $\pi (x_{i}) = \pi' (x_{i}), \forall i \in [1, n - 1]$ and $\pi (x_{n}) = \pi' (x_{n})$ ($\pi$ agree with $\pi'$ for all $x_{1}, \dots, x_{n - 1}$ but not for $x_{n}$).
We add the both $\pi$ and $\pi'$ to $\mathcal{G}_{1}$.

- $\pi$ belongs to $\mathcal{G}_{2}$ if doesn't belong to $\mathcal{G}_{1}$. 

Since the pairs $(\pi, \pi') \in \mathcal{G}_{1}$ have the same labels for $\mathbf{x}_{1}, \dots, \mathbf{x}_{n - 1}$  if we create $\mathcal{G}'_{1}$ by removing the labels for $\mathbf{x}_{n}$ in each $\pi \in \mathcal{G}_{1}$

$$
\mathcal{G}'_{1} = \{ (\pi (\mathbf{x}_{1}), \dots, \pi (\mathbf{x}_{n - 1})), \forall \pi \in \mathcal{G}_{1} \} \\
$$

then all of the pairs in $\mathcal{G}_{1}$ become the same label assignment,
but if we create $\mathcal{G}_{2}'$ using the same procedure above, 
the resulting label assignments in $\mathcal{G}_{2}'$ are still unique.

Also, by the definition of $\mathcal{G}_{1}$, $\mathcal{G}_{2}$, $\mathcal{G}_{1}'$, and $\mathcal{G}_{2}'$, 
the label assignments in $\mathcal{G}_{1}'$ and $\mathcal{G}_{2}'$ do not overlap,
and therefore 

$$
\mathcal{H} (\mathcal{S}) = \lvert \mathcal{G}_{1} \rvert + \lvert \mathcal{G}_{2} \rvert = 2 \lvert \mathcal{G}_{1}' \rvert + \lvert \mathcal{G}_{2}' \rvert.
$$

Then we will define 2 new hypotheses classes $\mathcal{H}_{1}$, $\mathcal{H}_{2}$ whose domain is a set $\mathcal{S}'$ that is constructed by removing $x_{n}$ from $\mathcal{S}$ 

$$
\mathcal{S}' = \{\mathbf{x}_{1} \dots, \mathbf{x}_{n - 1} \}.
$$

and whose projections on $\mathcal{S}'$ are defined as 

$$
\mathcal{H}_{1} (\mathcal{S}') = \mathcal{G}_{1}' \cup \mathcal{G}_{2}' \\
\mathcal{H}_{2} (\mathcal{S}') = \mathcal{G}_{1}',
$$

and therefore, 

$$
\lvert \mathcal{H} (\mathcal{S}) \rvert = 2 \lvert \mathcal{G}_{1}' \rvert + \lvert \mathcal{G}_{2}' \rvert = (\lvert \mathcal{G}_{1}' \rvert + \lvert \mathcal{G}_{2}' \rvert) + \lvert \mathcal{G}_{1}' \rvert = \lvert \mathcal{H}_{1} (\mathcal{S}') \rvert + \lvert \mathcal{H}_{2} (\mathcal{S}') \rvert.
$$

Although we never exactly defined what $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$ are, 
we have completely specified their projections on the entire domain $\mathcal{S}'$,
using which we can derive

$$
\mathrm{VC} (\mathcal{H}_{1}) \leq \mathrm{VC} (\mathcal{H}),
$$

since the $\mathcal{H}$ has all the same label assignments for $\mathcal{S}' = \{ \mathbf{x}_{1}, \dots, \mathbf{x}_{n - 1} \}$ that $\mathcal{H}_{1}$ has and any subset of $\mathcal{S}'$ that is shattered by $\mathcal{H}_{1}$ is shattered by $\mathcal{H}$. 

Furthermore, since $\mathcal{H}_{2} (\mathcal{S}') = \mathcal{G}_{1}$, 
if a subset $\mathcal{T} \subseteq \mathcal{S}'$ is shattered by $\mathcal{H}_{2}$,
then the set $\mathcal{T} \cup \{ x_{n} \}$ must be shattered by $\mathcal{H}$,
which means

$$
\mathrm{VC} (\mathcal{H}_{2}) + 1 \leq \mathrm{VC} (\mathcal{H}).
$$

Now we are ready to prove the general case of the lemma using the all results we proved above with $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$. 

According to the definition of growth function, 
for any hypothesis class $\mathcal{H}$ and any set $\mathcal{S}$ of size $n$

$$
\lvert \mathcal{H} (\mathcal{S}) \rvert \leq \Pi_{\mathcal{H}} (n)
$$

and since we have assumed that the lemma is correct for the case $(m, c)$ where $m < n, c < d$, 

$$
\Pi_{\mathcal{H}} (m) \leq \sum_{i = 0}^{c} {m \choose i},
$$

we have 

$$
\begin{aligned}
\lvert \mathcal{H} (\mathcal{S}) \rvert 
& = \lvert \mathcal{H}_{1} (\mathcal{S}') \rvert + \lvert \mathcal{H}_{2} (\mathcal{S}') \rvert
\\
& \leq \Pi_{\mathcal{H}_{1}} (n - 1) + \Pi_{\mathcal{H}_{2}} (n - 1).
\\
& \leq \sum_{i = 0}^{\mathrm{VC} (\mathcal{H}_{1})} {n - 1 \choose i} + \sum_{i = 0}^{\mathrm{VC} (\mathcal{H}_{2})} {n - 1 \choose i} 
\\
\end{aligned}
$$

Since we have proved that the relations between $\mathrm{VC} (\mathcal{H}_{1})$, $\mathrm{VC} (\mathcal{H}_{2})$ and $\mathrm{VC} (\mathcal{H})$,

$$
\begin{aligned}
\lvert \mathcal{H} (\mathcal{S}) \rvert 
& \leq \sum_{i = 0}^{\mathrm{VC} (\mathcal{H}_{1})} {n - 1 \choose i} + \sum_{i = 0}^{\mathrm{VC} (\mathcal{H}_{2})} {n - 1 \choose i} 
\\
& \leq \sum_{i = 0}^{\mathrm{VC} (\mathcal{H})} {n - 1 \choose i} + \sum_{i = 0}^{\mathrm{VC} (\mathcal{H}) - 1} {n - 1 \choose i} 
\\
& = \sum_{i = 0}^{\mathrm{VC} (\mathcal{H})} {n - 1 \choose i} + \sum_{i = 1}^{\mathrm{VC} (\mathcal{H})} {n - 1 \choose i - 1} + {n - 1 \choose -1}
\\
& = \sum_{i = 0}^{\mathrm{VC} (\mathcal{H})} {n - 1 \choose i} + \sum_{i = 0}^{\mathrm{VC} (\mathcal{H})} {n - 1 \choose i - 1} 
& [{n - 1 \choose - 1} = 0]
\\
& = \sum_{i = 0}^{\mathrm{VC} (\mathcal{H})} \left[
    {n - 1 \choose i} + {n - 1 \choose i - 1} 
\right]
\\
& = \sum_{i = 0}^{\mathrm{VC} (\mathcal{H})} {n \choose i}.
\end{aligned}
$$

Since all of the above proof is for any $\mathcal{S}$,
it also works for the largest $\lvert \mathcal{H} (\mathcal{S}) \rvert$,

$$
\sup_{\mathcal{S}} \lvert \mathcal{H} (\mathcal{S}) \rvert = \Pi_{\mathcal{H}} (n) \leq \sum_{i = 0}^{\mathrm{VC} (\mathcal{H})} {n \choose i},
$$

which proves the lemma under the general case.

:::

The following theorem uses Sauer's lemma to provide a closed form upper-bound of the growth function of any hypothesis class with its VC dimension.

:::{prf:theorem}

For any $1 < d = \mathrm{VC} (\mathcal{H}) < n$,
we have

$$
\Pi_{\mathcal{H}} (n) \leq \sum_{i = 0}^{d} {n \choose i} \leq \left(
    \frac{ e }{ d } n
\right)^{d} = O (n^d).
$$

:::{prf:proof}
:class: dropdown

First note that $(\frac{ d }{ n })^{d} < (\frac{ d }{ n })^{i}, i < d$ since $d < n$, 
and therefore

$$
\begin{aligned}
\sum_{i = 0}^{d} {n \choose i} \left(
    \frac{ d }{ n }
\right)^{d} 
& \leq \sum_{i = 0}^{d} \left[
    {n \choose i} \left(
        \frac{ d }{ n }
    \right)^{i} 
\right] 
\\
& = \sum_{i = 0}^{d} \left[
    {n \choose i} \left(
        \frac{ d }{ n }
    \right)^{i} 1^{n - i}
\right]
\\
& \leq \sum_{i = 0}^{n} \left[
    {n \choose i} \left(
        \frac{ d }{ n }
    \right)^{i} 1^{n - i}
\right]
\end{aligned}
$$

By applying Binomial theorem $(x + y)^{n} = \sum_{i = 0}^{n} {n \choose i} x^{i} y^{n - i}$

$$
\begin{aligned}
\sum_{i = 0}^{d} {n \choose i} \left(
    \frac{ d }{ n }
\right)^{d} 
& \leq \sum_{i = 0}^{n} \left[
    {n \choose i} \left(
        \frac{ d }{ n }
    \right)^{i} 1^{n - i}
\right]
\\
& = \left(
    \frac{ d }{ n } + 1
\right)^{n}
\\
& \leq e^{d}.
\end{aligned}
$$

:::

The theorem above shows that the VC dimension marks the threshold between the exponential growth and polynomial growth of the growth function.

- When $n < d$, 
    by the definition of the VC dimension,
    we can always find a set of instances of size $n$ $\mathcal{H}$ can shatter,
    so the growth function $\Pi_{\mathcal{H}} (n) = 2^{n}$, 
    which means it grows exponentially with a factor of 2 as $n$ increases, 

- When $n > d$, 
    by the theorem above, 
    the growth function is upper bounded by $n^{d}$,
    so it only grows in polynomials as $n$ increases.
