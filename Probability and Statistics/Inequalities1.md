## Markov's inequality

**Markov's inequality** states that the probability of a random variable larger than $t$ is less than $\frac{\mu}{t}$. 

Let $X \geq 0$ be a non-negative random variable with finite mean $\mu$. 
Then for any $t > 0$, 

$$
\mathbb{P}_{X} \left(
    x \geq t
\right) \leq \frac{ \mu }{ t }.
$$

:::{prf:proof} Markov's inequality
:label:markov's-inequality
:class:dropdown

Assuming $X$ is a discrete random variable, 

$$
\mu = \sum_{x} \mathbb{P}_{X} (x) x = \sum_{x \geq t} \mathbb{P}_{X} (x) x + \sum_{x < t} \mathbb{P}_{X} (x) x.
$$

Since $X \geq 0$, $\sum_{x < t} \mathbb{P}_{X} (x) x$ is non-negative, and therefore

$$
\begin{aligned}
\mu 
& = \sum_{x \geq t} \mathbb{P}_{X} (x) x + \sum_{x < t} \mathbb{P}_{X} (x) x.
\\
& \geq \sum_{x \geq t} \mathbb{P}_{X} (x)
\\
& = t \sum_{x \geq t} \mathbb{P}_{X} (x) 
\\
& = t \mathbb{P}_{X} (x \geq t)
\end{aligned}
$$

We have Markov's inequality by rearranging the term

$$
\mathbb{P}_{X} (x \geq t) \leq \frac{\mu}{t}.
$$

:::

## Chebyshev's inequality

**Chebyshev's inequality** states that the probability of the difference between a random variable and its mean larger than $a$ is less than $\frac{\sigma^{2}}{t^{2}}$.

Let $X$ be a random variable with finite mean $\mu$ and finite variance $\sigma^{2}$. 
Then for any $t > 0$, 

$$
\mathbb{P}_{X} \left(
    \lvert x - \mu \rvert \geq a
\right) \leq \frac{ \sigma^{2} }{ t^{2} }.
$$

:::{prf:proof} Chebyshev's inequality
:label:chebyshev's-inequality
:class:dropdown

Let $Y = (x - \mathbb{E}_{X} [x])^{2}$ and apply Markov's inequality on $Y$ to get

$$
\begin{aligned}
\mathbb{P}_{Y} (y \geq t^{2}) 
& \leq \frac{ \mathbb{E}_{Y} [y] }{ t^{2} }
\\
& = \frac{
    \mathbb{E}_{X} [(x - \mathbb{E}_{X} [x])^{2}]
}{ 
    a^{2}
}
\\
& = \frac{
    \mathrm{Var}_{X} [x]
}{
    t^{2}
}.
\end{aligned}
$$

Note that 

$$
\mathbb{P}_{Y} (y \geq t^{2}) = \mathbb{P}_{X} \left(
    (x - \mathbb{E}_{X} [x])^{2} \geq t^{2}
\right) = \mathbb{P}_{X} \left( 
    \lvert x - \mathbb{E}_{X} [x] \rvert \geq t
\right).
$$

Therefore, 

$$
\begin{aligned}
\mathbb{P}_{X} \left( 
    \lvert x - \mathbb{E}_{X} [x] \rvert \geq t
\right) 
& \leq \frac{ \mathrm{Var}_{X} [x] }{ t^{2} }.
\\
\mathbb{P}_{X} \left( 
    \lvert x - \mu \rvert \geq t
\right) 
& \leq \frac{ \sigma^{2} }{ t^{2} }.
\end{aligned}
$$

:::

### Average of random variables converge to mean  

Let $X_{1}, \dots, X_{n}$ be independent random variables with finite means $\mu_{1}, \dots, \mu_{n}$ and finite variances $\sigma_{1}^{2}, \dots, \sigma_{n}^{2}$. 
Then, for any $t > 0$

$$
\mathbb{P}_{X_{1}, \dots, X_{n}} \left(
    \left\lvert 
        \sum_{i = 1}^{n} x_{i} - \sum_{i = 1}^{n} \mu_{i}
    \right\rvert \geq t 
\right) \leq \frac{
    \sum_{i = 1}^{n} \sigma_{i}^{2}
}{
    t^{2}
}
$$

## Weak law of large numbers

The **weak law of large numbers** (WLLN) states that the mean of the i.i.d random variables $X_{1}, \dots, X_{n}$ converges to the mean of the distribution as $n$ increases. 

Let $X_{1}, \dots, X_{n}$ be i.i.d random variables with finite mean $\mu$ and finite variance $\sigma^{2}$. 
Then for any $a > 0$

