from pathlib import Path
from build_documents import Problem, Chapter, write_documents
import build_documents

chapters = [
    Chapter(
        name="I. Probability Basics",
        slug="chapter_I",
        problems=[
            Problem(
                id="1.2.1",
                title="Events as Sets",
                problem=r"""Let \(\{A_i : i \in I\}\) be a family of events. Prove De Morgan's laws:
\[
\left(\bigcup_{i \in I} A_i\right)^c = \bigcap_{i \in I} A_i^c, \qquad
\left(\bigcap_{i \in I} A_i\right)^c = \bigcup_{i \in I} A_i^c.
\]
""",
                solution=r"""If \(\omega \notin \bigcup_i A_i\) then \(\omega\) lies in none of the \(A_i\), hence belongs to \(\bigcap_i A_i^c\).
The reverse inclusion is identical. Taking complements yields the second identity.""",
            ),
            Problem(
                id="1.2.2",
                title="Events as Sets",
                problem=r"""Let \(\mathcal{F}\) be a \(\sigma\)-field on \(\Omega\) and let \(A,B \in \mathcal{F}\).
Show that \(A \cap B\), \(A \setminus B\), and \(A \triangle B\) all belong to \(\mathcal{F}\).""",
                solution=r"""Closure under complements and countable unions gives
\(A \cap B = (A^c \cup B^c)^c \in \mathcal{F}\) and \(A \setminus B = A \cap B^c \in \mathcal{F}\). Finally
\(A \triangle B = (A \setminus B) \cup (B \setminus A) \in \mathcal{F}\).""",
            ),
            Problem(
                id="1.2.3",
                title="Events as Sets",
                problem=r"""A knock-out tournament begins with \(2^n\) labelled players.
Describe the sample space of all possible outcomes and determine its cardinality.""",
                solution=r"""Record the winners of each round from the top of the draw. A complete outcome is an element of
\(V_n \times V_{n-1} \times \cdots \times V_1\) where \(V_k = \{1,2\} \times \cdots \times \{2^k-1,2^k\}\).
Consequently the sample space has \(2^{2^n-1}\) elements. If only the champion matters, the sample space has \(2^n\) points.""",
            ),
            Problem(
                id="1.3.1",
                title="Probability",
                problem=r"""Let \(\mathbb{P}(A) = \tfrac{3}{4}\) and \(\mathbb{P}(B) = \tfrac{1}{3}\).
Find sharp bounds for \(\mathbb{P}(A \cap B)\) and \(\mathbb{P}(A \cup B)\), and give examples attaining the bounds.""",
                solution=r"""The general inequalities yield \(\tfrac{1}{12} \le \mathbb{P}(A \cap B) \le \tfrac{1}{3}\) and
\(\tfrac{3}{4} \le \mathbb{P}(A \cup B) \le 1\). Choosing a uniform element of \(\{1,\dots,12\}\) and taking
\(A=\{1,\dots,9\}\) with \(B=\{9,10,11,12\}\) attains the lower bound; taking
\(B=\{1,2,3,4\}\) attains the upper bound.""",
            ),
            Problem(
                id="1.3.2",
                title="Probability",
                problem=r"""A fair coin is tossed indefinitely. Show that almost surely a head appears, and that every fixed finite pattern of heads and tails appears eventually.""",
                solution=r"""The probability of no head in the first \(n\) tosses is \(2^{-n}\), so no head ever has probability zero.
Partition the tosses into blocks matching any length-\(k\) pattern \(w\); each block equals \(w\) with probability \(2^{-k}\)
independently, so the chance that \(w\) never occurs is \(\lim_{m\to\infty}(1-2^{-k})^m=0\).""",
            ),
            Problem(
                id="1.3.3",
                title="Probability",
                problem=r"""Two each of red, white, and starred cups are randomly placed on matching saucers (two of each design).
All \(6!\) placements of labelled cups are equally likely. Find \(\mathbb{P}(\text{no cup matches its saucer})\).""",
                solution=r"""The number of visually distinct arrangements is \(6!/(2!)^3=90\). Exactly 10 are derangements,
so the desired probability equals \(1/9\).""",
            ),
            Problem(
                id="1.3.5",
                title="Probability",
                problem=r"""Let \(A_n\) satisfy \(\mathbb{P}(A_n)=1\) for every \(n\). Show that \(\mathbb{P}(\bigcap_{n\ge1}A_n)=1\).""",
                solution=r"""Since \(\mathbb{P}(A_n^c)=0\), the union bound gives \(\mathbb{P}(\bigcup_n A_n^c)\le \sum_n \mathbb{P}(A_n^c)=0\).
Taking complements yields the claim.""",
            ),
            Problem(
                id="1.4.1",
                title="Conditional Probability",
                problem=r"""Establish Bayes' identity \(\mathbb{P}(A\mid B)=\mathbb{P}(B\mid A)\mathbb{P}(A)/\mathbb{P}(B)\)
whenever \(\mathbb{P}(A),\mathbb{P}(B)>0\). Deduce that \(\mathbb{P}(A\mid B) > \mathbb{P}(A)\) implies \(\mathbb{P}(B\mid A) > \mathbb{P}(B)\).""",
                solution=r"""By definition \(\mathbb{P}(A\mid B)=\mathbb{P}(A\cap B)/\mathbb{P}(B)
=\mathbb{P}(B\mid A)\mathbb{P}(A)/\mathbb{P}(B)\). If \(\mathbb{P}(A\mid B) > \mathbb{P}(A)\), multiply both sides by \(\mathbb{P}(B)\) and divide by \(\mathbb{P}(A)\) to obtain the conclusion.""",
            ),
            Problem(
                id="1.4.2",
                title="Conditional Probability",
                problem=r"""Let \(A_1,\dots,A_n\) satisfy \(\mathbb{P}(A_1\cap\cdots\cap A_k)>0\) for each \(k\).
Prove the chain rule
\[
\mathbb{P}(A_1\cap\cdots\cap A_n) = \mathbb{P}(A_1) \prod_{k=2}^{n} \mathbb{P}(A_k\mid A_1\cap\cdots\cap A_{k-1}).
\]
""",
                solution=r"""Apply \(\mathbb{P}(E\cap F)=\mathbb{P}(E)\mathbb{P}(F\mid E)\) successively to obtain the product form.""",
            ),
            Problem(
                id="1.4.3",
                title="Conditional Probability",
                problem=r"""A box contains two double-headed coins, one double-tailed coin, and two fair coins.
A coin is chosen uniformly and tossed repeatedly.
1. Find \(\mathbb{P}(\text{lower face heads after first toss})\).
2. Given the first toss shows heads, find the conditional probability the lower face is a head.
3. Given the first two tosses show heads, find the probability the lower face is a head.
4. After discarding the coin, a new coin is selected and tossed once. Find the chance of heads.""",
                solution=r"""Let \(M,R,N\) denote picking a double-headed, double-tailed, or fair coin. Then
\(\mathbb{P}(M)=\mathbb{P}(N)=2/5\) and \(\mathbb{P}(R)=1/5\).
1. \(\mathbb{P}(\text{lower head})=2/5+0+2/5\cdot 1/2=3/5\).
2. By Bayes' rule, \(\mathbb{P}(M\mid \text{upper head})=2/3\) and \(\mathbb{P}(N\mid \text{upper head})=1/3\), so
\(\mathbb{P}(\text{lower head}\mid \text{upper head})=2/3+1/3\cdot1/2=5/6\).
3. Conditioning on two consecutive heads yields \(\mathbb{P}(M)=4/5\) and \(\mathbb{P}(N)=1/5\), giving probability
\(4/5+1/5\cdot1/2=9/10\).
4. After discarding, the composition resets, returning to \(3/5\).""",
            ),
            Problem(
                id="1.5.2",
                title="Independence",
                problem=r"""A fair die is rolled \(n\) times. For \(i<j\) let \(A_{ij}\) be the event that rolls \(i\) and \(j\) coincide.
Show \(\{A_{ij}\}\) is pairwise independent but not mutually independent.""",
                solution=r"""\(\mathbb{P}(A_{ij})=1/6\). If \(i<j<k\), \(\mathbb{P}(A_{ij}\cap A_{ik})=1/36=\mathbb{P}(A_{ij})\mathbb{P}(A_{ik})\).
Yet \(\mathbb{P}(A_{12}\cap A_{13}\cap A_{23})=1/36\neq(1/6)^3\); hence mutual independence fails.""",
            ),
            Problem(
                id="1.5.3",
                title="Independence",
                problem=r"""A fair coin is tossed repeatedly. Show that independence of tosses is equivalent to the statement that every fixed length-\(m\) word of heads and tails occurs in the first \(m\) positions with probability \(2^{-m}\).""",
                solution=r"""Independence immediately implies the product probability \(2^{-m}\). Conversely, if every word has probability \(2^{-m}\), then for any \(\epsilon_1,\dots,\epsilon_m\) we have
\(\mathbb{P}(X_1=\epsilon_1,\dots,X_m=\epsilon_m)=2^{-m}=\prod_{k=1}^m \mathbb{P}(X_k=\epsilon_k)\), proving independence.""",
            ),
            Problem(
                id="1.5.5",
                title="Independence",
                problem=r"""Give examples showing that conditional independence does not imply independence, and vice versa.
For which events \(C\) are the two concepts equivalent for all \(A,B\)?""",
                solution=r"""Two fair coins give independence between \(A\)=\{first head\} and \(B\)=\{second head\}, but conditioning on \(C\)=\{coins equal\} makes them dependent.
Conversely, let \(A\)=\{min die score \(\le3\}\), \(B\)=\{max die score \(\ge4\}\), and \(C\)=\{min \(\le3\), max \(\ge4\}\); then \(A,B\) are dependent but become independent given \(C\).
Conditional independence coincides with independence for all \(A,B\) exactly when \(\mathbb{P}(C)\in\{0,1\}.""",
            ),
            Problem(
                id="1.7.1",
                title="Worked Examples",
                problem=r"""Two roads connect \(A\) to \(B\) and two connect \(B\) to \(C\). Each road is blocked independently with probability \(p\).
Find \(\mathbb{P}(A \leftrightarrow B \mid A \not\leftrightarrow C)\). Show the answer is unchanged if an additional direct road from \(A\) to \(C\) is included and behaves independently.""",
                solution=r"""Let \(R_{XY}\) be the event of at least one open road between \(X\) and \(Y\).
Then \(\mathbb{P}(R_{AB})=1-p^2\). Without the direct road, \(R_{AC}=R_{AB}\cap R_{BC}\) so
\(\mathbb{P}(R_{AB}\mid R_{AC}^c) = \frac{(1-p^2)p^2}{1-(1-p^2)^2} = \frac{1-p^2}{2-p^2}\).
Adding a direct road multiplies numerator and denominator by the same factor, leaving the conditional probability unchanged.""",
            ),
            Problem(
                id="1.7.2",
                title="Worked Examples",
                problem=r"""From a standard deck, a 13-card hand is dealt. Compute
(i) \(\mathbb{P}(\text{exactly two kings and one ace})\);
(ii) \(\mathbb{P}(\text{exactly one ace} \mid \text{exactly two kings})\).""",
                solution=r"""(i) Select \(2\) kings, \(1\) ace and \(10\) of the remaining \(44\) cards:
\(\binom{4}{2}\binom{4}{1}\binom{44}{10}/\binom{52}{13}\).
(ii) Divide the count from (i) by the number of hands with two kings: \(\binom{4}{2}\binom{48}{11}\).""",
            ),
        ],
    ),
    Chapter(
        name="II. Random Variables",
        slug="chapter_II",
        problems=[
            Problem(
                id="2.1.1",
                title="Random Variables",
                problem=r"""Let \(X\) be a random variable and \(a \in \mathbb{R}\). Show \(aX\) is a random variable, and deduce that \(X-X\) is almost surely zero while \(X+X=2X\).""",
                solution=r"""For \(a>0\), \(\{aX \le x\} = \{X \le x/a\}\); for \(a<0\), \(\{aX \le x\} = \{X \ge x/a\}\) which is a countable intersection of events
\(\{X \le x/a + 1/m\}\). If \(a=0\) the event is \(\emptyset\) or \(\Omega\).
Thus \(aX\) is measurable. Setting \(a=0\) and \(a=2\) yields the final statements.""",
            ),
            Problem(
                id="2.1.2",
                title="Random Variables",
                problem=r"""Let \(Y=aX+b\) with \(a \neq 0\) and distribution function \(F\) for \(X\).
Express \(F_Y\) in terms of \(F\).""",
                solution=r"""If \(a>0\), \(F_Y(y)=F((y-b)/a)\). If \(a<0\), \(F_Y(y)=1-\lim_{x \uparrow (y-b)/a} F(x)\). When \(a=0\), \(Y\) is degenerate at \(b\).""",
            ),
            Problem(
                id="2.1.3",
                title="Random Variables",
                problem=r"""A coin with success probability \(p\) is tossed \(n\) times. Show \(\mathbb{P}(\text{exactly } k \text{ heads}) = \binom{n}{k}p^k(1-p)^{n-k}\).""",
                solution=r"""Independence gives \(p^k(1-p)^{n-k}\) for any particular sequence and there are \(\binom{n}{k}\) such sequences.""",
            ),
            Problem(
                id="2.2.1",
                title="Law of Averages",
                problem=r"""(Randomised response.) The true probability of a “yes” answer is \(q\). Each respondent flips a fair coin in secret and replies “yes” whenever the coin shows heads, regardless of the truth. What is the probability of observing “yes”, and how can \(q\) be estimated from the sample mean?""",
                solution=r"""Let \(R\) be the reported answer. Then \(\mathbb{P}(R=\text{yes}) = q + (1-q)/2 = (1+q)/2\).
If \(\bar{R}\) is the sample mean of indicators of “yes”, the estimator \(\hat{q}=2\bar{R}-1\) is unbiased with variance \((1-q^2)/N\) for \(N\) responses.""",
            ),
            Problem(
                id="2.2.2",
                title="Law of Averages",
                problem=r"""Let \(H_n\) and \(T_n\) denote heads and tails in \(n\) independent tosses of a coin with head probability \(p\).
Show that for \(\varepsilon>0\),
\[
\mathbb{P}\left(\left|\frac{H_n-T_n}{n}-(2p-1)\right|>\varepsilon\right) \le 2e^{-2n\varepsilon^2}.
\]
""",
                solution=r"""Because \(H_n-T_n = 2H_n-n\), the deviation is \(|H_n/n - p| > \varepsilon/2\).
Hoeffding's inequality yields the bound \(2\exp(-2n(\varepsilon/2)^2) = 2e^{-2n\varepsilon^2}\).""",
            ),
            Problem(
                id="2.3.1",
                title="Discrete and Continuous Variables",
                problem=r"""Let \(F\) be a distribution function and \((a_m)_{m \in \mathbb{Z}}\) satisfy \(a_m\uparrow\infty\), \(a_m\downarrow -\infty\).
Define \(G(x)=F(a_m)\) for \(x \in [a_{m-1},a_m)\). Show that if \(\sup_m |a_m-a_{m-1}| \to 0\), then \(G(x)\to F(x)\) at each continuity point of \(F\).""",
                solution=r"""For \(x \in [a_{m-1},a_m)\), \(|G(x)-F(x)| \le |F(a_m)-F(a_{m-1})|\). Right-continuity ensures this bound tends to zero as the mesh shrinks, yielding convergence.""",
            ),
            Problem(
                id="2.3.2",
                title="Discrete and Continuous Variables",
                problem=r"""Let \(g:\mathbb{R}\to\mathbb{R}\) be continuous and strictly increasing. Show that \(Y=g(X)\) is a random variable.""",
                solution=r"""The inverse \(g^{-1}\) exists and is continuous, so \(\{Y\le y\} = \{X \le g^{-1}(y)\}\) is measurable. Values outside the range correspond to \(\emptyset\) or \(\Omega\).""",
            ),
            Problem(
                id="2.3.3",
                title="Discrete and Continuous Variables",
                problem=r"""Let \(X\) be uniform on \([0,1]\) and let \(F\) be a continuous strictly increasing distribution function.
Define \(Y = F^{-1}(X)\). Show that \(Y\) has distribution \(F\).""",
                solution=r"""For any \(y\), \(\mathbb{P}(Y \le y) = \mathbb{P}(X \le F(y)) = F(y)\). Strict monotonicity of \(F\) ensures the inverse is well defined.""",
            ),
            Problem(
                id="2.4.1",
                title="Worked Examples",
                problem=r"""Let \(X\) have distribution function \(F\). Determine the distribution functions of:
(a) \(X^2\); (b) \(\sqrt{X}\) assuming \(X\ge0\); (c) \(\sin X\); (d) \(G^{-1}(X)\) where \(G\) is continuous increasing;
(e) \(F(X)\); (f) \(G^{-1}(F(X))\).""",
                solution=r"""(a) \(\mathbb{P}(X^2 \le y) = F(\sqrt{y})-F(-\sqrt{y}^{-})\) for \(y\ge0\).
(b) \(\mathbb{P}(\sqrt{X}\le y)=F(y^2)\) for \(y\ge0\).
(c) Use periodicity: sum contributions over intervals where \(\sin\) is monotone.
(d) \(\mathbb{P}(G^{-1}(X)\le y)=F(G(y))\).
(e) \(F(X)\) is uniform on \([0,1]\).
(f) Combining (d) and (e) shows the distribution is \(G\).""",
            ),
            Problem(
                id="2.4.2",
                title="Worked Examples",
                problem=r"""Let \(a<b\) and define \(Y=\min\{\max\{X,a\},b\}\) and \(Z=X\mathbf{1}_{\{a\le X \le b\}}\).
Find the distribution functions of \(Y\) and \(Z\).""",
                solution=r"""For \(Y\), \(F_Y(y)=0\) if \(y<a\), equals \(F(y)\) on \([a,b)\), and is \(1\) for \(y\ge b\), with point masses at \(a\) and \(b\).
For \(Z\), \(F_Z(y)=0\) when \(y<0\); \(F_Z(0)=F(a^-)+1-F(b)\); and for \(0<y\le b\), \(F_Z(y)=F(y)-F(a^-)\).""",
            ),
            Problem(
                id="2.5.1",
                title="Random Vectors",
                problem=r"""Let \((X,W)\) take values \((0,0),(0,1),(1,0),(1,1)\) each with probability \(1/4\).
Find the marginals and determine whether \(X\) and \(W\) are independent.""",
                solution=r"""Both marginals are Bernoulli(1/2). Since \(\mathbb{P}(X=1,W=1)=1/4\neq(1/2)^2\), the variables are dependent.""",
            ),
            Problem(
                id="2.5.2",
                title="Random Vectors",
                problem=r"""Suppose \((X,Y)\) equals \((1,0)\) with probability \(p\) and \((0,1)\) with probability \(1-p\).
Compute \(\operatorname{Cov}(X,Y)\).""",
                solution=r"""\(X\sim\mathrm{Bernoulli}(p)\) and \(Y\sim\mathrm{Bernoulli}(1-p)\) while \(XY=0\) almost surely.
Hence \(\operatorname{Cov}(X,Y)=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]=-p(1-p).""",
            ),
            Problem(
                id="2.5.3",
                title="Random Vectors",
                problem=r"""Let \((X,Y)\) have density \(f_{X,Y}(x,y)=e^{-x}/(y(1+y^2))\) for \(x>0,y>0\) and zero elsewhere.
Verify that this is a density and derive the marginal densities.""",
                solution=r"""Integrating in \(x\) gives \(\int_0^{\infty} e^{-x}\,dx=1\).
In \(y\), \(\int_0^{\infty} \frac{1}{y(1+y^2)}\,dy = 1\) by substitution. Hence the joint density integrates to one.
The marginals are \(f_X(x)=e^{-x}\) for \(x>0\) and \(f_Y(y)=1/(y(1+y^2))\) for \(y>0\).""",
            ),
            Problem(
                id="2.7.2",
                title="Problems",
                problem=r"""Define simple approximations \(X_m = \sum_{k\in\mathbb{Z}} k2^{-m} \mathbf{1}_{\{k2^{-m} \le X < (k+1)2^{-m}\}}\).
Show \(X_m(\omega)\to X(\omega)\) for every \(\omega\) and hence \(\{X\le x\}=\bigcap_{m\ge1}\{X_m\le x\}.""",
                solution=r"""For each \(\omega\), the interval containing \(X(\omega)\) shrinks with length <\(2^{-m}\), so \(|X(\omega)-X_m(\omega)|<2^{-m}\).
Taking limits yields the statement about inverse images.""",
            ),
            Problem(
                id="2.7.3",
                title="Problems",
                problem=r"""Let \(X\) and \(Y\) be random variables. Show \(XY\), \(X/Y\) (when \(Y \neq 0\) a.s.), \(|X|\), and \(\min\{X,Y\}\) are random variables.
Deduce that any finite linear combination of random variables is a random variable.""",
                solution=r"""The maps \((x,y)\mapsto xy\), \((x,y)\mapsto x/y\) (on \(y\neq0\)), \(x\mapsto|x|\), and \((x,y)\mapsto\min\{x,y\}\) are continuous.
Composition of measurable functions with continuous functions is measurable, yielding the claim for sums.""",
            ),
        ],
    ),
    Chapter(
        name="III. Discrete Distributions",
        slug="chapter_III",
        problems=[
            Problem(
                id="3.1.1",
                title="Probability Mass Functions",
                problem=r"""For each family decide the constant \(c\) that makes \(p_k\) a probability mass function:
(a) \(p_k = c\,2^{-k}\) for \(k \ge 0\); (b) \(p_k = c\,2^{-k}/k\) for \(k \ge 1\);
(c) \(p_k = c/k^2\) for \(k \ge 1\); (d) \(p_k = c\,k\,2^{-k}\) for \(k \ge 0\).""",
                solution=r"""(a) \(c=1/2\). (b) Use \(\sum_{k\ge1} 2^{-k}/k = \log 2\) giving \(c=1/\log 2\).
(c) \(c = 6/\pi^2\). (d) \(c = 1/2\) since \(\sum k2^{-k}=2\).""",
            ),
            Problem(
                id="3.1.2",
                title="Probability Mass Functions",
                problem=r"""Let \(X\) take values \(1,2,\dots\) with \(\mathbb{P}(X=k)=2^{-k}\).
Compute \(\mathbb{P}(X \text{ is even})\), \(\mathbb{E}[X]\), and \(\mathrm{Var}(X)\).""",
                solution=r"""\(\mathbb{P}(X \text{ even}) = \sum_{m\ge1}2^{-2m}=1/3\).
The pgf \(G(s)=s/(2-s)\) gives \(\mathbb{E}[X]=G'(1)=2\) and \(\mathbb{E}[X^2]=G''(1)+G'(1)=6\), so \(\mathrm{Var}(X)=2\).""",
            ),
            Problem(
                id="3.2.1",
                title="Independence",
                problem=r"""Let \(X\) and \(Y\) be independent Rademacher random variables and set \(Z=XY\).
Show every pair of \(X,Y,Z\) is independent but the triple is not jointly independent.""",
                solution=r"""Pairs have joint mass \(1/4\), matching the product of marginals.
However \(\mathbb{P}(X=1,Y=1,Z=1)=1/4\neq(1/2)^3\), so the three are dependent.""",
            ),
            Problem(
                id="3.2.5",
                title="Independence",
                problem=r"""Suppose \((X_1,\dots,X_n)\) and \((-X_1,\dots,-X_n)\) share the same distribution.
Show \(\mathbb{E}[X_i]=0\) for every \(i\).""",
                solution=r"""Take expectations and use symmetry: \(\mathbb{E}[X_i]=\mathbb{E}[-X_i]\). Hence \(\mathbb{E}[X_i]=0\).""",
            ),
            Problem(
                id="3.4.1",
                title="Indicators and Matching",
                problem=r"""Let \(\pi\) be a uniform random permutation of \(n\). Write \(M\) for the number of fixed points.
Show \(\mathbb{E}[M]=1\) and \(\mathbb{P}(M=0)\to e^{-1}\).""",
                solution=r"""\(M=\sum_{i=1}^n I_i\) with \(I_i=\mathbf{1}_{\{\pi(i)=i\}}\) and \(\mathbb{E}[I_i]=1/n\), giving \(\mathbb{E}[M]=1\).
Inclusion–exclusion shows \(\mathbb{P}(M=0) = 1 - 1 + 1/2! - \cdots + (-1)^n/n!\to e^{-1}\).""",
            ),
            Problem(
                id="3.4.2",
                title="Indicators and Matching",
                problem=r"""With \(M\) as above, compute \(\mathrm{Var}(M)\).""",
                solution=r"""Use \(\mathrm{Var}(M)=\sum_i \mathrm{Var}(I_i)+2\sum_{i<j}\mathrm{Cov}(I_i,I_j)\).
Since \(\mathbb{P}(\pi(i)=i,\pi(j)=j)=1/(n(n-1))\), the covariance equals \(-1/n^2(n-1)\) and the variance simplifies to 1.""",
            ),
            Problem(
                id="3.5.1",
                title="Multinomial Model",
                problem=r"""Show that the multinomial probability mass function is
\(\mathbb{P}(N_1=n_1,\dots,N_r=n_r) = \frac{n!}{n_1!\cdots n_r!} p_1^{n_1}\cdots p_r^{n_r}\) when \(\sum_i n_i = n\).""",
                solution=r"""Count sequences with specified counts: there are \(n!/(n_1!\cdots n_r!)\) such sequences, each occurring with probability \(p_1^{n_1}\cdots p_r^{n_r}\).""",
            ),
            Problem(
                id="3.5.2",
                title="Splitting a Poisson Process",
                problem=r"""If \(N\sim\mathrm{Poisson}(\lambda)\) and each event is independently retained with probability \(p\), show the number retained is \(\mathrm{Poisson}(\lambda p)\).""",
                solution=r"""Condition on \(N=n\); the retained count is \(\mathrm{Binomial}(n,p)\). Summing \(\sum_n e^{-\lambda}\lambda^n/n!\binom{n}{k}p^k(1-p)^{n-k}\) yields \(e^{-\lambda p}(\lambda p)^k/k!\).""",
            ),
            Problem(
                id="3.6.2",
                title="Marginals of the Multinomial",
                problem=r"""Show that each component \(N_i\) of a multinomial vector is \(\mathrm{Binomial}(n,p_i)\).""",
                solution=r"""Sum the multinomial pmf over the remaining indices to obtain the binomial pmf.""",
            ),
            Problem(
                id="3.6.3",
                title="Heavy Tails",
                problem=r"""Let \(X\) have \(\mathbb{P}(X=k)=1/(k(k+1))\) for \(k \ge 1\). Compute \(\mathbb{P}(X>n)\) and decide whether \(\mathbb{E}[X]\) exists.""",
                solution=r"""Telescoping gives \(\mathbb{P}(X>n)=1/(n+1)\). The mean diverges because \(\sum_k k/(k(k+1)) = \sum 1/(k+1) = \infty\).""",
            ),
            Problem(
                id="3.7.1",
                title="Conditional Expectation",
                problem=r"""Let \(X,Y,Z\) be integrable. Show \(\mathbb{E}[aY+bZ\mid X] = a\mathbb{E}[Y\mid X]+b\mathbb{E}[Z\mid X]\).""",
                solution=r"""Linearity follows from testing against bounded measurable functions of \(X\) in the defining property of conditional expectation.""",
            ),
            Problem(
                id="3.7.2",
                title="Uniqueness",
                problem=r"""If both \(g(X)\) and \(h(X)\) are versions of \(\mathbb{E}[Y\mid X]\), show \(g(X)=h(X)\) almost surely.""",
                solution=r"""For any bounded measurable \(\varphi\), \(\mathbb{E}[(g-h)(X)\varphi(X)]=0\).
Choosing indicator functions of generating sets implies \(g(X)=h(X)\) a.s.""",
            ),
            Problem(
                id="3.8.1",
                title="Discrete Convolution",
                problem=r"""Let \(X\sim\mathrm{Uniform}\{0,\dots,m\}\) and \(Y\sim\mathrm{Uniform}\{0,\dots,n\}\) be independent.
Find \(\mathbb{P}(X+Y=k)\).""",
                solution=r"""Count integer solutions \((i,j)\) to \(i+j=k\) with \(0\le i\le m\), \(0\le j\le n\); the count is
\(\max(0, \min(k,m) - \max(0,k-n) + 1)\). Divide by \((m+1)(n+1)\).""",
            ),
            Problem(
                id="3.8.2",
                title="Negative Binomial",
                problem=r"""Let \(X\) and \(Y\) be independent geometric(\(p\)) variables supported on \(\{1,2,\dots\}\).
Show \(X+Y\) is negative binomial with parameters \(2\) and \(p\).""",
                solution=r"""\(\mathbb{P}(X+Y=k) = \sum_{j=1}^{k-1} p^2 (1-p)^{k-2} = (k-1)p^2(1-p)^{k-2}\), the negative binomial pmf.""",
            ),
            Problem(
                id="3.9.1",
                title="Random Walk",
                problem=r"""For simple symmetric random walk \((S_n)\), compute \(\mathbb{P}(S_{2n}=0)\).""",
                solution=r"""Exactly \(n\) up-steps are needed, giving \(\binom{2n}{n} 2^{-2n}\).""",
            ),
        ],
    ),
]

build_documents.chapters = chapters
write_documents(Path.cwd())
