---
title: Linear Map and Rank
---

# Linear Map

Let $\mathcal{U}$ and $\mathcal{V}$ be the vector spaces over the same filed $\mathbb{F}$. 
A map $T: \mathcal{U} \to \mathcal{V}$ is linear if 

- $T (u + v) = T (u) + T (v) \quad u, v \in \mathcal{U}, T (u), T (v) \in \mathcal{V}$, and

- $T (\alpha \cdot v) = \alpha \cdot T (v) \quad \alpha \in \mathbb{F}, v \in \mathcal{u}, T (v) \in \mathcal{V}.$

## Properties of linear map

Let $\mathcal{U}$ and $\mathcal{V}$ be two vector spaces over the same filed $\mathbb{F}$, 
and suppose $T$ is a linear map $T: \mathcal{U} \to \mathcal{V}$.

- A linear map must satisfy $T (0) = 0$.

  ::: {.callout-note collapse="true" title="Proof"}
    
    We prove by contradiction. Suppose there exists a linear map such that 
    
    $$
    T (0) \neq 0. 
    $$
    
    Suppose $v = 0$ and according to the definition of the linear map 
    
    $$
    \begin{aligned}
    T (\alpha \cdot v) 
    & = \alpha \cdot T (v), \forall \alpha \in \mathbb{F}
    \\
    T (0) 
    & = \alpha \cdot T (0), \forall \alpha \in \mathbb{F}.
    \end{aligned}
    $$
    
    Since $T (0) \neq 0$, we can divide both sides by $T (0)$
    
    $$
    \alpha = 1, \forall \alpha \in \mathbb{F},
    $$
    
    which raises a contradiction.

  :::

- There exists a matrix representation of $T$.

  ::: {.callout-note collapse="true" title="Proof"}
    
    Suppose $\text{dim} (\mathcal{U}) = n$ and $\text{dim} (\mathcal{V}) = m$.
    
    Let $\{ u_{1}, \dots, u_{n} \}$ be a basis of $\mathcal{U}$, and $\{ v_{1}, \dots, v_{m} \}$ be a basis of $\mathcal{V}$. 
    
    Suppose any vector $x \in \mathcal{U}$ satisfies that
    
    $$
    x = \sum_{i=1}^{n} \alpha_{i} \cdot u_{i},
    $$
    
    and the mapped vector $T (x) \in \mathcal{V}$ satisfies that
    
    $$
    T (x) = \sum_{j=1}^{m} \beta_{j} \cdot v_{j}.
    $$
    
    Since $T (u_{i}) \in \mathcal{V}$, we have 
    
    $$
    T (u_{i}) = \sum_{j=1}^{m} c_{i, j} \cdot v_{j}, \forall i = 1, \dots, n.
    $$
    
    By the definition of the linear map,
    
    $$
    \begin{aligned}
    T (x) 
    & = T \left(
        \sum_{i=1}^{n} \alpha_{i} \cdot u_{i} 
    \right)
    \\
    & = \sum_{i=1}^{n} \alpha_{i} \cdot T (u_{i}).
    \\
    & = \sum_{i=1}^{n} \alpha_{i} \sum_{j=1}^{m} c_{i, j} \cdot v_{j}
    \\
    & = \sum_{j=1}^{m} \left( 
        \sum_{i=1}^{n} \alpha_{i} c_{i, j}
    \right) \cdot v_{j}.
    \\
    \end{aligned}
    $$
    
    Because of the unique representation property, 
    
    $$
    \begin{aligned}
    T(x) = \sum_{j=1}^{m} \beta_{j} \cdot v_{j} 
    & = \sum_{j=1}^{m} \left( 
        \sum_{i=1}^{n} \alpha_{i} c_{i, j}
    \right) \cdot v_{j}
    \\
    \beta_{j} 
    & = \sum_{i=1}^{n} \alpha_{i} c_{i, j} \quad \forall j = 1, \dots, m,
    \end{aligned}
    $$
    
    which can be represented in the matrix form
    
    $$
    \begin{bmatrix}
    \beta_{1} \\
    \vdots \\
    \beta_{m} \\
    \end{bmatrix}
    = 
    \begin{bmatrix}
    c_{1, 1} & \dots & c_{n, 1}  \\
    \vdots & \dots & \vdots \\
    c_{1, m} & \dots & c_{n, m} \\
    \end{bmatrix}
    \begin{bmatrix}
    \alpha_{1} \\
    \vdots \\
    \alpha_{n} \\
    \end{bmatrix}.
    $$
    
    Hence, given any vector $x \in \mathcal{U}$ that has basis coefficients in a given basis $\{ u_{1}, \dots, u_{n} \}$
    
    $$
    \mathbf{a} = \begin{bmatrix}
    \alpha_{1} \\
    \vdots \\
    \alpha_{n} \\
    \end{bmatrix},
    $$
    
    there is a mapped vector $T (x) \in \mathcal{V}$ with basis coefficients in a given basis $\{ v_{1}, \dots, v_{n} \}$
    
    $$
    \mathbf{b} = \begin{bmatrix}
    \beta_{1} \\
    \vdots \\
    \beta_{m} \\
    \end{bmatrix},
    $$
    
    where 
    
    $$
    \mathbf{b} = \mathbf{C} \mathbf{a}.
    $$
    
  :::

