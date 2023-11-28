# Joeyonng's Notebook

## Notations

### Mathematical definitions

| Symbol | Name | Description |
|:---:|:---:|:---:|
| $x$ | Scalar | Variables are scalars (numbers). |
| $\mathbf{x}$ | Vector | Bold non-capitalized variables are vectors. |
| $\hat{\mathbf{x}}$ | Unit vector | Vectors that have a hat are unit vectors. |
| $\mathbf{X}$ | Matrix | Bold capitalized variables are matrices. |
| $X$ | Random variable | Capitalized variables are random variables. |
| $\mathcal{X}$ | Set | Calligraphic variables are sets. |

### Mathematical operations

| Symbol | Name | Description |
|:---:|:---:|:---:|
| $\mathbf{a} \cdot \mathbf{b}$ | Dot product | Dot product between vector $\mathbf{a}$ and $\mathbf{b}$ (same as $\mathbf{a}^{T} \mathbf{b}$). |
| $\mathbf{A}\mathbf{b}$ | Matrix vector product | Matrix product between matrix $\mathbf{A}$ and vector $\mathbf{b}$ (column matrix). |
| $\mathbf{a}^{T}$ | Vector transpose | The transposed vector is a matrix of size $1 \times d$  |
| $\mathbf{A}^{T}$ | Matrix transpose | Transpose a matrix. |

### Mathematical indexing

| Symbol | Name | Description |
|:---:|:---:|:---:|
| $\mathbf{A}_{i, j}$ | Matrix element selection | Select the scalar at row $i$ and column $j$ of matrix $\mathbf{A}$. |
| $\mathbf{A}_{i, *}$ | Matrix row selection | Select the vector at row $i$ of matrix $\mathbf{A}$. |
| $\mathbf{A}_{*, j}$ | Matrix column selection | Select the vector at column $j$ of matrix $\mathbf{A}$. |
| $\mathbf{a}_{i}$ | Vector element selection | Select the scalar at index $i$ of vector $\mathbf{a}$. |

### Others

| Symbol | Name | Description |
|:---:|:---:|:---:|
| $\mathbb{1}_{cond}$ | Conditional operator | Evaluates to 1 if $cond$ is true, 0 otherwise. |

## Cheat sheet

### Logarithm

1. Product

    $$ \ln(xy) = \ln(x) + \ln(y) $$ 

1. Quotient

    $$ \ln \left( \frac{x}{y} \right) = \ln(x) - \ln(y) $$

1. Log of power

    $$ \ln(x^{y}) = y \ln(x) $$

1. Log reciprocal	

    $$ \ln \left( \frac{1}{x} \right) = \ln(1) - \ln(x) = 0 - \ln(x) = -\ln(x) $$

### Linear algebra

1. The squared norm of vector $\mathbf{x}$

    $$ \lVert \mathbf{x} \rVert^{2} = \mathbf{x} \cdot \mathbf{x} = \mathbf{x}^{T} \mathbf{x}$$
    
1. The squared norm of a vector difference between $\mathbf{a}$ and $\mathbf{b}$

    $$ \lVert \mathbf{a} - \mathbf{b} \rVert^{2} = (\mathbf{a} - \mathbf{b})^{T} (\mathbf{a} - \mathbf{b}) = \mathbf{a}^{T}\mathbf{a} - 2 \mathbf{a}^T\mathbf{b} + \mathbf{b}^{T}\mathbf{b} $$

1. The matrix form of the dot product between two vectors $\mathbf{a}$ and $\mathbf{b}$ with a coefficient $\lambda$

    $$ \lambda(\mathbf{a} \cdot \mathbf{b}) = \mathbf{a}^{T} \mathbf{\Lambda} \mathbf{b} $$

    where $\mathbf{\Lambda}$ is a diagonal matrix with value $\lambda$.
    
1. The transpose of the product of two matrices $\mathbf{A}$ and $\mathbf{B}$

    $$ (\mathbf{A}\mathbf{B})^{T} = \mathbf{B}^{T}\mathbf{A}^{T} $$

### Calculus

1. The derivative of the sigmoid function $\sigma$ is $\sigma (1 - \sigma)$

    $$ 
    \begin{align}
    \frac{\partial \sigma}{\partial x} & = \frac{\partial}{\partial x} \frac{1}{1 + e^{-x}} \\
    & = \frac{\partial}{\partial x} (1 + e^{-x})^{-1} \\
    & = -(1 + e^{-x})^{-2} \times -e^{-x} \\
    & = \frac{e^{-x}}{(1 + e^{-x})^{2}} \\
    & = \frac{e^{-x}}{1 + e^{-x}} \frac{1}{1 + e^{-x}} \\
    & = \frac{e^{-x}}{1 + e^{-x}} \left( \frac{1 + e^{-x}}{1 + e^{-x}} - \frac{e^{-x}}{1 + e^{-x}} \right) \\
    & = \frac{e^{-x}}{1 + e^{-x}} \left( 1 - \frac{e^{-x}}{1 + e^{-x}} \right) \\
    & = \sigma (1 - \sigma) \\
    \end{align}
    $$
