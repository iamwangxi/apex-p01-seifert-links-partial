# The merged partial extension and connected-sum closure

[Overview](../README.md) · [Objects](objects.md) · [Sources](../sources/bibliography.md) · [Scope](scope.md)

Merged proof sequence: [objects and elementary interfaces](objects.md) (§§1–2), [Seifert applications](seifert.md) (§3), and [closure and main theorem](main-theorem.md) (§§4–7). References to these numbered sections use this sequence.

## 4. Connected sums and fibred factors

“Fibred” always refers to the **specified oriented total spanning class** $`\phi`$; a fibration in a different class of the same exterior is irrelevant.

### 4.1. A fibred factor has only one spanning vertex

Let $`J`$ be non-split and fibred, with connected spanning fibre $`F`$. Any incompressible spanning surface disjoint from $`F`$ lies in $`E(J)\mathbin{\|}F=F\times I`$. Straighten its single boundary curve in every vertical annulus to the middle curve. Choose disjoint proper arcs cutting $`F`$ into a disk, and their vertical rectangles. Inessential intersection circles with these disks are removed by incompressibility and irreducibility. Each rectangle has exactly two boundary intersections and hence exactly one trace arc. Straighten these arcs successively. Cutting along them leaves an incompressible system in a ball, with exactly the boundary of the horizontal fibre disk. Cutting a surface along proper arcs injects the groups of its pieces into the original group; thus each piece has trivial group and is a disk. There is one boundary circle and hence one disk, isotopic to the horizontal disk. Gluing back proves the original system isotopic to $`F`$.

Kakimizu Theorem A (p. 226) says the original geometric incompressible complex is connected. The fibre vertex has no distinct geometric neighbor by the product argument, so it is its only vertex. This uses Kakimizu's **connectivity theorem**, not his false disconnected-surface metric formula. Therefore $`X(J)`$ is a point. The unknot follows from §2.3. This is also the argument of [the fibred-surface argument](connected-sum.md#61-a-fibred-link-has-just-one-incompressible-spanning-vertex); no claim that only minimum-norm fibred surfaces were classified is being substituted for it.

### 4.2. Every intermediate connected sum is non-split

Take specified components of two non-split oriented links $`J_1,J_2`$, remove small balls each meeting the specified component in an unknotted arc, and identify the boundary spheres with orientations matching the arcs. In the resulting exterior the punctured decomposing sphere is a proper meridional annulus $`A`$. Its core has $`\phi=\pm1`$, hence infinite order and injective cyclic group. Cutting the exterior along $`A`$ recovers the two factor exteriors, with corners rounded. They are irreducible. Gluing irreducible manifolds along an incompressible surface is irreducible, by the innermost-circle proof of H, pp. 14–15. Thus the sum exterior is irreducible and the sum link non-split. This applies to each node of any finite iterated sum, including unknot factors; pairwise nonzero linking numbers are not required.

### 4.3. Fibredness is exactly inherited from both factors

**Lemma 4.3.** A specified oriented component sum $`J_1\#J_2`$ is fibred in its spanning class if and only if both factors are fibred in their spanning classes.

**Proof.** The single-arc normal form of B §10, p. 22, applies to a spanning fibre as well as any other incompressible surface. For clarity, essential circles on the decomposing annulus are impossible since its core has $`\phi=\pm1`$, while loops on the surface have $`\phi=0`$. Inessential circles are removed by incompressibility and irreducibility. Longitudinal coefficient one leaves a single spanning arc, and cutting the surface gives incompressible factor spanning surfaces.

If the sum surface is a fibre, cutting its product complement along the annulus's remaining product disk gives factor products. Here the product-disk assertion can be seen without a fibredness criterion: in $`F\times I`$, that disk has one arc on each horizontal face and two on the vertical boundary. Projection of the disk gives a proper homotopy of the two horizontal arcs. Proper simple arcs homotopic with these endpoints are isotopic in the surface. Straighten the boundary to that of a vertical rectangle; irreducibility and the usual innermost-disk isotopy make the disk that rectangle. Its complement has the two factor product regions. Thus both factor surfaces are fibres in their prescribed spanning classes.

