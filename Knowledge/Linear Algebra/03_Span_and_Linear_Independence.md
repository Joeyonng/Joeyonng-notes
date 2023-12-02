---
title: Span and Linear Independence
---

# Span
Given a vector space $\mathcal{V}$ over a field $\mathbb{F}$, 
the span of a set of vectors $v_{1}, \dots, v_{n} \in \mathcal{V}$ is the set of all possible linear combinations of $v_{1}, \dots, v_{m}$

$$
\text{span} (v_{1}, \dots, v_{n}) = \left\{
    \sum_{i=1}^{n} \alpha_{i} \cdot v_{i}, \forall \alpha_{i} \in \mathbb{F}
\right\}.
$$

If $\mathcal{V}$ is $\mathbb{F}^{m}$,  the set vectors $v_{1}, 
\dots, v_{n}$ can be viewed as the columns of the matrix $\mathbf{A} \in \mathbb{F}^{m \times n}$. 
Then

$$
\text{span} (v_{1}, \dots, v_{n}) = R (\mathbf{A}).
$$

Since we have proved $R (\mathbf{A})$ is a subspace of $\mathcal{V}$, the span of a set of vectors is a subspace of $\mathcal{V}$.

## Spanning set

For a set of vectors $\mathcal{S} = v_{1}, \dots, v_{n}$, 
if the subspace $\mathcal{W}$ is the span of $\mathcal{S}$

$$
\mathcal{W} = \text{span} (\mathcal{S}),
$$

then the set of vectors $\mathcal{S}$ is the spanning set of the subspace $\mathcal{W}$.S.

## Properties of the spanning set

Consider a set of vectors $ \mathcal{A} = \left\{ v_{1}, \dots, v_{n} \right\}$ and a subspace $\mathcal{W}$.

(spanning-set-property-1)=

- If $\mathcal{A}$ is a spanning set of $\mathcal{W}$, 
    the new set

    $$
    \mathcal{A} \cup \left\{ 
        u_{1}, \dots, u_{n}
    \right\}
    $$
    
    is still a spanning set of $\mathcal{W}$ for arbitrary vectors $u_{1}, \dots, u_{n} \in \mathcal{W}$.

(spanning-set-property-2)=

- $\mathcal{A}$ is a spanning set of $\mathcal{W}$ if and only if 

    - all vectors in $\mathcal{W}$ are linear combinations of $v_{1}, \dots, v_{n}$ and
    
    - $v_{1}, \dots, v_{n} \in \mathcal{W}$.

  ::: {.callout-note collapse="true" title="Proof"}
    
    Since this statement has "if and only if", we first prove in the forward direction.
    
    If $v_{1}, \dots, v_{n}$ is a spanning set of $\mathcal{W}$, 
    then by the definition of spanning set, 
    the set of all linear combinations of $v_{1}, \dots, v_{n}$ is the subspace $\mathcal{W}$.
    
    Thus, all vectors in the subspace $\mathcal{W}$ are the linear combinations of $v_{1}, \dots, v_{n}$.
    
    Since every $v_{i}, i = 1, \dots, n$ is a linear combination of itself, 
    then $v_{1}, \dots, v_{n}$ are also in $\mathcal{W}$.
    
    Then we prove in the backward direction.
    
    Since all vectors in $\mathcal{W}$ are linear combinations of $v_{1}, \dots, v_{n}$, 
    by the definition of span,
    
    $$
    \mathcal{W} \subseteq \text{span} (v_{1}, \dots, v_{n}).
    $$
    
    Since $v_{1}, \dots, v_{n} \in \mathcal{W}$ and the closure property of the subspace, 
    all linear combinations of $v_{1}, \dots, v_{n}$ are also in $\mathcal{W}$, 
    which means that
    
    $$
    \text{span} (v_{1}, \dots, v_{n}) \subseteq \mathcal{W}.
    $$
    
    Thus, 
    
    $$
    \mathcal{W} = \text{span} (v_{1}, \dots, v_{n}).
    $$
    
  :::