## Generalization of null space and range space

Since every linear map has a matrix representation, 
the null space and range space defined using matrix can be redefined using linear map. 

Given a map $T: \mathcal{U} \to \mathcal{V}$, 
the null space (kernel) is

$$
N (T) = \left\{ 
    x \in \mathcal{U} \mid T (x) = 0 
\right\},
$$

and the range space (column space) is 

$$
R (T) = \left\{
    y \in \mathcal{V} \mid y \in T (x), \forall x \in \mathcal{U}
\right\}.
$$

# Rank

Consider matrix $\mathbf{A} \in \mathbb{F}^{m \times n}$, the rank of matrix $\mathbf{A}$ is 

$$
\text{rank} (\mathbf{A}) = \text{dim} (R (\mathbf{A})).
$$

## Properties of rank

Given a matrix $\mathbf{A} \in \mathbb{F}^{m \times n}$, 

(rank-property-1)=

- rank-nullity theorem: $\text{rank} (\mathbf{A}) + \text{dim} (N (\mathbf{A})) = n$

  ::: {.callout-note collapse="true" title="Proof"}

    Since $\mathbf{A}$ represents a linear transform $T: \mathcal{U} \to \mathcal{V}$ with $\mathrm{dim} (\mathcal{U}) = m, \mathrm{dim} (\mathcal{V}) = n$
    the rank-nullity theorem can also be stated as 

    $$
    \mathrm{dim} (R (T)) + \mathrm{dim} (N (T)) = \mathrm{dim} (\mathcal{U}).
    $$

    By assuming that $\text{dim} (N (T)) = k$,
    there exists a basis $\{ b_{1}, \dots, b_{k} \}$ of $N (T)$.

    Since by definition of the null space, $N (T)$ is a subspace of $\mathcal{U}$,
    then according to the [property of the basis](extension-of-a-basis),
    there exists a set of vectors $\{ b_{k + 1}, \dots, b_{n} \}$ in $\mathcal{U}$ such that 

    $$
    \{ b_{1}, \dots, b_{k}, b_{k + 1}, \dots, b_{n} \}
    $$

    is a basis of $\mathcal{U}$. 

    Consider any $x \in \mathcal{U}$, 

    $$
    \begin{aligned}
    T (x) 
    & = T \left(
        \sum_{i=1}^{n} \alpha_{i} b_{i} 
    \right)
    & [\{ b_{1}, \dots, b_{i} \} \text{ is a basis of } \mathcal{U}] 
    \\
    & = \sum_{i=1}^{n} \alpha_{i} T (b_{i}) 
    & [\text{T is linear}]
    \\
    \end{aligned}
    $$

    Since $\{ b_{1}, \dots, b_{k} \}$ is a basis of $N (T)$, 
    they are also in $N (T)$. 
    According to the definition of the null space 

    $$
    T (b_{i}) = 0 \quad i = 1, \dots, k.
    $$

    Then we can show that every $T (x)$ is a linear combination of $T (b_{k+1}) \dots, T (b_{n})$:

    $$
    \begin{aligned}
    T (x) 
    & = \sum_{i=1}^{n} \alpha_{i} T (b_{i}) 
    \\
    & = \sum_{i=1}^{k} \alpha_{i} T (b_{i}) + \sum_{i=k+1}^{n} \alpha_{i} T (b_{i})
    \\
    & = 0 + \sum_{i=k+1}^{n} \alpha_{i} T (b_{i})
    \\
    & = \sum_{i=k+1}^{n} \alpha_{i} T (b_{i})
    \end{aligned}.
    $$

    Since the definition of the range space is 

    $$
    R (T) = \{ y \mid y = T(x), \forall x \in \mathcal{U} \},
    $$

    all vectors in $R (T)$ are linear combinations of $T (b_{k+1}) \dots, T (b_{n})$.

    Also, since $b_{k+1}, \dots, b_{n} \in \mathcal{U}$, 
    we have

    $$
    T (b_{k+1}), \dots, T (b_{n}) \in R (T).
    $$

    by the definition of the range space.

    Thus, by the [property of span]()

    $$
    R (T) = \text{span} (T (b_{k+1}), \dots, T (b_{n})).
    $$

    Then we will show that $T (b_{k+1}), \dots, T (b_{n})$ are linearly independent by supposing a set of $\beta_{k+1}, \dots, \beta_{n}$ such that

    $$
    \begin{aligned}
    \sum_{i=k+1}^{n} \beta_{i} T (b_{i}) 
    & = 0
    \\
    T \left( 
        \sum_{i=k+1}^{n} \beta_{i} b_{i}
    \right)
    & = 0
    & [\text{T is linear}]
    \\
    \sum_{i=k+1}^{n} \beta_{i} b_{i} 
    & \in N (T)
    & [\text{def of null space}]
    \\
    \end{aligned}
    $$

    Since $\{ b_{1}, \dots, b_{k} \}$ is also a basis of the $N (T)$, there exists a set of $\gamma_{1}, \dots, \gamma_{k}$ such that

    $$
    \begin{aligned}
    \sum_{i=k+1}^{n} \beta_{i} b_{i} 
    & = \sum_{i=j}^{k} \gamma_{j} b_{j}
    \\
    \sum_{i=k+1}^{n} \beta_{i} b_{i} + \sum_{j=1}^{k} - \gamma_{j} b_{j}
    & = 0.
    \end{aligned}
    $$

    Since $\{ b_{1}, \dots, b_{n} \}$ are linearly independent, it must hold that

    $$
    \beta_{i} = \gamma_{j} = 0 \quad i = k + 1, \dots, n, j = 1, \dots, k.
    $$

    Thus, we have shown that 

    $$
    \sum_{i=k+1}^{n} \beta_{i} T (b_{i}) = 0 \iff \beta_{i} = 0 \quad i = k + 1, \dots, n,
    $$

    which means the vectors $T (b_{k + 1}), \dots, T (b_{n})$ are linearly independent and therefore is a basis of $R (T)$.

    Finally, since 

    - $\{ b_{1}, \dots, b_{k} \}$ is a basis of $N (T)$,

    - $\{ b_{k + 1}, \dots, b_{n} \}$ is a basis of $R (T)$, and
         
    - $\{ b_{1}, \dots, b_{n} \}$ is a basis of $\mathcal{U}$,

    we have the rank-nullity theorem

    $$
    \text{dim} (N (T)) + \text{dim} (R (T)) = \text{dim} (\mathcal{U}).
    $$

  :::

