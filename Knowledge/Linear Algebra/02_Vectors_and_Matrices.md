---
title: Vectors and Matrices
---

# Vectors

Let $\mathbb{F}$ be a field. The vector space $\mathbb{F}^{n}$ is defined as the set of all tuples (ordered lists) that have $n$ field elements of $\mathbb{F}$

$$
\mathbb{F}^{n} = 
\left\{
\begin{bmatrix}
    x_{1} \\
    \vdots \\
    x_{n} \\
\end{bmatrix},
x_{i} \in \mathbb{F}
\right\},
$$

where each element member is called a $n$ dimensional column vector.

- Vector addition: for $\mathbf{x}, \mathbf{y} \in \mathbb{F}^{n}$

    $$
    \mathbf{x} + \mathbf{y} = 
    \begin{bmatrix}
        x_{1} + y_{1} \\
        \vdots \\
        x_{n} + y_{n} \\
    \end{bmatrix}.
    $$
    
    That is, the vector addition of the vector space $\mathbb{F}^{n}$ is defined as the element-wise field addition between two vectors.

- Scalar multiplication: for $\alpha \in \mathbb{F}$ and $\mathbf{x} \in \mathbb{F}^{n}$

    $$
    \alpha \cdot \mathbf{x} = 
    \begin{bmatrix}
        \alpha \cdot x_{1} \\
        \vdots \\
        \alpha \cdot x_{n} \\
    \end{bmatrix}.
    $$
    
    That is, the scalar multiplication of the vector space $\mathbb{F}^{n}$ is defined as the element-wise field multiplication between the field element and the vector.

- "zero" vector and addictive inverse: for $\mathbf{x} \in \mathbb{F}$

    $$
    0 = 
    \begin{bmatrix}
        0 \\
        \vdots \\
        0 \\
    \end{bmatrix}
    \quad
    \mathbf{x}_{I} = 
    \begin{bmatrix}
        (x_{1})_{I} \\
        \vdots \\
        (x_{n})_{I} \\
    \end{bmatrix}.
    $$

# Matrices

Let $\mathbb{F}$ be a field. The vector space $\mathbb{F}^{m \times n}$ is defined as the set of all tables that have $m$ rows and $n$ columns of field elements of $\mathbb{F}$

$$
\mathbb{F}^{m \times n} = 
\left\{
\begin{bmatrix}
    x_{1, 1}, & \dots & x_{1, n} \\
    \vdots, & \dots & \vdots \\
    x_{m, 1}, & \dots & x_{m, n} \\
\end{bmatrix},
x_{i, j} \in \mathbb{F}
\right\},
$$

where each element member is called $m \times n$ dimensional matrix.

The definition of vector addition, scalar multiplication, zero, and addictive inverse are the same as $n$ dimensional column vectors.

(matrix-vector-multiplication)=

## Matrix-vector multiplication

Given a matrix $\mathbf{A} \in \mathbb{F}^{m \times n}$, 
the matrix-vector multiplication is a function that maps from vector space $\mathbf{x} \in \mathbb{F}^{n}$ to $\mathbf{y} \in \mathbb{F}^{m}$

$$
\mathbf{y} = \mathbf{A} \mathbf{x} = 
\begin{bmatrix}
    y_{1} = a_{1, 1} \cdot x_{1} + \dots a_{1, n} \cdot x_{n} \\
    \vdots \\
    y_{m} = a_{m, 1} \cdot x_{1} + \dots a_{m, n} \cdot x_{n} \\
\end{bmatrix}.
$$


If we view $\mathbf{A}$ as $n$ columns of $\mathbb{F}^{m}$ vectors,

$$
\mathbf{A} = 
\begin{bmatrix}
\mathbf{a}_{1} & \dots & \mathbf{a}_{n} \\
\end{bmatrix}
$$

the vector $\mathbf{y}$ can be interpreted as the linear combinations of columns of $\mathbf{A}$ with elements of $\mathbf{x}$ as coefficients

$$
\mathbf{y} = \sum_{i=1}^{n} x_{i} \mathbf{a}_{i}.
$$

(matrix-multiplication)=

## Matrix multiplication

