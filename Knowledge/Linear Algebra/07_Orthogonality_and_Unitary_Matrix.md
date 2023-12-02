---
title: Orthogonality and Unitary Matrix
---

# Orthogonality

A set of non-zero vectors $v_{1}, \dots, v_{k}$ are orthogonal if 

$$
\langle v_{i}, v_{j} \rangle = 0, \quad \forall i \neq j.
$$

## Properties of orthogonality

If $v_{1}, \dots, v_{k}$ are orthogonal vectors, 

(orthogonality-property-1)=

- $v_{1}, \dots, v_{k}$ are also linearly independent.

  ::: {.callout-note collapse="true" title="Proof"}
    
    TODO

  :::

(orthogonality-property-2)=

- Suppose $\mathcal{S}$ is a subspace with $\text{dim} (S) = n$ 
    and $v_{1}, \dots, v_{k} \in \mathcal{S}$, 
    then the set $\{ v_{1}, \dots, v_{k} \}$ forms a basis of $\mathcal{S}$.
    Then, $\{ v_{1}, \dots, v_{k} \}$ is an orthogonal basis of $\mathcal{S}$.
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    TODO

  :::

## Representing vectors using orthogonal basis

Suppose $\mathcal{S}$ is a subspace and $\{ v_{1}, \dots, v_{n} \}$ is an orthogonal basis of $\mathcal{S}$, 
any vector $v \in \mathcal{S}$ can be represented using $\{ v_{1}, \dots, v_{n} \}$:

$$
v = \sum_{i=1}^{n} \alpha_{i} v_{i},
$$

where 

$$
\alpha_{i} = 
\frac{
    \langle v, v_{i} \rangle
}{
    \lVert v_{i} \rVert_{ip}^{2}
}
$$

::: {.callout-note collapse="true" title="Proof"}

TODO

:::

## Orthonormal vectors

A set of vectors $v_{1}, \dots, v_{k}$ are **orthonormal** if all vectors in the set are orthogonal to each other,
and each vector has the inner product norm of 1.

If $\mathbf{a}_{1}, \dots, \mathbf{a}_{k} \in \mathbb{C}^{n}$ and are the columns of the matrix $\mathbf{A} \in \mathbb{C}^{n \times k}$, 
then $\mathbf{A}$ has orthonormal columns and thus

$$ 
\mathbf{A}^{H} \mathbf{A} = \mathbf{I}.
$$

# Unitary matrix

A *square* complex (real) matrix $\mathbf{U}$ is **unitary (orthogonal)** if and only if $\mathbf{U}$ has orthonormal columns.

## Properties of unitary matrix

(unitary-matrix-property-1)=

- The matrix $\mathbf{U}$ is unitary if and only if $\mathbf{U}^{H} = \mathbf{U}^{-1}$.

  ::: {.callout-note collapse="true" title="Proof"}
    
    By definition, $\mathbf{U}$ has orthogonal columns and thus linearly independent columns. 
    By the [rank property](rank-property-5), $\mathbf{U}$ has a unique inverse matrix $\mathbf{U}^{-1}$ such that
    
    $$
    \mathbf{U}^{-1} \mathbf{U} = \mathbf{I}_{n \times n}.
    $$
    
    Since by definition we know 
    
    $$
    \mathbf{U}^{H} \mathbf{U} = \mathbf{I}_{n \times n},
    $$
    
    then it must follow that 
    
    $$
    \mathbf{U}^{H} = \mathbf{U}^{-1}.
    $$
    
    The reverse can be proved backward following the procedure above. 

  :::

(unitary-matrix-property-2)=

- The matrix $\mathbf{U}$ is unitary if and only if $\mathbf{U}^{H} \mathbf{U} = \mathbf{U} \mathbf{U}^{H} = \mathbf{I}_{n \times n}.$

  ::: {.callout-note collapse="true" title="Proof"}
    
    Following the [unitary matrix property](unitary-matrix-property-1), 
    the inverse $\mathbf{U}^{-1}$ can be both left and right inverse
    
    $$
    \mathbf{U}^{-1} \mathbf{U} = \mathbf{U} \mathbf{U}^{-1} = \mathbf{I}. 
    $$
    
    Replacing $\mathbf{U}^{-1}$ with $\mathbf{U}^{H}$, we have the results:
    
    $$
    \mathbf{U}^{H} \mathbf{U} = \mathbf{U} \mathbf{U}^{H} = \mathbf{I}. 
    $$

  :::

(unitary-matrix-property-3)=

- The matrix $\mathbf{U}$ is unitary if and only if $\mathbf{U} \mathbf{x}$ doesn't change the length of $\mathbf{x}$:

    $$
    \lVert \mathbf{U} \mathbf{x} \rVert = \lVert \mathbf{x} \rVert.
    $$
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    $$
    \begin{aligned}
    \lVert \mathbf{U} \mathbf{x} \rVert 
    & = \sqrt{\lVert \mathbf{U} \mathbf{x} \rVert^{2}}
    \\
    & = \sqrt{\mathbf{x}^{H} \mathbf{U}^{H} \mathbf{U} \mathbf{x}}
    \\
    & = \sqrt{\mathbf{x}^{H} \mathbf{I} \mathbf{x}}
    & [\mathbf{U}^{H} \mathbf{U} = \mathbf{I}]
    \\
    & = \sqrt{\mathbf{x}^{H} \mathbf{x}}
    \\
    & = \sqrt{\lVert \mathbf{x} \rVert^{2}}
    \\
    & = \lVert \mathbf{x} \rVert
    \end{aligned}
    $$

  :::