(rank-property-2)=

- $\text{rank} (\mathbf{A}) \leq \min (m, n)$

  ::: {.callout-note collapse="true" title="Proof"}
    
    According to the [rank property](rank-property-1) 
    
    $$
    \text{dim} (N (\mathbf{\mathbf{A}})) = n - \text{rank} (\mathbf{A}).
    $$
    
    Since by definition, the number of vectors in a basis is non-negative
    
    $$
    \text{dim} (N (\mathbf{\mathbf{A}})) \geq 0,
    $$
    
    we have
    
    $$
    \text{rank} (\mathbf{A}) \leq n.
    $$
    
    Also, since $R (\mathbf{A})$ is a subspace of $\mathbb{F}^{m}$ and the [property]()
    
    $$
    \text{rank} (\mathbf{A}) = \text{dim} (R (\mathbf{A})) \leq m.
    $$
    
    Thus, 
    
    $$
    \text{rank} (\mathbf{A}) \leq \min(m, n).
    $$

  :::
    
    - If $\text{rank} (\mathbf{A}) = \min (m, n)$, matrix is called a full (row or column) rank matrix.
    
    - If $\text{rank} (\mathbf{A}) = n$, $\mathbf{a}_{*, 1}, \dots, \mathbf{a}_{*, n}$ are linearly independent.

