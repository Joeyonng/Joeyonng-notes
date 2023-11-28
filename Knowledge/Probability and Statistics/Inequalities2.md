## Sub-Gaussian random variables

A random variable $X$ with mean $\mu$ is called **Sub-Gaussian** with parameter $\sigma$ ($X \sim SubGau (\sigma)$) if 

$$
\mathbb{E}_{X} \left[
    e^{s (X - \mu)}
\right] \leq \exp \left[
    \frac{ s^{2} \sigma^{2} }{ 2 }
\right].
$$

The definition can equivalently be expressed in terms of bounds on the tail 
of $X$.
Let $X \sim SubGau (\sigma)$ and $\mu = \mathbb{E}_{X} [X]$. Then for any $t > 0$, 

$$
\mathbb{P}_{X} \left(
    X - \mu \geq t
\right) \leq \exp \left[
    \frac{ - t^{2} }{ 2 \sigma^{2} }
\right].
$$

:::{prf:proof} Bound of Sub-Gaussian
:label: bound-of-sub-gaussian
:class:dropdown

First use Chernoff bound to derive

$$
\begin{aligned}
\mathbb{P}_{X} (x \geq t) 
& \leq \inf_{s > 0} \frac{
    \mathbb{E}_{X} [e^{s x}]
}{
    e^{s t}
}
\\ 
& \leq \inf_{s > 0} \exp \left[
    \frac{ s^{2} \sigma^{2} }{ 2 } - s t
\right].
\end{aligned}
$$

Since $\exp \left[ \frac{ s^{2} \sigma^{2} }{ 2 } - s t \right]$ is a convex function

$$
\begin{aligned}
\frac{ d }{ d s } \exp \left[ 
    \frac{ s^{2} \sigma^{2} }{ 2 } - s t 
\right]
& = 0
\\
(\sigma^{2} s - t) \exp \left[
    \frac{ \sigma^{2} s^{2} }{ 2 } - t s
\right] 
& = 0
\\
s 
& = \frac{ t }{ \sigma^{2} }.
\end{aligned}
$$

Plug $s = \frac{ t }{ \sigma^{2} }$ back and we get derive the result

$$
\begin{aligned}
\mathbb{P}_{X} (x \geq t) 
& \leq \inf_{s > 0} \exp \left[
    \frac{ s^{2} \sigma^{2} }{ 2 } - s t
\right]
\\
& = \exp \left[
    \frac{ t^{2} }{ 2 \sigma^{2} } - \frac{ t^{2} }{ \sigma^{2} }
\right]
\\
& = \exp \left[
    \frac{ - t^{2} }{ 2 \sigma^{2} } 
\right].
\end{aligned}
$$

:::

## Hoeffding's inequality 

Hoeffding's inequality provides an upper bound on the probability that the sum of bounded independent random variables deviates from its expected value by more than a certain amount.

### Hoeffding's Lemma 

Let $X$ be a bounded random variable with $a \leq X \leq b$ and $\mu = \mathbb{E}_{X} [x]$.
Then for all $s > 0$,

$$
\mathbb{E}_{X} [e^{s (x - \mu)}] \leq \exp \left[
    \frac{ s^{2} (b - a)^{2} }{ 8 }
\right].
$$

:::{prf:proof} Hoeffding's Lemma
:label: hoeffding's-lemma
:class:dropdown

Since $f (x) = e^{a x}$ is a convex function,
the definition of the convex function states that 

$$
e^{s x} \leq \frac{ (x - a) e^{s b} }{ b - a } + \frac{ (b - x) e^{s a} }{ b - a }.
$$

Taking the expectation on the both ends and the fact that $\mathbb{E}_{X} (x) = 0$,

$$
\begin{aligned}
\mathbb{E}_{X} [e^{s x}] 
& \leq \mathbb{E}_{X} \left[
    \frac{ (x - a) e^{s b} }{ b - a } + \frac{ (b - x) e^{s a} }{ b - a }
\right]
\\
& = \frac{
    e^{s b} \mathbb{E}_{X} [x] - a e^{s b} + b e^{s a} - e^{s a} \mathbb{E}_{X} [x]
}{
    b - a
}
\\
& = \frac{ b e^{s a} - a e^{s b} }{ b - a }.
\end{aligned}
$$

Now we will prove that 

