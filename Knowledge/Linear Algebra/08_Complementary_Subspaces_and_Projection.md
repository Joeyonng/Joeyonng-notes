---
title: Complementary Subspaces and Projection
---

# Complementary Subspaces

Subspaces $\mathcal{X}, \mathcal{Y}$ of a vector space $\mathcal{V}$ are **complementary** if 

$$
\mathcal{V} = \mathcal{X} + \mathcal{Y},
$$

and

$$
\mathcal{X} \cap \mathcal{Y} = 0,
$$

in which case $\mathcal{V}$ is the direct sum of $\mathcal{X}$ and $\mathcal{Y}$ and is denoted as 

$$
\mathcal{V} = \mathcal{X} \oplus \mathcal{Y}.
$$

## Properties of complementary subspaces 

(complementary-subspaces-property-1)=

- $\mathcal{X}$ and $\mathcal{Y}$ are complementary if and only if 
    there exist unique vectors $x \in \mathcal{X}$ and $y \in \mathcal{Y}$ such that 
    
    $$
    v = x + y,
    $$
    
    for each $v \in \mathcal{V}$.
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    Suppose there are two pairs of $x_{1}, x_{2} \in \mathcal{X}$ and $y_{1}, y_{2} \in \mathcal{Y}$ such that
    
    $$
    v = x_{1} + y_{1} = x_{2} + y_{2}.
    $$
    
    Then 
    
    $$
    \begin{aligned}
    x_{1} + y_{1} 
    & = x_{2} + y_{2}
    \\
    x_{1} - x_{2} 
    & = y_{2} - y_{1}
    \\
    \end{aligned}
    $$
    
    According to the definition of the subspace 
    
    $$
    \begin{aligned}
    x_{1}, x_{2} \in \mathcal{X} 
    & \Rightarrow x_{1} - x_{2} \in \mathcal{X}
    \\
    y_{1}, y_{2} \in \mathcal{X} 
    & \Rightarrow y_{1} - y_{2} \in \mathcal{Y}.
    \end{aligned}
    $$
    
    which means
    
    $$
    x_{1} - x_{2} = y_{2} - y_{1} \Rightarrow x_{1} - x_{2} \in \mathcal{Y}.
    $$
    
    Thus, 
    
    $$
    x_{1} - x_{2} \in \mathcal{X} \cap \mathcal{Y}.
    $$
    
    However, since by definition $\mathcal{X} \cap \mathcal{Y} = 0$,
    
    $$
    \begin{aligned}
    x_{1} - x_{2} 
    & = 0.
    \\
    x_{1} 
    & =  x_{2}.
    \end{aligned}
    $$
    
    Similar argument can be made for $y_{1}$ and $y_{2}$.
    
  :::

(complementary-subspaces-property-2)=

- Suppose $\mathcal{X}$ has a basis $\mathcal{B}_{\mathcal{X}}$ and $\mathcal{Y}$ has a basis $\mathcal{B}_{\mathcal{Y}}$.
    Then $\mathcal{X}$ and $\mathcal{Y}$ are complementary if and only if 
    
    $$
    \mathcal{B}_{\mathcal{X}} \cap \mathcal{B}_{\mathcal{Y}} = \emptyset
    $$
    
    and 
    
    $$
    \mathcal{B}_{\mathcal{X}} \cup \mathcal{B}_{\mathcal{Y}}
    $$
    
    is a basis for $\mathcal{V}$.
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    TODO
    
  :::

# Projection

Suppose that $\mathcal{X}$ and $\mathcal{Y}$ are complementary subspaces in $\mathcal{V}$.
Thus, there exists unique $x \in \mathcal{X}$ and $y \in \mathcal{Y}$ such that $v = x + y$ for every vector $v \in \mathcal{V}$

Then the unique linear operator $\mathbf{P} \in \mathbb{C}^{n \times n}$ defined by 

$$
\mathbf{P} v = x
$$ 

is the **projection matrix** of $\mathcal{V}$ onto $\mathcal{X}$ along $\mathcal{Y}$ and $x \in \mathcal{X}$ is the **projection** of $v \in \mathcal{V}$ onto $\mathcal{X}$ along $\mathcal{Y}$.

## Properties of projection matrix

(projection-matrix-property-1)=

