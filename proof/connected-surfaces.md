# Connected spanning surfaces: a partial extension of Theorem D

Theorem D′ replaces linking-indecomposability by connectedness of every spanning surface. Its contractibility conclusion inherits the competition paper's connected, multiple-boundary geometric inputs and combinatorial Theorem B. These are stated precisely in §5.1; they are not independently certified here.

[Overview](../README.md) · [Objects](objects.md) · [Sources](../sources/bibliography.md) · [Scope](scope.md)

D′ proof sequence: [statement, connectivity and examples](connected-surfaces.md) (§§1–4); [exchange topology and fixed classes](connected-surfaces-exchange.md) (§§5.1–5.3); [collars and area gain](connected-surfaces-collars.md) (§§5.4–5.6); [contractibility and truncations](connected-surfaces-contractibility.md) (§§5.7–6). Section references in this sequence retain this numbering.

## 1. Conventions and statement

Let $`L=L_1\cup\cdots\cup L_n\subset S^3`$ be a nonempty oriented link, and let $`E=E(L)`$. A **spanning surface** means a compact oriented, properly embedded surface obtained by restricting an oriented surface $`\Sigma\subset S^3`$, with $`\partial\Sigma=L`$, to the exterior. It has **no closed components** and exactly one boundary curve on each boundary torus, with the orientation prescribed by $`L`$. It need not be incompressible, of minimum genus, or connected. The curves are the surface-framed longitudes, not generally the preferred longitudes.

This is Kakimizu's actual convention: K, p. 225. In particular, “all spanning surfaces” below includes compressible and non-minimal surfaces, but does not allow the addition of extraneous closed components. If arbitrary closed components were allowed, the connectedness hypothesis would be impossible, and the rank inequality below would be false after adding sufficiently many small spheres.

Write $`\mathrm{(C)}`$ for the condition that **every spanning surface for $`L`$ is connected**. Let $`IS(L)`$ be Kakimizu's original complex: its vertices are ambient-isotopy classes of componentwise incompressible spanning surfaces, and a finite collection of distinct classes is a simplex exactly when it has simultaneously pairwise disjoint representatives. We retain this geometric adjacency throughout.

**Theorem D′ (with the original geometric inputs).** Suppose $`L`$ is non-split, is not the unknot, and satisfies $`\mathrm{(C)}`$. Equip its exterior and its surface-framed boundary foliations with the same geometric interface used in the competition paper's Theorem D, described in §5 below. Then $`IS(L)`$ is contractible. Every nonempty full subcomplex whose vertex set is downward closed for the lexicographic complexity $`(g,A)`$ is contractible and isometrically embedded for the edge-path metric. In particular this applies to the nonempty genus truncations, and to

```math
D_{\ell,a}=\{v:g(v)<\ell\}\ \cup\ \{v:g(v)=\ell,\ A(v)\le a\}.
```

The geometric inheritance is part of the statement. It is neither a new existence/compactness theorem for disconnected surface systems nor an independent repair of the original analytic sources.

## 2. A computable sufficient condition for (C)

Let

```math
\phi:\pi_1(E)\longrightarrow\mathbb Z
```

send every oriented meridian to $`1`$. Let $`\widetilde E_\phi`$ be the corresponding infinite cyclic cover, with positive deck generator $`t`$. Put

```math
\Lambda=\mathbb Q[t,t^{-1}],\qquad K=\mathbb Q(t),\qquad
r_\phi(L)=\dim_K\bigl(H_1(\widetilde E_\phi;\mathbb Q)\otimes_\Lambda K\bigr).
```

**Lemma 2.1 (all-surface connectivity bound).** Every spanning surface $`F`$ satisfies

```math
b_0(F)-1\le r_\phi(L).
```

**Proof.** Set $`c=b_0(F)`$, and write $`F=F_1\sqcup\cdots\sqcup F_c`$. Three details of the proof are important.

**(a) The cut-open exterior is connected.** Since there are no closed components, each $`F_j`$ contains a boundary curve on some torus $`T_i`$. There is exactly one curve $`\lambda_i`$ of $`\partial F`$ on that torus. Its longitudinal coefficient is $`1`$, so an oriented meridian $`\mu_i\subset T_i`$ can be chosen to meet $`\lambda_i`$ transversely in exactly one point. Straighten the proper surface in a collar and push $`\mu_i`$ a little into $`E`$. The resulting loop meets $`F`$ exactly once, in $`F_j`$, and misses every other component. Removing its short crossing arc leaves a path in $`E\setminus F`$ joining the two local sides of $`F_j`$.