$$
\frac{ b e^{s a} - a e^{s b} }{ b - a } \leq \exp \left[
    \frac{ s^{2} (b - a)^{2} }{ 8 }
\right]
$$

which is same as proving 

$$
\log \left[
    \frac{ b e^{s a} - a e^{s b} }{ b - a } 
\right] \leq \frac{ s^{2} (b - a)^{2} }{ 8 }.
$$

By taking $p = \frac{ b }{ b - a }$ and $1 - p = -\frac{ a }{ b - a }$

$$
\begin{aligned}
\log \left[
    \frac{ b e^{s a} - a e^{s b} }{ b - a } 
\right] 
& = \log \left[
    \frac{ b e^{s a} }{ b - a } - \frac{ a e^{s b} }{ b - a } 
\right]
\\
& = \log \left[
    p e^{s a} + (1 - p) e^{s b}
\right]
\\
& = \log \left[
    e^{s a} e^{-s a} (p e^{s a} + (1 - p) e^{s b})
\right]
\\
& = s a + \log \left[
    (p + (1 - p) e^{s b - s a})
\right]
\end{aligned}
$$

and taking $u = (b - a) s$,
we can get a function

$$
\begin{aligned}
\phi (u)
& = s a + \log \left[
    (p + (1 - p) e^{s b - s a})
\right]
\\
& = (p - 1) u + \log \left[
    (p + (1 - p) e^{u})
\right].
\end{aligned}
$$

This function can be approximated using Taylor series until the second order term at point $a = 0$,

$$
\phi (u) = \phi (0) + \phi' (0) x + \frac{ \phi' (0) }{ 2 } x^{2},
$$

where 

$$
\phi' (u) = (p - 1) + \frac{ (1 - p) e^{u} }{ p + (1 - p) e^{u} } = 0,
$$

and

$$
\phi'' (u) = \frac{ p (1 - p) e^{u} }{ (p + (1 - p) e^{u})^{2} } = 0.
$$

Since $\phi (0) = 0$, $\phi' (0) = 0$ and 

$$
\phi'' (0) = \frac{ p (1 - p) }{ (p + (1 - p))^{2} }
$$

reaches its maximum of $0.25$ at $p = 0.5$,
we can derive

$$
\log \left[
    \frac{ b e^{s a} - a e^{s b} }{ b - a } 
\right] = \phi (u) \leq \frac{ u^{2} }{ 8 } = \frac{ s^{2} (b - a)^{2} }{ 8 }.
$$

Therefore, we can prove the lemma

$$
\mathbb{E}_{X} [e^{s x}] \leq \frac{ b e^{s a} - a e^{s b} }{ b - a } \leq \exp \left[
    \frac{ s^{2} (b - a)^{2} }{ 8 }
\right].
$$

:::

Equivalently, Hoeffding's lemma states that any random variable $X \in [a, b]$ is a subGaussian variable

$$
X \in SubGau \left(
    \frac{ (b - a)^{2} }{ 4 }
\right).
$$

### Hoeffding's inequality

Let $X_{1}, \dots, X_{n}$ be bounded independent random variables such that $X_{i} \in [a_{i}, b_{i}], \forall i$. 
Let $X = \sum_{i=1}^{n} X_{i}$ and $\mu = \mathbb{E}_{X} (x)$. Then for $t > 0$

$$
\mathbb{P}_{X} \left(
    x - \mu \geq t
\right) \leq \exp \left[
    \frac{
        - 2 t^{2}
    }{
        \sum_{i=1}^{n} (b_{i} - a_{i})^{2}
    }
\right].
$$

:::{prf:proof} Hoeffding's inequality
:label: hoeffding's-inequality
:class:dropdown

We can first apply Chernoff's bounding method 

$$
\begin{aligned}
\mathbb{P}_{X} (x - \mu \geq t) 
& \leq \inf_{s > 0} \frac{ M_{X} (s) }{ e^{s t} }
\\
& = \inf_{s > 0} \frac{ 
    \prod_{i = 1}^{n} M_{X_{i}} (s)
}{
    e^{s t}
}
\\
& = \inf_{s > 0} \frac{ 
    \prod_{i = 1}^{n} \mathbb{E}_{X} \left[
        e^{s (X_{i} - \mathbb{E}_{X_{i}} [x_{i}])}
    \right]
}{
    e^{s t}
}.
\end{aligned}
$$

