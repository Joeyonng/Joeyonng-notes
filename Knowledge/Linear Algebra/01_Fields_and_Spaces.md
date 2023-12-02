---
title: Fields and Spaces
---

# Fields

A field is a **set** $\mathbb{F}$, equipped with two operations addition $+$ and multiplication $\cdot$, obeying the rules (axioms) listed below.

## Axioms of fields

For all $x$, $y$, and $z$ in the field $\mathbb{F}$ ($\forall x, y, z \in \mathbb{F}$), we have:

- **Closure** under addition and multiplication:

    $$
    x + y \in \mathbb{F},
    $$
    
    $$
    x \cdot y \in \mathbb{F}.
    $$

- **Commutativity** of addition and multiplication:

    $$ 
    x + y = y + x,
    $$
    
    $$
    x \cdot y = y \cdot x.
    $$

- **Associativity** of addition and multiplication:

    $$ 
    (x + y) + z = x + (y + z), 
    $$
    
    $$ 
    (x \cdot y) \cdot z = x \cdot (y \cdot z).
    $$

- **Distributive property** of multiplication:

    $$
    (x + y) \cdot z = x \cdot z + y \cdot z.
    $$

- There is an element in $\mathbb{F}$ called **"zero"** $0 \in \mathbb{F}$ such that 

    $$ 
    x + 0 = x,
    $$
    
    and there is another element in $\mathbb{F}$ called **"one"** $1 \in \mathbb{F}$, $1 \neq 0$, such that
    
    $$
    x \cdot 1 = x.
    $$

- For each $x \in \mathbb{F}$, there is an element in $\mathbb{F}$ called **addictive inverse** $x_{I}$ of $x$ such that 

    $$
    x + x_{I} = 0,
    $$
    
    and if $x \neq 0$, there is an element in $\mathbb{F}$ called **multiplicative inverse** $x^{-1}$ of $x$ such that
    
    $$
    x \cdot x^{-1} = 1.
    $$

## Properties of fields

- **Zero and one are unique**: there is only one "zero" and one "one" in any field $\mathbb{F}$.

  ::: {.callout-note collapse="true" title="Proof"}

    We prove "zero" is unique by contradiction. 
    
    Suppose there are two different "zero"s $0_{0}$ and $0_{1}$.
    
    Due to the definition of "zero", 
        
    $$
    \begin{aligned}
    0_{1} + 0_{0} 
    & = 0_{1}
    & [0_{0} \text{ is "zero"}]
    \\
    0_{0} + 0_{1} 
    & = 0_{0}
    & [0_{1} \text{ is "zero"}]
    \\
    \end{aligned}
    $$

    Due to the Commutativity axiom, 
    
    $$
    \begin{aligned}
    0_{1} + 0_{0} 
    & = 0_{0} + 0_{1} 
    \\
    0_{1} 
    & = 0_{0}
    \\
    \end{aligned}
    $$
    
    which contradicts to the fact that $0_{0}$ and $0_{1}$ ($1_{0}$ and $1_{1}$) are different. 
    Thus, there is only a unique "zero" in $\mathbb{F}$.
    
    The proof that the "one" in any $\mathbb{F}$ is unique is the same as above by replacing every addition $+$ with multiplication $\cdot$ and $0_{0}$, $0_{1}$ with $1_{0}$, $1_{1}$.

  :::

- **Addictive and multiplicative inverse of every element are unique**: there is only one addictive inverse and multiplicative inverse of every element (other than "zero" for multiplicative inverse) in any field $\mathbb{F}$.

  ::: {.callout-note collapse="true" title="Proof"}
    
    We prove the addictive inverse is unique by contradiction. 
    
    Suppose there are two different addictive inverses of $x$: $x_{1}$ and $x_{2}$. 
    
    By following the definition of addictive inverse,
    
    $$
    (x + x_{1}) + x_{2} = 0 + x_{2} = x_{2}.
    $$
    
    Also,
    
    $$
    \begin{aligned}
    (x + x_{1}) + x_{2}
    & = x_{2}
    \\
    x + (x_{1} + x_{2})
    & = x_{2}
    & [\text{associativity}]
    \\
    x + (x_{2} + x_{1})
    & = x_{2}
    & [\text{commutativity}]
    \\
    (x + x_{2}) + x_{1}
    & = x_{2}
    & [\text{associativity}]
    \\
    x_{1}
    & = x_{2}
    \end{aligned}
    $$
    
    which contradicts to the fact that $x_{1}$ and $x_{2}$ are different.
    Thus, the addictive inverse of every element in any field is unique.
    
    The proof that the multiplicative inverse of every element in any field is unique is the same as above by replacing every addition $+$ with multiplication $\cdot$.

  :::