Conversely boundary-connect the two spanning fibres. Choose their monodromies to fix boundary collars and extend both across the connecting band by the identity. The mapping torus cuts along the meridional annulus into the original two mapping tori; it is the exterior of the specified connected sum. Its fibre has the required single boundary on each torus and is dual to the total $`\phi`$. ∎

In particular one non-fibred original factor makes every intermediate block containing it non-fibred. This checks the hypothesis that cannot be inferred just from an accumulated Euclidean coordinate.

### 4.4. The audited two-factor formulas

For two non-split, non-fibred oriented factors, Banks Theorem 10.3 and the audit [the connected-sum audit](connected-sum.md) give

```math
|X(J_1\#J_2)|\cong |X(J_1)|\times |X(J_2)|\times\mathbb R.
\qquad\text{(4.1)}
```

The exact original is B, p. 22. The checked Banks edition is **arXiv:1109.0965v1, 5 September 2011**; no later journal copy was compared. The product's triangulation, local-class invariance, winding coordinate and edge rule are the ones audited in [the connected-sum audit](connected-sum.md), §§3–4. In particular its distance labels are cyclic widths, not an imported equality of cyclic and graph distances for all incompressible vertices. The audit uses PS Proposition 3.3, Lemma 3.5, and §5's order argument, with the recorded $`R^1\to R^k`$ correction in Lemma 5.5; it does not use PS §4 or §6.

