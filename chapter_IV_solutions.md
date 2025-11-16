# Solutions — IV. Expectation and Variance
1. **Exercise 3.3.1** (_Geometric Moments_)
Using the pgf \(G(s)=\frac{ps}{1-(1-p)s}\), differentiate at \(s=1\) to obtain \(\mathbb{E}[X]=(1-p)/p\) and \(\mathrm{Var}(X)=(1-p)/p^2\).

2. **Exercise 3.3.2** (_Poisson Moments_)
Because \(M'_X(0)=\lambda\) and \(M''_X(0)=\lambda^2+\lambda\), we deduce \(\mathrm{Var}(X)=M''_X(0)-M'_X(0)^2=\lambda\).

3. **Exercise 3.3.3** (_Factorial Moment_)
Differentiate the mgf twice to get \(M''_X(0)=\lambda^2\); this equals \(\mathbb{E}[X(X-1)]\).

4. **Exercise 4.3.1** (_Polynomial Density_)
Compute \(\mathbb{E}[X]=\int_0^1 3x^3\,dx = 3/4\) and \(\mathbb{E}[X^2]=\int_0^1 3x^4\,dx = 3/5\); therefore \(\mathrm{Var}(X)=3/5-(3/4)^2=3/80\).

5. **Exercise 4.3.2** (_Rayleigh Distribution_)
Substitute \(u=x^2\): \(\mathbb{E}[X]=\int_0^\infty 2x^2 e^{-x^2}\,dx = \sqrt{\pi}/2\) and \(\mathbb{E}[X^2]=\int_0^\infty 2x^3 e^{-x^2}\,dx = 1\).

6. **Exercise 4.8.1** (_Sum of Exponentials_)
\(X+Y\) is gamma with shape 2 and rate \(\lambda\), so \(f_{X+Y}(x)=\lambda^2 x e^{-\lambda x}\) for \(x>0\).
The mean equals \(2/\lambda\) and the variance equals \(2/\lambda^2\).

7. **Exercise 4.8.2** (_Extrema of Exponentials_)
The minimum has rate \(2\lambda\) and mean \(1/(2\lambda)\). Since \(X+Y=\min+\max\) with mean \(2/\lambda\), we obtain \(\mathbb{E}[\max]=3/(2\lambda)\).

8. **Exercise 5.6.1** (_Sample Mean_)
Linearity and independence yield the stated expressions immediately.

9. **Exercise 5.6.2** (_Sum of i.i.d._)
Independence implies the variance of the sum is \(n\sigma^2\).

10. **Exercise 5.6.3** (_Normal Sample Mean_)
The mgf of \(\bar{X}\) is \(\exp(\mu t + \tfrac{1}{2}(\sigma^2/n)t^2)\), identifying \(\bar{X}\) as \(\mathcal{N}(\mu,\sigma^2/n)\).

11. **Exercise 5.7.1** (_Sum of Poisson Variables_)
The product of the mgfs \(\exp\{\lambda_i(e^t-1)\}\) equals \(\exp\{(\sum_i \lambda_i)(e^t-1)\}\).

12. **Exercise 5.7.2** (_Sum of Normals_)
Multiply the mgfs of \(X\) and \(Y\): the result is \(\exp((\mu_1+\mu_2)t + \tfrac{1}{2}(\sigma_1^2+\sigma_2^2)t^2)\).

13. **Exercise 5.7.3** (_Law of Total Expectation_)
Take expectations in the defining relation \(\mathbb{E}[X\mathbf{1}_A]=\mathbb{E}[\mathbb{E}[X\mid Y]\mathbf{1}_A]\) with \(A=\Omega\).

14. **Exercise 5.8.1** (_Characteristic Function_)
This is the characteristic function of \(\mathcal{N}(0,1)\).

15. **Exercise 5.8.2** (_Jensen's Inequality_)
Use supporting hyperplanes: \(g(y) \ge ay+b\) with equality at \(y=\mathbb{E}[X]\). Taking expectations gives the inequality.
