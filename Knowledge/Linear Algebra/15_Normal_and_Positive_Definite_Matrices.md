---
title: Normal and Positive Definite Matrices
---

# Normal Matrices

The matrix $\mathbf{A} \in \mathbb{C}^{n \times n}$ is a **normal matrix** if and only if 

$$
\mathbf{A}^{H} \mathbf{A} = \mathbf{A} \mathbf{A}^{H}.
$$

## Properties of normal matrices

(normal-matrices-property-1)=

- Unitary matrices are normal.

  ::: {.callout-note collapse="true" title="Proof"}
    
    According to the [property of unitary matrices](unitary-matrix-property-2),
    a matrix $\mathbf{U}$ is unitary if and only if
    
    $$
    \mathbf{U}^{-1} \mathbf{U} = \mathbf{U} \mathbf{U}^{-1} = \mathbf{I}. 
    $$
    
    Thus, unitary matrices are normal.
    
  :::

(normal-matrices-property-2)=

- Diagonal matrices are normal.

  ::: {.callout-note collapse="true" title="Proof"}
    
    Consider $\mathbf{D} \in \mathbb{C}^{n \times n}$ as a diagonal matrix with $d_{1}, \dots, d_{n}$ in its diagonal.
    
    $$
    \mathbf{D}^{H} \mathbf{D} = \sum_{i=1}^{n} d_{i}^{2} = \mathbf{D} \mathbf{D}^{H}.
    $$

  :::

(normal-matrices-property-3)=

- Unitary similarity preserves normality. 
    That is, if $\mathbf{A}$ is a normal matrix and is unitarily similar to $\mathbf{B}$ 
    
    $$
    \mathbf{U}^{-1} \mathbf{A} \mathbf{U} = \mathbf{B}
    $$ 
    
    or 
    
    $$
    \mathbf{U}^{H} \mathbf{A} \mathbf{U} = \mathbf{B},
    $$ 
    
    then $\mathbf{B}$ is also a normal matrix.

  ::: {.callout-note collapse="true" title="Proof"}
    
    The goal is to prove 
    
    $$
    \mathbf{B}^{H} \mathbf{B} = \mathbf{B} \mathbf{B}^{H}.
    $$
    
    First we expand $\mathbf{B}^{H} \mathbf{B}$ to have 
    
    $$
    \begin{aligned}
    \mathbf{B}^{H} \mathbf{B}
    & = (\mathbf{U}^{H} \mathbf{A} \mathbf{U})^{H} (\mathbf{U}^{H} \mathbf{A} \mathbf{U})
    \\
    & = \mathbf{U} \mathbf{A}^{H} \mathbf{U}^{H} \mathbf{U}^{H} \mathbf{A} \mathbf{U}
    \\
    & = \mathbf{U}^{H} \mathbf{A}^{H} \mathbf{U} \mathbf{U}^{H} \mathbf{A} \mathbf{U}
    & [TODO]
    \\
    & = \mathbf{U}^{H} \mathbf{A}^{H} \mathbf{I} \mathbf{A} \mathbf{U}
    & [\mathbf{U} \mathbf{U}^{H} = \mathbf{U} \mathbf{U}^{-1} = \mathbf{I}]
    \\
    & = \mathbf{U}^{H} \mathbf{A}^{H} \mathbf{A} \mathbf{U}.
    \end{aligned}
    $$
    
    Since $\mathbf{A}$ is a normal matrix,
    
    $$
    \mathbf{A} \mathbf{A}^{H} = \mathbf{A}^{H} \mathbf{A}.
    $$
    
    Continue from the derivation above,
    
    $$
    \begin{aligned}
    \mathbf{B}^{H} \mathbf{B}
    & = \mathbf{U}^{H} \mathbf{A} \mathbf{A}^{H} \mathbf{U}
    \\
    & = \mathbf{U}^{H} \mathbf{A}^{H} \mathbf{A} \mathbf{U}
    \\
    & = \mathbf{U}^{H} \mathbf{A}^{H} \mathbf{I} \mathbf{A} \mathbf{U}
    \\
    & = \mathbf{U}^{H} \mathbf{A}^{H} \mathbf{U} \mathbf{U}^{H} \mathbf{A} \mathbf{U}
    \\
    & = \mathbf{U} \mathbf{A}^{H} \mathbf{U}^{H} \mathbf{U}^{H} \mathbf{A} \mathbf{U}
    & [TODO]
    \\
    & = (\mathbf{U}^{H} \mathbf{A}^{H} \mathbf{U})^{H} (\mathbf{U}^{H} \mathbf{A} \mathbf{U})
    \\
    & = \mathbf{B} \mathbf{B}^{H}.
    \end{aligned}
    $$
    
  :::