- **For every $x$ in $\mathbb{F}$, $x \cdot 0 = 0$**

  ::: {.callout-note collapse="true" title="Proof"}
    
    Consider 
    
    $$
    \begin{aligned}
    x \cdot 0 + x \cdot 0 
    & = x \cdot (0 + 0) 
    & [\text{distributive property}]
    \\
    & = x \cdot 0
    & [\text{definition of } 0]
    \end{aligned}
    $$
    
    By the definition of addictive inverse, there must exist an addictive inverse $y$ of $x \cdot 0$ in $\mathbb{F}$ such that
    
    $$
    \begin{aligned}
    x \cdot 0 + y 
    & = 0
    \\
    (x \cdot 0 + x \cdot 0) + y
    & = 0
    \\
    x \cdot 0 + (x \cdot 0 + y)
    & = 0
    & [\text{associativity}]
    \\
    x \cdot 0 + 0
    & = 0
    & [\text{addictive inverse}]
    \\
    x \cdot 0
    & = 0 
    & [\text{definition of 0}]
    \end{aligned}
    $$

  :::

- **$x_{I} = 1_{I} \cdot x$**

  ::: {.callout-note collapse="true" title="Proof"}
    
    $$
    \begin{aligned}
    (x + x_{I}) + 1_{I} \cdot x
    & = 1_{I} \cdot x
    \\
    (x_{I} + x) + 1_{I} \cdot x
    & = 1_{I} \cdot x
    \\
    x_{I} + (x + 1_{I} \cdot x)
    & = 1_{I} \cdot x
    \\
    x_{I} + (1 \cdot x + 1_{I} \cdot x)
    & = 1_{I} \cdot x
    \\
    x_{I} + (1  + 1_{I}) \cdot x
    & = 1_{I} \cdot x
    \\
    x_{I} + 0 \cdot x
    & = 1_{I} \cdot x
    \\
    x_{I} + 0
    & = 1_{I} \cdot x
    \\
    x_{I}
    & = 1_{I} \cdot x
    \end{aligned}
    $$

  :::

# Vector spaces

A vector space, defined over a field $\mathbb{F}$, is a **non-empty set** $\mathcal{V}$ (whose members are called vectors), equipped with two operations: vector addition $+$ and scalar multiplication $\cdot$, obeying the rules (axioms) listed below.

## Axioms of vector spaces

For all $u$, $v$, and $w$ in the vector space $\mathcal{V}$ ($\forall u, v, w \in \mathcal{V}$) and for all $\alpha$ and $\beta$ in the field $\mathbb{F}$, we have

- **Closure** under vector addition and scalar multiplication

$$
u + v \in \mathcal{V},
$$

$$
\alpha \cdot v \in \mathcal{V}.
$$

- **Commutativity** of vector addition:

    $$ 
    u + v = v + u.
    $$
    
    Note that there is no requirement of the commutativity of scalar multiplication in the definition of the vector space.

- **Associativity** of vector addition and scalar multiplication:

    $$ 
    (u + v) + \mathbf{w} = u + (v + \mathbf{w}), 
    $$
    
    $$ 
    (\alpha \cdot \beta) \cdot v = \alpha \cdot (\beta \cdot v).
    $$
    
    Note that in the left hand side of the second equation, the first dot is field multiplication while the second one is the scalar multiplication, but the in the right hand side both dots are scalar multiplication.

- **Distributive property** of scalar multiplication:

    $$
    \alpha \cdot (u + v) = \alpha \cdot u + \alpha \cdot v,
    $$
    
    $$
    (\alpha + \beta) \cdot v = \alpha \cdot v + \beta \cdot v.
    $$

- There is an element in $\mathcal{V}$ called **"zero"** vector $0 \in \mathcal{V}$ such that 

    $$ 
    v + 0 = v,
    $$
    
    and the definition of **"one"** in the field $1 \in \mathbb{F}$ is applied in the vector space
    
    $$ 
    1 \cdot v = v.
    $$
    
    Note that there is no requirement for the existence of "one" vector in the definition of the vector space.

- For each $v \in \mathcal{V}$, there is an element in $\mathcal{V}$ called **addictive inverse** vector $v_{I}$ of $v$ such that 

    $$
    v + v_{I} = 0.
    $$
    
    Note that there is no requirement for the scalar multiplicative inverse in the definition of the vector space.

## Linear combination