(spanning-set-property-3)=

- If vectors in set $\mathcal{B}$ are linear combinations of the vectors in $\mathcal{A}$, 
    then 

    $$
    \text{span} (\mathcal{B}) \subseteq \text{span} (\mathcal{A}).
    $$
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    We prove by contradiction. 
    Suppose that the vectors in set $\mathcal{B}$ are linear combinations of the vectors in $\mathcal{A}$, 
    but there exists an vector $v \in \text{span} (\mathcal{B})$ but $v \notin \text{span} (\mathcal{A})$.

    Suppose $\mathcal{A} = \{ a_{1}, \dots, a_{n} \}$.
    Since $v \in \mathcal{B}$ is a linear combinations of vectors in $\mathcal{A}$,
    there exists a set of coefficients $\alpha_{1}, \dots, \alpha_{n}$ such that 
    
    $$
    v = \sum_{i = 1}^{n} \alpha_{i} a_{i}.
    $$
    
    which by definition of span means $v \in \text{span} (\mathbf{A})$.
    
    However, 
    we assume that $v \notin \text{span} (\mathbf{A})$, 
    which raises a contradiction.

  :::

(spanning-set-property-4)=

- If $\text{span} (\mathcal{A}) = \mathcal{W}$ and $\text{span} (\mathcal{B}) = \mathcal{U}$, 
    then 

    $$
    \text{span} (\mathcal{A} \cup \mathcal{B}) = \mathcal{W} + \mathcal{U},
    $$
    
    where 
    
    $$
    \mathcal{W} + \mathcal{U} = \left\{
        w + u \mid w \in \mathcal{W}, u \in \mathcal{U}
    \right\}.
    $$
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    Consider $\mathcal{A} = \{ a_{1}, \dots, a_{n} \}, \mathcal{B} = \{ b_{1}, \dots, b_{m} \}$,
    then 
    
    $$
    \text{span} (\mathcal{A} \cup \mathcal{B}) = \left\{ 
        \sum_{i=1}^{n} \alpha_{i} a_{i} + \sum_{i=1}^{n} \beta_{i} b_{i}, \forall \alpha_{i}, \beta_{i} \in \mathbb{F}
    \right\}.
    $$
    
    Note that 
    
    $$
    w \in \mathcal{W} = \sum_{i=1}^{n} \alpha_{i} a_{i}, \forall \alpha_{i} \in \mathbb{F},
    $$
    
    $$
    u \in \mathcal{U} = \sum_{i=1}^{n} \beta_{i} b_{i}, \forall \beta_{i} \in \mathbb{F}.
    $$
    
    Thus,
    
    $$
    \text{span} (\mathcal{A} \cup \mathcal{B}) = \left\{
        w + u \mid w \in \mathcal{W}, u \in \mathcal{U}
    \right\} = \mathcal{W} + \mathcal{U}.
    $$
    
  :::

# Linear independence

Given a vector space $\mathcal{V}$ over a field $\mathbb{F}$, 
a set of non-zero vectors $v_{1}, \dots, v_{n} \in \mathcal{V}$ is linearly independent when

$$
\sum_{i=1}^{n} \alpha_{i} \cdot v_{i} = 0 \iff \alpha_{i} = 0, i = 1, \dots, n.
$$

## Properties of linear independence 

- Given a matrix $\mathbf{A}$ whose columns are vectors $\mathbf{v}_{1}, \dots, \mathbf{v}_{n} \in \mathbb{F}^{m}$
    the set of vectors $\mathcal{S} = \{ \mathbf{v}_{1}, \dots, \mathbf{v}_{n} \}$  is linearly independent when the null space of $\mathbf{A}$ only contains $\mathbf{0} \in \mathbb{F}^{n}$.

    $$ 
    N (\mathbf{A}) = \left\{
        \mathbf{0}
    \right\}
    $$

  ::: {.callout-note collapse="true" title="Proof"}

    By definition, $N (\mathbf{A}) = \{ \mathbf{0} \}$ says that the only set of $\alpha_{1}, \dots, \alpha_{n}$ satisfying 

    $$
    \sum_{i = 1}^{n} \alpha_{i} \mathbf{A}_{*, i} = 0
    $$

    is $\alpha_{1}, \dots, \alpha_{n} = 0$, which is equivalent to saying the columns of $\mathbf{A}$ are a linearly independent set.

  :::