## Unitary diagonalization

A matrix $\mathbf{A} \in \mathbb{C}^{n \times n}$ is normal if and only if $\mathbf{A}$ is unitarily similar to a diagonal matrix

$$
\mathbf{A}^{H} \mathbf{A} = \mathbf{A} \mathbf{A}^{H} \iff \mathbf{U}^{-1} \mathbf{A} \mathbf{U} = \mathbf{\Lambda}.
$$

where $\mathbf{U}$ is a unitary matrix and $\mathbf{\Lambda}$ is a diagonal matrix.

::: {.callout-note collapse="true" title="Proof"}

We first prove that 

$$
\mathbf{A}^{H} \mathbf{A} = \mathbf{A} \mathbf{A}^{H} \Rightarrow \mathbf{U}^{-1} \mathbf{A} \mathbf{U} = \mathbf{\Lambda}.
$$

TODO

Then we prove that 

$$
\mathbf{U}^{-1} \mathbf{A} \mathbf{U} = \mathbf{\Lambda} \Rightarrow \mathbf{A}^{H} \mathbf{A} = \mathbf{A} \mathbf{A}^{H}.
$$

According to the [property of unitary matrices](normal-matrices-property-3), 
unitary similarity preserves normality. 

Also according to [property of unitary matrices](normal-matrices-property-2),
all diagonal matrices are normal. 

Thus, $\mathbf{A}$ is normal because $\mathbf{A}$ is unitarily similar to a diagonal matrix, which is always normal.

:::

Since the columns of $\mathbf{U}$ are eigenvectors of $\mathbf{A}$ and are orthonormal to each other
the columns of $\mathbf{U}$ must be a complete orthonormal set of eigenvectors for $\mathbf{A}$,
and the diagonal entries of $\mathbf{\Lambda}$ are the associated eigenvalues.

## Hermitian (symmetric) matrices 

A square complex (real) matrix $\mathbf{A}$ is hermitian (symmetric) if and only if 

$$
\mathbf{A}^{H} = \mathbf{A},
$$

which implies **a hermitian (symmetric) matrix is a normal matrix**. 

All eigenvalues of Hermitian matrices are real.

::: {.callout-note collapse="true" title="Proof"}

Suppose $(\lambda, \mathbf{v})$ is a eigenpair for the Hermitian matrix $\mathbf{A}$.

$$
\mathbf{A} \mathbf{v} = \lambda \mathbf{v}.
$$

Multiplying both sides by $\mathbf{v}^{H}$ on the left to get,

$$
\begin{aligned}
\mathbf{A} \mathbf{v} 
& = \lambda \mathbf{v}
\\
\mathbf{v}^{H} \mathbf{A} \mathbf{v} 
& = \lambda \mathbf{v}^{H} \mathbf{v}
\\
\mathbf{v}^{H} \mathbf{A} \mathbf{v} 
& = \lambda \lVert \mathbf{v} \rVert^{2}.
\\
\end{aligned}
$$

Alternatively we can take the transpose conjugate of both sides,
and then multiply both sides by $\mathbf{v}$ on the right to get,

$$
\begin{aligned}
\mathbf{A} \mathbf{v} 
& = \lambda \mathbf{v}
\\
(\mathbf{A} \mathbf{v})^{H}
& = (\lambda \mathbf{v})^{H}
\\
\mathbf{v}^{H} \mathbf{A}^{H}
& = \lambda^{*} \mathbf{v}^{H}
\\
\mathbf{v}^{H} \mathbf{A}^{H} \mathbf{v}
& = \lambda^{*} \mathbf{v}^{H} \mathbf{v}
\\
\mathbf{v}^{H} \mathbf{A}^{H} \mathbf{v}
& = \lambda^{*} \lVert \mathbf{v} \rVert^{2}
\\
\end{aligned}
$$