Let $\mathcal{V}$ be a vector space over the field $\mathbb{F}$. 
Given a set of vectors $v_{1}, \dots, v_{n} \in \mathcal{V}$ and a set of field elements $\alpha_{1}, \dots, \alpha_{n} \in \mathbb{F}$, 
the vector $u$ is a linear combination of $v_{1}, \dots, v_{n}$ with $\alpha_{1}, \dots, \alpha_{n}$ as coefficients if

$$
u = \sum_{i=1}^{n} \alpha_{i} v_{i}.
$$

# Subspaces

Given a vector space $\mathcal{V}$ over a field $\mathbb{F}$, a subspace $\mathcal{W}$ of $\mathcal{V}$ is a non-empty subset of $\mathcal{V}$ ($\mathcal{W} \subseteq \mathcal{V}$) that follows the **closure** axioms. 

For all $u$ and $v$ in the subspace $\mathcal{W}$ ($\forall u, v \in \mathcal{W}$) and for all $\alpha$ in the field $\mathbb{F}$ ($\forall \alpha \in \mathbb{F}$), we have

$$
u + v \in \mathcal{W},
$$

$$
\alpha \cdot v \in \mathcal{W}.
$$

## Properties of subspace

Let $\mathcal{U}$ and $\mathcal{V}$ be the subspaces of a vector space over $\mathbb{F}$. 

- $0 \in \mathcal{W}$.

  ::: {.callout-note collapse="true" title="Proof"}
    
    Since the subspace $\mathcal{W}$ cannot be empty, there is at least an element $v \in \mathcal{W}$. 
    
    Since $1 \in \mathbb{F}$ and $1_{I} \in \mathbb{F}$, 
    
    $$
    1_{I} \cdot v = v_{I} \in \mathcal{W},
    $$ 
    
    according to the axiom of the closure under scalar multiplication. 
    
    According to the axiom of the closure under vector addition,
    
    $$
    v + v_{I} = 0 \in \mathcal{W}.
    $$
    
    Thus, "zero" vector must be in $\mathcal{W}$.

  :::

- $\mathcal{W}$ is also a vector space.

  ::: {.callout-note collapse="true" title="Proof"}
    
    By virtue of the closure axioms, all axioms of the vector space are obeyed by $\mathcal{W}$. 
    
    Since all elements in $\mathcal{W}$ are also in the vector space $\mathcal{V}$, the axioms of 
    
    - closure
    
    - commutativity
    
    - associativity
    
    - distributive property
    
    - $1 \cdot v = v$
    
    in $\mathcal{W}$ follow directly from those in $\mathcal{V}$
    
    The existence of "zero" vector and addictive inverse are proved in the proof above.

  :::

- The subspace

    $$
    \mathcal{W} + \mathcal{U} = \left\{
        w + u \mid w \in \mathcal{W}, u \in \mathcal{U}
    \right\}
    $$
    
    is also a subspace.

  ::: {.callout-note collapse="true" title="Proof"}
    
    Since $0 \in \mathcal{W}$ and $0 \in \mathcal{U}$, 
    then $0 \in \mathcal{W} + \mathcal{U}$. 
    Thus, $\mathcal{W} + \mathcal{U}$ is non-empty.
    
    Suppose $a, b \in \mathcal{W} + \mathcal{U}$, 
    then there exists elements $a_{1} \in \mathcal{W}, a_{2} \in \mathcal{U}$ such that $a = a_{1} + a_{2}$ 
    and $b_{1} \in \mathcal{W}, b_{2} \in \mathcal{U}$ such that $b = b_{1} + b_{2}$.
    
    Because of closure under addition, 
    
    $$
    a_{1} + b_{1} \in \mathcal{W},
    $$
    
    $$
    a_{2} + b_{2} \in \mathcal{U}.
    $$
    
    Thus, according to the definition of the set addition
    
    $$
    a + b = (a_{1} + b_{1}) + (a_{2} + b_{2}) \in \mathcal{W} + \mathcal{U}.
    $$
    
    Again, suppose $x \in \mathcal{W} + \mathcal{U}$, 
    then there exists elements $x_{1} \in \mathcal{W}, x_{2} \in \mathcal{U}$ such that $x = x_{1} + x_{2}$.
    
    Because of closure under scalar multiplication, 
    
    $$
    \alpha \cdot x_{1} \in \mathcal{W} \quad \forall \alpha \in \mathbb{F},
    $$
    
    $$
    \alpha \cdot x_{2} \in \mathcal{U} \quad \forall \alpha \in \mathbb{F}.
    $$
    
    Thus, according to the definition of the set addition
    
    $$
    \alpha \cdot x = \alpha \cdot x_{1} + \alpha \cdot x_{2} \in \mathcal{W} + \mathcal{U} \quad \forall \alpha \in \mathbb{F}.
    $$
    
    Thus, $\mathcal{W} + \mathcal{U}$ is a non-empty set that is closed for both vector addition and scalar multiplication and thus is a subspace.
    
  :::

