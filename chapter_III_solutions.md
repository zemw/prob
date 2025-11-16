# Solutions — III. Discrete Distributions
1. **Exercise 3.1.1** (_Probability Mass Functions_)
(a) \(c=1/2\). (b) Use \(\sum_{k\ge1} 2^{-k}/k = \log 2\) giving \(c=1/\log 2\).
(c) \(c = 6/\pi^2\). (d) \(c = 1/2\) since \(\sum k2^{-k}=2\).

2. **Exercise 3.1.2** (_Probability Mass Functions_)
\(\mathbb{P}(X \text{ even}) = \sum_{m\ge1}2^{-2m}=1/3\).
The pgf \(G(s)=s/(2-s)\) gives \(\mathbb{E}[X]=G'(1)=2\) and \(\mathbb{E}[X^2]=G''(1)+G'(1)=6\), so \(\mathrm{Var}(X)=2\).

3. **Exercise 3.2.1** (_Independence_)
Pairs have joint mass \(1/4\), matching the product of marginals.
However \(\mathbb{P}(X=1,Y=1,Z=1)=1/4\neq(1/2)^3\), so the three are dependent.

4. **Exercise 3.2.5** (_Independence_)
Take expectations and use symmetry: \(\mathbb{E}[X_i]=\mathbb{E}[-X_i]\). Hence \(\mathbb{E}[X_i]=0\).

5. **Exercise 3.4.1** (_Indicators and Matching_)
\(M=\sum_{i=1}^n I_i\) with \(I_i=\mathbf{1}_{\{\pi(i)=i\}}\) and \(\mathbb{E}[I_i]=1/n\), giving \(\mathbb{E}[M]=1\).
Inclusion–exclusion shows \(\mathbb{P}(M=0) = 1 - 1 + 1/2! - \cdots + (-1)^n/n!\to e^{-1}\).

6. **Exercise 3.4.2** (_Indicators and Matching_)
Use \(\mathrm{Var}(M)=\sum_i \mathrm{Var}(I_i)+2\sum_{i<j}\mathrm{Cov}(I_i,I_j)\).
Since \(\mathbb{P}(\pi(i)=i,\pi(j)=j)=1/(n(n-1))\), the covariance equals \(-1/n^2(n-1)\) and the variance simplifies to 1.

7. **Exercise 3.5.1** (_Multinomial Model_)
Count sequences with specified counts: there are \(n!/(n_1!\cdots n_r!)\) such sequences, each occurring with probability \(p_1^{n_1}\cdots p_r^{n_r}\).

8. **Exercise 3.5.2** (_Splitting a Poisson Process_)
Condition on \(N=n\); the retained count is \(\mathrm{Binomial}(n,p)\). Summing \(\sum_n e^{-\lambda}\lambda^n/n!\binom{n}{k}p^k(1-p)^{n-k}\) yields \(e^{-\lambda p}(\lambda p)^k/k!\).

9. **Exercise 3.6.2** (_Marginals of the Multinomial_)
Sum the multinomial pmf over the remaining indices to obtain the binomial pmf.

10. **Exercise 3.6.3** (_Heavy Tails_)
Telescoping gives \(\mathbb{P}(X>n)=1/(n+1)\). The mean diverges because \(\sum_k k/(k(k+1)) = \sum 1/(k+1) = \infty\).

11. **Exercise 3.7.1** (_Conditional Expectation_)
Linearity follows from testing against bounded measurable functions of \(X\) in the defining property of conditional expectation.

12. **Exercise 3.7.2** (_Uniqueness_)
For any bounded measurable \(\varphi\), \(\mathbb{E}[(g-h)(X)\varphi(X)]=0\).
Choosing indicator functions of generating sets implies \(g(X)=h(X)\) a.s.

13. **Exercise 3.8.1** (_Discrete Convolution_)
Count integer solutions \((i,j)\) to \(i+j=k\) with \(0\le i\le m\), \(0\le j\le n\); the count is
\(\max(0, \min(k,m) - \max(0,k-n) + 1)\). Divide by \((m+1)(n+1)\).

14. **Exercise 3.8.2** (_Negative Binomial_)
\(\mathbb{P}(X+Y=k) = \sum_{j=1}^{k-1} p^2 (1-p)^{k-2} = (k-1)p^2(1-p)^{k-2}\), the negative binomial pmf.

15. **Exercise 3.9.1** (_Random Walk_)
Exactly \(n\) up-steps are needed, giving \(\binom{2n}{n} 2^{-2n}\).