Then by applying the Hoeffding's Lemma, 

$$
\mathbb{E}_{X_{i}} \left[
    e^{s (X_{i} - \mathbb{E}_{X_{i}} [x_{i}])} 
\right] \leq \exp \left[
    \frac{ s^{2} (b_{i} - a_{i})^{2} }{ 8 }
\right]
$$

we can have

$$
\begin{aligned}
\mathbb{P}_{X} (x - \mu \geq t) 
& \leq \inf_{s > 0} \frac{
    \prod_{i = 1}^{n} \mathbb{E}_{X_{i}} \left[
        e^{s (X_{i} - \mathbb{E}_{X_{i}} [x_{i}])}
    \right]
}{
    e^{s t}
}
\\
& \leq \inf_{s > 0} \frac{
    \prod_{i = 1}^{n} \exp\left[
        \frac{ s^{2} (b_{i} - a_{i})^{2} }{ 8 }
    \right]
}{e^{s t}}
\\
& = \inf_{s > 0} \exp\left[
    \frac{ s^{2} \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} }{ 8 } - s t
\right].
\end{aligned}
$$

Since $\exp \left[ \frac{ s^{2} \sum_{i = 1}^{n} (a_{n} - b_{n})^{2} }{ 8 } - s t \right]$ is a convex function,

$$
\begin{aligned}
\frac{ d }{ d s } \exp \left[
    \frac{ s^{2} \sum_{i = 1}^{n} (a_{n} - b_{n})^{2} }{ 8 } - s t
\right]
& = 0
\\
\left(
    \frac{ s \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} }{ 4 } - t
\right)
\exp\left[
    \frac{ s^{2} \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} }{ 8 }  - s t
\right]
& = 0
\\
\frac{ s \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} }{ 4 } - t
& = 0
\\
s 
& = \frac{ 4 t }{ \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} }
\end{aligned}
$$

Therefore, we have proved Hoeffding's inequality

$$
\begin{aligned}
\mathbb{P}_{X} (x - \mu \geq t) 
& \leq \inf_{s > 0} \exp\left[
    \frac{ s^{2} }{ 8 } \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} - s t
\right]
\\
& = \exp \left[
    \frac{
        \left(
            \frac{ 4 t }{ \sum_{i}^{n} (b_{i} - a_{i})^{2} }
        \right)^{2}
    }{
        8
    } \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} - \frac{ 4 t }{ \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} } t 
\right]
\\
& = \exp \left[
    \frac{ - 2 t^{2} }{ \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} }
\right].
\end{aligned}
$$

:::

Another version is to bound the estimated mean. 

Let $X_{1}, \dots, X_{n}$ be bounded independent random variables such that $X_{i} \in [a_{i}, b_{i}], \forall i$. 
Let $\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_{i}$ and $\mu = \mathbb{E}_{\bar{X}} (x)$. Then for $t > 0$

$$
\mathbb{P}_{\bar{X}} \left(
    x - \mu \geq t
\right) \leq \exp \left[
    -\frac{ 2 n^{2} t^{2} }{ \sum_{i=1}^{n} (b_{i} - a_{i})^{2} }
\right]
$$

## Martingales

### Martingale sequence

Given a sequence of random variables $X_{1}, \dots, X_{\infty}$, 
define another sequence of random variables $Y_{1}, \dots, Y_{\infty}$ where $Y_{n}$ is a measurable function of $X_{1}, \dots X_{n}$

$$
Y_{n} = f (X_{1}, \dots, X_{n}).
$$

For all $Y_{n}$, if $\mathbb{E}_{Y_{n}} [y_{n}]$ is finite and 

$$
\mathbb{E}_{Y_{n + 1} \mid X_{1}, \dots, X_{n}} [Y_{n + 1} \mid X_{1}, \dots, X_{n}] = Y_{n},
$$

then $Y_{1}, \dots, Y_{\infty}$ is a **martingale sequence** with respect to $X_{1}, \dots, X_{\infty}$. 

### Martingale difference sequence 

Given a sequence of random variables $X_{1}, \dots, X_{\infty}$, 
define another sequence of random variables $Z_{1}, \dots, Z_{\infty}$ where $Z_{n}$ is a measurable function of $X_{1}, \dots X_{n}$

$$
Z_{n} = f (X_{1}, \dots, X_{n}).
$$