$$
\mathbb{P}_{X_{1}, \dots, X_{n}} \left(
    \left\lvert 
        \frac{\sum_{i = 1}^{n} x_{i}}{n} - \mu
        \right\rvert \geq \epsilon
\right) \leq \frac{\sigma^{2}}{n \epsilon^{2}}
$$


:::{prf:proof} Weak law of large number
:label:weak-law-of-large-number
:class:dropdown

Applying the Chebyshev's inequality over multiple random variables,
we get

$$
\begin{aligned}
\mathbb{P}_{X_{1}, \dots, X_{n}} \left(
    \left\lvert 
        \sum_{i = 1}^{n} x_{i} - \sum_{i = 1}^{n} \mu_{i}
    \right\rvert \geq a
\right) 
& \leq \frac{\sum_{i = 1}^{n} \sigma_{i}^{2}}{a^{2}} 
\\
\mathbb{P}_{X_{1}, \dots, X_{n}} \left(
    \left\lvert 
        \sum_{i = 1}^{n} x_{i} - n \mu
    \right\rvert \geq a
\right) 
& \leq \frac{n \sigma^{2}}{a^{2}} 
\end{aligned}
$$

Setting $a = n \epsilon$,

$$
\begin{aligned}
\mathbb{P}_{X_{1}, \dots, X_{n}} \left(
    \left\lvert 
        \sum_{i = 1}^{n} x_{i} - n \mu
    \right\rvert \geq n \epsilon
\right) 
& \leq \frac{n \sigma^{2}}{n^{2} \epsilon^{2}}.
\\
\mathbb{P}_{X_{1}, \dots, X_{n}} \left(
    \left\lvert 
        \frac{\sum_{i = 1}^{n} x_{i}}{n} - \mu
    \right\rvert \geq \epsilon
\right) 
& \leq \frac{\sigma^{2}}{n \epsilon^{2}}.
\end{aligned}
$$

:::

## Moment Generating Function

The $n$th moment of a random variable $X$ is $\mathbb{E}_{X} [x^{n}]$ and the $n$th central moment of $X$ is $\mathbb{E}_{X} [(x - \mathbb{E}_{X} [x])^{n}]$. 

The moment generating function (MGF) of a random variable $X$ is a function $M_{X} (s)$ that is defined as 

$$
M_{X} (s) = \mathbb{E}_{X} [e^{s x}].
$$

The $n$th moment of the random variable can be derived by taking the $n$th derivative of $M_{X} (s)$ and evaluating it at $s = 0$

$$
\mathbb{E}_{X} [x^{n}] = \frac{d^{n}}{ds^{n}} M_{X} (s) \left.\right|_{s = 0}.
$$

:::{prf:proof} Finding moments from MGF
:label: finding-moments-from-mgf
:class:dropdown

Recall that the Taylor series for $e^{x}$ is 

$$
e^{x} = 1 + x + \frac{x^{2}}{2!} + \dots = \sum_{i = 0}^{\infty} \frac{x^{i}}{i !}.
$$

Therefore, the Taylor series of $e^{s x}$ is 

$$
e^{sx} = \sum_{i = 0}^{\infty} \frac{(s x)^{i}}{i !} = \sum_{i = 0}^{\infty} \frac{s^{i} x^{i}}{i !}.
$$

The moment generating function can be written as 

$$
M_{X} (s) = \mathbb{E}_{X} [e^{s x}] = \mathbb{E}_{X} \left[
    \sum_{i = 0}^{\infty} \frac{s^{i} x^{i}}{i !}
\right] = \sum_{i = 0}^{\infty} \frac{\mathbb{E}_{X} [x^{i}] s^{i} }{i !}.
$$

The $n$th moment is the coefficient of $\frac{s^{k}}{k !}$ in the Taylor series of$M_{X} (s)$,
which can be obtained by taking $n$th derivative $M_{X} (s)$ and evaluating it at $s = 0$.

:::

### Properties of moment generating function

Suppose $X_{1}, \dots, X_{n}$ are independent random variables and $X = \sum_{i = 1}^{n} X_{i}$.

$$
M_{X} (s) = \prod_{i = 1}^{n} M_{X_{i}} (s)
$$

:::{prf:proof} Finding moments from MGF
:label: finding-moments-from-mgf
:class:dropdown

$$
\begin{aligned}
M_{X} (s) 
& = \mathbb{E} [e^{s X}]
\\
& = \mathbb{E} [e^{s \sum_{i = 1} X_{i}}]
\\
& = \mathbb{E} [\prod_{i = 1}^{n} e^{s X_{i}}]
\\
& = \prod_{i = 1}^{n} [e^{s X_{i}}] 
& [X_{i}\text{s are independent}]
\\
& = \prod_{i = 1}^{n} M_{X_{i}} (s)
\\
\end{aligned}
$$

:::

## Chernoff bound

### Chernoff's bounding method 