- The subspace

    $$
    \mathcal{W} \cap \mathcal{U} = \left\{
        v \mid v \in \mathcal{W}, v \in \mathcal{U}
    \right\}
    $$
    
    is also a subspace.

  ::: {.callout-note collapse="true" title="Proof"}
    
    Since $0 \in \mathcal{W}$ and $0 \in \mathcal{U}$, 
    then $0 \in \mathcal{W} \cap \mathcal{U}$. 
    Thus, $\mathcal{W} \cap \mathcal{U}$ is non-empty.
    
    Suppose $a, b \in \mathcal{W} \cap \mathcal{U}$, 
    then because of the closure axiom of the subspaces
    
    $$
    a + b \in \mathcal{W},
    \\
    a + b \in \mathcal{U}.
    $$ 
    
    Thus, by definition, 
    
    $$
    a + b \in \mathcal{W} \cap \mathcal{U}.
    $$
    
    Again, suppose $x \in \mathcal{W} \cap \mathcal{U}$, 
    then because of the closure axiom of the subspaces,
    
    $$
    \alpha \cdot x \in \mathcal{W}, \forall \alpha \in \mathbb{F},
    \\
    \alpha \cdot x \in \mathcal{U}, \forall \alpha \in \mathbb{F}.
    $$
    
    Thus, by definition, $\alpha \cdot x \in \mathcal{W} \cap \mathcal{U}, \forall \alpha \in \mathbb{F}$.
    
    Thus, $\mathcal{W} \cap \mathcal{U}$ is a non-empty set that is closed for both vector addition and scalar multiplication and thus is a subspace.
    
  :::

- The subspace
    
    $$
    \mathcal{W} \cup \mathcal{U} = \left\{
        v \mid v \in \mathcal{W} \mathop{\text{or}} v \in \mathcal{U}
    \right\}
    $$
    
    is a subspace if and only if $\mathcal{W} \subseteq \mathcal{U}$ or $\mathcal{U} \subseteq \mathcal{W}$
    
  ::: {.callout-note collapse="true" title="Proof"}
    
    First we prove if $\mathcal{U} \subseteq \mathcal{W}$, 
    then $\mathcal{U} \cup \mathcal{W}$ is a subspace.
    
    Since $\mathcal{U} \subseteq \mathcal{W}$, 
    
    $$
    \mathcal{U} \cup \mathcal{W} = \mathcal{W}
    $$
    
    and thus is a subspace.
    
    The same argument can be made for $\mathcal{W} \subseteq \mathcal{U}$.
    
    Then we prove if $\mathcal{U} \cup \mathcal{W}$ is a subspace, 
    then one subspace is contained in the other by contradiction.
    
    Suppose $\mathcal{U} \cup \mathcal{W}$ is a subspace, 
    but $\mathcal{U} \nsubseteq \mathcal{W}$ and $\mathcal{W} \nsubseteq \mathcal{U}$.
    This means there exists at least two vectors $u$ and $w$ such that
    
    $$
    u \in \mathcal{U}, u \notin \mathcal{W}
    $$
    
    $$
    w \in \mathcal{W}, w \notin \mathcal{U}.
    $$
    
    Since $u, w \in \mathcal{U} \cup \mathcal{W}$ and closure under addition property, 
    the vector
    
    $$
    v = u + w
    $$
    
    is also in $\mathcal{U} \cup \mathcal{W}$,
    which means it must also be in $\mathcal{U}$ or $\mathcal{W}$. 
    
    If $v \in \mathcal{U}$, 
    because there must exist an addictive inverse of $u \in \mathcal{U}$,
    then
    
    $$
    \begin{aligned}
    v 
    & = u + w
    \\
    v + u_{I} 
    & = u + u_{I} + w
    \\
    w 
    & = v + u_{I}
    \\
    \end{aligned}
    $$
    
    which shows that $w \in \mathcal{U}$ and contradicts to our assumption. 
    
    The same contradiction can also be found when $v \in \mathcal{W}$. 
    
  :::

## Example: subspaces of 2-dimensional real-value column vectors

The 2-dimensional real-value column vector space $\mathbb{R}^{2}$ has 3 types of subspaces

1. The subspace of the zero vector only,

    $$
    \mathcal{W} = \left\{ 0 \right\}.
    $$
    
1. The subspace of the vector space itself,

    $$
    \mathcal{W} = \mathbb{R}^{2}.
    $$
    
1. Any "line" that goes through zero vector