Since $\mathbf{A}$ is a hermitian matrix 

$$
\begin{aligned}
\mathbf{v}^{H} \mathbf{A} \mathbf{v} 
& = \mathbf{v}^{H} \mathbf{A}^{H} \mathbf{v}
\\
\lambda \lVert \mathbf{v} \rVert^{2}
& = \lambda^{*} \lVert \mathbf{v} \rVert^{2}
\\
\lambda 
& = \lambda^{*},
\end{aligned}
$$

which means $\lambda$ is a real number. 

:::

## Rayleigh quotient 

Given a Hermitian matrix $\mathbf{M} \in \mathbb{C}^{n \times n}$,
the Rayleigh quotient is a function $R_{\mathbf{M}} (\mathbf{x}): \mathbb{C}^{n} \setminus \{ 0 \} \rightarrow \mathbb{R}$

$$
R_{\mathbf{M}} (\mathbf{x}) = \frac{
    \mathbf{x}^{H} \mathbf{M} \mathbf{x}
}{
    \mathbf{x}^{H} \mathbf{x}
}
$$

that takes a nonzero vector $\mathbf{x}$ and returns a real number.

Since the Hermitian matrix $\mathbf{M}$ has all real eigenvalues,
they can be ordered.
Suppose $\lambda_{1}, \dots, \lambda_{n}$ is the eigenvalues in descending orders. 

Then, given a Hermitian matrix,
its Rayleigh quotient is upper bounded and lower bounded by maximum and minimum eigenvalues of $\mathbf{M}$ respectively,

$$
\lambda_{1} \geq R_{\mathbf{M}} (\mathbf{x}) \geq \lambda_{n}.
$$

That is, 

$$
\lambda_{1} = \max_{\mathbf{x} \neq 0} \frac{
    \mathbf{x}^{H} \mathbf{M} \mathbf{x}
}{
    \mathbf{x}^{H} \mathbf{x}
},
$$

$$
\lambda_{n} = \min_{\mathbf{x} \neq 0} \frac{
    \mathbf{x}^{H} \mathbf{M} \mathbf{x}
}{
    \mathbf{x}^{H} \mathbf{x}
}.
$$

::: {.callout-note collapse="true" title="Proof"}

Since $\mathbf{M}$ is a Hermitian matrix,
we can expand it using unitary diagonalization:

$$
\begin{aligned}
\frac{
    \mathbf{x}^{H} \mathbf{M} \mathbf{x}
}{
    \mathbf{x}^{H} \mathbf{x}
}
& = \frac{
    \mathbf{x}^{H} \mathbf{U}^{H} \mathbf{\Lambda} \mathbf{U} \mathbf{x}
}{
    \mathbf{x}^{H} \mathbf{x}
}
\\
& = \frac{
    \mathbf{y}^{H} \mathbf{\Lambda} \mathbf{y}
}{
    \mathbf{x}^{H} \mathbf{x}
}
&
[\mathbf{y} = \mathbf{U} \mathbf{x}].
\end{aligned}
$$

Since $\mathbf{U}$ is a unitary matrix,
according to the [property of the unitary matrix](unitary-matrix-property-3),

$$
\mathbf{y}^{H} \mathbf{y} = \mathbf{x}^{H} \mathbf{x}.
$$

Thus,

$$
\begin{aligned}
\frac{
    \mathbf{y}^{H} \mathbf{\Lambda} \mathbf{y}
}{
    \mathbf{x}^{H} \mathbf{x}
}
& = 
\frac{
    \mathbf{y}^{H} \mathbf{\Lambda} \mathbf{y}
}{
    \mathbf{y}^{H} \mathbf{y}
}
\\
& = 
\frac{
    \sum_{i=1}^{n} \lambda_{i} y_{i}^{2}
}{
    \sum_{i=1}^{n} y_{i}^{2}
}.
\end{aligned}
$$