Given two matrices $\mathbf{A} \in \mathbb{F}^{m \times n}$ and $\mathbf{B} \in \mathbb{F}^{n \times r}$, 
the matrix multiplication is a function that applies vector matrix multiplication on the matrix $\mathbf{A} \in \mathbb{F}^{m \times n}$ and the vector $\mathbf{b}_{i} \in \mathbb{F}^{n}$ 
($i$th column of $\mathbf{B}$)

$$
\mathbf{C} = \mathbf{A} \mathbf{B} = 
\begin{bmatrix}
\mathbf{c}_{1} = \mathbf{A} \mathbf{b}_{1} & \dots & \mathbf{c}_{r} = \mathbf{A} \mathbf{b}_{r} \\
\end{bmatrix},
$$ 

which results in a vector $\mathbf{c}_{i} \in \mathbb{F}^{m}$ as the $i$th column of the $\mathbf{C}$.

- The column $i$ of $\mathbf{C}$ is a linear combination of columns of $\mathbf{A}$ using the elements of the column $i$ of $\mathbf{B}$ as coefficients.

- The row $i$ of $\mathbf{C}$ is a linear combination of rows of $\mathbf{B}$ using the elements of row $i$ of $\mathbf{A}$ as coefficients.

# Well-known Subspaces for Matrix

Given a matrix $\mathbf{A} \in \mathbb{F}^{m \times n}$, the matrix-vector multiplication 

$$
\mathbf{y} = \mathbf{A} \mathbf{x} = 
\begin{bmatrix}
    y_{1} = a_{1, 1} \cdot x_{1} + \dots a_{1, n} \cdot x_{n} \\
    \vdots \\
    y_{m} = a_{m, 1} \cdot x_{1} + \dots a_{m, n} \cdot x_{n} \\
\end{bmatrix}
$$

is a function that maps from vector space $x \in \mathbb{F}^{n}$ to $y \in \mathbb{F}^{m}$.

Given a matrix $\mathbf{A} \in \mathbb{F}^{m \times n}$, we can define several subspaces of $\mathbb{F}^{n}$ or $\mathbb{F}^{m}$ using the matrix-vector multiplication of matrix $\mathbf{A}$.

## Null space

The null space of the matrix $\mathbf{A}$ is the set

$$
N (\mathbf{A}) = \left\{ 
    \mathbf{x} \in \mathbb{F}^{n} \mid \mathbf{A} \mathbf{x} = \mathbf{0} \in \mathbb{F}^{m}
\right\},
$$

which is the set of the vectors in $\mathbb{F}^{n}$ that is mapped to $0 \in \mathbb{F}^{m}$ by matrix $\mathbf{A}$.

::: {.callout-note collapse="true" title="Proof"}

Since $\mathbf{A} 0 = 0 \in \mathbb{F}^{n}$, $\mathbf{x} = 0 \in N (A)$. Thus $N (A)$ is not empty.

Consider $\mathbf{x}_{1}, \mathbf{x}_{2} \in N (A)$. 
According to the definition of the $N (A)$, 
$\mathbf{A} \mathbf{x}_{1} = 0$ and  $\mathbf{A} \mathbf{x}_{2} = 0$.

Then,

$$
\begin{aligned}
\mathbf{A} \mathbf{x}_{1} + \mathbf{A} \mathbf{x}_{2}
& = 0
\\
\mathbf{A} (\mathbf{x}_{1} + \mathbf{x}_{2})
& = 0.
\end{aligned}
$$

Thus $N (\mathbf{A})$ is closed under vector addition

$$
\mathbf{x}_{1} + \mathbf{x}_{2} \in N (\mathbf{A}).
$$

Also, for all $\alpha \in \mathbb{F}$,

$$
\begin{aligned}
\alpha \cdot \mathbf{A} \mathbf{x}_{1} 
& = \alpha \cdot 0
\\
\mathbf{A} (\alpha \cdot \mathbf{x}_{1})
& = 0.
\end{aligned}
$$

Thus $N (\mathbf{A})$ is closed under scalar multiplication

$$
\alpha \cdot \mathbf{x}_{1} \in N (\mathbf{A}).
$$

Thus, $N (\mathbf{A})$ is a non-empty set that is closed for both vector addition and scalar multiplication and thus is a subspace.

:::

## Range (image) space

The range (image) space of the matrix $\mathbf{A}$ is the set 

