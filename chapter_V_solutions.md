# Solutions — V. Continuous Distributions
1. **Exercise 4.1.1** (_Normalising a Density_)
\(c^{-1}=\int_0^1 x^2\,dx = 1/3\), so \(c=3\). Consequently \(F(x)=0\) for \(x<0\), equals \(x^3\) on \([0,1]\), and is 1 for \(x\ge1\).

2. **Exercise 4.1.2** (_Tail Behaviour_)
\(F(x)=1-1/(1+x)\). The expectation equals \(\int_0^\infty x/(1+x)^2\,dx\), which diverges; hence \(\mathbb{E}[X]=\infty\).

3. **Exercise 4.2.1** (_Independence Check_)
\(f_X(x)=\int_0^1 4xy\,dy=2x\), \(f_Y(y)=2y\). Because \(f_{X,Y}(x,y)=f_X(x)f_Y(y)\), the variables are independent.

4. **Exercise 4.2.2** (_Sum of Independent Exponentials_)
Convolution yields \(f_S(s)=\int_0^s \lambda^2 e^{-\lambda s}\,du = \lambda^2 s e^{-\lambda s}\), \(s>0\), the gamma(2,\(\lambda\)) density.

5. **Exercise 4.4.1** (_Gamma Function_)
Integrate by parts to obtain the recursion \(\Gamma(n+1)=n\Gamma(n)\) with \(\Gamma(1)=1\).

6. **Exercise 4.4.2** (_Beta Function_)
Use the substitution \(x=u/(u+v)\) and the definition of the gamma function to express the integral as \(\Gamma(a)\Gamma(b)/\Gamma(a+b)\).

7. **Exercise 4.4.3** (_Exponential Median_)
Solve \(1-e^{-\lambda m}=1/2\) to obtain \(m=(\log 2)/\lambda\).

8. **Exercise 4.5.2** (_Covariance of Exponentials_)
Symmetry gives \(\mathbb{P}(X>Y)=1/2\). Independence yields \(\operatorname{Cov}(X,Y)=0\).

9. **Exercise 4.5.3** (_Min and Max of Uniforms_)
\(\mathbb{P}(U>u)=(1-u)^2\) for \(0\le u\le1\), so \(f_U(u)=2(1-u)\). Similarly \(\mathbb{P}(V\le v)=v^2\) giving \(f_V(v)=2v\).

10. **Exercise 4.5.4** (_Sum of Uniforms_)
The region \(x+y\le1\) inside the unit square has area \(1/2\), hence the probability is \(1/2\).

11. **Exercise 4.6.1** (_Conditional Density_)
The marginal \(f_X(x)=\int_0^x 2\,dy = 2x\). Therefore \(f_{Y\mid X}(y\mid x)=\frac{2}{2x}=\frac{1}{x}\) for \(0<y<x\), i.e. uniform on \([0,x]\).

12. **Exercise 4.6.2** (_Conditional Expectation_)
Since the conditional density is uniform on \([0,x]\), \(\mathbb{E}[Y\mid X=x]=x/2\).

13. **Exercise 4.6.3** (_Conditioning on a Sum_)
The joint density of \((X,X+Y)\) shows that conditional on \(X+Y=s\), \(X\) is uniform on \([0,s]\).

14. **Exercise 4.7.1** (_Sine Transformation_)
For \(y\in(-1,1)\), two pre-images exist. Using the change of variables formula gives \(f_Y(y)=\frac{1}{\pi\sqrt{1-y^2}}\).

15. **Exercise 4.7.2** (_Polar Coordinates_)
Transform to polar coordinates: the joint density is \((2\pi)^{-1} e^{-r^2/2} r\). After integrating over the angle, \(f_R(r)=r e^{-r^2/2}\) for \(r\ge0\) (a Rayleigh density).
