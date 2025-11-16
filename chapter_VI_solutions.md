# Solutions — VI. Sampling Distributions
1. **Exercise 4.10.2** (_Adding Chi-squared Variables_)
The mgf of \(\chi^2_k\) is \((1-2t)^{-k/2}\). Multiplying the mgfs of \(U\) and \(V\) yields \((1-2t)^{-(m+n)/2}\), the mgf of \(\chi^2_{m+n}\).

2. **Exercise 4.10.3** (_Student's t Moments_)
Symmetry gives mean zero. The variance exists for \(\nu>2\) and equals \(\nu/(\nu-2)\).

3. **Exercise 4.10.5** (_Normal Samples_)
Express the vector of centered observations via an orthogonal transformation; one coordinate equals \(\bar{X}\) while the remaining \(n-1\) coordinates are independent standard normals scaled by \(\sigma\). Independence follows because multivariate normals are independent when uncorrelated.

4. **Exercise 4.10.6** (_Scaled Sample Variance_)
The \(n-1\) centered orthogonal coordinates are independent \(\mathcal{N}(0,\sigma^2)\); their squared sum divided by \(\sigma^2\) is \(\chi^2_{n-1}\).

5. **Exercise 4.11.1** (_Inverse Transform Sampling_)
Partition \((0,1)\) into \(n\) subintervals of length \(1/n\) and return the index of the subinterval containing \(U\).

6. **Exercise 4.11.2** (_Fisher–Yates Shuffle_)
Iterate for \(k=n,\dots,2\): pick \(J\sim\mathrm{Uniform}\{1,\dots,k\}\) and swap positions \(J\) and \(k\). The result is uniform over all \(n!\) permutations.

7. **Exercise 4.11.3** (_Generating Exponentials_)
Compute \(\mathbb{P}(X \le x) = \mathbb{P}(U \ge 1-e^{-\lambda x}) = 1-e^{-\lambda x}\).

8. **Exercise 4.11.4** (_Acceptance–Rejection_)
Draw \(Y \sim g\) and \(U\sim\mathrm{Uniform}(0,1)\). Accept \(Y\) as a sample from \(f\) if \(U \le f(Y)/(Mg(Y))\); otherwise repeat.

9. **Exercise 4.11.5** (_Acceptance Probability_)
Conditioning on \(Y\) gives acceptance probability \(\int f(y)\,dy / M = 1/M\).

10. **Exercise 4.11.6** (_Mixture Sampling_)
Select component \(I\) with probabilities \(w_i\), then draw from \(f_I\). The resulting sample has density \(f\).

11. **Exercise 5.10.1** (_CLT Approximation_)
Standardise: \(\sqrt{n}(\bar{X}-\mu)/\sigma \Rightarrow \mathcal{N}(0,1)\). Hence \(\mathbb{P}(|\bar{X}-\mu|\le\varepsilon) \approx \Phi\left(\tfrac{\sqrt{n}\varepsilon}{\sigma}\right)-\Phi\left(-\tfrac{\sqrt{n}\varepsilon}{\sigma}\right)\).

12. **Exercise 5.10.2** (_Binomial Normal Approximation_)
Use \(X\) approximately \(\mathcal{N}(np,np(1-p))\) together with a continuity correction: \(\mathbb{P}(X\le k) \approx \Phi\left(\frac{k+0.5-np}{\sqrt{np(1-p)}}\right).

13. **Exercise 5.10.3** (_Asymptotic Normality of the Mean_)
If \(X_i\) are i.i.d. with mean \(\mu\) and variance \(\sigma^2\), then \(\sqrt{n}(\bar{X}-\mu)/\sigma \Rightarrow \mathcal{N}(0,1)\) as \(n\to\infty\).

14. **Exercise 5.11.1** (_Chernoff Bound_)
Optimise the mgf bound \(\mathbb{P}(S_n\ge np+t) \le \inf_{\theta>0} e^{-\theta(np+t)}(pe^{\theta}+1-p)^n\); the minimiser yields the divergence expression.

15. **Exercise 5.11.2** (_Hoeffding's Inequality_)
If \(X_i\in[a_i,b_i]\), then \(\mathbb{P}(\bar{X}-\mathbb{E}[\bar{X}]\ge \varepsilon) \le \exp\left(-\frac{2n^2 \varepsilon^2}{\sum (b_i-a_i)^2}\right)\).
For Bernoulli(\(p\)) variables this gives \(\mathbb{P}(S_n-np\ge t)\le \exp(-2t^2/n)\).