Let $X$ be a random variable on $\mathbb{R}$. 
Then for all the $t > 0$

$$
\mathbb{P}_{X} (x \geq t) \leq \inf_{s > 0} \frac{
    M_{X} (s)
}{
    e^{s t}
} = \inf_{s > 0} \frac{
    \mathbb{E}_{X} [e^{s x}]
}{
    e^{s t}
}
$$

where $M_{X} (s)$ is the MGF of $X$. 

:::{prf:proof} Chernoff's bounding method
:label: chernoff's-bounding-method
:class:dropdown

For any $t > 0$,
we can apply Markov's inequality

$$
\begin{aligned}
\mathbb{P}_{X} (x \geq t) 
& = \mathbb{P}_{X} (e^{s x} \geq e^{s t})
\\
& \leq \frac{ \mathbb{E}_{X} [e^{s x}] }{ e^{s t} }
\\
& \leq \frac{M_{X} (s) }{ e^{s t} }.
\end{aligned}
$$

Since $\mathbb{P}_{X} (x \geq t) \leq \frac{ M_{X} (s) }{ e^{s t} }$ for any $s > 0$,
$\mathbb{P}_{X} (x \geq t)$ is less than the $s$ that minimizes $\frac{ M_{X} (s) }{ e^{s t} }$,
which is written as 

$$
\mathbb{P}_{X} (x \geq t) \leq \inf_{s > 0} \frac{M_{X} (s)}{e^{s t}}.
$$

:::

The closed-form solution of the optimization problem 

$$
\inf_{s > 0} \frac{
    \mathbb{E}_{X} [e^{s x}]
}{
    e^{s t}
} = \inf_{s > 0} f (s)
$$

can be obtained by solving $f' (s) = 0$ if $f (s)$ is a convex function.

### Chernoff bound for Bernoulli random variables

Let $X_{1}, \dots, X_{n}$ be bounded independent Bernoulli random variables such that $X_{i} \sim \mathrm{Ber} (p_{i}), \forall i$. 
Let $X = \sum_{i=1}^{n} X_{i}$ and $\mu = \mathbb{E}_{X} (x)$.

- Upper tail: for all $\delta > 0$

    $$
    \mathbb{P}_{X} (X \geq (1 + \delta) \mu) \leq \exp \left[
        -\frac{ \delta^{2} \mu }{ 2 + \delta }
    \right]
    $$

- Lower tail: for all $0 < \delta < 1$

    $$
    \mathbb{P}_{X} (X \leq (1 - \delta) \mu) \leq \exp \left[
        -\frac{ \delta^{2} \mu }{ 2 }
    \right]
    $$

:::{prf:proof} Chernoff bound
:label: chernoff-bound
:class:dropdown

Let $X_{i} \sim \mathrm{Ber} (p)$ be a Bernoulli variable. 
Then the MGF of $X_{i}$ can be written as

$$
\begin{aligned}
M_{X_{i}} (s) 
& = \mathbb{E}_{X_{i}} (e^{s X_{i}})
\\
& = p e^{1 \times s} + (1 - p) e^{0 \times s}
\\
& = 1 + p (e^{s} - 1).
\\
\end{aligned}
$$

We can obtain the following inequality for MGF of $X_{i}$

$$
M_{X_{i}} (s) = 1 + p (e^{s} - 1) \leq \exp[p (e^{s} - 1)],
$$

which follows from the fact that $1 + a \leq e^{a}$ for any $a$.

According to the property of the MGF,
the same inequality can be obtained for the MGF of $X = \sum_{i = 1}^{n} X_{i}$

$$
\begin{aligned}
\mathbb{E}_{X} [e^{s x}]
& = M_{X} (s) 
\\
& = \prod_{i = 1}^{n} M_{X_{i}} (s) 
\\
& \leq \prod_{i = 1}^{n} \exp[p (e^{s} - 1)]
\\
& = \exp \left[
    (e^{s} - 1) \sum_{i = 1}^{n} p_{i}
\right]
\\
& = \exp \left[
    (e^{s} - 1) \mu
\right]
\end{aligned}
$$

where $\mu = \mathbb{E}_{X} (x) = \sum_{i = 1}^{n} p_{i}$. 

Now according to the Markov's inequality, 
we can derive a upper bound for $\mathbb{P}_{X} (x \geq (1 + \delta) \mu)$

$$
\begin{aligned}
\mathbb{P}_{X} (x \geq (1 + \delta) \mu) 
& = \mathbb{P}_{X} (e^{s x} \geq e^{s (1 + \delta) \mu}) 
\\
& \leq \frac{
    \mathbb{E}_{X} [e^{s x}]
}{
    e^{s (1 + \delta) \mu}
}
\\
& \leq \frac{
    \exp[(e^{s} - 1) \mu]
}{
    e^{s (1 + \delta) \mu}
}
\end{aligned}
$$

