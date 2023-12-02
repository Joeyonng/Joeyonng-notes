---
title: Basis and Dimension
---

# Basis

A set of vectors $v_{1}, \dots, v_{k}$ is a basis of a subspace $\mathcal{W}$ of a vector space $\mathcal{V}$ over a field $\mathbb{F}$, if 

- $\mathcal{W} = \text{span} (v_{1}, \dots, v_{k})$, and

- $v_{1}, \dots, v_{k}$ are linearly independent.

## Properties of basis

- If $\mathcal{B} = \{ b_{1}, \dots, b_{n} \}$ is a basis of the subspace $\mathcal{W}$,
    $\mathcal{B}$ is a minimal spanning set for $\mathcal{W}$.
    That is, there is no vector in $\mathcal{B}$ that can be removed such that $\mathcal{B}$ is still a spanning set.
    
  ::: {.callout-note collapse="true" title="Proof"}

    We will prove by contradiction. 
    Assume $\mathcal{B}$ is a basis of the subspace $\mathcal{W}$ but is not a minimal spanning set,
    which means that the vectors in $\mathcal{B}$ are linear independent and
    $\mathcal{B}$ contains at least one vector $b$ such that $\hat{\mathcal{B}} = \mathcal{B} \setminus \{ b \}$ is still a spanning set. 

    Therefore, there exists a set of coefficients $\alpha_{1}, \dots, \alpha_{n - 1}$ such that $b$ is a linear combination of the vectors in $\hat{\mathcal{B}}$

    $$
    b = \sum_{b_{i} \in \hat{\mathcal{B}}} \alpha_{i} b_{i}.
    $$

    However, this means that the vectors in $\mathcal{B}$ are linear dependent, 
    which violates our assumption. 

  :::

- If $\mathcal{B} = \{ b_{1}, \dots, b_{n} \}$ is a basis of the subspace $\mathcal{W}$,
    $\mathcal{B}$ is a maximal linearly independent subset of $\mathcal{W}$.
    That is, there is no vector in $\mathcal{W}$ that can be added to $\mathcal{B}$ such that $\mathcal{B}$ is still a linearly independent set.
    
  ::: {.callout-note collapse="true" title="Proof"}

    We will prove by contradiction. 
    Assume $\mathcal{B}$ is a basis of the subspace $\mathcal{W}$ but is not a maximal linearly independent set,
    which means that $\mathcal{B}$ is a spanning set of $\mathcal{W}$ and
    there exists a vector $b \in \mathcal{W}$ that can be added to $\mathcal{B}$ such that $\hat{\mathcal{B}} = \mathcal{B} \cup \{ b \}$ is still a linearly independent set. 

    However, since $\mathcal{B}$ is a spanning set of $\mathcal{W}$,
    there exists a set of coefficients $\alpha_{1}, \dots, \alpha_{n}$ such that $b$ is a linear combination of the vectors in $\mathcal{B}$

    $$
    b = \sum_{b_{i} \in \mathcal{B}} \alpha_{i} b_{i}.
    $$

    which means that the vectors in $\hat{\mathcal{B}}$ are linear dependent, 
    which violates our assumption. 

  :::

(existence-of-basis)=

- Existence of basis

    A subspace may NOT have a basis e.g. $\mathcal{W} = \{ 0 \}$ has no linearly independent vector, but a subspace must have a basis if it has a finite spanning set. 
    
    That is, every finite spanning set of a subspace contains a basis.
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    Suppose the subspace $\mathcal{W}$ has a finite spanning set of 
    
    $$
    \mathcal{A}_{0} = \{ v_{i}, \dots, v_{n} \}.
    $$
    
    If the spanning set is linearly independent, 
    the set $\{ v_{i}, \dots, v_{n} \}$ is a basis of $\mathcal{W}$.
    
    If the spanning set is not linearly independent, then there exists $j$ $(1 \leq j \leq n)$ such that 
    
    $$
    v_{j} = \sum_{i=1, i \neq j}^{n} \alpha_{i} v_{i},
    $$
    
    and the set 
    
    $$
    \mathcal{A}_{1} = \{ v_{1}, \dots, v_{n} \} \setminus \{ v_{j} \}
    $$ 
    
    is still a spanning set.
    
    We can continue removing such $v_{j}$ if the resulting set $\mathcal{A}_{i}$ is not linearly independent. 
    
    Since the resulting set $\mathcal{A}_{i}$ is always a spanning set of $\mathcal{W}$, we will eventually get to the step $i$ where the $\mathcal{A}_{i}$ is linearly dependent and $\mathcal{A}_{i}$ will be the basis for the subspace $\mathcal{W}$.

  :::