For all $Z_{n}$, if $E_{Z_{n}} [z_{n}]$ is finite and 

$$
\mathbb{E}_{Z_{n + 1} \mid X_{1}, \dots, X_{n}} [Z_{n + 1} \mid X_{1}, \dots, X_{n}] = 0
$$

then $Z_{1}, \dots, Z_{\infty}$ is a **martingale difference sequence** with respect to $X_{1}, \dots, X_{\infty}$. 

### A common Martingale sequence

If $X_{1}, \dots, X_{\infty}$ is a sequence of independent random variables where $\mathbb{E}_{X_{i}} [x_{i}] = 0, \forall X_{i}$,
then $Y_{1}, \dots, X_{\infty}$ with $Y_{n} = \sum_{i = 1}^{n} X_{i}$ is martingale sequence. 

$$
\begin{aligned}
\mathbb{E}_{Y_{n + 1} \mid X_{1}, \dots, X_{n}} 
& = \mathbb{E}_{Y_{n} + X_{n + 1} \mid X_{1}, \dots, X_{n}} 
\\
& = \mathbb{E}_{Y_{n} \mid X_{1}, \dots, X_{n}} + \mathbb{E}_{X_{n + 1} \mid X_{1}, \dots, X_{n}} 
\\
& = Y_{n} + \mathbb{E}_{X_{n + 1}} 
\\
& = Y_{n}
\end{aligned}
$$


Suppose $Y_{1}, \dots, Y_{n}$ is a martingale sequence with respect to $X_{1}, \dots, X_{n}$.
then the sequence $Z_{1}, \dots, Z_{\infty}$ with $Z_{n} = Y_{n} - Y_{n - 1}$ is a martingale difference sequence. 

$$
\begin{aligned}
\mathbb{E}_{Z_{n + 1} \mid X_{1}, \dots, X_{n}} 
& = \mathbb{E}_{Y_{n + 1} - Y_{n} \mid X_{1}, \dots, X_{n}} 
\\
& = \mathbb{E}_{Y_{n + 1} \mid X_{1}, \dots, X_{n}} - \mathbb{E}_{Y_{n} \mid X_{1}, \dots, X_{n}} 
\\
& = Y_{n} - Y_{n}
\\
& = 0
\end{aligned}
$$

## Azuma Inequality 

For a sequence of Martingale difference sequence of bounded random variable $Z_{1}, \dots, Z_{\infty}$ with $Z_{i} \in [a_{i}, b_{i}], \forall i$, 
then:

$$
\mathbb{P}_{Z_{1}, \dots, Z_{n}} \left[
    \sum_{i = 1}^{n} z_{i} \geq t 
\right] \leq \exp \left[
    \frac{ - 2 t^{2} }{ \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} }
\right].
$$

:::{prf:proof} Azuma Inequality
:label: azuma-inequality
:class:dropdown

First we can apply Chernoff bound to derive

$$
\begin{aligned}
\mathbb{P}_{Z_{1}, \dots, Z_{n}} \left[
    \sum_{i = 1}^{n} z_{i} \geq t 
\right] 
& \leq \inf_{s > 0} \frac{
    \mathbb{E}_{Z_{1}, \dots, Z_{n}} \left[
        e^{s \sum_{i = 1}^{n} z_{i}}
    \right]
}{
    e^{s t}
}
\\
& = \inf_{s > 0} \frac{
    \mathbb{E}_{Z_{1}, \dots, Z_{n}} \left[
        \prod_{i = 1}^{n} e^{s z_{i}}
    \right]
}{
    e^{s t}
}
\end{aligned}
$$

Then we can use the law of total expectation to derive 