where the first equality is true for any $s \in \mathbb{R}$. 

The upper bound 

$$
\frac{ \exp[(e^{s} - 1) \mu] }{ e^{s (1 + \delta) \mu} }
$$

for $\mathbb{P}_{X} (x \geq (1 + \delta) \mu)$ can be minimized as a function of $s$ by taking its derivative and set it to $0$

$$
\begin{aligned}
\frac{ d }{ d s } \frac{ \exp[(e^{s} - 1) \mu] }{ e^{s (1 + \delta) \mu} } 
& = 0
\\
\frac{ d }{ d s } \exp\left[
    (e^{s} - 1) \mu - (1 + \delta) \mu s
\right]
& = 0
\\
(\mu e^{s} - (1 + \delta) \mu) \exp\left[
    (e^{s} - 1) \mu - (1 + \delta) \mu s
\right]
& = 0
\\
\mu e^{s} - (1 + \delta) \mu
& = 0
\\
s 
& = \log [1 + \delta].
\end{aligned}
$$


Now let's select $s = \log [1 + \delta]$ to get the tight upper bound

$$
\begin{aligned}
\mathbb{P}_{X} (x \geq (1 + \delta) \mu) 
& = \frac{
    \exp[(e^{\log[1 + \delta]} - 1) \mu]
}{
    e^{\log[1 + \delta] (1 + \delta) \mu}
}
\\
& = \frac{
    e^{\delta \mu}
}{
    (1 + \delta)^{(1 + \delta) \mu}
}
\\
& = \left(
    \frac{e^{\delta}}{(1 + \delta)^{1 + \delta}} 
\right)^{\mu}.
\end{aligned}
$$

Taking $\exp \log$ on the upper bound to derive 

$$
\begin{aligned}
\left(
    \frac{ e^{\delta} }{ (1 + \delta)^{1 + \delta} } 
\right)^{\mu}
& = \exp \left[
    \log \left[
        \left(
            \frac{ e^{\delta} }{ (1 + \delta)^{1 + \delta} } 
        \right)^{\mu}
    \right]
\right]
\\
& = \exp \left[
    \mu \left(
        \log e^{\delta} - \log \left[
            (1 + \delta)^{1 + \delta}
        \right]
    \right)
\right]
\\
& = \exp \left[
    \mu \left(
        \delta - (1 + \delta) \log [(1 + \delta)]
    \right)
\right].
\end{aligned}
$$

Since $\log [1 + x] \geq \frac{ x }{ 1 + \frac{x}{2} }$ for all $x > 0$,

$$
\begin{aligned}
\exp \left[
    \mu \left(
        \delta - (1 + \delta) \log [(1 + \delta)]
    \right)
\right]
& \leq \exp \left[
    \mu \left(
        \delta - \frac{ (1 - \delta) \delta }{ 1 + \frac{\delta}{2} }
    \right)
\right]
\\
& = \exp \left[
    \mu \left(
        \frac{ (1 + \frac{\delta}{2}) \delta }{ 1 + \frac{ \delta }{ 2 } } - \frac{ (1 - \delta) \delta }{ 1 + \frac{ \delta }{ 2 } }
    \right)
\right]
\\
& = \exp \left[
    - \left(
        \frac{ \delta^{2} }{ 2 + \delta }
    \right) \mu
\right].
\end{aligned}
$$

Putting all together to derive the upper tail of Chernoff bound

$$
\mathbb{P}_{X} (x \geq (1 + \delta) \mu) \leq \exp \left[
    - \left(
        \frac{ \delta^{2} }{ 2 + \delta }
    \right) \mu
\right].
$$

The proof for the lower tail is similar except that 

- taking $s = \log [1 - \delta]$ to maximize the lower bound, and

- applies the inequality $\log [1 - x] \geq -x + \frac{ x^{2} }{ 2 }$ in the last step for $0 < x < 1$. 

:::

### General Chernoff bound

Let $X_{1}, \dots, X_{n}$ be bounded independent random variables such that $X_{i} \in [a, b], \forall i$. 
Let $X = \sum_{i=1}^{n} X_{i}$ and $\mu = \mathbb{E}_{X} (x)$. Then for $\delta > 0$

- Upper tail: 

    $$
    \mathbb{P}_{X} (X \geq (1 + \delta) \mu) \leq \exp \left[
        -\frac{ 2 \delta^{2} \mu^{2} }{ n (b - a)^{2} }
    \right]
    $$

- Lower tail:

    $$
    \mathbb{P}_{X} (X \leq (1 - \delta) \mu) \leq \exp \left[
        -\frac{ \delta^{2} \mu^{2} }{ n (b - a)^{2} }
    \right]
    $$