If exactly one factor $`Q`$ is fibred and the other $`J`$ non-fibred, [fibred-factor absorption](connected-sum.md#62-absorption-of-a-fibred-summand-including-edges) proves the all-incompressible absorption

```math
X(J\#Q)\cong X(J).
\qquad\text{(4.2)}
```

This is not inferred from B Proposition 1.3's statement about $`MS`$. The interface is as follows. Cutting any vertex in single-arc normal form gives the unique fibre vertex on the $`Q`$ side. The product-region cutting proof of B Lemma 7.3's first half (p. 15) preserves the other local class under unrestricted global isotopy. Moving the fibre once through its fibration winds its joining boundary once in the meridional direction, since $`\phi_Q(\mu)=1`$, and absorbs every integral band winding. Boundary movement on the other $`Q`$ tori is allowed. This proves the vertex bijection. Width-one configurations on the $`J`$ side extend by two fibre phases and compatible rectangles (B Lemma 8.1); conversely the single-arc normalization of an adjacent pair restricts its whole width-one blocks to width at most one in $`J`$ (B Proposition 8.3, p. 17). Distinct restricted classes have width one. Hence the bijection preserves and reflects edges, and flagness gives (4.2). This is the fibred-link, not merely fibred-knot, absorption proved in the cited audit.

If both factors are fibred, Lemma 4.3 and §4.1 make the sum complex a point. An unknot component-sum is isotopic to the other link and requires no twisting coordinate. All cases are thereby covered.

## 5. The finite closure theorem and the merged partial extension

**Theorem 5.1 (finite specified-component closure).** Let $`J_1,\ldots,J_N`$, $`N\ge1`$, be oriented non-split links with contractible $`X(J_i)`$. Form a binary iterated connected sum, always joining specified components in two previously disjoint blocks. Component choices and the binary tree are arbitrary. Let $`r`$ be the number of original factors non-fibred for their oriented spanning class. Then the result $`L`$ is non-split and

```math
\begin{cases}
X(L)=\{*\},&r=0,\\[2mm]
|X(L)|\cong\displaystyle\prod_{J_i\ \mathrm{nonfibred}}|X(J_i)|\times\mathbb R^{r-1},&r\ge1.
\end{cases}
\qquad\text{(5.1)}
```

In particular $`X(L)`$ is contractible. The second formula is a choice-dependent realization homeomorphism with an ordered product triangulation, not an ordinary categorical product of simplicial complexes. Empty Euclidean dimension means a point; a negative dimension is never used.

**Proof.** By §4.2 every node is non-split; by Lemma 4.3 a node is fibred exactly when its block has zero non-fibred leaves. Induct on the binary tree. Two blocks with zero non-fibred leaves give a point. If just one has non-fibred leaves, absorb the fibred block by (4.2). If their positive leaf counts are $`a,b`$, apply (4.1). The exponent becomes

```math
(a-1)+(b-1)+1=a+b-1,
```

and the factor list is the union of their non-fibred lists. This proves (5.1) for every tree. The component count is $`\sum_i|J_i|-(N-1)`$, as a further check that only component sums, not distant unions or self-gluings, occur. Finite products of contractible factors and a Euclidean space are contractible. The ordinary-product topology here is the one already justified in [the connected-sum audit](connected-sum.md), §4 using countability of the surface complexes and the countable-CW product theorem. ∎

**Theorem 5.2 (merged partial extension).** Let $`\mathcal S`$ consist of nonempty oriented non-split links in the following classes:

- knots, with contractibility supplied by Competition Theorem A and the separate unknot argument;
- links whose incompressible spanning surfaces are all connected, under the connected multiple-boundary geometric inputs stated for D′;
- every balanced Hopf fibre link $`H_{2m}`$, $`m\ge1`$; unbalanced Hopf fibre links are included among the fibred factors below;
- links fibred in their prescribed oriented spanning class;
- two oppositely oriented zero-framed parallels of a nontrivial knot satisfying (SB), as defined in [the cone theorem](parallel-satellites.md);
- two oppositely oriented zero-framed parallels of $`K_{7/19}`$ and its mirror.

Then every finite specified-component connected sum of factors in $`\mathcal S`$ has contractible $`X(L)`$. Formula (5.1) gives its realization and its exact Euclidean exponent. Torus-knot parallel factors have exactly one edge; the $`K_{7/19}`$ parallel factor has the complete tree computed in [the tree theorem](parallel-satellites-k719-tree.md), and its annulus is not a cone vertex. Among two-bridge companions, (SB) has the criterion proved in [§6 of the two-bridge proof](parallel-satellites-two-bridge.md); it holds for $`K_{(2m-1)/(4m-1)}`$, $`m\ge1`$, and their mirrors.

**Proof.** The knot input is stated in §1 of [objects](objects.md). For the all-connected class, Lemma 2.2 converts incompressible connectedness into connectedness of all spanning surfaces, and the connected-edge alignment identifies D′'s geometric complex with $`X`$. D′ then gives contractibility under its declared inputs. The [Hopf-four proof](hopf-four.md) constructs and contracts the tree. The [all-hole Hopf proof](hopf-contraction.md), Theorem 9.1, nullhomotopes every finite inclusion in a finite output complex and applies the CW criterion. Section 4.1 makes a fibred factor a point. The [parallel-satellite cone theorem](parallel-satellites.md), Theorem 1.1, gives a cone for each (SB) factor, and the [torus proof](parallel-satellites-torus.md), Theorem 1.1, gives the exact edge. The [parallel tree theorem](parallel-satellites-k719-tree.md), Theorem 9.1, handles $`K_{7/19}`$. These satellites are non-split by the irreducibility and group-injection proofs. Reflection transports surfaces, their isotopies and essentiality to mirrors; reversing the cover-index convention does not change a width. Hence the reflected factors have isomorphic cyclic complexes. Apply Theorem 5.1. ∎

The product, fibred-factor absorption and induction in Theorem 5.1 do not use PS's projection (§4) or general contractibility proof (§7). The Banks audit still uses PS §3 and §5, as listed in §4.4. No claim of independence from all PS results is made.

The universal all-minimal factor class is not part of this theorem. If a particular such factor has an independent proof that its reduced minimum-norm complex is contractible, it can be added by the conditional reduction in [scope](scope.md). The general $`k=0`$ Seifert branch with exceptional fibres remains outside the supplied contraction theorem; the Hopf fibre family is treated independently.

## 6. All Hopf fibre links and local knot insertions

### 6.1. The four-fibre tree

[the Hopf-four calculation](hopf-four.md) gives a complete description without PS's projection or Theorem 1.1. In its fixed pillowcase marking,

```math
V(X(H_4))=\{p/q:\gcd(p,q)=1,\ q>0\text{ odd}\},
```

```math
p/q\sim p'/q'\quad\Longleftrightarrow\quad |pq'-p'q|=1.
\qquad\text{(6.1)}
```

This is the induced Farey graph on two of the three parity classes, **an infinite tree**, not the full Farey graph. There are no higher simplices. The marking identifies which parity class is deleted, but does not identify vertices by boundary-label permutations. [the Hopf-four calculation](hopf-four.md), §§2–5 prove the annulus-system and slope bijections and use only PS §3 to realize the class-distance minimum; §§6–7 compute the whole-block widths and prove (6.1).

For completeness the final tree proof is short. A slope with odd denominator $`q>1`$ has exactly one neighbor of smaller positive odd denominator: the two determinant equations have denominator residues $`r,q-r`$, and exactly one is odd. Following this neighbor descends to the integer line, whose edges are between consecutive integers. A finite cycle with maximum denominator greater than one would give its maximum-denominator vertex two smaller-denominator neighbors, a contradiction; the integer line has no cycle either. Thus the flag complex is the tree and is contractible. This preserves the stronger structural result, rather than merely replacing it with (3.7).

In particular, for local knot insertions on the four labelled components,

```math
L=H_4\#_1K_1\#_2K_2\#_3K_3\#_4K_4,\qquad
I=\{i:K_i\text{ nonfibred}\},
```

```math
|X(L)|\cong |T|\times\prod_{i\in I}|X(K_i)|\times\mathbb R^{|I|}.
\qquad\text{(6.2)}
```

$`H_4`$ is non-fibred: its kernel is $`\mathbb Z\times\ker(F_3\twoheadrightarrow\mathbb Z)`$, and the latter free kernel has infinitely many Schreier generators; a compact fibre would have finitely generated group ([the Hopf non-fibredness certificate](connected-sum.md), §5). Thus the original non-fibred count in (5.1) is $`1+|I|`$, explaining the exponent $`|I|`$, not $`|I|-1`$. The tree and product description do not use Competition Theorem A. Contractibility for arbitrary non-fibred knot factors in (6.2) uses Theorem A. When there are no such factors, $`X(L)\cong T`$. No equality $`X(L)=IS_{\mathrm{disj}}(L)`$ is asserted for this disconnected family.

### 6.2. The arbitrary-hole matching model and finite nullhomotopies

The [matching model](hopf-model.md), Theorem 1.1, identifies every vertex of $`X(H_{2m})`$ with an $`m`$-arc positive-negative perfect matching on a sphere with $`2m`$ labelled holes. Normalised overlays give the whole-block formula $`\delta=\max H-\min H`$. Distance one implies disjoint normal representatives for every $`m`$. The converse holds for six holes, whose complex contains a tetrahedron; it is not asserted for arbitrary $`m`$.

The [contraction](hopf-contraction.md), Theorem 9.1 and §§9–12, produces, for every finite $`K\subset X(H_{2m})`$ and fixed $`M_*`$, a finite $`Y`$ containing $`K\cup\{M_*\}`$ and a homotopy of the inclusion to $`M_*`$ inside $`Y`$. Common equivariant heights are interpolated, and monotone boundary restrictions certify legal regular-fibre matchings after closed components are removed. Phase averaging takes place in arc coordinates, producing a flow in the perfect-matching polytope of the actual embedded support graph.

The fixed-graph Theorem 1.1 proves that region-potential common rounding decodes this flow into a true cyclic simplex. It covers disconnected graphs, bridges, non-disk regions and common arcs. It is continuous, agrees after zero-edge deletion and recovers every true input simplex's barycentric coordinates exactly. Finite templates provide a uniform finite arc coordinate set, so finitely many graph decoders glue along common zero faces. Initial band-occupation lengths give the original input flow, and interpolation to $`M_*`$ gives the required nullhomotopy. Compact-image finiteness and Whitehead prove contractibility; $`Y`$ itself need not be contractible.

Circle maps, regular fibres and averaging are credited to Hatcher 2008, second proof, pp.5–6. The planar bipartite face-height structure is classical background, as in Propp, arXiv:math/0209005v3, §3, Theorem 2, pp.21–22; all rounding facts used here are proved in full. PS Theorem 1.1's statement already covers the balanced Hopf family. The contribution is an independent family proof with this finite-input mechanism, avoiding PS §§4–7 and retaining the §3 model and distance interface.

**Corollary 6.2 (all Hopf fibre links).** Every nonempty oriented link consisting of fibres of the Hopf fibration has contractible $`X`$.

**Proof.** Choose a reference Hopf orientation and let $`\epsilon_i=\pm1`$ be the actual signs. The regular fibre has


```math
k=\phi(f)=\sum_i\epsilon_i.
```


If $`k=0`$, the link is $`H_{2m}`$ for some $`m\ge1`$, handled by Theorem 9.1 of the contraction. If $`k\ne0`$, the [Seifert dichotomy](seifert.md), Theorem 3.1, proves fibration in the prescribed spanning class, and §4.1 makes $`X`$ a point. A single fibre is the unknot. Pairwise reference linking number one proves non-splitness when there is more than one fibre. Reflection gives the corresponding mirror convention. ∎

This corollary does not include arbitrary unions of fibres of Seifert fibrations with exceptional fibres; those require their own vertical-case proof.

### 6.3. Fibredness and the exact $`2m`$-insertion exponent

For every balanced Hopf link,


```math
\pi_1(E(H_{2m}))=\mathbb Z\langle f\rangle\times F_{2m-1},\qquad\phi(f)=0.
```


The restriction $`\psi:F_{2m-1}\to\mathbb Z`$ is onto. Choose a free basis $`x,y_1,\ldots,y_{2m-2}`$ with values $`1,0,\ldots,0`$; a positive peripheral free generator supplies $`x`$, and elementary Nielsen changes remove the other values. Reidemeister–Schreier gives the free basis


```math
\{x^ny_jx^{-n}:n\in\mathbb Z,\ 1\le j\le2m-2\}
```


for $`\ker\psi`$. If $`m\ge2`$, it has infinite rank, and $`\ker\phi=\mathbb Z\times\ker\psi`$ is not finitely generated. A compact connected spanning fibre would have a finitely generated kernel group. Thus every balanced $`H_{2m}`$ with $`m\ge2`$ is nonfibred. This is the [four-fibre kernel argument](connected-sum.md), §5, with $`2m-2`$ zero-valued generators.

For $`m=1`$, $`P_2`$ is an annulus, and projection $`S^1_f\times P_2\to S^1`$ onto its annular circle is the prescribed spanning fibration, with annular fibre. Its kernel is $`\mathbb Z\langle f\rangle`$, and $`X(H_2)`$ is a point. There is no infinite-rank argument in this case.

Put


```math
L_m=H_{2m}\#_1K_1\cdots\#_{2m}K_{2m},\qquad I=\{i:K_i\text{ is nonfibred}\}.
```


Each insertion is an oriented component sum between the current block and a new knot factor. For $`m\ge2`$, the original nonfibred count is $`r=1+|I|`$, so Theorem 5.1 gives


```math
|X(L_m)|\cong |X(H_{2m})|\times\prod_{i\in I}|X(K_i)|\times\mathbb R^{|I|}.\qquad\text{(6.3)}
```


Fibred knots add no winding coordinate. If $`I`$ is empty the realization is $`|X(H_{2m})|`$. For the fibred base $`H_2`$, $`r=|I|`$, and the exact formula instead is


```math
\begin{cases}
X(L_1)=\{*\},&I=\varnothing,\\ 
|X(L_1)|\cong\displaystyle\prod_{i\in I}|X(K_i)|\times\mathbb R^{|I|-1},&|I|\ge1.
\end{cases}\qquad\text{(6.4)}
```


No negative exponent occurs. The structural products use Banks and fibred absorption; contraction of arbitrary nonfibred knot factors additionally invokes Competition Theorem A.

For the $`K_{7/19}`$ two-parallel factor, [normalisation](parallel-satellites-normalisation.md), §3, proves that $`\pi_1(T)=\mathbb Z^2`$ injects into $`\pi_1(E(L))`$. Total oriented linking vanishes on all of the companion group, so this torus group lies in $`\ker\phi`$. A compact connected spanning fibre has a free group, which cannot contain $`\mathbb Z^2`$. This factor and its mirror are therefore non-fibred in their specified spanning class. The same argument applies to the nontrivial (SB) parallel factors.

## 7. Dependency boundaries and the remaining problem

### 7.1. Dependency table

| Conclusion | Inputs actually used | Limits |
|---|---|---|
| Boundary formula, connected complement and compression implication (2.2) | Meridional homology; elementary compression and cover arguments | No projection or analytic input |
| Seifert $`k=0`$ annuli, norm zero and $`X=MS`$ | H Lemmas 1.10–1.11, Proposition 1.12 and the exact boundary slopes | Structure only; no general contraction |
| Seifert $`k\ne0`$ fibration and point | H horizontal cover and product complement, pp. 22–23; §4.1 | No D′ analytic or PS projection input needed |
| Seifert-exterior link classification | H model and section moves; explicit filling presentations; triangle reflection and genus-one gluing | No general JSJ classification |
| Fibred factor is a point; intermediate non-splitness and fibredness | Product disks; Kakimizu Theorem A connectivity; decomposing annulus | No disconnected metric equivalence |
| Banks product, fibred absorption and (5.1) | B Theorem 10.3; [the all-incompressible audit](connected-sum.md); PS Proposition 3.3, Lemma 3.5 and §5 order, with the recorded subscript correction | No PS §4 projection, §6 observer lemma or §7 contraction; no general path-metric equality |
| Knot factors | Competition Theorem A and the unknot exception | Its analytic inputs are inherited |
| All-connected factors | D′, with $`U,E`$, (Fin), regularity and local exchange inputs; (2.2) | The multiple-boundary analytic package is not independently certified |
| $`H_4`$ tree and contraction | [Slope, whole-block width and tree proofs](hopf-four.md); PS §3 | No projection or PS general contraction |
| All balanced $`H_{2m}`$: model and finite-input contraction | [Matching/whole-block model](hopf-model.md), PS §3; [finite heights, arc flow, fixed-graph rounding and zero-face gluing](hopf-contraction.md); Hatcher 2008 method; classical Propp face-height background; CW compactness and Whitehead | Every $`m\ge1`$; no PS §§4–7 input; no exceptional-fibre vertical contraction |
| Two torus-knot parallels: exactly one edge | [All-genus companion and joint-isotopy classification](parallel-satellites-torus.md); direct two-chamber width and lower bound | No Competition Theorem A, D′ or PS projection/contraction |
| (SB) parallels: annulus cone | [Minimum cut pieces, same-representative disjointness and whole-block separation](parallel-satellites.md) | No classification of the remaining vertices |
| Two-bridge (SB) criterion and infinite family | HT Theorem 1, Propositions 1–2; neighbourhood double and component counts; exact continued fractions | Not every two-bridge knot satisfies (SB) |
| $`K_{7/19}`$ complete tree | [Joint normal forms](parallel-satellites-k719-normal-forms.md), [torus comparison](parallel-satellites-normalisation.md), [zero return subgroup and both directions of arc correspondence](parallel-satellites-k719-tree.md); HT; B Proposition 4.10 and §10 | All genera and twists included; (SB) fails and the annulus is not a cone vertex |
| PS three-statement counterexample and finite filling | [Self-contained certificate](ps-counterexample.md), PS §3/§5 and Banks sections/edges/ordered products | PS Theorem 1.1's statement is not refuted; no general replacement contraction |
| Merged Theorem 5.2 | The applicable factor result, then (5.1) | No independent certification of inherited inputs; no all-link conclusion |

Banks's product theorem is an existing result. The Hopf-family proof adapts Hatcher's 2008 method and proves the necessary planar matching-height decoder, with Propp's lattice structure as classical background. The principal contributions relative to the target are the fixed-boundary finite-input mechanism and the complete satellite cone, edge and tree calculations; connectedness and the audited closure organise them. The bounded literature-search status and the PS counterexample's effect on the factor list are explained in [scope](scope.md).

### 7.2. Remaining problem

The general $`k=0`$ Seifert branch retains its vertical-annulus classification and equality with reduced $`MS`$. This package proves contractibility for every balanced $`H_{2m}`$ in that branch, and for unbalanced Hopf fibre links in the horizontal branch. No general exceptional-fibre vertical contraction is supplied. A remaining link need not have a non-minimal vertex: disconnected all-minimal systems already lie beyond the proved factor list.

The (SB) parallel links enter the closure despite their disconnected non-minimal vertices. The $`K_{7/19}`$ factor is additionally included by its independent tree theorem, beyond (SB). Its distance-two annulus example is compatible with that contraction. General satellite/JSJ gluing, disconnected cyclic/geometric comparison, and all-link contractibility remain outside the conclusions.