$$
\begin{aligned}
\mathbb{E}_{Z_{1}, \dots, Z_{n}} \left[
    \prod_{i = 1}^{n} e^{s z_{i}}
\right]
& = \mathbb{E}_{Z_{1}, \dots, Z_{n - 1}} \left[
    \mathbb{E}_{Z_{1}, \dots, Z_{n} \mid Z_{1}, \dots Z_{n - 1}} \left[
        \prod_{i = 1}^{n} e^{s z_{i}} \mid z_{1}, \dots, z_{n - 1}
    \right]
\right]
\\
& = \mathbb{E}_{Z_{1}, \dots, Z_{n - 1}} \left[
    \mathbb{E}_{Z_{1}, \dots, Z_{n} \mid Z_{1}, \dots Z_{n - 1}} \left[
        e^{s z_{n}} \prod_{i = 1}^{n - 1} e^{s z_{i}} \mid z_{1}, \dots, z_{n - 1}
    \right]
\right]
\\
& = \mathbb{E}_{Z_{1}, \dots, Z_{n - 1}} \left[
    \prod_{i = 1}^{n - 1} e^{s z_{i}} \mathbb{E}_{Z_{n} \mid Z_{1}, \dots, Z_{n - 1}} \left[
        e^{s z_{n}} \mid z_{1}, \dots, z_{n - 1}
    \right]
\right],
\end{aligned}
$$

where the last equality is derived because $\prod_{i = 1}^{n - 1} e^{s z_{i}}$ is a constant given $z_{1}, \dots, z_{n - 1}$.  

We can derive a upper bound by applying the Hoeffding's lemma 

$$
\begin{aligned}
\mathbb{E}_{Z_{1}, \dots, Z_{n}} \left[
    \prod_{i = 1}^{n} e^{s z_{i}}
\right]
& \leq \mathbb{E}_{Z_{1}, \dots, Z_{n - 1}}\ \left[
    \prod_{i = 1}^{n - 1} e^{s z_{i}} \exp \left[
        \frac{ s^{2} (a_{n} - b_{n})^{2} }{ 8 }
    \right]
\right] 
\\
& = \exp \left[
    \frac{ s^{2} (a_{n} - b_{n})^{2} }{ 8 }
\right] \mathbb{E}_{Z_{1}, \dots, Z_{n - 1}}\ \left[
    \prod_{i = 1}^{n - 1} e^{s z_{i}} 
\right] 
\end{aligned}
$$

We can apply the same procedure for $\mathbb{E}_{Z_{1}, \dots, Z_{n - 1}} [ \prod_{i = 1}^{n - 1} e^{s z_{i}} ]$

$$
\mathbb{E}_{Z_{1}, \dots, Z_{n - 1}} \left[
    \prod_{i = 1}^{n - 1} e^{s z_{i}}
\right] = \exp \left[
    \frac{ s^{2} (a_{n - 1} - b_{n - 1})^{2} }{ 8 }
\right] \mathbb{E}_{Z_{1}, \dots, Z_{n - 2}}\ \left[
    \prod_{i = 1}^{n - 2} e^{s z_{i}} 
\right] 
$$

and do this iteratively to derive 

$$
\begin{aligned}
\mathbb{E}_{Z_{1}, \dots, Z_{n}} \left[
    \prod_{i = 1}^{n} e^{s z_{i}}
\right]
& = \exp \left[
    \frac{ s^{2} (a_{n} - b_{n})^{2} }{ 8 }
\right] \times \dots \times \exp \left[
    \frac{ s^{2} (a_{1} - b_{1})^{2} }{ 8 }
\right] 
\\
& = \exp \left[
    \frac{ s^{2} \sum_{i = 1}^{n} (a_{n} - b_{n})^{2} }{ 8 }
\right].
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\mathbb{P}_{Z_{1}, \dots, Z_{n}} \left[
    \sum_{i = 1}^{n} z_{i} \geq t 
\right] 
& \leq \inf_{s > 0} \frac{
    \mathbb{E}_{Z_{1}, \dots, Z_{n}} \left[
        e^{s \sum_{i = 1}^{n} z_{i}}
    \right]
}{
    e^{s t}
}
\\
& = \inf_{s > 0} \exp \left[
    \frac{ s^{2} \sum_{i = 1}^{n} (a_{n} - b_{n})^{2} }{ 8 } - s t
\right]
\end{aligned}
$$

Since $\exp \left[ \frac{ s^{2} \sum_{i = 1}^{n} (a_{n} - b_{n})^{2} }{ 8 } - s t \right]$ is a convex function,

$$
\begin{aligned}
\frac{ d }{ d s } \exp \left[
    \frac{ s^{2} \sum_{i = 1}^{n} (a_{n} - b_{n})^{2} }{ 8 } - s t
\right]
& = 0
\\
\left(
    \frac{ s \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} }{ 4 } - t
\right)
\exp\left[
    \frac{ s^{2} \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} }{ 8 }  - s t
