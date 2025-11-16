from pathlib import Path
from build_documents import Problem, Chapter, write_documents
import build_documents
import generate_docs

additional_chapters: list[Chapter] = [
    Chapter(
        name="IV. Expectation and Variance",
        slug="chapter_IV",
        problems=[
            Problem(
                id="3.3.1",
                title="Geometric Moments",
                problem=r"""Let \(X\) be geometric with support \(\{0,1,2,\dots\}\) and parameter \(p\), so \(\mathbb{P}(X=k)=(1-p)^k p\).
Compute \(\mathbb{E}[X]\) and \(\mathrm{Var}(X)\).""",
                solution=r"""Using the pgf \(G(s)=\frac{ps}{1-(1-p)s}\), differentiate at \(s=1\) to obtain \(\mathbb{E}[X]=(1-p)/p\) and \(\mathrm{Var}(X)=(1-p)/p^2\).""",
            ),
            Problem(
                id="3.3.2",
                title="Poisson Moments",
                problem=r"""Suppose \(M_X(t)=\exp\{\lambda (e^t-1)\}\). Show \(\mathbb{E}[X]=\lambda\) and \(\mathrm{Var}(X)=\lambda\).""",
                solution=r"""Because \(M'_X(0)=\lambda\) and \(M''_X(0)=\lambda^2+\lambda\), we deduce \(\mathrm{Var}(X)=M''_X(0)-M'_X(0)^2=\lambda\).""",
            ),
            Problem(
                id="3.3.3",
                title="Factorial Moment",
                problem=r"""For \(X\sim\mathrm{Poisson}(\lambda)\), compute \(\mathbb{E}[X(X-1)]\).""",
                solution=r"""Differentiate the mgf twice to get \(M''_X(0)=\lambda^2\); this equals \(\mathbb{E}[X(X-1)]\).""",
            ),
            Problem(
                id="4.3.1",
                title="Polynomial Density",
                problem=r"""Let \(X\) have density \(f(x)=3x^2\) on \([0,1]\). Find \(\mathbb{E}[X]\) and \(\mathrm{Var}(X)\).""",
                solution=r"""Compute \(\mathbb{E}[X]=\int_0^1 3x^3\,dx = 3/4\) and \(\mathbb{E}[X^2]=\int_0^1 3x^4\,dx = 3/5\); therefore \(\mathrm{Var}(X)=3/5-(3/4)^2=3/80\).""",
            ),
            Problem(
                id="4.3.2",
                title="Rayleigh Distribution",
                problem=r"""If \(X\) has density \(f(x)=2x e^{-x^2}\) for \(x>0\), evaluate \(\mathbb{E}[X]\) and \(\mathbb{E}[X^2]\).""",
                solution=r"""Substitute \(u=x^2\): \(\mathbb{E}[X]=\int_0^\infty 2x^2 e^{-x^2}\,dx = \sqrt{\pi}/2\) and \(\mathbb{E}[X^2]=\int_0^\infty 2x^3 e^{-x^2}\,dx = 1\).""",
            ),
            Problem(
                id="4.8.1",
                title="Sum of Exponentials",
                problem=r"""Let \(X,Y\) be independent \(\mathrm{Exp}(\lambda)\) random variables. Determine the distribution, mean, and variance of \(X+Y\).""",
                solution=r"""\(X+Y\) is gamma with shape 2 and rate \(\lambda\), so \(f_{X+Y}(x)=\lambda^2 x e^{-\lambda x}\) for \(x>0\).
The mean equals \(2/\lambda\) and the variance equals \(2/\lambda^2\).""",
            ),
            Problem(
                id="4.8.2",
                title="Extrema of Exponentials",
                problem=r"""For \(X,Y\sim\mathrm{Exp}(\lambda)\) independent, compute \(\mathbb{E}[\min(X,Y)]\) and \(\mathbb{E}[\max(X,Y)]\).""",
                solution=r"""The minimum has rate \(2\lambda\) and mean \(1/(2\lambda)\). Since \(X+Y=\min+\max\) with mean \(2/\lambda\), we obtain \(\mathbb{E}[\max]=3/(2\lambda)\).""",
            ),
            Problem(
                id="5.6.1",
                title="Sample Mean",
                problem=r"""Let \(X_1,\dots,X_n\) be i.i.d. with mean \(\mu\) and variance \(\sigma^2\). Show \(\mathbb{E}[\bar{X}]=\mu\) and \(\mathrm{Var}(\bar{X})=\sigma^2/n\).""",
                solution=r"""Linearity and independence yield the stated expressions immediately.""",
            ),
            Problem(
                id="5.6.2",
                title="Sum of i.i.d.",
                problem=r"""With \(X_i\) as above, evaluate \(\mathrm{Var}(\sum_{i=1}^n X_i)\).""",
                solution=r"""Independence implies the variance of the sum is \(n\sigma^2\).""",
            ),
            Problem(
                id="5.6.3",
                title="Normal Sample Mean",
                problem=r"""If \(X_i\sim\mathcal{N}(\mu,\sigma^2)\) i.i.d., determine the distribution of \(\bar{X}\).""",
                solution=r"""The mgf of \(\bar{X}\) is \(\exp(\mu t + \tfrac{1}{2}(\sigma^2/n)t^2)\), identifying \(\bar{X}\) as \(\mathcal{N}(\mu,\sigma^2/n)\).""",
            ),
            Problem(
                id="5.7.1",
                title="Sum of Poisson Variables",
                problem=r"""Show that the sum of independent \(\mathrm{Poisson}(\lambda_i)\) variables is \(\mathrm{Poisson}(\sum_i \lambda_i)\).""",
                solution=r"""The product of the mgfs \(\exp\{\lambda_i(e^t-1)\}\) equals \(\exp\{(\sum_i \lambda_i)(e^t-1)\}\).""",
            ),
            Problem(
                id="5.7.2",
                title="Sum of Normals",
                problem=r"""Let \(X\sim\mathcal{N}(\mu_1,\sigma_1^2)\) and \(Y\sim\mathcal{N}(\mu_2,\sigma_2^2)\) be independent.
Show \(X+Y\sim\mathcal{N}(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)\).""",
                solution=r"""Multiply the mgfs of \(X\) and \(Y\): the result is \(\exp((\mu_1+\mu_2)t + \tfrac{1}{2}(\sigma_1^2+\sigma_2^2)t^2)\).""",
            ),
            Problem(
                id="5.7.3",
                title="Law of Total Expectation",
                problem=r"""Prove \(\mathbb{E}[X]=\mathbb{E}[\mathbb{E}[X\mid Y]]\) for integrable \(X\).""",
                solution=r"""Take expectations in the defining relation \(\mathbb{E}[X\mathbf{1}_A]=\mathbb{E}[\mathbb{E}[X\mid Y]\mathbf{1}_A]\) with \(A=\Omega\).""",
            ),
            Problem(
                id="5.8.1",
                title="Characteristic Function",
                problem=r"""Suppose \(\varphi_X(t)=e^{-t^2/2}\). Identify the distribution of \(X\).""",
                solution=r"""This is the characteristic function of \(\mathcal{N}(0,1)\).""",
            ),
            Problem(
                id="5.8.2",
                title="Jensen's Inequality",
                problem=r"""Let \(g\) be convex and \(X\) integrable. Show \(g(\mathbb{E}[X]) \le \mathbb{E}[g(X)]\).""",
                solution=r"""Use supporting hyperplanes: \(g(y) \ge ay+b\) with equality at \(y=\mathbb{E}[X]\). Taking expectations gives the inequality.""",
            ),
        ],
    ),
    Chapter(
        name="V. Continuous Distributions",
        slug="chapter_V",
        problems=[
            Problem(
                id="4.1.1",
                title="Normalising a Density",
                problem=r"""Let \(f(x)=c x^2\) on \([0,1]\) and 0 otherwise. Determine \(c\) and the distribution function \(F\).""",
                solution=r"""\(c^{-1}=\int_0^1 x^2\,dx = 1/3\), so \(c=3\). Consequently \(F(x)=0\) for \(x<0\), equals \(x^3\) on \([0,1]\), and is 1 for \(x\ge1\).""",
            ),
            Problem(
                id="4.1.2",
                title="Tail Behaviour",
                problem=r"""Let \(f(x)=1/(1+x)^2\) for \(x\ge 0\) and 0 otherwise. Find \(F(x)\) and decide whether \(\mathbb{E}[X]\) is finite.""",
                solution=r"""\(F(x)=1-1/(1+x)\). The expectation equals \(\int_0^\infty x/(1+x)^2\,dx\), which diverges; hence \(\mathbb{E}[X]=\infty\).""",
            ),
            Problem(
                id="4.2.1",
                title="Independence Check",
                problem=r"""Suppose \(f_{X,Y}(x,y)=4xy\) on \([0,1]^2\). Find the marginals and conclude whether \(X\) and \(Y\) are independent.""",
                solution=r"""\(f_X(x)=\int_0^1 4xy\,dy=2x\), \(f_Y(y)=2y\). Because \(f_{X,Y}(x,y)=f_X(x)f_Y(y)\), the variables are independent.""",
            ),
            Problem(
                id="4.2.2",
                title="Sum of Independent Exponentials",
                problem=r"""Let \(X,Y\) be independent with joint density \(\lambda^2 e^{-\lambda (x+y)}\) on \(x,y>0\).
Find the density of \(S=X+Y\).""",
                solution=r"""Convolution yields \(f_S(s)=\int_0^s \lambda^2 e^{-\lambda s}\,du = \lambda^2 s e^{-\lambda s}\), \(s>0\), the gamma(2,\(\lambda\)) density.""",
            ),
            Problem(
                id="4.4.1",
                title="Gamma Function",
                problem=r"""Show \(\Gamma(n)=\int_0^\infty x^{n-1} e^{-x}\,dx = (n-1)!\) for integer \(n\ge1\).""",
                solution=r"""Integrate by parts to obtain the recursion \(\Gamma(n+1)=n\Gamma(n)\) with \(\Gamma(1)=1\).""",
            ),
            Problem(
                id="4.4.2",
                title="Beta Function",
                problem=r"""Prove \(B(a,b)=\int_0^1 x^{a-1}(1-x)^{b-1}\,dx = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}\).""",
                solution=r"""Use the substitution \(x=u/(u+v)\) and the definition of the gamma function to express the integral as \(\Gamma(a)\Gamma(b)/\Gamma(a+b)\).""",
            ),
            Problem(
                id="4.4.3",
                title="Exponential Median",
                problem=r"""Let \(X\sim\mathrm{Exp}(\lambda)\). Find the median of \(X\).""",
                solution=r"""Solve \(1-e^{-\lambda m}=1/2\) to obtain \(m=(\log 2)/\lambda\).""",
            ),
            Problem(
                id="4.5.2",
                title="Covariance of Exponentials",
                problem=r"""For independent \(X,Y\sim\mathrm{Exp}(\lambda)\), compute \(\mathbb{P}(X>Y)\) and \(\operatorname{Cov}(X,Y)\).""",
                solution=r"""Symmetry gives \(\mathbb{P}(X>Y)=1/2\). Independence yields \(\operatorname{Cov}(X,Y)=0\).""",
            ),
            Problem(
                id="4.5.3",
                title="Min and Max of Uniforms",
                problem=r"""If \(X,Y\) are i.i.d. uniform on \([0,1]\), find the distribution of \(U=\min(X,Y)\) and \(V=\max(X,Y)\).""",
                solution=r"""\(\mathbb{P}(U>u)=(1-u)^2\) for \(0\le u\le1\), so \(f_U(u)=2(1-u)\). Similarly \(\mathbb{P}(V\le v)=v^2\) giving \(f_V(v)=2v\).""",
            ),
            Problem(
                id="4.5.4",
                title="Sum of Uniforms",
                problem=r"""For \(X,Y\) as above, compute \(\mathbb{P}(X+Y \le 1)\).""",
                solution=r"""The region \(x+y\le1\) inside the unit square has area \(1/2\), hence the probability is \(1/2\).""",
            ),
            Problem(
                id="4.6.1",
                title="Conditional Density",
                problem=r"""Let \(f_{X,Y}(x,y)=2\) on the triangle \(0<y<x<1\). Find the conditional density of \(Y\) given \(X=x\).""",
                solution=r"""The marginal \(f_X(x)=\int_0^x 2\,dy = 2x\). Therefore \(f_{Y\mid X}(y\mid x)=\frac{2}{2x}=\frac{1}{x}\) for \(0<y<x\), i.e. uniform on \([0,x]\).""",
            ),
            Problem(
                id="4.6.2",
                title="Conditional Expectation",
                problem=r"""Using the density in the previous problem, compute \(\mathbb{E}[Y\mid X=x]\).""",
                solution=r"""Since the conditional density is uniform on \([0,x]\), \(\mathbb{E}[Y\mid X=x]=x/2\).""",
            ),
            Problem(
                id="4.6.3",
                title="Conditioning on a Sum",
                problem=r"""Let \(X,Y\) be independent exponentials with parameter \(\lambda\). Determine the conditional distribution of \(X\) given \(X+Y=s\).""",
                solution=r"""The joint density of \((X,X+Y)\) shows that conditional on \(X+Y=s\), \(X\) is uniform on \([0,s]\).""",
            ),
            Problem(
                id="4.7.1",
                title="Sine Transformation",
                problem=r"""Let \(X\sim\mathrm{Uniform}[0,\pi]\). Find the density of \(Y=\sin X\).""",
                solution=r"""For \(y\in(-1,1)\), two pre-images exist. Using the change of variables formula gives \(f_Y(y)=\frac{1}{\pi\sqrt{1-y^2}}\).""",
            ),
            Problem(
                id="4.7.2",
                title="Polar Coordinates",
                problem=r"""Let \(X,Y\) be independent \(\mathcal{N}(0,1)\). Find the density of \(R=\sqrt{X^2+Y^2}\).""",
                solution=r"""Transform to polar coordinates: the joint density is \((2\pi)^{-1} e^{-r^2/2} r\). After integrating over the angle, \(f_R(r)=r e^{-r^2/2}\) for \(r\ge0\) (a Rayleigh density).""",
            ),
        ],
    ),
    Chapter(
        name="VI. Sampling Distributions",
        slug="chapter_VI",
        problems=[
            Problem(
                id="4.10.2",
                title="Adding Chi-squared Variables",
                problem=r"""Let \(U\sim\chi^2_{m}\) and \(V\sim\chi^2_{n}\) be independent. Show \(U+V\sim\chi^2_{m+n}\).""",
                solution=r"""The mgf of \(\chi^2_k\) is \((1-2t)^{-k/2}\). Multiplying the mgfs of \(U\) and \(V\) yields \((1-2t)^{-(m+n)/2}\), the mgf of \(\chi^2_{m+n}\).""",
            ),
            Problem(
                id="4.10.3",
                title="Student's t Moments",
                problem=r"""For a Student's \(t_\nu\) distribution with \(\nu>2\), compute \(\mathbb{E}[T]\) and \(\mathrm{Var}(T)\).""",
                solution=r"""Symmetry gives mean zero. The variance exists for \(\nu>2\) and equals \(\nu/(\nu-2)\).""",
            ),
            Problem(
                id="4.10.5",
                title="Normal Samples",
                problem=r"""Let \(X_1,\dots,X_n\) be i.i.d. \(\mathcal{N}(\mu,\sigma^2)\). Show that \(\bar{X}\) and \(S^2 = \frac{1}{n-1}\sum (X_i-\bar{X})^2\) are independent.""",
                solution=r"""Express the vector of centered observations via an orthogonal transformation; one coordinate equals \(\bar{X}\) while the remaining \(n-1\) coordinates are independent standard normals scaled by \(\sigma\). Independence follows because multivariate normals are independent when uncorrelated.""",
            ),
            Problem(
                id="4.10.6",
                title="Scaled Sample Variance",
                problem=r"""Under the assumptions above, prove \((n-1)S^2/\sigma^2 \sim \chi^2_{n-1}\).""",
                solution=r"""The \(n-1\) centered orthogonal coordinates are independent \(\mathcal{N}(0,\sigma^2)\); their squared sum divided by \(\sigma^2\) is \(\chi^2_{n-1}\).""",
            ),
            Problem(
                id="4.11.1",
                title="Inverse Transform Sampling",
                problem=r"""Describe how to generate a discrete uniform variable on \(\{1,\dots,n\}\) from \(U\sim\mathrm{Uniform}(0,1)\).""",
                solution=r"""Partition \((0,1)\) into \(n\) subintervals of length \(1/n\) and return the index of the subinterval containing \(U\).""",
            ),
            Problem(
                id="4.11.2",
                title="Fisher–Yates Shuffle",
                problem=r"""Outline the Fisher–Yates algorithm for sampling a random permutation of \(n\) items.""",
                solution=r"""Iterate for \(k=n,\dots,2\): pick \(J\sim\mathrm{Uniform}\{1,\dots,k\}\) and swap positions \(J\) and \(k\). The result is uniform over all \(n!\) permutations.""",
            ),
            Problem(
                id="4.11.3",
                title="Generating Exponentials",
                problem=r"""Show that if \(U\sim\mathrm{Uniform}(0,1)\) then \(X=-\log(1-U)/\lambda\) has the \(\mathrm{Exp}(\lambda)\) distribution.""",
                solution=r"""Compute \(\mathbb{P}(X \le x) = \mathbb{P}(U \ge 1-e^{-\lambda x}) = 1-e^{-\lambda x}\).""",
            ),
            Problem(
                id="4.11.4",
                title="Acceptance–Rejection",
                problem=r"""Suppose \(f\) is bounded by \(M g\) for a density \(g\). Describe the acceptance–rejection algorithm to sample from \(f\).""",
                solution=r"""Draw \(Y \sim g\) and \(U\sim\mathrm{Uniform}(0,1)\). Accept \(Y\) as a sample from \(f\) if \(U \le f(Y)/(Mg(Y))\); otherwise repeat.""",
            ),
            Problem(
                id="4.11.5",
                title="Acceptance Probability",
                problem=r"""In the acceptance–rejection scheme above, show that the overall acceptance probability is \(1/M\).""",
                solution=r"""Conditioning on \(Y\) gives acceptance probability \(\int f(y)\,dy / M = 1/M\).""",
            ),
            Problem(
                id="4.11.6",
                title="Mixture Sampling",
                problem=r"""Given a mixture density \(f=\sum_{i=1}^k w_i f_i\), explain how to sample from \(f\) using composition.""",
                solution=r"""Select component \(I\) with probabilities \(w_i\), then draw from \(f_I\). The resulting sample has density \(f\).""",
            ),
            Problem(
                id="5.10.1",
                title="CLT Approximation",
                problem=r"""Let \(X_1,\dots,X_n\) be i.i.d. with mean \(\mu\) and variance \(\sigma^2\). Use the central limit theorem to approximate \(\mathbb{P}(|\bar{X}-\mu| \le \varepsilon)\) for large \(n\).""",
                solution=r"""Standardise: \(\sqrt{n}(\bar{X}-\mu)/\sigma \Rightarrow \mathcal{N}(0,1)\). Hence \(\mathbb{P}(|\bar{X}-\mu|\le\varepsilon) \approx \Phi\left(\tfrac{\sqrt{n}\varepsilon}{\sigma}\right)-\Phi\left(-\tfrac{\sqrt{n}\varepsilon}{\sigma}\right)\).""",
            ),
            Problem(
                id="5.10.2",
                title="Binomial Normal Approximation",
                problem=r"""For \(X\sim\mathrm{Binomial}(n,p)\) with large \(n\), give the normal approximation to \(\mathbb{P}(X \le k)\).""",
                solution=r"""Use \(X\) approximately \(\mathcal{N}(np,np(1-p))\) together with a continuity correction: \(\mathbb{P}(X\le k) \approx \Phi\left(\frac{k+0.5-np}{\sqrt{np(1-p)}}\right).""",
            ),
            Problem(
                id="5.10.3",
                title="Asymptotic Normality of the Mean",
                problem=r"""State the central limit theorem for the sample mean of i.i.d. observations with finite variance.""",
                solution=r"""If \(X_i\) are i.i.d. with mean \(\mu\) and variance \(\sigma^2\), then \(\sqrt{n}(\bar{X}-\mu)/\sigma \Rightarrow \mathcal{N}(0,1)\) as \(n\to\infty\).""",
            ),
            Problem(
                id="5.11.1",
                title="Chernoff Bound",
                problem=r"""Let \(S_n=\sum_{i=1}^n X_i\) with independent Bernoulli(\(p\)) summands. Show that for any \(t>0\),
\(\mathbb{P}(S_n \ge np + t) \le \exp\{-n D(p+t/n\Vert p)\}\), where \(D\) is the Kullback–Leibler divergence.""",
                solution=r"""Optimise the mgf bound \(\mathbb{P}(S_n\ge np+t) \le \inf_{\theta>0} e^{-\theta(np+t)}(pe^{\theta}+1-p)^n\); the minimiser yields the divergence expression.""",
            ),
            Problem(
                id="5.11.2",
                title="Hoeffding's Inequality",
                problem=r"""State Hoeffding's inequality for bounded independent variables and apply it to \(S_n\) as above.""",
                solution=r"""If \(X_i\in[a_i,b_i]\), then \(\mathbb{P}(\bar{X}-\mathbb{E}[\bar{X}]\ge \varepsilon) \le \exp\left(-\frac{2n^2 \varepsilon^2}{\sum (b_i-a_i)^2}\right)\).
For Bernoulli(\(p\)) variables this gives \(\mathbb{P}(S_n-np\ge t)\le \exp(-2t^2/n)\).""",
            ),
        ],
    ),
]

generate_docs.chapters.extend(additional_chapters)
build_documents.chapters = generate_docs.chapters

write_documents(Path.cwd())
