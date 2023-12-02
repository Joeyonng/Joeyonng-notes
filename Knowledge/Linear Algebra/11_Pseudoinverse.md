---
title: Pseudoinverse
---

# Pseudoinverse

A generalized inverse for any matrix can be defined using URV factorization or SVD. 

Given a URV factorization of matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$

$$
\mathbf{A} = \mathbf{U} 
\begin{bmatrix}
\mathbf{C} & 0 \\
0 & 0 \\
\end{bmatrix}
\mathbf{V}^{T}
$$

the pseudoinverse of $\mathbf{A}$ is defined as 

$$
\mathbf{A}^{\dagger} = \mathbf{V} 
\begin{bmatrix}
\mathbf{C}^{-1} & 0 \\
0 & 0 \\
\end{bmatrix}
\mathbf{U}^{T}.
$$

The pseudoinverse of matrix $\mathbf{A}$ can also be stated as a matrix $\mathbf{A}^{\dagger}$ that satisfies the following:

$$
\mathbf{A} \mathbf{A}^{\dagger} \mathbf{A} = \mathbf{A}, 
$$ 

$$
\mathbf{A}^{\dagger} \mathbf{A} \mathbf{A}^{\dagger} = \mathbf{A}^{\dagger},
$$

where $\mathbf{A} \mathbf{A}^{\dagger}$ and $\mathbf{A}^{\dagger} \mathbf{A}$ are symmetric matrix:

$$
(\mathbf{A} \mathbf{A}^{\dagger})^{T} = \mathbf{A} \mathbf{A}^{\dagger}, 
$$ 

$$
(\mathbf{A}^{\dagger} \mathbf{A})^{T} = \mathbf{A}^{\dagger} \mathbf{A}.
$$

## Properties of pseudoinverse 

- The pseudoinverse $\mathbf{A}^{\dagger}$ of $\mathbf{A}$ is unique. 

  ::: {.callout-note collapse="true" title="Proof"}

    We prove by contradiction. 
    Suppose that there are 2 pseudoinverse $\mathbf{B}, \mathbf{C}$ for $\mathbf{A}$. 

    $$
    \begin{aligned}
    \mathbf{A} \mathbf{B} 
    & = (\mathbf{A} \mathbf{C} \mathbf{A}) \mathbf{B}
    & [\mathbf{A} \mathbf{A}^{\dagger} \mathbf{A} = \mathbf{A}]
    \\
    & = (\mathbf{C}^{T} \mathbf{A}^{T}) (\mathbf{B}^{T} \mathbf{A}^{T})
    & [(\mathbf{A} \mathbf{A}^{\dagger})^{T} = \mathbf{A} \mathbf{A}^{\dagger}]
    \\
    & = \mathbf{C}^{T} (\mathbf{A}^{T} \mathbf{B}^{T} \mathbf{A}^{T})
    \\
    & = \mathbf{C}^{T} (\mathbf{A} \mathbf{B} \mathbf{A})^{T}
    \\
    & = \mathbf{C}^{T} \mathbf{A}^{T}
    \\
    & = \mathbf{A} \mathbf{C}
    \\
    \end{aligned}
    $$

    $$
    \begin{aligned}
    \mathbf{B} \mathbf{A} 
    & = \mathbf{B} (\mathbf{A} \mathbf{C} \mathbf{A})
    & [\mathbf{A} \mathbf{A}^{\dagger} \mathbf{A} = \mathbf{A}]
    \\
    & = (\mathbf{A}^{T} \mathbf{B}^{T}) (\mathbf{A}^{T} \mathbf{C}^{T})
    & [(\mathbf{A} \mathbf{A}^{\dagger})^{T} = \mathbf{A} \mathbf{A}^{\dagger}]
    \\
    & = (\mathbf{A}^{T} \mathbf{B}^{T} \mathbf{A}^{T}) \mathbf{C}^{T}
    \\
    & = (\mathbf{A} \mathbf{B} \mathbf{A})^{T} \mathbf{C}^{T}
    \\
    & = \mathbf{A}^{T} \mathbf{C}^{T}
    \\
    & = \mathbf{C} \mathbf{A}
    \\
    \end{aligned}
    $$

    Thus, 

    $$
    \begin{aligned}
    \mathbf{B} 
    & = \mathbf{B} \mathbf{A} \mathbf{B} 
    & [\mathbf{A}^{\dagger} \mathbf{A} \mathbf{A}^{\dagger} = \mathbf{A}^{\dagger}]
    \\
    & = \mathbf{C} \mathbf{A} \mathbf{B}
    & [\mathbf{C} \mathbf{A} = \mathbf{B} \mathbf{A}]
    \\
    & = \mathbf{C} \mathbf{A} \mathbf{C}
    & [\mathbf{A} \mathbf{B} = \mathbf{A} \mathbf{C}]
    \\
    & = \mathbf{C}
    \end{aligned}
    $$
    
  :::

