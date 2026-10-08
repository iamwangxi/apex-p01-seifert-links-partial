# D′: collar perturbations, the length correction and area gain

[Overview](../README.md) · [Objects](objects.md) · [Sources](../sources/bibliography.md) · [Scope](scope.md)

D′ proof sequence: [statement, connectivity and examples](connected-surfaces.md) (§§1–4); [exchange topology and fixed classes](connected-surfaces-exchange.md) (§§5.1–5.3); [collars and area gain](connected-surfaces-collars.md) (§§5.4–5.6); [contractibility and truncations](connected-surfaces-contractibility.md) (§§5.7–6). Section references in this sequence retain this numbering.

### 5.4 R2: the actual collar function has no critical points

Let $`\mathcal J\subset\{1,\ldots,n\}`$ index the tori where $`\partial_iA=\partial_iB=:\mathcal L_i`$. Shrink disjoint ambient boundary collars so that the portion of $`B`$ in each common-boundary collar is exactly its boundary annulus, and choose graph coordinates in which $`A=\{y=f_i(s,r_i)\}`$, $`B=\{y=0\}`$, $`f_i(s,0)=0`$. The common leaf $`\mathcal L_i`$ is on $`T_i`$, not the link core $`L_i`$. Competition Proposition 5.7(25), p. 19, gives $`df_i\ne0`$ throughout $`0<r_i<r_0^{(i)}`$, although boundary critical points may occur. Shrink the collars so the interior tangency discs miss their closures. Choose smooth $`0\le\chi_i\le1`$, one near $`r_i=0`$, zero near $`r_i=r_0^{(i)}`$, with derivative supported in a compact transition band $`K_i\subset\{0<r_i<r_0^{(i)}\}`$. The **actual** perturbation difference is

```math
h_{i,t}=f_i+\varsigma_i t\chi_i(r_i),\qquad
\Gamma_t\cap C_i=\{h_{i,t}=0\},\quad C_i=\mathcal L_i\times(0,r_0^{(i)}).
```

The full perturbation uses these local graph changes and $`f_p-t\psi_p`$ in separate interior tangency charts; it is not a single global graph function. The interior bumps are constant on smaller cores. Either sign there is allowed by the two-sided competition Proposition 5.7(24). This is the finite-collar version of competition (39), p. 34 and p. 22.

**Lemma 5.5 (correct collar perturbation).** For all sufficiently small $`t>0`$, $`dh_{i,t}\ne0`$ throughout $`C_i`$, simultaneously for $`i\in\mathcal J`$. The intersection misses $`I_i\times(0,r_1^{(i)}]`$, where $`I_i,\varsigma_i,r_1^{(i)}`$ are the sign-arc data of Lemma B.1 and $`r_1^{(i)}\le r_0^{(i)}/4`$. Every closed intersection component contained in $`C_i`$ is essential in that annulus.

**Proof.** On the compact transition band put

```math
c_i=\min_{K_i}|df_i|>0,\qquad M_i=\sup_{K_i}|d\chi_i|<\infty.
```

Choose $`tM_i<c_i/2`$, with no restriction needed if $`M_i=0`$. There $`|dh_{i,t}|\ge c_i-tM_i>c_i/2`$. Off that band $`d\chi_i=0`$, so $`dh_{i,t}=df_i\ne0`$. This proves the collar-wide assertion without a uniform positive gradient bound as $`r_i\downarrow0`$. Take the minimum of finitely many thresholds.

By competition Lemma B.1, p. 33, $`\varsigma_i f_i\ge a_0^{(i)}r_i/2>0`$ on $`I_i\times(0,r_1^{(i)}]`$. Hence

```math
\varsigma_i h_{i,t}=\varsigma_i f_i+t\chi_i>0
```

there, whether or not $`\chi_i=1`$. If a closed component in $`C_i`$ were null-homotopic, its Jordan disc $`D\subset C_i`$ would have $`h_{i,t}=0`$ on the boundary. A nonzero interior value gives an interior extremum and hence a critical point; identically zero on $`D`$ also gives critical points. Both contradict the assertion just proved. $`\square`$

