# Solutions — I. Probability Basics
1. **Exercise 1.2.1** (_Events as Sets_)
If \(\omega \notin \bigcup_i A_i\) then \(\omega\) lies in none of the \(A_i\), hence belongs to \(\bigcap_i A_i^c\).
The reverse inclusion is identical. Taking complements yields the second identity.

2. **Exercise 1.2.2** (_Events as Sets_)
Closure under complements and countable unions gives
\(A \cap B = (A^c \cup B^c)^c \in \mathcal{F}\) and \(A \setminus B = A \cap B^c \in \mathcal{F}\). Finally
\(A \triangle B = (A \setminus B) \cup (B \setminus A) \in \mathcal{F}\).

3. **Exercise 1.2.3** (_Events as Sets_)
Record the winners of each round from the top of the draw. A complete outcome is an element of
\(V_n \times V_{n-1} \times \cdots \times V_1\) where \(V_k = \{1,2\} \times \cdots \times \{2^k-1,2^k\}\).
Consequently the sample space has \(2^{2^n-1}\) elements. If only the champion matters, the sample space has \(2^n\) points.

4. **Exercise 1.3.1** (_Probability_)
The general inequalities yield \(\tfrac{1}{12} \le \mathbb{P}(A \cap B) \le \tfrac{1}{3}\) and
\(\tfrac{3}{4} \le \mathbb{P}(A \cup B) \le 1\). Choosing a uniform element of \(\{1,\dots,12\}\) and taking
\(A=\{1,\dots,9\}\) with \(B=\{9,10,11,12\}\) attains the lower bound; taking
\(B=\{1,2,3,4\}\) attains the upper bound.

5. **Exercise 1.3.2** (_Probability_)
The probability of no head in the first \(n\) tosses is \(2^{-n}\), so no head ever has probability zero.
Partition the tosses into blocks matching any length-\(k\) pattern \(w\); each block equals \(w\) with probability \(2^{-k}\)
independently, so the chance that \(w\) never occurs is \(\lim_{m\to\infty}(1-2^{-k})^m=0\).

6. **Exercise 1.3.3** (_Probability_)
The number of visually distinct arrangements is \(6!/(2!)^3=90\). Exactly 10 are derangements,
so the desired probability equals \(1/9\).

7. **Exercise 1.3.5** (_Probability_)
Since \(\mathbb{P}(A_n^c)=0\), the union bound gives \(\mathbb{P}(\bigcup_n A_n^c)\le \sum_n \mathbb{P}(A_n^c)=0\).
Taking complements yields the claim.

8. **Exercise 1.4.1** (_Conditional Probability_)
By definition \(\mathbb{P}(A\mid B)=\mathbb{P}(A\cap B)/\mathbb{P}(B)
=\mathbb{P}(B\mid A)\mathbb{P}(A)/\mathbb{P}(B)\). If \(\mathbb{P}(A\mid B) > \mathbb{P}(A)\), multiply both sides by \(\mathbb{P}(B)\) and divide by \(\mathbb{P}(A)\) to obtain the conclusion.

9. **Exercise 1.4.2** (_Conditional Probability_)
Apply \(\mathbb{P}(E\cap F)=\mathbb{P}(E)\mathbb{P}(F\mid E)\) successively to obtain the product form.

10. **Exercise 1.4.3** (_Conditional Probability_)
Let \(M,R,N\) denote picking a double-headed, double-tailed, or fair coin. Then
\(\mathbb{P}(M)=\mathbb{P}(N)=2/5\) and \(\mathbb{P}(R)=1/5\).
1. \(\mathbb{P}(\text{lower head})=2/5+0+2/5\cdot 1/2=3/5\).
2. By Bayes' rule, \(\mathbb{P}(M\mid \text{upper head})=2/3\) and \(\mathbb{P}(N\mid \text{upper head})=1/3\), so
\(\mathbb{P}(\text{lower head}\mid \text{upper head})=2/3+1/3\cdot1/2=5/6\).
3. Conditioning on two consecutive heads yields \(\mathbb{P}(M)=4/5\) and \(\mathbb{P}(N)=1/5\), giving probability
\(4/5+1/5\cdot1/2=9/10\).
4. After discarding, the composition resets, returning to \(3/5\).

11. **Exercise 1.5.2** (_Independence_)
\(\mathbb{P}(A_{ij})=1/6\). If \(i<j<k\), \(\mathbb{P}(A_{ij}\cap A_{ik})=1/36=\mathbb{P}(A_{ij})\mathbb{P}(A_{ik})\).
Yet \(\mathbb{P}(A_{12}\cap A_{13}\cap A_{23})=1/36\neq(1/6)^3\); hence mutual independence fails.

12. **Exercise 1.5.3** (_Independence_)
Independence immediately implies the product probability \(2^{-m}\). Conversely, if every word has probability \(2^{-m}\), then for any \(\epsilon_1,\dots,\epsilon_m\) we have
\(\mathbb{P}(X_1=\epsilon_1,\dots,X_m=\epsilon_m)=2^{-m}=\prod_{k=1}^m \mathbb{P}(X_k=\epsilon_k)\), proving independence.

13. **Exercise 1.5.5** (_Independence_)
Two fair coins give independence between \(A\)=\{first head\} and \(B\)=\{second head\}, but conditioning on \(C\)=\{coins equal\} makes them dependent.
Conversely, let \(A\)=\{min die score \(\le3\}\), \(B\)=\{max die score \(\ge4\}\), and \(C\)=\{min \(\le3\), max \(\ge4\}\); then \(A,B\) are dependent but become independent given \(C\).
Conditional independence coincides with independence for all \(A,B\) exactly when \(\mathbb{P}(C)\in\{0,1\}.

14. **Exercise 1.7.1** (_Worked Examples_)
Let \(R_{XY}\) be the event of at least one open road between \(X\) and \(Y\).
Then \(\mathbb{P}(R_{AB})=1-p^2\). Without the direct road, \(R_{AC}=R_{AB}\cap R_{BC}\) so
\(\mathbb{P}(R_{AB}\mid R_{AC}^c) = \frac{(1-p^2)p^2}{1-(1-p^2)^2} = \frac{1-p^2}{2-p^2}\).
Adding a direct road multiplies numerator and denominator by the same factor, leaving the conditional probability unchanged.

15. **Exercise 1.7.2** (_Worked Examples_)
(i) Select \(2\) kings, \(1\) ace and \(10\) of the remaining \(44\) cards:
\(\binom{4}{2}\binom{4}{1}\binom{44}{10}/\binom{52}{13}\).
(ii) Divide the count from (i) by the number of hands with two kings: \(\binom{4}{2}\binom{48}{11}\).