Since $\lambda_{1} \geq \lambda_{i} \geq \lambda_{n}, \forall i = 1, \dots, n$, 

$$
\lambda_{1} 
= 
\lambda_{1}
\frac{
    \sum_{i=1}^{n} y_{i}^{2}
}{
    \sum_{i=1}^{n} y_{i}^{2}
}
=
\frac{
    \sum_{i=1}^{n} \lambda_{1} y_{i}^{2}
}{
    \sum_{i=1}^{n} y_{i}^{2}
}
\geq 
\frac{
    \sum_{i=1}^{n} \lambda_{i} y_{i}^{2}
}{
    \sum_{i=1}^{n} y_{i}^{2}
},
$$

$$
\lambda_{n}
=
\lambda_{n}
\frac{
    \sum_{i=1}^{n} y_{i}^{2}
}{
    \sum_{i=1}^{n} y_{i}^{2}
}
= 
\frac{
    \sum_{i=1}^{n} \lambda_{n} y_{i}^{2}
}{
    \sum_{i=1}^{n} y_{i}^{2}
} 
\leq
\frac{
    \sum_{i=1}^{n} \lambda_{i} y_{i}^{2}
}{
    \sum_{i=1}^{n} y_{i}^{2}
}.
$$

:::

# Positive Definite Matrices 

Given a *Hermitian matrix* $\mathbf{A} \in \mathbb{C}^{n \times n}$,
it is **positive definite** if and only if 

$$
\mathbf{x}^{H} \mathbf{A} \mathbf{x} > 0,
$$

for all nonzero vectors $\mathbf{x} \in \mathbb{C}^{n}$,
and it is **positive semi-definite** if and only if 

$$
\mathbf{x}^{H} \mathbf{A} \mathbf{x} \geq 0,
$$

for all vectors $\mathbf{x}$.

## Properties of definite matrices

(definite-matrices-property-1)=

- Positive definite matrix always has full rank.

  ::: {.callout-note collapse="true" title="Proof"}
    
    We prove by contradiction. 
    
    Suppose a positive definite matrix $\mathbf{A}$ does NOT have full rank, 
    which means that there exists at least one non-zero vector $\mathbf{x} \in N (\mathbf{A})$ such that 
    
    $$
    \mathbf{A} \mathbf{x} = 0.
    $$
    
    Then, multiplying both sides by $\mathbf{x}^{H}$,
    
    $$
    \mathbf{x}^{H} \mathbf{A} \mathbf{x} = 0.
    $$
    
    which contradicts to the fact that $\mathbf{A}$ is positive definite. 
    
    Thus, positive definite matrix always has full rank.

  :::

(definite-matrices-property-2)=

