# Compiled Exercises

## I. Probability Basics
1. **Exercise 1.2.1** (_Events as Sets_)

Let \(\{A_i : i \in I\}\) be a family of events. Prove De Morgan's laws:
\[
\left(\bigcup_{i \in I} A_i\right)^c = \bigcap_{i \in I} A_i^c, \qquad
\left(\bigcap_{i \in I} A_i\right)^c = \bigcup_{i \in I} A_i^c.
\]

2. **Exercise 1.2.2** (_Events as Sets_)

Let \(\mathcal{F}\) be a \(\sigma\)-field on \(\Omega\) and let \(A,B \in \mathcal{F}\).
Show that \(A \cap B\), \(A \setminus B\), and \(A \triangle B\) all belong to \(\mathcal{F}\).

3. **Exercise 1.2.3** (_Events as Sets_)

A knock-out tournament begins with \(2^n\) labelled players.
Describe the sample space of all possible outcomes and determine its cardinality.

4. **Exercise 1.3.1** (_Probability_)

Let \(\mathbb{P}(A) = \tfrac{3}{4}\) and \(\mathbb{P}(B) = \tfrac{1}{3}\).
Find sharp bounds for \(\mathbb{P}(A \cap B)\) and \(\mathbb{P}(A \cup B)\), and give examples attaining the bounds.

5. **Exercise 1.3.2** (_Probability_)

A fair coin is tossed indefinitely. Show that almost surely a head appears, and that every fixed finite pattern of heads and tails appears eventually.

6. **Exercise 1.3.3** (_Probability_)

Two each of red, white, and starred cups are randomly placed on matching saucers (two of each design).
All \(6!\) placements of labelled cups are equally likely. Find \(\mathbb{P}(\text{no cup matches its saucer})\).

7. **Exercise 1.3.5** (_Probability_)

Let \(A_n\) satisfy \(\mathbb{P}(A_n)=1\) for every \(n\). Show that \(\mathbb{P}(\bigcap_{n\ge1}A_n)=1\).

8. **Exercise 1.4.1** (_Conditional Probability_)

Establish Bayes' identity \(\mathbb{P}(A\mid B)=\mathbb{P}(B\mid A)\mathbb{P}(A)/\mathbb{P}(B)\)
whenever \(\mathbb{P}(A),\mathbb{P}(B)>0\). Deduce that \(\mathbb{P}(A\mid B) > \mathbb{P}(A)\) implies \(\mathbb{P}(B\mid A) > \mathbb{P}(B)\).

9. **Exercise 1.4.2** (_Conditional Probability_)

Let \(A_1,\dots,A_n\) satisfy \(\mathbb{P}(A_1\cap\cdots\cap A_k)>0\) for each \(k\).
Prove the chain rule
\[
\mathbb{P}(A_1\cap\cdots\cap A_n) = \mathbb{P}(A_1) \prod_{k=2}^{n} \mathbb{P}(A_k\mid A_1\cap\cdots\cap A_{k-1}).
\]

10. **Exercise 1.4.3** (_Conditional Probability_)

A box contains two double-headed coins, one double-tailed coin, and two fair coins.
A coin is chosen uniformly and tossed repeatedly.
1. Find \(\mathbb{P}(\text{lower face heads after first toss})\).
2. Given the first toss shows heads, find the conditional probability the lower face is a head.
3. Given the first two tosses show heads, find the probability the lower face is a head.
4. After discarding the coin, a new coin is selected and tossed once. Find the chance of heads.

11. **Exercise 1.5.2** (_Independence_)

A fair die is rolled \(n\) times. For \(i<j\) let \(A_{ij}\) be the event that rolls \(i\) and \(j\) coincide.
Show \(\{A_{ij}\}\) is pairwise independent but not mutually independent.

12. **Exercise 1.5.3** (_Independence_)

A fair coin is tossed repeatedly. Show that independence of tosses is equivalent to the statement that every fixed length-\(m\) word of heads and tails occurs in the first \(m\) positions with probability \(2^{-m}\).