This replaces $`f=-\varsigma t`$ over the entire collar in competition p. 34, an equality valid only where $`\chi=1`$, and the unsupported uniform gradient bound in p. 34. Compare v2 p. 46 and p. 47.

**Properties of the full perturbation.** The cutoff graph changes match the unchanged sheets smoothly at their support edges and converge smoothly to $`A`$. Their small graph track, including its zero-parameter input endpoint, gives a neat ambient isotopy of the input surface with its boundary sliding in the prescribed leaf families. Thus $`A_t`$ is embedded, incompressible, and in the same vertex as $`A`$; it misses $`S`$ for all small $`t`$. On common-boundary tori the new leaf is $`y=\varsigma_i t`$, and on the other tori its boundary is unchanged and already disjoint from $`B`$. Lemma 5.5 proves transversality throughout each common-boundary collar. In an interior constant-bump core the only critical point of $`f_p`$ is $`p`$ with critical value zero, so its nonzero shifted level is regular. On the compact bump transition annulus a positive minimum of $`|df_p|`$ dominates $`t|d\psi_p|`$. Elsewhere the original pair was transverse. Taking the minimum of finitely many thresholds gives a smooth transverse pair with fully disjoint boundary tuples for every sufficiently small positive $`t`$. These are precisely the regular-level steps in competition p. 34 and p. 38. Using zero parameter for this smooth **input** graph track does not insert a zero parameter into the output isotopies of §5.3.

**Corollary 5.6 (repaired noncollapsing step).** There are $`\rho_0,\delta_0>0`$, fixed by the original inputs and perturbation scheme, such that every closed component of $`\Gamma_t`$, $`0<t\le\delta_0`$, has diameter at least $`\rho_0`$.

**Proof.** Otherwise choose $`t_k\downarrow0`$ and closed components with diameter tending to zero, converging to a point of $`A\cap B`$. At an interior transverse point a fixed smaller graph chart has a unique through-arc, and smooth convergence retains that description; it cannot contain a whole closed component. At an interior tangency $`p`$, the projected Jordan disc eventually lies in the constant-bump core. Its boundary has actual graph difference zero; on this disc that difference is $`f_p`$ minus a constant. The only possible critical point is $`p`$, and $`f_p`$ has both signs arbitrarily close to $`p`$, so $`p`$ is not an extremum, even after subtracting a constant. An interior extremum or an identically zero disc is impossible.

At a boundary or collar point, use a sufficiently small half-disc chart on $`B`$. The projected Jordan disc stays in $`r_i>0`$: the linear coordinate $`r_i`$ has its minimum on the boundary of a planar disc, and that boundary curve is in $`r_i>0`$. The disc stays in the chart and collar. Lemma 5.5 applies to the **actual** $`h_{i,t_k}`$, zero on the disc boundary and without critical points inside, giving the same extremum/constancy contradiction. This includes limits on $`r_i=0`$, without a boundary gradient minimum. All limits are covered. $`\square`$

This is competition Lemma B.2, p. 34, with its collar inference replaced rather than assumed; v2 p. 46 gives the corrected Jordan-disc argument.

### 5.5 R3: correction to the original paper's §6.3 length classification

**Correction to the competition paper, not an extra link hypothesis.** Competition p. 22 assigns every curve staying in a chosen collar to Case C. This omits a curve that enters its short collar, stays in the full collar, but rises above half-depth. Appendix B's actual Case C, p. 35, requires $`\max_\gamma r_i\le r_0^{(i)}/2`$. The written case split must be replaced by the following one. This is a defect in the length argument, not a constructed counterexample to the link theorem; (C) does not remove it.

