# Solutions — II. Random Variables
1. **Exercise 2.1.1** (_Random Variables_)
For \(a>0\), \(\{aX \le x\} = \{X \le x/a\}\); for \(a<0\), \(\{aX \le x\} = \{X \ge x/a\}\) which is a countable intersection of events
\(\{X \le x/a + 1/m\}\). If \(a=0\) the event is \(\emptyset\) or \(\Omega\).
Thus \(aX\) is measurable. Setting \(a=0\) and \(a=2\) yields the final statements.

2. **Exercise 2.1.2** (_Random Variables_)
If \(a>0\), \(F_Y(y)=F((y-b)/a)\). If \(a<0\), \(F_Y(y)=1-\lim_{x \uparrow (y-b)/a} F(x)\). When \(a=0\), \(Y\) is degenerate at \(b\).

3. **Exercise 2.1.3** (_Random Variables_)
Independence gives \(p^k(1-p)^{n-k}\) for any particular sequence and there are \(\binom{n}{k}\) such sequences.

4. **Exercise 2.2.1** (_Law of Averages_)
Let \(R\) be the reported answer. Then \(\mathbb{P}(R=\text{yes}) = q + (1-q)/2 = (1+q)/2\).
If \(\bar{R}\) is the sample mean of indicators of “yes”, the estimator \(\hat{q}=2\bar{R}-1\) is unbiased with variance \((1-q^2)/N\) for \(N\) responses.

5. **Exercise 2.2.2** (_Law of Averages_)
Because \(H_n-T_n = 2H_n-n\), the deviation is \(|H_n/n - p| > \varepsilon/2\).
Hoeffding's inequality yields the bound \(2\exp(-2n(\varepsilon/2)^2) = 2e^{-2n\varepsilon^2}\).

6. **Exercise 2.3.1** (_Discrete and Continuous Variables_)
For \(x \in [a_{m-1},a_m)\), \(|G(x)-F(x)| \le |F(a_m)-F(a_{m-1})|\). Right-continuity ensures this bound tends to zero as the mesh shrinks, yielding convergence.

7. **Exercise 2.3.2** (_Discrete and Continuous Variables_)
The inverse \(g^{-1}\) exists and is continuous, so \(\{Y\le y\} = \{X \le g^{-1}(y)\}\) is measurable. Values outside the range correspond to \(\emptyset\) or \(\Omega\).

8. **Exercise 2.3.3** (_Discrete and Continuous Variables_)
For any \(y\), \(\mathbb{P}(Y \le y) = \mathbb{P}(X \le F(y)) = F(y)\). Strict monotonicity of \(F\) ensures the inverse is well defined.

9. **Exercise 2.4.1** (_Worked Examples_)
(a) \(\mathbb{P}(X^2 \le y) = F(\sqrt{y})-F(-\sqrt{y}^{-})\) for \(y\ge0\).
(b) \(\mathbb{P}(\sqrt{X}\le y)=F(y^2)\) for \(y\ge0\).
(c) Use periodicity: sum contributions over intervals where \(\sin\) is monotone.
(d) \(\mathbb{P}(G^{-1}(X)\le y)=F(G(y))\).
(e) \(F(X)\) is uniform on \([0,1]\).
(f) Combining (d) and (e) shows the distribution is \(G\).

10. **Exercise 2.4.2** (_Worked Examples_)
For \(Y\), \(F_Y(y)=0\) if \(y<a\), equals \(F(y)\) on \([a,b)\), and is \(1\) for \(y\ge b\), with point masses at \(a\) and \(b\).
For \(Z\), \(F_Z(y)=0\) when \(y<0\); \(F_Z(0)=F(a^-)+1-F(b)\); and for \(0<y\le b\), \(F_Z(y)=F(y)-F(a^-)\).

11. **Exercise 2.5.1** (_Random Vectors_)
Both marginals are Bernoulli(1/2). Since \(\mathbb{P}(X=1,W=1)=1/4\neq(1/2)^2\), the variables are dependent.

12. **Exercise 2.5.2** (_Random Vectors_)
\(X\sim\mathrm{Bernoulli}(p)\) and \(Y\sim\mathrm{Bernoulli}(1-p)\) while \(XY=0\) almost surely.
Hence \(\operatorname{Cov}(X,Y)=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]=-p(1-p).

13. **Exercise 2.5.3** (_Random Vectors_)
Integrating in \(x\) gives \(\int_0^{\infty} e^{-x}\,dx=1\).
In \(y\), \(\int_0^{\infty} \frac{1}{y(1+y^2)}\,dy = 1\) by substitution. Hence the joint density integrates to one.
The marginals are \(f_X(x)=e^{-x}\) for \(x>0\) and \(f_Y(y)=1/(y(1+y^2))\) for \(y>0\).

14. **Exercise 2.7.2** (_Problems_)
For each \(\omega\), the interval containing \(X(\omega)\) shrinks with length <\(2^{-m}\), so \(|X(\omega)-X_m(\omega)|<2^{-m}\).
Taking limits yields the statement about inverse images.

15. **Exercise 2.7.3** (_Problems_)
The maps \((x,y)\mapsto xy\), \((x,y)\mapsto x/y\) (on \(y\neq0\)), \(x\mapsto|x|\), and \((x,y)\mapsto\min\{x,y\}\) are continuous.
Composition of measurable functions with continuous functions is measurable, yielding the claim for sums.
