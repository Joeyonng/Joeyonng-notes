---
title: Determinants and Eigensystems
---

# Determinants

For an matrix $\mathbf{A} \in \mathbb{C}^{n \times n}$, 
the determinant of A is defined to be the scalar

$$
\text{det} (\mathbf{A}) = \lvert \mathbf{A} \rvert = \sum_{p \in \mathcal{P}} \sigma (p) \prod_{i=1}^{n} a_{i, p_{i}}
$$

where 

- $\mathcal{P}$ is the set of all permutations of the set of $(1, 2, \dots, n)$,

- $\sigma (p)$ is the parity of the permutation $p$. 

Note that each term a1p1a2p2 · · · anpn in (6.1.1) contains exactly one entry from each row and each column of A. 

# Eigensystems

For a matrix $\mathbf{A} \in \mathbb{C}^{n \times n}$, 
$(\lambda, \mathbf{x})$ is an **eigenpair** for $\mathbf{A}$ if 

$$
\mathbf{A} \mathbf{x} = \lambda \mathbf{x}
$$

where 

- the scalar $\lambda$ is an **eigenvalue** for $\mathbf{A}$,

- the non-zero vector $\mathbf{x}$ is an **eigenvector** associated with $\lambda$ for $\mathbf{A}$.

The set of all distinct eigenvalues, denoted by $\sigma (A)$, is the **spectrum** of A

## Eigenspace

Given a eigenvalue $\lambda$, 

$$
\begin{aligned}
\mathbf{A} \mathbf{x} 
& = \lambda \mathbf{x}
\\
(\mathbf{A} - \lambda \mathbf{I}) \mathbf{x} 
& = 0
\\
\mathbf{x}
& \in N (\mathbf{A} - \lambda \mathbf{I}),
\\
\end{aligned}
$$

which shows that 

$$
\{ \mathbf{x} \neq 0 \mid \mathbf{x} \in N (\mathbf{A} - \lambda \mathbf{I}) \}
$$

is the set of all eigenvectors associated with the $\lambda$, 
and $N (\mathbf{A} - \lambda \mathbf{I})$ is an **eigenspace** for $\mathbf{A}$. 

Because of $\mathbf{x} \neq \mathbf{0}$ and rank-nullity theorem,

$$
N (\mathbf{A} - \lambda \mathbf{I}) \neq \{ \mathbf{0} \} 
\Rightarrow \text{rank} (\mathbf{A} - \lambda \mathbf{I}) < n
$$

which, according to the [property of rank](rank-property-5),
indicates that $\mathbf{A} - \lambda \mathbf{I}$ is a singular matrix,
that is,

$$
\text{det} (\mathbf{A} - \lambda \mathbf{I}) = 0.
$$

## Characteristic polynomial and equation

The characteristic polynomial of $\mathbf{A} \in \mathbb{C}^{n \times n}$ is a function

$$
p (\lambda) = \text{det} (\mathbf{A} - \lambda \mathbf{I}).
$$

- The degree of $p (\lambda)$ is $n$, 

- the leading term in $p (\lambda)$ is $(-1)^{n} \lambda^{n}$.

The characteristic equation for $\mathbf{A}$ is 

$$
p (\lambda) = 0.
$$

- The eigenvalues of $\mathbf{A}$ are the solutions of the characteristic equation.

- Thus, $\mathbf{A}$ has $n$ eigenvalues, 
    but some may be complex numbers (even if the entries of A are real numbers), and some eigenvalues may be repeated.

## Multiplicities

Let $\lambda_{1}, \dots, \lambda_{n} \in \sigma (\mathbf{A})$ be the unique eigenvalues for $\mathbf{A}$. 
Then

-  the **algebraic multiplicity** of an eigenvalue $\lambda_{i}$ is the number of times it appears as the root of $p (\lambda)$,
    
    $$
    \text{alg mult}_{\mathbf{A}} (\lambda_{i}) = a_{i} \iff \dots + (\lambda - \lambda_{i})^{a_{i}} + \dots = 0.
    $$
    
    That is, the algebraic multiplicity of $\lambda_{i}$ is the number of times $\lambda_{i}$ has repeated in all eigenvalues.
    
- the **geometric multiplicity** of an eigenvalue $\lambda_{i}$ is the number of the dimension of eigenspace associated with $\lambda_{i}$,
    
    $$
    \text{geo mult}_{\mathbf{A}} (\lambda_{i}) = \text{dim} N (\mathbf{A} - \lambda_{i} \mathbf{I}).
    $$
    
    That is, the geometric multiplicity of $\lambda_{i}$ is the number of linearly independent eigenvectors associated with $\lambda_{i}$.

### Special multiplicities

- When $\text{alg mult}_{\mathbf{A}} (\lambda_{i}) = 1$, 
$\lambda_{i}$ is called a simple eigenvalue,
since there can only be one unique eigenvector associated with this eigenvalue. 