Choose disjoint interior tangency balls $`B_{2\rho_2}(p)`$ with $`4N\rho_2<\rho_0/8`$, small enough to miss every common-boundary band $`r_i\le r_0^{(i)}/2`$. Omit the first restriction when $`N=0`$. Set

```math
P=\bigcup_{p\in\mathcal T}B_{2\rho_2}(p),\qquad G=E\setminus P,\qquad
G'=E\setminus\bigcup_{p\in\mathcal T}B_{\rho_2}(p).
```

Here $`\mathcal T`$ is the finite interior tangency set. Regard $`r_i`$ as boundary-collar height, extended continuously by $`r_0^{(i)}`$ outside its collar, and put

```math
\mathcal H=G\cap\bigcap_{i\in\mathcal J}\{r_i\ge r_1^{(i)}\}.
```

The quotient-length argument gives $`\mathrm{length}(\gamma\cap G)\ge3\rho_0/8`$. Choose two points of $`\gamma`$ at distance at least $`\rho_0/2`$, collapse each tangency ball to a point, and lift a shortest or arbitrarily near-shortest quotient path without repeated visits to a collapsed point. Lifting adds at most $`4\rho_2`$ per ball. The projected curve path has length at most $`\mathrm{length}(\gamma\cap G)`$, giving at least $`\rho_0/2-4N\rho_2>3\rho_0/8`$. No bound on the original curve's number of visits to a ball is needed. This is competition Corollary B.4(1), p. 35, using Corollary 5.6 for diameter; it requires no angle or width bound.

**Proposition 5.7 (complete multi-torus length estimate).** Let $`C_{\mathrm{col}}\ge1`$ bound the finitely many collar height and longitude projection Lipschitz constants. After intersecting the thresholds already chosen, every closed component $`\gamma\subset\Gamma_t`$ satisfies

```math
\mathrm{length}(\gamma\cap\mathcal H)\ge c_*>0,\qquad
c_*=\frac1{C_{\mathrm{col}}}\min\!\left(\{3\rho_0/8\}\cup
\{r_0^{(i)}/2,\ \mathrm{length}(I_i):i\in\mathcal J\}\right).
```

For $`\mathcal J=\varnothing`$, take $`C_{\mathrm{col}}=1`$ and $`c_*=3\rho_0/8`$.

**Proof.** All perturbed boundary tuples are disjoint, so the intersection is a finite union of interior closed curves.

**Case A.** If $`\gamma`$ meets no short collar $`\{r_i<r_1^{(i)}\}`$, then $`\gamma\cap G\subset\mathcal H`$; apply the quotient-length estimate.

Otherwise fix an $`i\in\mathcal J`$ whose short collar is entered.

**Case B, including the missing class.** If $`\gamma`$ reaches $`r_i>r_0^{(i)}/2`$ before leaving that collar, use Case B. Every curve leaving the collar must reach such a level; a curve staying in the collar but exceeding half-depth also belongs here. The two directions around the circle give two disjoint subarcs from $`r_i=r_1^{(i)}`$ to $`r_i=r_0^{(i)}/2`$, contained in this band. Since $`r_1^{(i)}\le r_0^{(i)}/4`$, each has length at least $`r_0^{(i)}/(4C_{\mathrm{col}})`$. The band misses tangency balls and all other boundary collars, so both arcs lie in $`\mathcal H`$, with total length at least $`r_0^{(i)}/(2C_{\mathrm{col}})`$.

**Case C, only below half-depth.** Otherwise the whole curve stays in $`C_i`$ with $`r_i\le r_0^{(i)}/2`$. Lemma 5.5 makes it essential in the annulus. Its projection to $`\mathcal L_i`$ is onto: a loop omitting a point of that circle would lie in an interval times $`(0,r_0^{(i)})`$ and be null-homotopic. Every point over $`I_i`$ has $`r_i>r_1^{(i)}`$ by the swept-clear strip. This portion is below half-depth, so misses the tangency balls, and also misses other collars. It lies in $`\mathcal H`$. Its image covers $`I_i`$, so its length is at least $`\mathrm{length}(I_i)/C_{\mathrm{col}}`$.