$$
R (\mathbf{A}) = \left\{ 
    \mathbf{y} \in \mathbb{F}^{m} \mid \mathbf{y} = \mathbf{A} \mathbf{x}, \forall \mathbf{x} \in \mathbb{F}^{n}
\right\},
$$

which is the set of vectors in $\mathbb{F}^{m}$ that can be mapped from $\mathbb{F}^{n}$ by matrix $\mathbf{A}$.

::: {.callout-note collapse="true" title="Proof"}

Since $\mathbf{x} = 0 \in \mathbb{F}^{n}$, $\mathbf{y} = 0 \in R (A)$. Thus $R (A)$ is not empty.

Consider $\mathbf{y}_{1}, \mathbf{y}_{2} \in R (A)$. 
According to the definition of the $R (A)$, 
there exists an $\mathbf{x}_{1} \in \mathbb{F}^{m}$ for $\mathbf{y}_{1}$ and an $\mathbf{x}_{2} \in \mathbb{F}^{m}$ for $\mathbf{y}_{2}$.

Then,

$$
\begin{aligned}
\mathbf{y}_{1} + \mathbf{y}_{2} 
& = \mathbf{A} \mathbf{x}_{1} + \mathbf{A} \mathbf{x}_{2}
\\
& = \mathbf{A} (\mathbf{x}_{1} + \mathbf{x}_{2})
\end{aligned}
$$

Since by the closure under addition property, 

$$
\mathbf{x}_{1} + \mathbf{x}_{2} \in \mathbb{F}^{m}
$$

and thus $R (\mathbf{A})$ is closed under vector addition

$$
\mathbf{y}_{1} + \mathbf{y}_{2} \in R (\mathbf{A}).
$$

Also, for all $\alpha \in \mathbb{F}$,

$$
\begin{aligned}
\alpha \cdot \mathbf{y}_{1}
& = \alpha \cdot \mathbf{A} \mathbf{x}_{1} 
\\
& = \mathbf{A} (\alpha \cdot \mathbf{y}_{1})
\end{aligned}
$$

Again, since by the closure under scalar multiplication property, 

$$
\alpha \cdot \mathbf{x}_{1} \in \mathbb{F}^{m}, \forall \alpha \in \mathbb{F},
$$

and thus $R (\mathbf{A})$ is closed under scalar multiplication

$$
\alpha \cdot \mathbf{y}_{1} \in R (\mathbf{A}).
$$

Thus, $R (\mathbf{A})$ is a non-empty set that is closed for both vector addition and scalar multiplication and thus is a subspace.

:::

## Column and row space

The column space of the matrix $\mathbf{A}$ is the set of linear combinations of columns of $\mathbf{A}$

$$
C (\mathbf{A}) = \left\{ 
    \mathbf{y} \in \mathbb{F}^{m} \mid \mathbf{y} = \sum_{i=1}^{n} \alpha_{i} \cdot \mathbf{a}_{*, i}, \forall \alpha_{i} \in \mathbb{F}
\right\},
$$

and the row space of the matrix $\mathbf{A}$ is the set of linear combinations of rows of $\mathbf{A}$

$$
C (\mathbf{A}^{T}) = \left\{ 
    \mathbf{y} \in \mathbb{F}^{m} \mid \mathbf{y} = \sum_{i=1}^{n} \alpha_{i} \cdot \mathbf{a}_{i, *}^{T}, \forall \alpha_{i} \in \mathbb{F}
\right\},
$$

which is the same as the column space of $\mathbf{A}^{T}$.

By the definition of matrix-vector multiplication,
the column space of $\mathbf{A}$ is the same as the range space of $\mathbf{A}$

$$
C (\mathbf{A}) = \left\{ 
    \mathbf{y} \in \mathbb{F}^{m} \mid \mathbf{y} = \sum_{i=1}^{n} \alpha_{i} \cdot \mathbf{a}_{*, i}, \forall \alpha_{i} \in \mathbb{F}
\right\} = \left\{ 
    \mathbf{y} \in \mathbb{F}^{m} \mid \mathbf{y} = \mathbf{A} \mathbf{x}, \forall \mathbf{x} \in \mathbb{F}^{n}
\right\} = R (\mathbf{A}).
$$