- Eigenvalues such that $\text{alg mult}_{\mathbf{A}} (\lambda_{i}) = \text{geo mult}_{\mathbf{A}} (\lambda_{i})$ are called semi-simple eigenvalues of A,
as all eigenvectors associated with the eigenvalues that have the value of $\lambda_{i}$ are linearly independent.

### Properties of multiplicities 

(multiplicities-property-1)=

- For every $\mathbf{A} \in \mathbb{C}^{n \times n}$, and for each $\lambda_{i} \in \sigma(\mathbf{A})$,

    $$
    \text{geo mult}_{\mathbf{A}} (\lambda_{i}) \leq \text{alg mult}_{\mathbf{A}} (\lambda_{i}).
    $$
    
  ::: {.callout-note collapse="true" title="Proof"}

    TODO
    
  :::

## Independent eigenvectors

Let $\{ \lambda_{1}, \dots, \lambda_{k} \}$ be a set of distinct eigenvalues for $\mathbf{A}$.

- If $\{ (\lambda_{1}, \mathbf{x}_{1}), \dots, (\lambda_{k}, \mathbf{x}_{k}) \}$ is a set of eigenpairs for $\mathbf{A}$, 
    then $\{ \mathbf{x}_{1}, \dots, \mathbf{x}_{k} \}$ is a linearly independent set.
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    We prove by contradiction.
    
    Suppose $\{ \mathbf{x}_{1}, \dots, \mathbf{x}_{k} \}$ is linearly dependent, 
    but has been reordered so that the first $r$ eigenvectors $\{ \mathbf{x}_{1}, \dots, \mathbf{x}_{k} \}$ is linearly independent. 
    
    Thus, the $r + 1$th eigenvector is 
    
    $$
    \mathbf{x}_{r + 1} = \sum_{i=1}^{r} \alpha_{i} \mathbf{x}_{i}.
    $$
    
    Multiply the both sides by the $\mathbf{A} - \lambda_{r + 1} \mathbf{I}$ to get
    
    $$
    (\mathbf{A} - \lambda_{r + 1} \mathbf{I}) \mathbf{x}_{r + 1} = (\mathbf{A} - \lambda_{r + 1} \mathbf{I}) \sum_{i=1}^{r} \alpha_{i} \mathbf{x}_{i}.
    $$
    
    Since $(\lambda_{r + 1}, x_{r + 1})$ is an eigenpair, 
    
    $$
    \begin{aligned}
    (\mathbf{A} - \lambda_{r + 1} \mathbf{I}) \mathbf{x}_{r + 1} 
    & = 0
    \\
    (\mathbf{A} - \lambda_{r + 1} \mathbf{I}) \sum_{i=1}^{r} \alpha_{i} \mathbf{x}_{i}
    & = 0
    \\
    \sum_{i=1}^{r} \alpha_{i} (\mathbf{A} - \lambda_{r + 1} \mathbf{I}) \mathbf{x}_{i}
    & = 0
    \\
    \sum_{i=1}^{r} \alpha_{i} (\mathbf{A} \mathbf{x}_{i} - \lambda_{r + 1} \mathbf{x}_{i}) 
    & = 0
    \\
    \sum_{i=1}^{r} \alpha_{i} (\lambda_{i} \mathbf{x}_{i} - \lambda_{r + 1} \mathbf{x}_{i}) 
    & = 0
    & [\mathbf{A} \mathbf{x}_{i} = \lambda_{i} \mathbf{x}_{i}]
    \\
    \sum_{i=1}^{r} \alpha_{i} (\lambda_{i}  - \lambda_{r + 1}) \mathbf{x}_{i}
    & = 0
    \\
    \end{aligned}
    $$ 
    
    Since $\{ \mathbf{1}, \dots, \mathbf{x}_{r} \}$ are linearly independent, 
    
    $$
    \alpha_{i} (\lambda_{i}  - \lambda_{r + 1}) = 0, \forall i = 1, \dots, r
    $$
    
    but since we assume $\lambda_{i}, \dots, \lambda_{r + 1}, \dots, \lambda_{n}$ are different,
    
    $$
    \lambda_{i} \neq \lambda_{r + 1} \Rightarrow \alpha_{i} = 0, \forall i = 1, \dots, r,
    $$
    
    which means 
    
    $$
    \mathbf{x}_{r + 1} = \sum_{i=1}^{r} \alpha_{i} \mathbf{x}_{i} = 0.
    $$
    
    However, eigenvectors are all non-zero vectors and thus an contradiction occurs. 

  :::

- If $\mathcal{B}_{i}$ is a basis for $N (\mathbf{A} - \lambda_{i} \mathbf{I})$, 
    then $\mathcal{B} = \mathcal{B}_{1} \cup \dots, \cup \mathcal{B}_{k}$ is a linearly independent set. 
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    TODO

  :::