- A matrix $\mathbf{A}$ is positive definite (semi-definite) if and only if its eigenvalues are positive (non-negative).
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    We first prove that a matrix $\mathbf{A}$ is positive definite (semi-definite) if its all eigenvalues are positive (non-negative). 
    
    Since $\mathbf{A}$ is a Hermitian matrix, 
    it can be unitarily diagonalized:
    
    $$
    \mathbf{A} = \mathbf{U} \mathbf{\Lambda} \mathbf{U}^{H},
    $$
    
    where the columns of $\mathbf{U}$ contains the orthonormal eigenvectors of $\mathbf{A}$ 
    and diagonal of $\mathbf{\Lambda}$ has the corresponding real eigenvalues.
    
    Since we are told all eigenvalues are positive or non-negative(TODO), 
    
    $$
    \mathbf{\Lambda} = \mathbf{\Lambda}^{\frac{1}{2}} \mathbf{\Lambda}^{\frac{1}{2}} 
    = \mathbf{\Lambda}^{\frac{1}{2}} (\mathbf{\Lambda}^{\frac{1}{2}})^{H}
    $$
    
    Thus, 
    
    $$
    \begin{aligned}
    \mathbf{A} 
    & = \mathbf{U} \mathbf{\Lambda} \mathbf{U}^{H}
    \\
    & = \mathbf{U} \mathbf{\Lambda}^{\frac{1}{2}} (\mathbf{\Lambda}^{\frac{1}{2}})^{H} \mathbf{U}^{H}
    \\
    & = \mathbf{U} \mathbf{\Lambda}^{\frac{1}{2}} (\mathbf{U} \mathbf{\Lambda}^{\frac{1}{2}})^{H}
    \\
    \end{aligned}
    $$
    
    Multiplying $\mathbf{A}$ with $\mathbf{x}$ to get
    
    $$
    \begin{aligned}
    \mathbf{x}^{H} \mathbf{A} \mathbf{x}
    & = \mathbf{x}^{H} \mathbf{U} \mathbf{\Lambda}^{\frac{1}{2}} (\mathbf{\Lambda}^{\frac{1}{2}} \mathbf{U})^{H} \mathbf{x}
    \\
    & = \mathbf{x}^{H} \mathbf{U} \mathbf{\Lambda}^{\frac{1}{2}} (\mathbf{x}^{H} \mathbf{U} \mathbf{\Lambda}^{\frac{1}{2}})^{H}
    \\
    & = \lVert \mathbf{x}^{H} \mathbf{U} \mathbf{\Lambda}^{\frac{1}{2}} \rVert^{2} 
    & [\mathbf{x}^{H} \mathbf{U} \mathbf{\Lambda}^{\frac{1}{2}} \in \mathbb{C}^{n}].
    \\
    \end{aligned}
    $$
    
    Since $\lVert \mathbf{x}^{H} \mathbf{U} \mathbf{\Lambda}^{\frac{1}{2}} \rVert^{2}$ is non-negative for any vector $\mathbf{x}$, 
    the matrix $\mathbf{A}$ is positive semi-definite.
    
    If all eigenvalues are positive,
    there is no zero in $\mathbf{\Lambda}$.
    Since $\mathbf{\Lambda}^{\frac{1}{2}}$ is a diagonal matrix, 
    the matrix $\mathbf{U} \mathbf{\Lambda}^{\frac{1}{2}}$ has scaled columns of $\mathbf{U}$. 
    Since $\mathbf{U}$ is a unitary matrix, 
    its columns are all linearly independent and thus $\mathbf{U} \mathbf{\Lambda}^{\frac{1}{2}}$ also have linearly independent columns. 
    Thus, $\mathbf{U} \mathbf{\Lambda}^{\frac{1}{2}}$ has full rank and 
    
    $$
    N (\mathbf{U} \mathbf{\Lambda}^{\frac{1}{2}}) = \{ 0 \}.
    $$
    
    Thus,
    $\lVert \mathbf{x}^{H} \mathbf{U} \mathbf{\Lambda}^{\frac{1}{2}} \rVert^{2} > 0$ for any non-zero vector $\mathbf{x}$.
    Therefore,
    the matrix $\mathbf{A}$ is positive definite.
    
    Then we prove that all eigenvalues of positive definite (semi-definite) matrices are positive (non-negative). 
    
    Consider any eigenpair $(\lambda, \mathbf{v})$ of $\mathbf{A}$.
    
    Since $\mathbf{v}$ is non-zero by the definition of eigenvector, 
    we have
    
    $$
    \begin{aligned}
    \mathbf{A} \mathbf{v} 
    & = \lambda \mathbf{v}
    \\
    \mathbf{v}^{H} \mathbf{A} \mathbf{v} 
    & = \lambda \mathbf{v}^{H} \mathbf{v}
    \\
    \mathbf{v}^{H} \mathbf{A} \mathbf{v} 
    & = \lambda \lVert \mathbf{v} \rVert^{2}
    \\
    \lambda 
    & = \frac{
        \mathbf{v}^{H} \mathbf{A} \mathbf{v} 
    }{
        \lVert \mathbf{v} \rVert^{2}
    }
    \end{aligned}
    $$
    
    Since $\mathbf{A}$ is positive definite (semi-definite), 
    
    $$ 
    \mathbf{v}^{H} \mathbf{A} \mathbf{v} > 0 \quad (\mathbf{v}^{H} \mathbf{A} \mathbf{v} \geq 0),
    $$
    
    which means 
    
    $$
    \lambda > 0 \quad (\lambda \geq 0).
    $$
    
  :::

- TODO $\mathbf{A} = \mathbf{B}^{H} \mathbf{B}$