- If vectors $v_{1}, \dots, v_{n} \in \mathcal{V}$ are linearly independent and the subspace $\mathcal{W} = \text{span} (v_{1}, \dots, v_{n})$, 
    the set of field elements $\{ \alpha_{1}, \dots, \alpha_{n} \}$ that is paired with the set of vectors $\{ v_{1}, \dots, v_{n} \}$ to represent any vector $u \in \mathcal{W}: u = \sum_{i=1}^{n} \alpha_{i} v_{i}$ is unique.

  ::: {.callout-note collapse="true" title="Proof"}
    
    Proof by contradiction. 
    Suppose there is another set of field elements that can be paired with $v_{1}, \dots, v_{n}$ to represent $u$
    
    $$
    \left\{
        \beta_{1}, \dots, \beta_{n} \mid u = \sum_{i=1}^{n} \beta_{i} \cdot v_{i}
    \right\}.
    $$
    
    Then,
    
    $$
    \begin{aligned}
    \sum_{i=1}^{n} \alpha_{i} \cdot v_{i}
    & = \sum_{i=1}^{n} \beta_{i} \cdot v_{i}
    \\
    \sum_{i=1}^{n} \alpha_{i} \cdot v_{i} - \sum_{i=1}^{n} \beta_{i} \cdot v_{i}
    & = 0
    \\
    \sum_{i=1}^{n} (\alpha_{i} - \beta_{i}) \cdot v_{i}
    & = 0
    \\
    \alpha_{i} - \beta_{i}
    & = 0
    \\
    \alpha_{i} 
    & = \beta_{i},
    \end{aligned}
    $$
    
    which contradicts to the fact $\alpha_{i}$ and  $\beta_{i}$ should be different.

  :::

## Linear dependence 

Given a vector space $\mathcal{V}$ over a field $\mathbb{F}$, 
a set of non-zero vectors $v_{1}, \dots, v_{n} \in \mathcal{V}$ is linear dependent when there exists an $\alpha_{i} \neq 0$ such that 

$$
\sum_{i=1}^{n} \alpha_{i} \cdot v_{i} = 0.
$$

(existence-of-linear-combination)=

If a set of vectors $\{ v_{1}, \dots, v_{n} \}$ is linearly dependent, there exists an index $j$ $(1 \leq j \leq n)$ such that $v_{j}$ is a linear combination of the rest of the vectors:

$$
v_{j} = \sum_{i=1, i \neq j}^{n} \alpha_{i} \cdot v_{i}.
$$

::: {.callout-note collapse="true" title="Proof"}

Since the set $\{ v_{1}, \dots, v_{n} \}$ is linearly dependent, there exists an $\beta_{j} \neq 0$ $(1 \leq j \leq n)$ such that 

$$
\beta_{1} \cdot v_{1} + \dots \beta_{j} \cdot v_{j} + \dots \beta_{n} \cdot v_{n} = 0.
$$

Thus, 

$$
\begin{aligned}
\beta_{j} \cdot v_{j} 
& = - \sum_{i=1, i \neq j} \beta_{i} \cdot v_{i} 
\\
v_{j} 
& = - \beta_{j}^{-1} \cdot \sum_{i=1, i \neq j} \beta_{i} \cdot v_{i} 
\\
v_{j} 
& = \sum_{i=1, i \neq j} - \beta_{j}^{-1} \beta_{i} \cdot v_{i} 
\\
v_{j} 
& = \sum_{i=1, i \neq j} \alpha_{i} \cdot v_{i} 
& [\text{rewrite } - \beta_{j}^{-1} \beta_{i} = \alpha_{i}]
\\
\end{aligned}
$$

:::