\right]
& = 0
\\
\frac{ s \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} }{ 4 } - t
& = 0
\\
s 
& = \frac{ 4 t }{ \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} }
\end{aligned}
$$

and therefore

$$
\begin{aligned}
\mathbb{P}_{Z_{1}, \dots, Z_{n}} \left[
    \sum_{i = 1}^{n} z_{i} \geq t 
\right] 
& \leq \inf_{s > 0} \exp \left[
    \frac{ s^{2} \sum_{i = 1}^{n} (a_{n} - b_{n})^{2} }{ 8 } - s t
\right]
\\
& = \exp \left[
    \frac{
        \left(
            \frac{ 4 t }{ \sum_{i}^{n} (b_{i} - a_{i})^{2} }
        \right)^{2}
    }{
        8
    } \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} - \frac{ 
        4 t 
    }{ 
        \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} 
    } t
\right]
\\
& = \exp \left[
    \frac{ - 2 t^{2} }{ \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} }
\right].
\end{aligned}
$$

:::

## McDiarmid’s Inequality

Given a function $f: \mathbb{R}^{n} \to \mathbb{R}$ with the bounded difference property, 
that is, 
the maximum change of the function output induced by replacing any $x_{i}$ with $x'_{i}$ is bounded by $c_{i}$,

$$
\lvert f (x_{1}, \dots, x_{i}, \dots, x_{n}) - f (x_{1}, \dots, x'_{i}, \dots, x_{n}) \rvert \leq c_{i},
$$

then the function $f$ of independent random variables $X_{1}, \dots, X_{n}$ satisfies

$$
\mathbb{P}_{X_{1}, \dots, X_{n}} \left[
    f (X_{1}, \dots, X_{n}) - \mathbb{E}_{X_{1}, \dots, X_{n}} \left[
        f (X_{1}, \dots, X_{n})
    \right] \geq t
\right] \leq \exp \left[
    \frac{
        - 2 t^{2}
    }{
        \sum_{i=1}^{n} c_{i}^{2}
    }
\right].
$$

:::{prf:proof} McDiarmid's Inequality
:label: micdiarmid's-inequality
:class:dropdown

Let $X_{1}, \dots, X_{n}$ be a sequence of independent random variable, 
and $Y_{1}, \dots, Y_{n}$ be a Martingale sequence with respect to $X_{1}, \dots, X_{n}$ where

$$
Y_{i} = g (X_{1}, \dots, X_{i}) = \mathbb{E}_{X_{1}, \dots, X_{n} \mid X_{1}, \dots, X_{i}} \left[
    f (X_{1}, \dots, X_{n}) \mid X_{1}, \dots, X_{i}
\right].
$$

Note that we have 

$$
\begin{aligned}
Y_{0} 
& = \mathbb{E}_{X_{1}, \dots, X_{n}} \left[
    f (X_{1}, \dots, X_{n})
\right],
\\
Y_{n}
& = \mathbb{E}_{X_{1}, \dots, X_{n} \mid X_{1}, \dots, X_{n}} \left[
    f (X_{1}, \dots, X_{n}) \mid X_{1}, \dots, X_{n}
\right] = f (X_{1}, \dots, X_{n}).
\end{aligned}
$$

Let $Z_{1}, \dots, Z_{n}$ be an independent random variable with $Z_{i} = Y_{i} - Y_{i - 1}$, 
which is proved to be a Martingale difference sequence.

Note that 

$$
\sum_{i = 1}^{n} Z_{i} = Y_{n} - Y_{0} = f (X_{1}, \dots, X_{n}) - \mathbb{E}_{X_{1}, \dots, X_{n}} \left[
    X_{1}, \dots, X_{n}
\right]
$$

For each $Z_{i}$, 
its upper bound $U_{i}$ and lower bound $L_{i}$ can be written as 

$$
\begin{aligned}
U_{i} 
& = \sup_{x_{i} \in X_{i}} \mathbb{E}_{X_{1}, \dots, X_{n} \mid X_{1}, \dots, X_{i}} \left[
    f (X_{1}, \dots, x_{i}, \dots X_{n}) \mid X_{1}, \dots, X_{i - 1}
\right] - \mathbb{E}_{X_{1}, \dots, X_{n} \mid X_{1}, \dots, X_{i - 1}} \left[
    f (X_{1}, \dots, X_{n}) \mid X_{1}, \dots, X_{i - 1}
\right] 
\\
L_{i} 
& = \inf_{x_{i} \in X_{i}} \mathbb{E}_{X_{1}, \dots, X_{n} \mid X_{1}, \dots, X_{i}} \left[
    f (X_{1}, \dots, x_{i}, \dots, X_{n}) \mid X_{1}, \dots, X_{i - 1}
\right] - \mathbb{E}_{X_{1}, \dots, X_{n} \mid X_{1}, \dots, X_{i - 1}} \left[
    f (X_{1}, \dots, X_{n}) \mid X_{1}, \dots, X_{i - 1}
\right] 
\end{aligned}
$$

The difference between $U_{i}$ and $L_{i}$ is less than $c_{i}$ because of the bounded property property of $f$,

$$
\begin{aligned}
U_{i} - L_{i} 
& = \sup_{x_{i} \in X_{i}} \mathbb{E}_{X_{1}, \dots, X_{n} \mid X_{1}, \dots, X_{i}} \left[
    f (X_{1}, \dots, x_{i}, \dots X_{n}) \mid X_{1}, \dots, X_{i - 1}
\right] - \inf_{x_{i} \in X_{i}} \mathbb{E}_{X_{1}, \dots, X_{n} \mid X_{1}, \dots, X_{i}} \left[
    f (X_{1}, \dots, x_{i}, X_{n}) \mid X_{1}, \dots, X_{i - 1}
\right] 
\\
& = \sup_{x_{i}, x'_{i} \in X_{i}} \left[
    \mathbb{E}_{X_{1}, \dots, X_{n} \mid X_{1}, \dots, X_{i}} \left[
        f (X_{1}, \dots, x_{i}, \dots, X_{n}) \mid X_{1}, \dots, X_{i - 1}
    \right] - \mathbb{E}_{X_{1}, \dots, X_{n} \mid X_{1}, \dots, X_{i}} \left[
        f (X_{1}, \dots, x'_{i}, \dots, X_{n}) \mid X_{1}, \dots, X_{i - 1}
    \right] 
\right]
\\
& = \sup_{x_{i}, x'_{i} \in X_{i}} \left[
    \mathbb{E}_{X_{1}, \dots, X_{n} \mid X_{1}, \dots, X_{i}} \left[
        f (X_{1}, \dots, x_{i}, \dots, X_{n}) - 
        f (X_{1}, \dots, x'_{i}, \dots, X_{n}) \mid X_{1}, \dots, X_{i - 1}
    \right] 
\right]
\\
& = \mathbb{E}_{X_{1}, \dots, X_{n} \mid X_{1}, \dots, X_{i}} \left[
    \sup_{x_{i}, x'_{i} \in X_{i}} f (X_{1}, \dots, x_{i}, \dots, X_{n}) - 
    f (X_{1}, \dots, x'_{i}, \dots, X_{n}) \mid X_{1}, \dots, X_{i - 1}
\right] 
\\
& \leq \mathbb{E}_{X_{1}, \dots, X_{n} \mid X_{1}, \dots, X_{i}} \left[
    c_{i}
    \mid X_{1}, \dots, X_{i - 1}
\right] 
\\
& \leq c_{i}.
\end{aligned}
$$

Therefore, we have a Martingale difference sequence of bounded random variable $Z_{1}, \dots, Z_{n}$,
where $Z_{i} \in [a_{i}, b_{i}], \forall i$ and $b_{i} - a_{i} \leq c_{i}$.
We can apply Azuma inequality to obtain McDiarmid's inequality.

$$
\begin{aligned}
\mathbb{P}_{Z_{1}, \dots, Z_{n}} \left[
    \sum_{i = 1}^{n} z_{i} \geq t 
\right] 
& = \mathbb{P}_{Z_{1}, \dots, Z_{n}} \left[
    \mathbb{E}_{X_{1}, \dots, X_{n}} \left[
        X_{1}, \dots, X_{n}
    \right]
\right] 
\\
& \leq \exp \left[
    \frac{ - 2 t^{2} }{ \sum_{i = 1}^{n} (b_{i} - a_{i})^{2} }
\right]
\\
& \leq \exp \left[
    \frac{ - 2 t^{2} }{ \sum_{i = 1}^{n} c_{i}^{2} }
\right].
\end{aligned}
$$

:::