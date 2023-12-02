---
title: Similarity and Diagonalization
---

# Similarity

Two matrices $\mathbf{A}, \mathbf{B} \in \mathbb{C}^{n \times n}$ are similar if there exists a non-singular matrix $\mathbf{P}$ such that 

$$
\mathbf{P}^{-1} \mathbf{A} \mathbf{P} = \mathbf{B},
$$

$$
 \mathbf{A} = \mathbf{P} \mathbf{B} \mathbf{P}^{-1}.
$$

Similar matrices have the same eigenvalues. 

::: {.callout-note collapse="true" title="Proof"}

Suppose $\lambda_{1}, \dots, \lambda_{n}$ are eigenvalues of $\mathbf{B}$. 

$$
\begin{aligned}
\text{det} (\mathbf{B} - \lambda \mathbf{I}) 
& = 0
\\
\text{det} (\mathbf{P}^{-1} \mathbf{A} \mathbf{P} - \lambda \mathbf{I}) 
& = 0
\\
\text{det} (\mathbf{P}^{-1} \mathbf{A} \mathbf{P} - \lambda \mathbf{P}^{-1} \mathbf{P}) 
& = 0
\\
\text{det} (\mathbf{P}^{-1} (\mathbf{A} - \lambda \mathbf{I}) \mathbf{P}) 
& = 0
\\
\text{det} (\mathbf{P}^{-1}) \text{det} (\mathbf{A} - \lambda \mathbf{I}) \text{det} (\mathbf{P}) 
& = 0
\\
\text{det} (\mathbf{P}^{-1}) \text{det} (\mathbf{P}) \text{det} (\mathbf{A} - \lambda \mathbf{I})
& = 0
\\
\text{det} (\mathbf{A} - \lambda \mathbf{I})
& = 0
& [\text{det} (\mathbf{P}^{-1}) = \frac{1}{\text{det} (\mathbf{P})}]
\\
\end{aligned}
$$

:::

## Unitarily similar

Two matrices $\mathbf{A}, \mathbf{B} \in \mathbb{C}^{n \times n}$ are unitarily similar if there exists an unitary matrix $\mathbf{U}$ such that 

$$
\mathbf{U}^{-1} \mathbf{A} \mathbf{U} = \mathbf{B},
$$

which, according to the [property of unitary matrix](unitary-matrix-property-1), can also be written as 

$$
\mathbf{U}^{H} \mathbf{A} \mathbf{U} = \mathbf{B}.
$$

# Diagonalization

A square matrix $\mathbf{A} \in \mathbb{C}^{n \times n}$ is diagonalizable if $\mathbf{A}$ is similar to a diagonal matrix:

$$
\mathbf{A} = \mathbf{P} \Lambda \mathbf{P}^{-1}
$$

where $\Lambda$ is a diagonal matrix.

## Diagonalization and eigensystems

$\mathbf{A}$ is diagonalizable if and only if $\mathbf{A}$ has $n$ linearly independent eigenvectors. 
That is,

$$
\mathbf{A} = \mathbf{P} \mathbf{\Lambda} \mathbf{P}^{-1}
$$ 

or 

$$
\mathbf{P}^{-1} \mathbf{A} \mathbf{P} = \mathbf{\Lambda},
$$ 

where 

- the columns of $\mathbf{P} \in \mathbb{C}^{n \times n}$ are $n$ linearly independent eigenvectors,

- the diagonal values of $\mathbf{\Lambda}$ are corresponding eigenvalues. 

::: {.callout-note collapse="true" title="Proof"}

We first prove that If $\mathbf{A}$ is diagonalizable,
then $\mathbf{A}$ has $n$ linearly independent eigenvectors.

First note that

$$
\begin{aligned}
\mathbf{A} 
& = \mathbf{P} \mathbf{\Lambda} \mathbf{P}^{-1}
\\
\mathbf{A} \mathbf{P}
& = \mathbf{P} \mathbf{\Lambda}
\\
\end{aligned}
$$

Since $\mathbf{\Lambda}$ is a diagonal matrix with $\lambda_{1}, \dots, \lambda_{n}$ on its diagonal,

$$
\mathbf{A} \mathbf{P}_{*, i} = \mathbf{P}_{*, i} \lambda_{i} = \lambda_{i} \mathbf{P}_{*, i}.
$$

Thus, $(\lambda, \mathbf{P}_{*, i})$ is an eigenpair of $\mathbf{A}$,
and $\mathbf{A}$ has $n$ such eigenpairs.

Since $\mathbf{P}$ is non-singular (full-rank), 
$\mathbf{P}$ has independent columns. 
Thus, $\mathbf{A}$ has $n$ independent eigenvectors.

Then we prove that if $\mathbf{A}$ has $n$ linearly independent eigenvectors,
then $\mathbf{A}$ is diagonalizable.

Assume the columns of $\mathbf{P} \in \mathbf{C}^{n \times n}$ are the eigenvectors of $\mathbf{A}$,
and $\lambda_{1}, \dots, \lambda_{n}$ are corresponding eigenvalues,

$$
\mathbf{A} \mathbf{P}_{*, i} = \lambda_{i} \mathbf{P}_{*, i} \quad \forall i = 1, \dots, n.
$$

By rewriting $\lambda_{1}, \dots, \lambda_{n}$ as diagonals for the diagonal matrix $\mathbf{\Lambda}$,

$$
\mathbf{A} \mathbf{P} = \mathbf{P} \mathbf{\Lambda}.
$$

Since the columns of the $\mathbf{P}$ are linearly independent, 
$\mathbf{P}$ has full rank and thus there exists the inverse of $\mathbf{P}$

$$
\begin{aligned}
\mathbf{A} \mathbf{P} 
& = \mathbf{P} \mathbf{\Lambda}
\\
\mathbf{P}^{-1} \mathbf{A} \mathbf{P} 
& = \mathbf{\Lambda}
\end{aligned}
$$

which shows that $\mathbf{A}$ is similar to $\mathbf{\Lambda}$ and thus is diagonalizable.

:::

## Diagonalizability and multiplicities

TODO