(rank-property-3)=

- $\text{rank} (\mathbf{A}) = \text{rank} (\mathbf{A}^{T})$

  ::: {.callout-note collapse="true" title="Proof"}
    
    Suppose $\mathbf{A} \in \mathbb{F}^{m \times n}$.
    Let $\{ \mathbf{a}_{1}, \dots, \mathbf{a}_{n} \in \mathbb{F}^{m} \}$ be the columns of $\mathbf{A}$
    
    $$
    \mathbf{A} = 
    \begin{bmatrix}
    \mathbf{a}_{1} & \dots & \mathbf{a}_{n}
    \end{bmatrix}.
    $$
    
    Let $\text{rank} (\mathbf{A}) = r$. 
    
    By the definition of the range space, the columns of $\mathbf{A}$ are in its range space
    
    $$
    \mathbf{a}_{1}, \dots, \mathbf{a}_{n} \in R (\mathbf{A})
    $$
    
    and thus the columns of $\mathbf{A}$ are linear combinations of any basis of $R (\mathbf{A})$.
    
    Suppose there exists a basis of $R (\mathbf{A})$ as columns of $\mathbf{B}$ 
    
    $$
    \mathbf{B} = 
    \begin{bmatrix}
    \mathbf{b}_{1} & \dots & \mathbf{b}_{r}
    \end{bmatrix}.
    $$
    
    and a matrix $\mathbf{C} \in \mathbb{F}^{r \times n}$ 
    
    $$
    \mathbf{C} = 
    \begin{bmatrix}
    c_{1, 1} & \dots & c_{n, 1} \\
    \vdots & \dots & \vdots \\
    c_{1, r} & \dots & c_{n, r} \\
    \end{bmatrix}
    $$
    
    such that the columns of $\mathbf{A}$ are linear combinations of the basis $\mathbf{B}$ using the columns of $\mathbf{C}$ as cofficients
    
    $$
    \mathbf{A} = \mathbf{B} \mathbf{C}.
    $$
    
    By the defintion of [matrix multiplication](matrix-multiplication), 
    the rows of $\mathbf{A}$ are also linear combinations of rows of $\mathbf{C}$ using the rows of $\mathbf{B}$ as coefficients.
    Thus, by the [spanning set property](spanning-set-property-3), 
    
    $$
    R (\mathbf{A}^{T}) \subseteq R (\mathbf{C}^{T}). 
    $$
    
    Then, by the [dimension property](dimension-property-1), 
    
    $$
    \begin{aligned}
    \text{dim} (R (\mathbf{A}^{T})) 
    & \leq \text{dim} (R (\mathbf{C}^{T}))
    \\
    \text{rank} (\mathbf{A}^{T})
    & \leq \text{rank} (\mathbf{C}^{T}).
    \end{aligned}
    $$
    
    Since $\mathbf{C}^{T} \in \mathbb{F}^{n \times n}$, 
    according to the [rank property](rank-property-2) 
    
    $$ \text{rank} (\mathbf{C}^{T}) \leq r = \text{rank} (\mathbf{A}). $$
    
    Thus, 
    
    $$
    \text{rank} (\mathbf{A}^{T}) \leq \text{rank} (\mathbf{A}).
    $$
    
    Finally, we can use the same argument to prove 
    
    $$
    \text{rank} (\mathbf{A}) \leq \text{rank} (\mathbf{A}^{T}).
    $$
    
    by substituting $\mathbf{A}$ as $\mathbf{A}^{T}$. 
    
    Since $\text{rank} (\mathbf{A}^{T}) \leq \text{rank} (\mathbf{A})$ and $ \text{rank} (\mathbf{A}) \leq \text{rank} (\mathbf{A}^{T})$ at the same time, 
    we can prove
    
    $$
    \text{rank} (\mathbf{A}) = \text{rank} (\mathbf{A}^{T}).
    $$

  :::