These cases exhaust the possibilities, including equality at half-depth in Case C. The finite minimum is positive and fixed before $`t`$. $`\square`$

The single-torus cases are competition p. 35; the defective multi-torus wording is p. 22. The corrected split is also in v2 p. 66. The correction changes neither boundary slopes nor attainment/compactness assumptions.

### 5.6 All-torus boundary clearance and a fixed positive gain

For $`j\notin\mathcal J`$, the compact original intersection misses $`T_j`$, because the two boundary leaves there are disjoint. Record

```math
d_j=\mathrm{dist}(A\cap B,T_j)>0\qquad(j\notin\mathcal J).
```

For all small $`t`$, $`\mathrm{dist}(\Gamma_t,T_j)\ge d_j/2`$. Otherwise a convergent subsequence of intersection points would limit to a point of $`A\cap B`$ violating that distance. For points of $`\Gamma_t`$ in the buffered good region at a common-boundary torus, $`r_i\ge r_1^{(i)}/2`$ gives distance at least $`r_1^{(i)}/(2C_{\mathrm{col}})`$ from $`T_i`$. Thus, for $`\Gamma_t`$ in that buffered region, a lower bound for distance to **all** of $`\partial E`$ is

```math
d_{\partial}=\min\!\left(\{r_1^{(i)}/(2C_{\mathrm{col}}):i\in\mathcal J\}\cup
\{d_j/2:j\notin\mathcal J\}\right)>0.
```

The set is nonempty since the link is nonempty. Reduce these bounds by a fixed factor if needed for chart buffers. The rounding caps use this minimum, not just a common-boundary collar height. This boundary-clearance qualification fills the omission at competition p. 22 and p. 35; compare v2 p. 66. If $`\mathcal J=\varnothing`$, use the positive boundary clearance of configuration (T1), competition p. 37.

We next assemble the no-disc and strict-area conclusions. On the buffered good region

```math
G'\cap\bigcap_{i\in\mathcal J}\{r_i>r_1^{(i)}/2\},
```

the inherited local angle/tube/rounding estimates along $`\Gamma_t`$, with the all-torus clearance, give common $`\theta_1,a,b>0`$, independent of small $`t`$, with $`\theta_t\ge\theta_1`$, $`\eta_{\max,t}\ge a`$, and $`\kappa_t\ge b`$. Take common sector bounds for both frontiers and disc exchange. Uniformity is needed on this buffered region, not near excluded tangencies or the boundary. These are the local estimates of competition Corollary B.4(2),(3), pp. 35–36, in the inherited interface of §5.1.

Choose fixed smooth $`0\le\zeta\le1`$, equal to one on $`\mathcal H`$, with support in that buffered region, and set $`L_\zeta=\sup|d\zeta|<\infty`$. Multiply the finite interior-ball cutoffs by one cutoff per common-boundary collar, zero for $`r_i\le5r_1^{(i)}/8`$ and one for $`r_i\ge r_1^{(i)}`$. Other collar factors equal one on a chosen collar's band, since the collars are disjoint. If $`\mathcal J=\varnothing`$, only ball factors are used. Fix **before $`t`$**

```math
\eta_1=\min\{a/2,\ b/(2\max\{1,L_\zeta\})\}>0,\qquad
\varepsilon_*=g_0(\theta_1)\eta_1c_*>0.
```

For any sufficiently small fixed $`t>0`$, compact transversality gives positive full-seam caps. Choose

```math
0<\eta_2(t)\le\min\{\eta_1/2,\ \tfrac12\min_{\Gamma_t}\eta_{\max,t}\},\qquad
\eta_t=\eta_2(t)+(\eta_1-\eta_2(t))\zeta|_{\Gamma_t}.
```