For completeness, form the dual adjacency graph of the cut-open exterior: vertices are its connected regions, and one edge for each connected two-sided component $`F_j`$, joining the regions on its two sides. Each side of a connected $`F_j`$ has a connected collar, so these endpoints are well defined. The preceding meridian argument says that every edge is a loop. The graph is connected: a path in the connected manifold $`E`$, put in general position relative to $`F`$, gives a walk between any two regions. A connected graph all of whose edges are loops has one vertex. Thus the cut-open manifold $`C`$, and equivalently $`E\setminus F`$, is connected. This argument uses neither incompressibility nor minimum genus, nor even non-splitness.

This agrees with the relevant assertions in K, p. 226, and PV, p. 6. The argument above supplies the missing explicit meridian justification rather than treating either assertion as a connectedness assumption.

**(b) The cyclic cover is the stack obtained by cutting along the whole surface.** With the specified orientations, intersection with $`F`$ represents $`\phi`$: it takes value $`1`$ on every oriented meridian, and meridians form a basis of $`H_1(E;\mathbb Z)`$. In particular every loop avoiding $`F`$ has $`\phi=0`$.

Take copies $`C_k`$ of the connected cut-open manifold, indexed by $`k\in\mathbb Z`$. Label the two cut faces so that a positive crossing increases the index, and glue the corresponding face of $`F_j`$ in $`C_k`$ to the other face in $`C_{k+1}`$, **for every $`j`$**. Locally this is an ordinary covering, including the boundary half-space charts. The index change of a lifted loop is its algebraic intersection with $`F`$, hence $`\phi`$. The space is connected since $`C`$ is connected and the nonempty interfaces join successive levels. Thus this is $`\widetilde E_\phi`$, with $`t(C_k)=C_{k+1}`$. There is no assumption that $`F`$ is connected in this construction, and no assignment of different surface components to different deck steps.

**(c) The Mayer–Vietoris sequence detects the number of components.** The equivariant graph-of-spaces Mayer–Vietoris sequence for this stack contains

```math
\begin{aligned}
H_1(F;\mathbb Q)\otimes\Lambda
&\longrightarrow H_1(C;\mathbb Q)\otimes\Lambda
\longrightarrow H_1(\widetilde E_\phi;\mathbb Q)\\ 
&\xrightarrow{\delta} H_0(F;\mathbb Q)\otimes\Lambda
\xrightarrow{i_- -t i_+} H_0(C;\mathbb Q)\otimes\Lambda
\longrightarrow H_0(\widetilde E_\phi;\mathbb Q)\longrightarrow0.
\end{aligned}
```

One can obtain this directly from the cellular chain sequence for the vertex spaces $`C_k`$ and interface mapping cylinders $`F\times[0,1]`$; direct sums over $`k`$ are identified with tensoring by $`\Lambda`$. The two endpoint inclusions give the difference $`i_- -t i_+`$. All tensor products in this displayed sequence before localization are over $`\mathbb Q`$.

Since $`C`$ is connected, both endpoint inclusions send the generator of $`H_0(F_j;\mathbb Q)`$ to the unique generator of $`H_0(C;\mathbb Q)`$. Consequently the last nontrivial map is

```math
\Lambda^c\longrightarrow\Lambda,\qquad
(a_1,\ldots,a_c)\longmapsto(1-t)\sum_{j=1}^c a_j.
```

Its kernel is free of rank $`c-1`$, with basis $`e_j-e_c`$, $`1\le j<c`$. Exactness makes $`\delta`$ surjective onto that kernel. Localization from $`\Lambda`$ to $`K`$ is flat, so it preserves this surjection and yields

```math
H_1(\widetilde E_\phi;\mathbb Q)\otimes_\Lambda K\twoheadrightarrow K^{c-1}.
```

The asserted inequality follows. $`\square`$

**Corollary 2.2.** If $`r_\phi(L)=0`$, every spanning surface for $`L`$ is connected. Thus the total-linking Alexander module being torsion is a sufficient condition for $`\mathrm{(C)}`$.

**Corollary 2.3.** If $`r_\phi(L)=0`$, $`L`$ is non-split. Indeed a splitting sphere divides $`L`$ into two nonempty sublinks contained in disjoint balls. Apply the usual Seifert construction separately inside those balls. The union of the resulting surfaces, restricted to the exterior, is a disconnected spanning surface with no closed components, contradicting Corollary 2.2. This is a certificate of non-splitness independent of the desired contractibility conclusion.

