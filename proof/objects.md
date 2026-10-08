# Objects, boundary data and elementary interfaces

[Overview](../README.md) · [Objects](objects.md) · [Sources](../sources/bibliography.md) · [Scope](scope.md)

Merged proof sequence: [objects and elementary interfaces](objects.md) (§§1–2), [Seifert applications](seifert.md) (§3), and [closure and main theorem](main-theorem.md) (§§4–7). References to these numbered sections use this sequence.

## 1. Object, boundary data, and the factor inputs

All links are nonempty, tame, oriented links in $`S^3`$. Write $`E=E(L)`$, $`T_i=\partial N(L_i)`$, and let

```math
\phi:\pi_1(E)\longrightarrow\mathbb Z,\qquad \phi(\mu_i)=1,
```

where $`\mu_i`$ is positive for the actual orientation of $`L_i`$. Let $`\alpha=\mathrm{PD}(\phi)\in H_2(E,\partial E;\mathbb Z)`$. A spanning surface is oriented and properly embedded, has **no closed components**, and has exactly one oriented boundary curve on each labelled $`T_i`$, extending across $`N(L_i)`$ to the oriented link. Incompressibility is componentwise. Ambient isotopies start at the identity and preserve the boundary-torus labels; the boundary curves can slide. These are the link-spanning conventions of Kakimizu, p. 225, and Banks Definition 2.1, p. 2.

For spanning surfaces $`S,R`$, take a connected lift $`V_R`$ of the **whole** open complement $`E\setminus R`$ to the cover defined by $`\ker\phi`$, and translates $`V_{S,j}=\tau^j V_{S,0}`$. Define

```math
D(S,R)=\max\{j:V_R\cap V_{S,j}\ne\varnothing\}
       -\min\{j:V_R\cap V_{S,j}\ne\varnothing\},
\qquad
\delta([S],[R])=\min_{S'\in[S],\,R'\in[R]}D(S',R').
```

An independent deck choice for each component is not permitted. $`X(L)=IS_{\mathrm{cyc}}(L)`$ is the flag complex whose vertices are the incompressible spanning classes and whose distinct vertices are adjacent when $`\delta=1`$. This is exactly Banks Definition 10.1, p. 22. Realizations carry the weak simplicial topology, and the products below are ordinary topological products, with Banks's ordered triangulation at the simplicial level. We set $`X(U)=\{*\}`$ for the unknot, also proved directly in §2.3.

The norm complexity is

```math
\chi_-(F)=\sum_{C\subset F}\max\{0,-\chi(C)\}.
```

In $`MS(E(L))=MS(E,\gamma,\alpha)`$, the prescribed oriented boundary $`\gamma`$ is the one in §2.1, and we use the **reduced link-spanning convention, with no closed components**. This is essential to any claimed equality with $`X`$. The journal PS general wording explicitly excludes tori (p. 1490); a literal enlargement by null-homotopic sphere components would have extra vertices and a disconnected complement, contrary to its complete-complement construction (p. 1492). Such spheres are suppressed in the usual essential/reduced reading of its link complex. We do not assert that deletion is an ambient isotopy, or identify $`X`$ with a sphere-adjoining enlargement. Equality with reduced $`MS`$ below is a structural statement and does not invoke PS Theorem 1.1 for contractibility.

The contractibility inputs and direct computations are kept separate:

1. **Competition Theorem A:** $`IS(K)`$ is contractible for nontrivial knots; the unknot is a point. Source C, p. 2. For connected spanning surfaces its graph is the cyclic graph, and its complex is flag, so it gives contractibility of $`X(K)`$.
2. **D′:** if every spanning surface is connected and the link is non-split and nontrivial, its geometric complex is contractible, under the connected multiple-boundary geometric interface explicitly inherited in [D′](connected-surfaces.md), §§5.1–5.7. This includes $`U`$, fixed and sliding attainment $`E`$, compactness/finiteness (Fin), boundary regularity, and the stated local exchange estimates. We do not replace this by an independently proved analytic theorem. Source C, pp. 7–8 and pp. 21–22; [D′ geometric inputs](connected-surfaces-exchange.md), §5.1.
3. **Direct factor results:** the [matching model](hopf-model.md) and [finite-input contraction](hopf-contraction.md) prove contractibility of every balanced $`X(H_{2m})`$, $`m\ge1`$; the [four-fibre calculation](hopf-four.md) retains its Farey tree. The [Seifert dichotomy](seifert.md) covers unbalanced Hopf fibre links as prescribed-class fibred links, and the [fibred-surface argument](connected-sum.md#61-a-fibred-link-has-just-one-incompressible-spanning-vertex) makes each fibred factor a point. The [parallel-satellite proofs](parallel-satellites.md) give the annulus cone under (SB), [exactly one edge for torus companions](parallel-satellites-torus.md), and a [complete tree for $`K_{7/19}`$ and its mirror](parallel-satellites-k719-tree.md). These contractions avoid PS's projection and general contraction. Hopf models retain PS §3; the Banks audit retains its declared PS §3 and §5 interfaces. The finite-input proof credits Hatcher 2008's circle-map method and Propp's classical planar matching-height background, while proving its fixed-graph rounding and parameter gluing explicitly.

PS Theorem 1.1 is not a contractibility input to this package. The [counterexample](ps-counterexample.md) refutes three intermediate statements in its disconnected range; this does not refute Theorem 1.1's statement, which already covers the norm-zero balanced Hopf family. See [scope](scope.md).

Source codes H, J, B, C and K identify the exact editions in the [bibliography](../sources/bibliography.md). Citations use their printed page numbers.

## 2. Elementary interfaces needed for the applications

### 2.1. The longitude is determined by the whole oriented link

Let $`\ell_i`$ be the preferred longitude of the individual component. Every spanning surface has boundary slope

```math
\gamma_i=\ell_i-s_i\mu_i,\qquad
s_i=\sum_{j\ne i}\mathrm{lk}(L_i,L_j).
\qquad\text{(2.1)}
```

Indeed $`\partial F=\sum_i(\ell_i+b_i\mu_i)`$ is zero in $`H_1(E;\mathbb Z)`$, and

```math
H_1(E;\mathbb Z)=\bigoplus_i\mathbb Z[\mu_i],\qquad
[\ell_i]=\sum_{j\ne i}\mathrm{lk}(L_i,L_j)[\mu_j].
```

The coefficient of $`\mu_i`$ gives $`b_i=-s_i`$. Also $`\phi(\ell_i)=s_i`$, so $`\phi(\gamma_i)=0`$. Thus $`(\mu_i,\gamma_i)`$ is a basis of $`H_1(T_i;\mathbb Z)`$, and $`\gamma_i`$ generates the primitive kernel of $`\phi|_{T_i}`$. The individual zero-framed longitudes cannot be substituted for (2.1). This rederives C, equation (26), p. 20, pp. 20–21.

Intersection with the oriented whole surface represents $`\phi`$, since it is one on every oriented meridian. In particular all loops on the surface have $`\phi=0`$: push them into a normal collar, off the entire surface system.

**Connected-complement fact.** The cut-open exterior of any spanning surface, even a compressible or disconnected one, is connected. A meridian at a boundary of each component crosses that component once and misses all the others. After deleting its crossing segment it connects that component's two sides in the complement. In the dual graph of complement regions, every surface-component edge is therefore a loop. The graph is connected because $`E`$ is connected; hence it has one vertex. Stacking copies of this cut block, with every component glued to the next common level, constructs the cover for $`\phi`$. This proves the fact used by K, p. 226, without assuming surface connectedness.

### 2.2. Incompressible connectedness is enough for D′

**Lemma 2.2.** Every spanning surface can be compressed, discarding closed components, to an incompressible spanning surface. The number of boundary-bearing components cannot decrease. Consequently

```math
\text{every incompressible spanning surface is connected}
\quad\Longleftrightarrow\quad
\text{every spanning surface is connected}.
\qquad\text{(2.2)}
```

**Proof.** Compression is in the interior and never joins two existing components. Every original component has boundary, and at least one descendant retains that boundary after each compression. Closed descendants can be discarded without affecting the spanning boundary or relative class: the map $`H_2(E)\to H_2(E,\partial E)`$ is zero. For link exteriors this also follows because absolute $`H_2`$ is generated by boundary-torus classes.

For termination put $`n=|L|`$, $`c=b_0(F)`$, and

```math
q(F)=\frac{n-\chi(F)}2=\sum_C g(C)+n-c\in\mathbb N.
```

A nonseparating compression drops $`q`$ by one. A separating compression with boundary on both sides increases (c) by one and drops $`q`$ by one. If one side is closed, its genus is $`h\ge1`$, since a genus-zero side would make the compressing circle inessential; discarding that side drops $`q`$ by $`h`$. Thus every essential compression strictly decreases $`q`$. If some component is compressible, an innermost intersection argument applied to a compressing disk supplies a compressing disk with interior disjoint from the whole system: remove inessential circles on the system, or take an innermost essential one as the new disk. Termination therefore gives componentwise incompressibility. A disconnected initial surface cannot become connected. The reverse implication in (2.2) is immediate. ∎

On this class the connected-surface disjointness and cyclic distance-one edge conventions agree. In one direction a connected surface disjoint from another lifts into one complete cut block; successive connected walls of its translates bound a block meeting at most two consecutive blocks of the other surface. Distinct classes have positive width, so the width is one. Conversely the simplified-position width-one argument gives almost disjoint representatives; for connected distinct classes a coincident component would be the whole surface, so the representatives are disjoint. This is the all-incompressible version of B Lemma 4.13 (p. 9), audited in [the connected-sum audit](connected-sum.md), §§3–4. The fibred one-vertex exception is handled in [the merged proof](main-theorem.md#41-a-fibred-factor-has-only-one-spanning-vertex). D′ supplies flagness on its class, so equality of these graphs identifies its whole geometric complex with $`X`$; no comparison theorem for disconnected vertices is being used.

### 2.3. Ambient and boundary exceptions

A Seifert-fibred link exterior is irreducible: H Proposition 1.13, pp. 23–24, has only closed exceptional manifolds. Its boundary is nonempty. A splitting sphere would bound no ball in the exterior, so such a link is automatically non-split.

For any non-split link other than the unknot, the boundary tori are incompressible. To see the exception directly, let a compressing disk for a boundary torus have essential primitive boundary $`a\mu_i+b\ell_i`$. Its image in $`H_1(E)`$ is zero, forcing $`a=0`$ and $`b=\pm1`$, and forcing the cross-linking coefficients to vanish. Attaching the collar annulus to $`L_i`$ produces a disk bounded by $`L_i`$, disjoint from all other components. A small ball neighborhood of that disk separates this unknotted component from the others. This contradicts non-splitness when $`n>1`$, and makes the knot an unknot when $`n=1`$. The same disk argument excludes disk components of spanning surfaces in the nontrivial non-split case.

Every nondisk incompressible spanning component is therefore essential in Hatcher's sense. H Lemma 1.11 (p. 20) leaves either boundary-incompressibility or a boundary-parallel annulus. That annulus has two boundary curves on the same ambient torus, forbidden by the one-curve-per-torus convention. This is why H Proposition 1.12 is applicable; incompressibility alone was not its hypothesis.

If $`E`$ is a solid torus, there is one link component and it is the unknot: a meridian disk of $`E`$ extends to a disk bounded by that component. Lemma 1.11 excludes the annulus exception for a one-boundary spanning surface, and H Lemma 1.10 (pp. 19–20) says the remaining essential surface is its meridian disk. Hence $`X(U)`$ is a point. H uses a convention excluding disks from the word “incompressible” (p. 13); our convention includes spanning disks, and his essential-disk clause covers this case.

Every Seifert fibering of a solid torus is a model fibering (H Corollary 1.15, p. 25). A regular fibre represents $`\pm q`$ times its core for some multiplicity $`q\ge1`$ (H, pp. 17–18). Since $`\phi`$ is a primitive generator for the unknot exterior, $`k=\phi(f)=\pm q\ne0`$. The meridian disk is horizontal. There is consequently no omitted solid-torus $`k=0`$ case. PS's boundary-irreducible-manifold hypothesis is not applied to the unknot.