- $\mathbf{I} - \mathbf{P}$ is the complementary projection matrix of $\mathbf{v}$ onto $\mathcal{Y}$ along $\mathcal{X}$.

  ::: {.callout-note collapse="true" title="Proof"}
    
    According to the definition of projection matrix,
    
    $$
    \begin{aligned}
    v 
    & = x + y 
    \\
    & = \mathbf{P} v + y.
    \end{aligned}
    $$
    
    Thus, 
    
    $$
    \begin{aligned}
    y 
    & = v - \mathbf{P} v 
    \\
    & = (\mathbf{I} - \mathbf{P})v.
    \end{aligned}
    $$

  :::

(projection-matrix-property-2)=

- $R (\mathbf{P}) = N (\mathbf{I} - \mathbf{P}) = \mathcal{X}$ and $N (\mathbf{P}) = R (\mathbf{I} - \mathbf{P}) = \mathcal{Y}$.

  ::: {.callout-note collapse="true" title="Proof"}
    
    Since $v \in \mathcal{V}$ and $\mathcal{X}$, 
    
    $$
    \mathbf{P} v = x \Rightarrow R (\mathbf{P}) = \mathcal{X}.
    $$
    
    Also,
    for all $v \in N (\mathbf{I} - \mathbf{P})$,
    
    $$
    \begin{aligned}
    (\mathbf{I} - \mathbf{P}) v 
    & = 0 
    \\
    v - \mathbf{P} v 
    & = 0
    \\
    v - x
    & = 0
    \\
    v 
    & = x
    \end{aligned}
    $$
    
    which means $v \in \mathcal{X} \Rightarrow \mathcal{V} \subseteq N (\mathbf{I} - \mathbf{P})$.
    
    Since $N (\mathbf{I} - \mathbf{P}) \subseteq \mathcal{V}$,
    
    $$
    N (\mathbf{I} - \mathbf{P}) = \mathcal{V}.
    $$
    
    The proof for $N (\mathbf{P}) = R (\mathbf{I} - \mathbf{P}) = \mathcal{Y}$ is the same.

  :::

(projection-matrix-property-3)=

- For $x \in \mathcal{X}, y \in \mathcal{Y}$, 

    $$ 
    \mathbf{P} x = x,
    $$
    
    and
    
    $$
    \mathbf{P} y = 0.
    $$
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    TODO
    
  :::

(projection-matrix-property-4)=

- A linear operator $\mathbf{P}$ on $\mathcal{V}$ is a projection matrix if and only if $\mathbf{P}$ is idempotent ($\mathbf{P} = \mathbf{P}^{2}$).

  ::: {.callout-note collapse="true" title="Proof"}
    
    According to the definition of the projector
    $$
    \mathbf{P}^{2} v = \mathbf{P} \mathbf{P} v = \mathbf{P} x.
    $$
    
    According to the [property of projection matrix](projection-matrix-property-3)
    
    $$
    \mathbf{P} x = x = \mathbf{P} v.
    $$
    
    Thus, 
    $$
    \mathbf{P} v = \mathbf{P}^{2} v \Rightarrow \mathbf{P} = \mathbf{P}^{2}.
    $$

  :::

(projection-matrix-property-5)=

- If $\mathcal{V} = \mathbb{R}^{n}$ or $\mathbb{C}^{n}$, 
    then $\mathbf{P}$ is given by
    
    $$
    \mathbf{P} = 
    \begin{bmatrix}
        \mathbf{X} & \mathbf{0} 
    \end{bmatrix}
    \begin{bmatrix}
        \mathbf{X} & \mathbf{Y} 
    \end{bmatrix}^{-1}
    = 
    \begin{bmatrix}
        \mathbf{X} & \mathbf{Y} 
    \end{bmatrix}
    \begin{bmatrix}
        \mathbf{I} & \mathbf{0} \\
        \mathbf{0} & \mathbf{0} 
    \end{bmatrix}
    \begin{bmatrix}
        \mathbf{X} & \mathbf{Y} 
    \end{bmatrix}^{-1}
    $$

    where the columns of $\mathbf{X}$ and $\mathbf{Y}$ are respective bases for $\mathcal{X}$ and $\mathcal{Y}$.
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    TODO

  :::

(projection-matrix-property-6)=

- $\mathbf{P}$ is unique for a given $\mathcal{X}$ and $\mathcal{Y}$.

  ::: {.callout-note collapse="true" title="Proof"}
    
    TODO
    
  :::