The width is smooth and positive. Where $`\zeta>0`$, it is at most $`\eta_1\le a/2`$ and its arclength derivative has magnitude at most $`\eta_1L_\zeta\le b/2`$. Where $`\zeta=0`$, smooth nonnegativity gives $`d\zeta=0`$, so the width is constant $`\eta_2(t)`$ and its derivative zero. Thus the size and absolute-derivative constraints hold on **all** of $`\Gamma_t`$, even with small bad-region caps. On $`\mathcal H`$, $`\eta_t=\eta_1`$ exactly. This directly realizes the plateau required by competition (44), p. 37, without losing it when smoothing a minimum; see also the elementary formula at v2 p. 49 and p. 66.

Slicewise nonnegativity and Proposition 5.7 give, for every closed component,

```math
\mathcal G_t(\gamma)=\int_\gamma g_0(\theta_t)\eta_t\,ds
\ge g_0(\theta_1)\eta_1\,\mathrm{length}(\gamma\cap\mathcal H)\ge\varepsilon_*.
```

Let $`e(t)=\mathrm{Area}(A_t)-\mathrm{Area}(A)\ge0`$, since $`A_t`$ is in the class of the minimizer $`A`$; smooth convergence gives $`e(t)\to0`$. A disc patch would imply, by the inherited disc-exchange inequality (14), competition p. 15 and p. 17,

```math
2\varepsilon_*\le\mathcal G_t(a)+\mathcal G_t(b)\le e(t).
```

After fixing $`\varepsilon_*`$, reduce $`\delta>0`$ so $`e(t)<\varepsilon_*/2`$ for $`0<t\le\delta`$. There are no disc patches, and the frontier construction applies. All these inputs are connected under (C); no disconnected-system minimization is used.

The intersection $`\Gamma_t`$ is nonempty: otherwise $`A_t,B`$ would be disjoint representatives of the input vertices, contradicting their distance two. For the genus-equality branch, every genus inequality in §5.2 is an equality, so no genuine compression occurred. The whole unrounded frontiers partition $`A_t\cup B`$ up to seams of area zero. Rounding saves at least $`\varepsilon_*`$ in total. After fixing both roundings, obtain the finite total push-off constant $`C(t)`$; choose positive $`\sigma`$ with $`C(t)\sigma<\varepsilon_*/4`$. Discarding closed components decreases area. Hence

```math
\begin{aligned}
A(w_\uparrow)+A(w_\downarrow)
&\le\mathrm{Area}(P_\uparrow)+\mathrm{Area}(P_\downarrow)\\ 
&\le\mathrm{Area}(A_t)+\mathrm{Area}(B)-\varepsilon_*+C(t)\sigma\\ 
&\lt A(w)+A(u)-\varepsilon_*/4.
\end{aligned}
```

No uniform $`C(t)`$ as $`t\downarrow0`$ is needed. The dependency order is

```math
(A,B,S)\longrightarrow\text{fixed collars, sign arcs and perturbation scheme}
\longrightarrow(\rho_0,\rho_2,c_*,d_{\partial},\theta_1,a,b,\zeta)
\longrightarrow(\eta_1,\varepsilon_*)\longrightarrow\delta\longrightarrow t
\longrightarrow\eta_2(t)\longrightarrow\text{roundings}\longrightarrow C(t)\longrightarrow\sigma.
```

For (T0), use a small positive constant width on the fixed compact transverse seam. The angle has a positive minimum, each curve has positive gain, and the disc-exchange inequality with $`e=0`$ excludes disc patches. The two frontiers have a positive total saving; choose push-off cost smaller than it, as in competition p. 17 and p. 18. For (T1), the assembly above uses Corollary 5.6 and $`\mathcal H=G`$, omits common-boundary collar terms, and retains clearance to every torus. All equal/disjoint boundary tuples are covered.

The area estimate is established on one set of representatives **before** a later $`z`$. Shrinking widths to avoid that $`Z`$ need not preserve this same numerical saving: the inequality concerns the already fixed vertex area infima, unchanged by later representatives.