No converse to Corollary 2.2 is asserted. We use the module-rank definition, rather than an unspecified normalization of a one-variable Alexander polynomial.

## 3. The two-component case

A two-component link is a **boundary link** if its two components bound disjoint connected oriented Seifert surfaces in $`S^3`$.

**Proposition 3.1.** For a two-component oriented link, the following are equivalent:

1. There exists a disconnected spanning surface in the above convention.
2. The link is a boundary link.

**Proof, 1 ⇒ 2.** A spanning surface has two boundary curves and no closed components. Thus, if disconnected, it has exactly two connected components, each with one boundary curve. Extend each component across its own tubular neighborhood by the collar annulus joining that surface-framed longitude to the oriented core $`L_i`$. These extensions are disjoint, since the two neighborhoods and the original surface components are disjoint. They are connected oriented Seifert surfaces for $`L_1`$ and $`L_2`$.

**Proof, 2 ⇒ 1.** Start with the two disjoint oriented Seifert surfaces. Choose sufficiently small tubular neighborhoods of the two link components, meeting the surfaces in boundary collars. Restrict the surfaces to the exterior. Their union is a disconnected spanning surface with no closed components. Any initially fixed tubular neighborhood can be used after the usual collar adjustment by ambient isotopy. $`\square`$

This equivalence does not require non-splitness. In particular, $`\mathrm{(C)}`$ is equivalent to “not a boundary link” for two components. Theorem D′ therefore applies, with its inherited geometric inputs, to every non-split two-component link which is not a boundary link. This does not claim that every two-component link satisfies $`r_\phi=0`$, nor that $`r_\phi>0`$ characterizes boundary links. For three or more components, merely not being a boundary link is insufficient: a disconnected spanning surface may partition the components into fewer than $`n`$ blocks.

## 4. Exact new examples

The accompanying [script](../scripts/example-certificates.py) uses Python and Sympy and writes [the exact certificate](../scripts/example-certificates-results.json) next to itself. The recorded and repeated runs use Sympy 1.14.0. Words, matrices, all nonzero maximal minors, crossing ownership and the packaged script SHA-256 are included. See [reproduction instructions](../scripts/README.md).

### 4.1 Why the computation gives the module rank

For an $`m`$-strand braid, use free meridians $`x_1,\ldots,x_m`$ and the Artin action

```math
\begin{aligned}
\rho(\sigma_i)(x_i)&=x_i x_{i+1}x_i^{-1},&
\rho(\sigma_i)(x_{i+1})&=x_i,\\ 
\rho(\sigma_i^{-1})(x_i)&=x_{i+1},&
\rho(\sigma_i^{-1})(x_{i+1})&=x_{i+1}^{-1}x_i x_{i+1}.
\end{aligned}
```

All other generators are fixed. Our convention is
$`\rho(g_1\cdots g_k)=\rho(g_1)\circ\cdots\circ\rho(g_k)`$.
The closed-braid group has presentation

```math
\langle x_1,\ldots,x_m\mid \rho(\beta)(x_j)x_j^{-1},\ 1\le j\le m\rangle.
```

To see this without a link-table identification, the complement of the braid together with its axis is the mapping torus of the punctured disk, with the additional stable-letter conjugation relations implementing $`\rho(\beta)`$. Filling back the axis kills the stable letter (the axis meridian), yielding precisely the displayed presentation.

Compute Fox derivatives of the actual freely reduced relator words and substitute $`x_i=t`$ for every $`i`$. If $`J_\beta`$ is the abelianized Fox Jacobian of $`\rho(\beta)`$, the relation matrix is

```math
A_\beta=J_\beta-I_m.
```

The associated presentation-cover chain complex has

```math
d_2=A_\beta^{\mathsf T},\qquad
d_1=(t-1,\ldots,t-1).
```

Its first homology is the Alexander module of the link: first homology of the cover depends on the kernel subgroup of the presented fundamental group, so no asphericity of the presentation complex is needed. The Fox identity gives $`A_\beta\mathbf1=0`$. Since $`d_1`$ has rank $`1`$ over $`K`$,

```math
r_\phi(\widehat\beta)=(m-1)-\mathrm{rank}_K A_\beta.
```

Thus, for $`m=3`$, a nonzero two-by-two minor and the identity $`A_\beta\mathbf1=0`$ certify rank exactly $`2`$, hence $`r_\phi=0`$.

### 4.2 The specified two-component braid

Take

```math
\beta_2=(\sigma_1\sigma_2^{-1})^2\sigma_1.
```