- Given a full rank matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$.

    If $m > n$,
    the left inverse of $\mathbf{A}$ is the pseudoinverse of $\mathbf{A}$ and is written as 

    $$
    (\mathbf{A}^{T} \mathbf{A})^{-1} \mathbf{A}^{T}.
    $$

    If $m < n$,
    the right inverse of $\mathbf{A}$ is the pseudoinverse of $\mathbf{A}$ and is written as 

    $$
    \mathbf{A}^{T} (\mathbf{A} \mathbf{A}^{T})^{-1} .
    $$

    If $m = n$,
    the inverse of $\mathbf{A}$ is the pseudoinverse of $\mathbf{A}$.

  ::: {.callout-note collapse="true" title="Proof"}

    We first prove that $(\mathbf{A}^{T} \mathbf{A})^{-1}$ (when $m > n$) and $(\mathbf{A} \mathbf{A}^{T})^{-1}$ (when $m < n$) exist. 

    Since $\mathbf{A}$ is a full rank matrix, 

    $$
    \text{rank} (\mathbf{A}) = \min (m, n).
    $$

    According to the [property of rank](rank-property-6), 
    
    $$
    \text{rank} (\mathbf{A}^{T} \mathbf{A}) = \text{rank} (\mathbf{A} \mathbf{A}^{T}) = \text{rank} (\mathbf{A}) = \text{min} (m, n).
    $$

    Thus, $\mathbf{A}^{T} \mathbf{A}$ ($m > n$) and $\mathbf{A} \mathbf{A}^{T}$ ($m < n$) are non-singular. 
    
    - if $m > n$, $\mathbf{A}^{T} \mathbf{A} \in \mathbb{R}^{n \times n}$ is full rank because $\text{rank} (\mathbf{A}^{T} \mathbf{A}) = \min (m, n) = n$,

    - if $m < n$, $\mathbf{A} \mathbf{A}^{T} \in \mathbb{R}^{m \times m}$ is full rank because $\text{rank} (\mathbf{A}^{T} \mathbf{A}) = \min (m, n) = m$.

    we prove that $(\mathbf{A}^{T} \mathbf{A})^{-1} \mathbf{A}^{T}$ when ($m > n$) is the pseudoinverse of $\mathbf{A}$.

    $$
    \mathbf{A} \mathbf{A}^{\dagger} \mathbf{A} = \mathbf{A} (\mathbf{A}^{T} \mathbf{A})^{-1} \mathbf{A}^{T} \mathbf{A} = \mathbf{A} \mathbf{I}_{n \times n} = \mathbf{A}
    $$

    $$
    \mathbf{A}^{\dagger} \mathbf{A} \mathbf{A}^{\dagger} = (\mathbf{A}^{T} \mathbf{A})^{-1} \mathbf{A}^{T} \mathbf{A} (\mathbf{A}^{T} \mathbf{A})^{-1} \mathbf{A}^{T} = \mathbf{I}_{n \times n} \mathbf{A}^{\dagger} = \mathbf{A}^{\dagger}
    $$

    $$
    \mathbf{A}^{\dagger} \mathbf{A} = (\mathbf{A}^{T} \mathbf{A})^{-1} \mathbf{A}^{T} \mathbf{A} = \mathbf{I}_{n \times n} = \mathbf{A}^{T} \mathbf{A} (\mathbf{A}^{T} \mathbf{A})^{-1} = \mathbf{A}^{T} (\mathbf{A}^{\dagger})^{\mathbf{T}}= (\mathbf{A}^{\dagger} \mathbf{A})^{T}
    $$

    $$
    \mathbf{A} \mathbf{A}^{\dagger} = \mathbf{A} (\mathbf{A}^{T} \mathbf{A})^{-1} \mathbf{A}^{T} = (\mathbf{A}^{\dagger})^{T} \mathbf{A}^{T} = (\mathbf{A} \mathbf{A}^{\dagger})^{T}
    $$

    The case that $\mathbf{A}^{T} (\mathbf{A} \mathbf{A}^{T})^{-1}$ when ($m < n$) can be proved similarly.

    Then we prove that $(\mathbf{A}^{T} \mathbf{A})^{-1} \mathbf{A}^{T}$ is the left inverse of $\mathbf{A}$ when $m > n$: 

    $$
    \mathbf{A}^{\dagger} \mathbf{A} = (\mathbf{A}^{T} \mathbf{A})^{-1} \mathbf{A}^{T} \mathbf{A} = \mathbf{I}_{n \times n}.
    $$

    The case that $\mathbf{A}^{T} (\mathbf{A} \mathbf{A}^{T})^{-1}$ is the right inverse of $\mathbf{A}$ when $m < n$ can be proved similarly.
    
    Thus we have proved that $(\mathbf{A}^{T} \mathbf{A})^{-1} \mathbf{A}^{T}$ ($m > n$) and $\mathbf{A}^{T} (\mathbf{A} \mathbf{A}^{T})^{-1}$ ($m < n$) are the left and right inverse of $\mathbf{A}$. 

    When $m = n$, 
    we have both

    $$
    \mathbf{A} \mathbf{A}^{-1} \mathbf{A} = \mathbf{A},
    $$

    $$
    \mathbf{A} \mathbf{A}^{\dagger} \mathbf{A} = \mathbf{A},
    $$

    but since $\mathbf{A}^{-1}$ and $\mathbf{A}^{\dagger}$ are both unique, 
    it must be that 

    $$
    \mathbf{A}^{-1} = \mathbf{A}^{\dagger}.
    $$
    
  :::