(rank-property-6)=

- If $\mathbf{A} \in \mathbb{R}^{m \times n}$, then

    $$
    \text{rank} (\mathbf{A}) = \text{rank} (\mathbf{A}^{T} \mathbf{A}).
    $$

  ::: {.callout-note collapse="true" title="Proof"}
    
    TODO
    
  ::: 

(rank-property-4)=

- If $\mathbf{A} \in \mathbb{R}^{m \times n}$ and $\mathbf{B} \in \mathbb{R}^{m \times m}$ and $\mathbf{C} \in \mathbb{R}^{n \times n}$ are full rank matrices,
    then

    $$
    \text{rank} (\mathbf{A}) = \text{rank} (\mathbf{B} \mathbf{A}) = \text{rank} (\mathbf{A} \mathbf{C}).
    $$

  ::: {.callout-note collapse="true" title="Proof"}
    
    TODO
    
  ::: 

## Rank and matrix inverse 

(rank-property-4)=

- Suppose $\mathbf{A} \in \mathbb{F}^{m \times n}$. 

    There exists a left inverse matrix $\mathbf{B} \in \mathbb{F}^{n \times m}$ of $\mathbf{A}$ such that

    $$
    \mathbf{B} \mathbf{A} = \mathbf{I}_{n \times n},
    $$
    
    if and only if $\text{rank} (\mathbf{A}) = n$.

    There exists a right inverse matrix $\mathbf{C} \in \mathbb{F}^{n \times m}$ of $\mathbf{A}$ such that

    $$
    \mathbf{A} \mathbf{C} = \mathbf{I}_{m \times m}.
    $$
    
    if and only if $\text{rank} (\mathbf{A}) = m$.
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    To prove this, we first prove that there exists a matrix $\mathbf{C}$ such that
    
    $$
    \mathbf{A} \mathbf{C} = \mathbf{I}_{m \times m} \iff \mathbf{e}_{1}, \dots \mathbf{e}_{m} \in R (A).
    $$
    
    First notice that 
    
    $$
    \mathbf{I}_{m \times m} = 
    \begin{bmatrix}
    \mathbf{e}_{1} & \dots & \mathbf{e}_{m}
    \end{bmatrix}
    $$
    
    where $\mathbf{e}_{1}, \dots, \mathbf{e}_{m} \in \mathbb{F}^{m}$.
    
    Thus, $\mathbf{e}_{1}, \dots, \mathbf{e}_{m}$ is a linear combination of the columns of $\mathbf{A}$.
    By the definition of the range space, 
    we can see
    
    $$
    \mathbf{e}_{1}, \dots, \mathbf{e}_{m} \in R (\mathbf{A}).
    $$
    
    Conversely, since $\mathbf{e}_{1}, \dots, \mathbf{e}_{m} \in R (\mathbf{A})$,
    each $\mathbf{e}_{i}, i = 1, \dots, m$ is a linear combination of the columns in $\mathbf{A}$.
    
    Thus, there exists a set of coefficients $c_{j, i}, j = 1, \dots, n$ for the linear combination of $\mathbf{e}_{i}$,
    and the matrix of these coefficients is
    
    $$
    \mathbf{C} = 
    \begin{bmatrix}
    c_{1, 1} & \dots & c_{1, m} \\
    \vdots & c_{j, i} & \vdots \\
    c_{n, 1} & \dots & c_{n, m} \\
    \end{bmatrix}.
    $$
    
    Then we prove that
    
    $$
    \mathbf{e}_{1}, \dots \mathbf{e}_{m} \in R (\mathbf{A}) \iff \text{rank} (\mathbf{A}) = m.
    $$
    
    Again notice that $\mathbf{e}_{1}, \dots \mathbf{e}_{m}$ is the standard basis of $\mathbb{F}^{m}$.
    
    Since $R (\mathbf{A}) \subseteq \mathbb{F}^{m}$, 
    all vectors in $R (\mathbf{A})$ are linear combinations of $\mathbf{e}_{1}, \dots \mathbf{e}_{m}$. 
    
    Since we know that $\mathbf{e}_{1}, \dots \mathbf{e}_{m} \in R (\mathbf{A})$, 
    according to the [spanning set property](spanning-set-property-2),
    
    $$
    R (\mathbf{A}) = \text{span} (\mathbf{e}_{1}, \dots, \mathbf{e}_{m}).
    $$
    
    Since by definition $\mathbf{e}_{1}, \dots \mathbf{e}_{m}$ are linearly independent, 
    the set $\mathbf{e}_{1}, \dots, \mathbf{e}_{m}$ is a basis for $R (\mathbf{A})$. 
    
    According to the [cardinality of basis](cardinality-of-basis), 
    
    $$
    \text{rank} (\mathbf{A}) = m.
    $$
    
    Conversely, since we know $\text{rank} (\mathbf{A}) = m = \text{dim} (\mathbb{F}^{m}$ and $ R (\mathbf{A}) \subseteq \mathbb{F}^{m}$,
    
    $$
    R (\mathbf{A}) = \mathbb{F}^{m}. 
    $$
    
    Since by definition $\mathbf{e}_{1}, \dots \mathbf{e}_{m} \in \mathbb{F}^{m}$,
    
    $$
    \mathbf{e}_{1}, \dots \mathbf{e}_{m} \in R (\mathbf{A}).
    $$
    
    In conclusion, we have proven that there exists a matrix $\mathbf{C}$ such that 
    
    $$
    \mathbf{A} \mathbf{C} = \mathbf{I}_{m \times m} \iff \mathbf{e}_{1}, \dots \mathbf{e}_{m} \in R (A) \iff \text{rank} (\mathbf{A}) = m.
    $$
    
  :::
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    We first notice that 
    
    $$
    \begin{aligned}
    (\mathbf{B} \mathbf{A})^{T} 
    & = \mathbf{I}_{n \times n}^{T} 
    \\
    \mathbf{A}^{T} \mathbf{B}^{T} 
    & = \mathbf{I}_{n \times n}.
    \end{aligned}
    $$
    
    By applying the proof above,
    we can prove that 
    
    $$
    \text{rank} (\mathbf{A}^{T}) = n.
    $$
    
    According to the [rank property](rank-property-3),
    
    
    $$
    \text{rank} (\mathbf{A}^{T}) = \text{rank} (\mathbf{A}) = n.
    $$
    
  ::: 

(rank-property-5)=

- If $\mathbf{A} \in \mathbb{F}^{n \times n}$ is a square matrix and has full rank ($\text{rank}(\mathbf{A}) = n$),
    then $\mathbf{A}$ has a unique inverse matrix $\mathbf{A}^{-1}$ such that 
    
    $$
    \mathbf{A} \mathbf{A}^{-1} = \mathbf{A}^{-1} \mathbf{A} = \mathbf{I}_{n \times n}.
    $$

  ::: {.callout-note collapse="true" title="Proof"}
    
    TODO
    
  ::: 