Tracking the top labels through the five crossings gives bottom-position labels $`(1,3,2)`$, with closure cycles $`\{1\}`$ and $`\{2,3\}`$: **two components**. The crossing between labels $`2,3`$ is a self-crossing of the second component. The four intercomponent crossing signs, in braid order, are $`+,-,-,+`$, so their half-sum is **linking number zero**. For two components this is exactly failure of linking-indecomposability.

The script gives

```math
A_{\beta_2}=\begin{pmatrix}
-(t-1)^3&t(t-1)^2&-(t-1)^2\\ 
(t-1)^2&-t^2+t-1&t\\ 
-(t-1)^2/t^2&1&-(2t-1)/t^2
\end{pmatrix}.
```

The first two rows and first two columns have determinant

```math
\det\begin{pmatrix}
-(t-1)^3&t(t-1)^2\\ 
(t-1)^2&-t^2+t-1
\end{pmatrix}=(t-1)^3\ne0.
```

This is the same minor as the discussion's certificate after reversing the signs of both displayed rows. Row sums vanish, so the rank is exactly $`2`$, and **$`r_\phi=0`$**. Corollary 2.3 certifies **non-splitness**. The link is therefore outside the original Theorem D's hypothesis and inside Theorem D′'s hypothesis.

No assertion of a standard table name is needed or made; the explicit braid is the definition of the example.

### 4.3 A three-component example

Take

```math
\beta_3=(\sigma_1\sigma_2^{-1})^3.
```

Its bottom-position labels are $`(1,2,3)`$, so its closure has **three components**. Every pair of top labels crosses twice, once positively and once negatively. Thus **all three pairwise linking numbers are zero**. Every nontrivial partition has all cross-linking sums zero, so the link is not linking-indecomposable.

The exact relation matrix is

```math
A_{\beta_3}=\begin{pmatrix}
-(t-1)^3&t(t-1)^2&-(t-1)^2\\ 
-(t-1)^2/t^2&0&(t-1)^2/t^2\\ 
(t-1)^2(t^2-t+1)/t^3&-(t-1)^2/t&(t-1)^3/t^3
\end{pmatrix}.
```

Its first two rows and first two columns have determinant

```math
\frac{(t-1)^4}{t}\ne0.
```

Again the row sums vanish, giving rank exactly $`2`$, **$`r_\phi=0`$**, and therefore **non-splitness**. This is a second explicit example outside the original hypothesis. We do not rely on identifying it with a standard named link.

### 4.4 Independent implementation cross-check

Separately from free-word substitution and differentiation, the script multiplies hard-coded generator matrices with the blocks

```math
J_{\sigma_i}=\begin{pmatrix}1-t&t\\1&0\end{pmatrix},\qquad
J_{\sigma_i^{-1}}=\begin{pmatrix}0&1\\t^{-1}&1-t^{-1}\end{pmatrix}.
```

Because every Artin image has total exponent $`1`$, the abelianized left Fox chain rule is
$`J_{\alpha\circ\gamma}=J_\gamma J_\alpha`$, fixing the product order. This separately implemented product agrees entry by entry with the Jacobian obtained from the expanded free words for both examples.

It also descends to the quotient by the invariant line $`K\mathbf1`$. The determinants of $`I`$ minus the resulting two-dimensional matrices are, respectively,

```math
\frac{(t-1)^3(t^2+t+1)}{t^2},\qquad
\frac{(t-1)^4(t^2+t+1)}{t^3}.
```

Both are nonzero, independently confirming that the unreduced matrix has exactly a one-dimensional fixed space. The JSON also records their quotient by $`1+t+t^2`$ as a Burau closure-polynomial cross-check; no polynomial-normalization convention is needed for the rank proof.

This is an independent computational route to the same Alexander invariant, not a claim of a second unrelated topological invariant. Convention checks include positive and negative generator inverses, the braid relation in both free words and matrices, the two-component unlink (rank $`1`$), and the positive Hopf link (rank $`0`$, linking number $`1`$). No floating-point specialization is used.

As a separate presentation check, specializing the relation matrices at $`t=1`$ gives ordinary first-homology dimensions $`2`$ and $`3`$, agreeing with the component counts obtained by tracking crossings. There is also no ambiguity from reversing the stacking order for these particular examples: the five-letter word $`\beta_2`$ is a palindrome, while the reverse of $`\beta_3`$ is $`(\sigma_2^{-1}\sigma_1)^3`$, a cyclic conjugate of $`\beta_3`$, with the same oriented closure.