13. **Exercise 1.5.5** (_Independence_)

Give examples showing that conditional independence does not imply independence, and vice versa.
For which events \(C\) are the two concepts equivalent for all \(A,B\)?

14. **Exercise 1.7.1** (_Worked Examples_)

Two roads connect \(A\) to \(B\) and two connect \(B\) to \(C\). Each road is blocked independently with probability \(p\).
Find \(\mathbb{P}(A \leftrightarrow B \mid A \not\leftrightarrow C)\). Show the answer is unchanged if an additional direct road from \(A\) to \(C\) is included and behaves independently.

15. **Exercise 1.7.2** (_Worked Examples_)

From a standard deck, a 13-card hand is dealt. Compute
(i) \(\mathbb{P}(\text{exactly two kings and one ace})\);
(ii) \(\mathbb{P}(\text{exactly one ace} \mid \text{exactly two kings})\).

## II. Random Variables
1. **Exercise 2.1.1** (_Random Variables_)

Let \(X\) be a random variable and \(a \in \mathbb{R}\). Show \(aX\) is a random variable, and deduce that \(X-X\) is almost surely zero while \(X+X=2X\).

2. **Exercise 2.1.2** (_Random Variables_)

Let \(Y=aX+b\) with \(a \neq 0\) and distribution function \(F\) for \(X\).
Express \(F_Y\) in terms of \(F\).

3. **Exercise 2.1.3** (_Random Variables_)

A coin with success probability \(p\) is tossed \(n\) times. Show \(\mathbb{P}(\text{exactly } k \text{ heads}) = \binom{n}{k}p^k(1-p)^{n-k}\).

4. **Exercise 2.2.1** (_Law of Averages_)

(Randomised response.) The true probability of a “yes” answer is \(q\). Each respondent flips a fair coin in secret and replies “yes” whenever the coin shows heads, regardless of the truth. What is the probability of observing “yes”, and how can \(q\) be estimated from the sample mean?

5. **Exercise 2.2.2** (_Law of Averages_)

Let \(H_n\) and \(T_n\) denote heads and tails in \(n\) independent tosses of a coin with head probability \(p\).
Show that for \(\varepsilon>0\),
\[
\mathbb{P}\left(\left|\frac{H_n-T_n}{n}-(2p-1)\right|>\varepsilon\right) \le 2e^{-2n\varepsilon^2}.
\]

6. **Exercise 2.3.1** (_Discrete and Continuous Variables_)

Let \(F\) be a distribution function and \((a_m)_{m \in \mathbb{Z}}\) satisfy \(a_m\uparrow\infty\), \(a_m\downarrow -\infty\).
Define \(G(x)=F(a_m)\) for \(x \in [a_{m-1},a_m)\). Show that if \(\sup_m |a_m-a_{m-1}| \to 0\), then \(G(x)\to F(x)\) at each continuity point of \(F\).

7. **Exercise 2.3.2** (_Discrete and Continuous Variables_)

Let \(g:\mathbb{R}\to\mathbb{R}\) be continuous and strictly increasing. Show that \(Y=g(X)\) is a random variable.

8. **Exercise 2.3.3** (_Discrete and Continuous Variables_)

Let \(X\) be uniform on \([0,1]\) and let \(F\) be a continuous strictly increasing distribution function.
Define \(Y = F^{-1}(X)\). Show that \(Y\) has distribution \(F\).

9. **Exercise 2.4.1** (_Worked Examples_)

Let \(X\) have distribution function \(F\). Determine the distribution functions of:
(a) \(X^2\); (b) \(\sqrt{X}\) assuming \(X\ge0\); (c) \(\sin X\); (d) \(G^{-1}(X)\) where \(G\) is continuous increasing;
(e) \(F(X)\); (f) \(G^{-1}(F(X))\).

10. **Exercise 2.4.2** (_Worked Examples_)