(cardinality-of-basis)=

- Cardinality of basis

    The numbers of elements of all bases of a given subspace are the same. 
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    Suppose $\mathcal{A}$ is a basis of a subspace $\mathcal{S}$ and $\mathcal{B}$ is another basis of $\mathcal{S}$. 
    Thus, $\mathcal{A}$ and $\mathcal{B}$ are both linearly independent and spanning sets.
    
    Since $\mathcal{A}$ is a spanning set and $\mathcal{B}$ is linearly independent, 
    
    $$
    \lvert \mathcal{A} \rvert \geq \lvert \mathcal{B} \rvert.
    $$ 
    
    Since $\mathcal{B}$ is a spanning set and $\mathcal{A}$ is linearly independent, 
    
    $$
    \lvert \mathcal{A} \rvert \leq \lvert \mathcal{B} \rvert.
    $$ 
    
    Thus, 
    
    $$
    \lvert \mathcal{A} \rvert = \lvert \mathcal{B} \rvert.
    $$ 
    
  :::

(extension-of-a-basis)=

- Extension of a basis

    If the subspace $\mathcal{U}$ is a subset of a finite dimensional subspace $\mathcal{V}$
    and $\{ b_{1}, \dots, b_{k} \}$ is a basis of $\mathcal{U}$, 
    then there exists an extension of $\{ b_{1}, \dots, b_{k} \}$
    
    $$
    \{ b_{1}, \dots, b_{k}, b_{k + 1}, \dots, b_{n} \}
    $$
    
    that is a basis for $\mathcal{V}$ 
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    $\{ b_{1}, \dots, b_{k}, b_{k + 1}, \dots, b_{n} \}$ is a basis for $\mathcal{V}$ if $\mathcal{U} \subseteq \mathcal{V}$ and $\{ b_{1}, \dots, b_{k} \}$ is a basis of $\mathcal{U}$.

  :::

# Dimension

The dimension of a subspace is the common cardinality of its all bases.

## Properties of dimension

(dimension-property-1)=

- If a subspace $\mathcal{U}$ is a subset of a finite dimensional subspace $\mathcal{V}$,
    then
    
    $$
    \text{dim} (\mathcal{U}) \leq \text{dim} (\mathcal{V}).
    $$
    
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    Suppose there is a basis 
    
    $$
    \mathcal{A} = \{ b_{1}, \dots, b_{n} \}
    $$ 
    
    for $\mathcal{U}$.
    
    Since $\mathcal{U} \subseteq \mathcal{V}$, 
    there are 2 cases.
    
    In the case where $\mathcal{U} = \mathcal{V}$, 
    $\mathcal{A}$ is also a basis of $\mathcal{V}$ and
    thus, 
    
    $$
    \text{dim} (\mathcal{U}) = \text{dim} (\mathcal{V}).
    $$
    
    In the case where $\mathcal{U} \subset \mathcal{V}$, 
    there is at least 1 vector $x \in \mathcal{V}$ such that 
    
    $$
    x \notin \text{span} (\mathcal{A}).
    $$
    
    
  :::

(dimension-property-2)=

- If a subspace $\mathcal{U}$ is a subset of a finite dimensional subspace $\mathcal{V}$
    and $\text{dim} (\mathcal{U}) = \text{dim} (\mathcal{V})$,
    then
    
    $$
    \mathcal{U} = \mathcal{V}.
    $$
    
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    Since $\mathcal{U} \subset \mathcal{V}$ and according to the property of [extension of the basis](extension-of-a-basis),
    there exists a basis $b_{\mathcal{U}}$ for $\mathcal{U}$ and $b_{\mathcal{V}}$ for $\mathcal{V}$ such that
    
    $$
    \mathcal{B}_{\mathcal{U}} \subset \mathcal{B}_{\mathcal{V}}.
    $$
    
    However, since $\text{dim} (\mathcal{U}) = \text{dim} (\mathcal{V})$, 
    it must follows that
    
    $$
    \mathcal{B}_{\mathcal{U}} = \mathcal{B}_{\mathcal{V}}.
    $$
    
    Since $\mathcal{U}$ and $\mathcal{V}$ shares the same basis, 
    
    $$
    \mathcal{U} = \mathcal{V}.
    $$
    
  :::

(dimension-property-3)=