Let \(a<b\) and define \(Y=\min\{\max\{X,a\},b\}\) and \(Z=X\mathbf{1}_{\{a\le X \le b\}}\).
Find the distribution functions of \(Y\) and \(Z\).

11. **Exercise 2.5.1** (_Random Vectors_)

Let \((X,W)\) take values \((0,0),(0,1),(1,0),(1,1)\) each with probability \(1/4\).
Find the marginals and determine whether \(X\) and \(W\) are independent.

12. **Exercise 2.5.2** (_Random Vectors_)

Suppose \((X,Y)\) equals \((1,0)\) with probability \(p\) and \((0,1)\) with probability \(1-p\).
Compute \(\operatorname{Cov}(X,Y)\).

13. **Exercise 2.5.3** (_Random Vectors_)

Let \((X,Y)\) have density \(f_{X,Y}(x,y)=e^{-x}/(y(1+y^2))\) for \(x>0,y>0\) and zero elsewhere.
Verify that this is a density and derive the marginal densities.

14. **Exercise 2.7.2** (_Problems_)

Define simple approximations \(X_m = \sum_{k\in\mathbb{Z}} k2^{-m} \mathbf{1}_{\{k2^{-m} \le X < (k+1)2^{-m}\}}\).
Show \(X_m(\omega)\to X(\omega)\) for every \(\omega\) and hence \(\{X\le x\}=\bigcap_{m\ge1}\{X_m\le x\}.

15. **Exercise 2.7.3** (_Problems_)

Let \(X\) and \(Y\) be random variables. Show \(XY\), \(X/Y\) (when \(Y \neq 0\) a.s.), \(|X|\), and \(\min\{X,Y\}\) are random variables.
Deduce that any finite linear combination of random variables is a random variable.

## III. Discrete Distributions
1. **Exercise 3.1.1** (_Probability Mass Functions_)

For each family decide the constant \(c\) that makes \(p_k\) a probability mass function:
(a) \(p_k = c\,2^{-k}\) for \(k \ge 0\); (b) \(p_k = c\,2^{-k}/k\) for \(k \ge 1\);
(c) \(p_k = c/k^2\) for \(k \ge 1\); (d) \(p_k = c\,k\,2^{-k}\) for \(k \ge 0\).

2. **Exercise 3.1.2** (_Probability Mass Functions_)

Let \(X\) take values \(1,2,\dots\) with \(\mathbb{P}(X=k)=2^{-k}\).
Compute \(\mathbb{P}(X \text{ is even})\), \(\mathbb{E}[X]\), and \(\mathrm{Var}(X)\).

3. **Exercise 3.2.1** (_Independence_)

Let \(X\) and \(Y\) be independent Rademacher random variables and set \(Z=XY\).
Show every pair of \(X,Y,Z\) is independent but the triple is not jointly independent.

4. **Exercise 3.2.5** (_Independence_)

Suppose \((X_1,\dots,X_n)\) and \((-X_1,\dots,-X_n)\) share the same distribution.
Show \(\mathbb{E}[X_i]=0\) for every \(i\).

5. **Exercise 3.4.1** (_Indicators and Matching_)

Let \(\pi\) be a uniform random permutation of \(n\). Write \(M\) for the number of fixed points.
Show \(\mathbb{E}[M]=1\) and \(\mathbb{P}(M=0)\to e^{-1}\).

6. **Exercise 3.4.2** (_Indicators and Matching_)

With \(M\) as above, compute \(\mathrm{Var}(M)\).

7. **Exercise 3.5.1** (_Multinomial Model_)

Show that the multinomial probability mass function is
\(\mathbb{P}(N_1=n_1,\dots,N_r=n_r) = \frac{n!}{n_1!\cdots n_r!} p_1^{n_1}\cdots p_r^{n_r}\) when \(\sum_i n_i = n\).

8. **Exercise 3.5.2** (_Splitting a Poisson Process_)

If \(N\sim\mathrm{Poisson}(\lambda)\) and each event is independently retained with probability \(p\), show the number retained is \(\mathrm{Poisson}(\lambda p)\).

9. **Exercise 3.6.2** (_Marginals of the Multinomial_)

Show that each component \(N_i\) of a multinomial vector is \(\mathrm{Binomial}(n,p_i)\).

10. **Exercise 3.6.3** (_Heavy Tails_)

Let \(X\) have \(\mathbb{P}(X=k)=1/(k(k+1))\) for \(k \ge 1\). Compute \(\mathbb{P}(X>n)\) and decide whether \(\mathbb{E}[X]\) exists.

11. **Exercise 3.7.1** (_Conditional Expectation_)

Let \(X,Y,Z\) be integrable. Show \(\mathbb{E}[aY+bZ\mid X] = a\mathbb{E}[Y\mid X]+b\mathbb{E}[Z\mid X]\).

12. **Exercise 3.7.2** (_Uniqueness_)

If both \(g(X)\) and \(h(X)\) are versions of \(\mathbb{E}[Y\mid X]\), show \(g(X)=h(X)\) almost surely.

13. **Exercise 3.8.1** (_Discrete Convolution_)

Let \(X\sim\mathrm{Uniform}\{0,\dots,m\}\) and \(Y\sim\mathrm{Uniform}\{0,\dots,n\}\) be independent.
Find \(\mathbb{P}(X+Y=k)\).

14. **Exercise 3.8.2** (_Negative Binomial_)

Let \(X\) and \(Y\) be independent geometric(\(p\)) variables supported on \(\{1,2,\dots\}\).
Show \(X+Y\) is negative binomial with parameters \(2\) and \(p\).

15. **Exercise 3.9.1** (_Random Walk_)

For simple symmetric random walk \((S_n)\), compute \(\mathbb{P}(S_{2n}=0)\).

## IV. Expectation and Variance
1. **Exercise 3.3.1** (_Geometric Moments_)

Let \(X\) be geometric with support \(\{0,1,2,\dots\}\) and parameter \(p\), so \(\mathbb{P}(X=k)=(1-p)^k p\).
Compute \(\mathbb{E}[X]\) and \(\mathrm{Var}(X)\).

2. **Exercise 3.3.2** (_Poisson Moments_)

Suppose \(M_X(t)=\exp\{\lambda (e^t-1)\}\). Show \(\mathbb{E}[X]=\lambda\) and \(\mathrm{Var}(X)=\lambda\).

3. **Exercise 3.3.3** (_Factorial Moment_)

For \(X\sim\mathrm{Poisson}(\lambda)\), compute \(\mathbb{E}[X(X-1)]\).

4. **Exercise 4.3.1** (_Polynomial Density_)

Let \(X\) have density \(f(x)=3x^2\) on \([0,1]\). Find \(\mathbb{E}[X]\) and \(\mathrm{Var}(X)\).

5. **Exercise 4.3.2** (_Rayleigh Distribution_)

If \(X\) has density \(f(x)=2x e^{-x^2}\) for \(x>0\), evaluate \(\mathbb{E}[X]\) and \(\mathbb{E}[X^2]\).

6. **Exercise 4.8.1** (_Sum of Exponentials_)

Let \(X,Y\) be independent \(\mathrm{Exp}(\lambda)\) random variables. Determine the distribution, mean, and variance of \(X+Y\).

7. **Exercise 4.8.2** (_Extrema of Exponentials_)

For \(X,Y\sim\mathrm{Exp}(\lambda)\) independent, compute \(\mathbb{E}[\min(X,Y)]\) and \(\mathbb{E}[\max(X,Y)]\).

8. **Exercise 5.6.1** (_Sample Mean_)

Let \(X_1,\dots,X_n\) be i.i.d. with mean \(\mu\) and variance \(\sigma^2\). Show \(\mathbb{E}[\bar{X}]=\mu\) and \(\mathrm{Var}(\bar{X})=\sigma^2/n\).

9. **Exercise 5.6.2** (_Sum of i.i.d._)

With \(X_i\) as above, evaluate \(\mathrm{Var}(\sum_{i=1}^n X_i)\).

10. **Exercise 5.6.3** (_Normal Sample Mean_)

If \(X_i\sim\mathcal{N}(\mu,\sigma^2)\) i.i.d., determine the distribution of \(\bar{X}\).

11. **Exercise 5.7.1** (_Sum of Poisson Variables_)

Show that the sum of independent \(\mathrm{Poisson}(\lambda_i)\) variables is \(\mathrm{Poisson}(\sum_i \lambda_i)\).

12. **Exercise 5.7.2** (_Sum of Normals_)

Let \(X\sim\mathcal{N}(\mu_1,\sigma_1^2)\) and \(Y\sim\mathcal{N}(\mu_2,\sigma_2^2)\) be independent.
Show \(X+Y\sim\mathcal{N}(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)\).

13. **Exercise 5.7.3** (_Law of Total Expectation_)

Prove \(\mathbb{E}[X]=\mathbb{E}[\mathbb{E}[X\mid Y]]\) for integrable \(X\).

14. **Exercise 5.8.1** (_Characteristic Function_)

Suppose \(\varphi_X(t)=e^{-t^2/2}\). Identify the distribution of \(X\).

15. **Exercise 5.8.2** (_Jensen's Inequality_)

Let \(g\) be convex and \(X\) integrable. Show \(g(\mathbb{E}[X]) \le \mathbb{E}[g(X)]\).

## V. Continuous Distributions
1. **Exercise 4.1.1** (_Normalising a Density_)

Let \(f(x)=c x^2\) on \([0,1]\) and 0 otherwise. Determine \(c\) and the distribution function \(F\).

2. **Exercise 4.1.2** (_Tail Behaviour_)

Let \(f(x)=1/(1+x)^2\) for \(x\ge 0\) and 0 otherwise. Find \(F(x)\) and decide whether \(\mathbb{E}[X]\) is finite.

3. **Exercise 4.2.1** (_Independence Check_)

Suppose \(f_{X,Y}(x,y)=4xy\) on \([0,1]^2\). Find the marginals and conclude whether \(X\) and \(Y\) are independent.

4. **Exercise 4.2.2** (_Sum of Independent Exponentials_)

Let \(X,Y\) be independent with joint density \(\lambda^2 e^{-\lambda (x+y)}\) on \(x,y>0\).
Find the density of \(S=X+Y\).

5. **Exercise 4.4.1** (_Gamma Function_)

Show \(\Gamma(n)=\int_0^\infty x^{n-1} e^{-x}\,dx = (n-1)!\) for integer \(n\ge1\).

6. **Exercise 4.4.2** (_Beta Function_)

Prove \(B(a,b)=\int_0^1 x^{a-1}(1-x)^{b-1}\,dx = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}\).

7. **Exercise 4.4.3** (_Exponential Median_)

Let \(X\sim\mathrm{Exp}(\lambda)\). Find the median of \(X\).

8. **Exercise 4.5.2** (_Covariance of Exponentials_)

For independent \(X,Y\sim\mathrm{Exp}(\lambda)\), compute \(\mathbb{P}(X>Y)\) and \(\operatorname{Cov}(X,Y)\).

9. **Exercise 4.5.3** (_Min and Max of Uniforms_)

If \(X,Y\) are i.i.d. uniform on \([0,1]\), find the distribution of \(U=\min(X,Y)\) and \(V=\max(X,Y)\).

10. **Exercise 4.5.4** (_Sum of Uniforms_)

For \(X,Y\) as above, compute \(\mathbb{P}(X+Y \le 1)\).

11. **Exercise 4.6.1** (_Conditional Density_)

Let \(f_{X,Y}(x,y)=2\) on the triangle \(0<y<x<1\). Find the conditional density of \(Y\) given \(X=x\).

12. **Exercise 4.6.2** (_Conditional Expectation_)

Using the density in the previous problem, compute \(\mathbb{E}[Y\mid X=x]\).

13. **Exercise 4.6.3** (_Conditioning on a Sum_)

Let \(X,Y\) be independent exponentials with parameter \(\lambda\). Determine the conditional distribution of \(X\) given \(X+Y=s\).

14. **Exercise 4.7.1** (_Sine Transformation_)

Let \(X\sim\mathrm{Uniform}[0,\pi]\). Find the density of \(Y=\sin X\).

15. **Exercise 4.7.2** (_Polar Coordinates_)

Let \(X,Y\) be independent \(\mathcal{N}(0,1)\). Find the density of \(R=\sqrt{X^2+Y^2}\).

## VI. Sampling Distributions
1. **Exercise 4.10.2** (_Adding Chi-squared Variables_)

Let \(U\sim\chi^2_{m}\) and \(V\sim\chi^2_{n}\) be independent. Show \(U+V\sim\chi^2_{m+n}\).

2. **Exercise 4.10.3** (_Student's t Moments_)

For a Student's \(t_\nu\) distribution with \(\nu>2\), compute \(\mathbb{E}[T]\) and \(\mathrm{Var}(T)\).

3. **Exercise 4.10.5** (_Normal Samples_)

Let \(X_1,\dots,X_n\) be i.i.d. \(\mathcal{N}(\mu,\sigma^2)\). Show that \(\bar{X}\) and \(S^2 = \frac{1}{n-1}\sum (X_i-\bar{X})^2\) are independent.

4. **Exercise 4.10.6** (_Scaled Sample Variance_)

Under the assumptions above, prove \((n-1)S^2/\sigma^2 \sim \chi^2_{n-1}\).

5. **Exercise 4.11.1** (_Inverse Transform Sampling_)

Describe how to generate a discrete uniform variable on \(\{1,\dots,n\}\) from \(U\sim\mathrm{Uniform}(0,1)\).

6. **Exercise 4.11.2** (_Fisher–Yates Shuffle_)

Outline the Fisher–Yates algorithm for sampling a random permutation of \(n\) items.

7. **Exercise 4.11.3** (_Generating Exponentials_)

Show that if \(U\sim\mathrm{Uniform}(0,1)\) then \(X=-\log(1-U)/\lambda\) has the \(\mathrm{Exp}(\lambda)\) distribution.

8. **Exercise 4.11.4** (_Acceptance–Rejection_)

Suppose \(f\) is bounded by \(M g\) for a density \(g\). Describe the acceptance–rejection algorithm to sample from \(f\).

9. **Exercise 4.11.5** (_Acceptance Probability_)

In the acceptance–rejection scheme above, show that the overall acceptance probability is \(1/M\).

10. **Exercise 4.11.6** (_Mixture Sampling_)

Given a mixture density \(f=\sum_{i=1}^k w_i f_i\), explain how to sample from \(f\) using composition.

11. **Exercise 5.10.1** (_CLT Approximation_)

Let \(X_1,\dots,X_n\) be i.i.d. with mean \(\mu\) and variance \(\sigma^2\). Use the central limit theorem to approximate \(\mathbb{P}(|\bar{X}-\mu| \le \varepsilon)\) for large \(n\).

12. **Exercise 5.10.2** (_Binomial Normal Approximation_)

For \(X\sim\mathrm{Binomial}(n,p)\) with large \(n\), give the normal approximation to \(\mathbb{P}(X \le k)\).

13. **Exercise 5.10.3** (_Asymptotic Normality of the Mean_)

State the central limit theorem for the sample mean of i.i.d. observations with finite variance.

14. **Exercise 5.11.1** (_Chernoff Bound_)

Let \(S_n=\sum_{i=1}^n X_i\) with independent Bernoulli(\(p\)) summands. Show that for any \(t>0\),
\(\mathbb{P}(S_n \ge np + t) \le \exp\{-n D(p+t/n\Vert p)\}\), where \(D\) is the Kullback–Leibler divergence.

15. **Exercise 5.11.2** (_Hoeffding's Inequality_)

State Hoeffding's inequality for bounded independent variables and apply it to \(S_n\) as above.