- Given $\mathcal{U}$ and $\mathcal{V}$ are subspaces, then

    $$
    \text{dim} (\mathcal{U} + \mathcal{V}) = \text{dim} (\mathcal{U}) + \text{dim} (\mathcal{V}) - \text{dim} (\mathcal{U} \cap \mathcal{V}).
    $$
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    Suppose $\text{dim} (\mathcal{U} \cap \mathcal{V}) = k$,  $\text{dim} (\mathcal{U}) = m$, and $\text{dim} (\mathcal{V}) = n$.
    
    Assume there is a basis 
    
    $$
    \mathcal{B} = \{ b_{1}, \dots, b_{k} \}
    $$ 
    
    for $\mathcal{U} \cap \mathcal{V}$. 
    
    Since $\mathcal{U} \cap \mathcal{V} \subseteq \mathcal{U}$ and $\mathcal{U} \cap \mathcal{V} \subseteq \mathcal{V}$, 
    there exists a basis $\mathcal{A}$ for $\mathcal{U}$ and $\mathcal{C}$ for $\mathcal{V}$ 
    
    $$
    \mathcal{A} = \{ b_{1}, \dots, b_{k}, a_{k + 1}, \dots, a_{m} \}
    $$
    
    $$
    \mathcal{C} = \{ b_{1}, \dots, b_{k}, c_{k + 1}, \dots, c_{n} \}
    $$
    
    as extensions of $\mathcal{B}$, according to [extension of basis property](extension-of-a-basis).
    
    Consider the set 
    
    $$
    \mathcal{A} \cup \mathcal{C} = \{ b_{1}, \dots, b_{k}, a_{k + 1}, \dots, a_{m}, c_{k + 1}, \dots, c_{n} \}
    $$
    
    we will prove that it is a basis of $\mathcal{U} + \mathcal{V}$. 
    
    First, consider all $x \in \mathcal{U} + \mathcal{V}$,
    which can be represented using the basis of $\mathcal{U}$ and the basis of $\mathcal{V}$
    
    $$
    \begin{aligned}
    x 
    & = \sum_{i=1}^{k} \alpha_{i} b_{i} + \sum_{i=k+1}^{m} \alpha_{i} a_{i} + \sum_{i=1}^{k} \beta_{i} b_{i} + \sum_{i=k+1}^{m} \beta_{i} c_{i}
    \\
    & = \sum_{i=1}^{k} (\alpha_{i} + \beta_{i}) b_{i} + \sum_{i=k+1}^{m} \alpha_{i} a_{i} + \beta_{i} c_{i}.
    \end{aligned}
    $$
    
    Thus, any vector $x \in \mathcal{U} + \mathcal{V}$ is a linear combination of vectors in $\mathcal{A} \cup \mathcal{C}$ and we have 
    
    $$
    \mathcal{U} + \mathcal{V} \subseteq \text{span} \left( \mathcal{A} \cup \mathcal{C} \right).
    $$
    
    Conversely, 
    all $x \in \text{span} \left( \mathcal{A} \cup \mathcal{C} \right)$ can be written as the linear combinations of vectors in $\mathcal{A}$ and $\mathcal{C}$,
    and thus
    
    $$
    \text{span} \left( \mathcal{A} \cup \mathcal{C} \right) \subseteq \mathcal{U} + \mathcal{V}.
    $$
    
    Thus, 
    
    $$
    \mathcal{U} + \mathcal{V} = \text{span} \left( \mathcal{A} \cup \mathcal{C} \right).
    $$
    
    Next, we will prove the vectors in $\mathcal{A} \cup \mathcal{C}$ are linearly independent by contradiction. 
    
    Consider $x \in \mathcal{U} \cap \mathcal{V}$, 
    which can be represented by the basis of $\mathcal{U} \cap \mathcal{V}$, $\mathcal{U}$ and, $\mathcal{V}$ at the same time
    
    $$
    \begin{aligned}
    x 
    & = \sum_{i=1}^{k} \alpha_{i} b_{i} + \sum_{i=k+1}^{m} \alpha_{i} a_{i}
    \\
    & = \sum_{i=1}^{k} \beta_{i} b_{i} + \sum_{i=k+1}^{n} \beta_{i} c_{i}
    \\
    & = \sum_{i=1}^{k} \epsilon_{i} b_{i}.
    \end{aligned}
    $$
    
    Suppose $x = 0$, then because 
    
  :::

## Types of the subspaces 

We can classify the types of the subspaces based on their dimensions.
For example, in $\mathbb{R}^{n}$ there are $n$ types of subspaces

- 0 dimension subspace: $\{ 0 \}$.

- 1 dimension subspaces.

    ...

- n dimension subspace: $\mathbb{R}^{n}$ itself.
