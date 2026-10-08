# Two parallels of K_{7/19}: joint longitudinal normal forms

[Overview](../README.md) · [Objects](objects.md) · [Sources](../sources/bibliography.md) · [Scope](scope.md)

## 1. Object and conventions

Fix the knot $`C=K_{7/19}`$ in Hatcher-Thurston's convention, and its two oppositely oriented, zero-framed parallels $`L`$. Write

```math
M=E(L)=Q\cup_T P,\qquad Q=E(C),\qquad
P=S^1_\lambda\times B,
```

where $`B`$ is a pair of pants with labelled boundary circles $`b_0,b_+,b_-`$. The outer circle $`b_0`$ corresponds to $`T`$; $`b_+,b_-`$ correspond to the actual link tori. The fibre on all these tori is the preferred longitude. On $`T`$ use coordinates $`(\lambda,\mu)`$, and read longitude circles in the positive meridian direction.

A vertex is an ambient-isotopy class of an oriented incompressible spanning surface, possibly disconnected, with no closed component. It uses the actual tori once each, with boundary signs $`+,-`$. Boundary curves may move on their labelled tori. Isotopies begin at the identity. There is no genus or norm restriction. The edges of $`X=IS_{\mathrm{cyc}}(L)`$ use the minimum whole-complement cyclic-cover width, not geometric disjointness alone.

All companion systems below are compact, properly embedded, have no closed component, and are componentwise incompressible and boundary-incompressible. Empty systems are allowed. A sign on a companion boundary means its orientation as a boundary of the companion piece. At a gluing circle the two cut-side boundary orientations must be opposite.

We distinguish a **covering normal form** from unique numerical coordinates. Every vertex has a representative in the covering family of Section 7. The test in Section 8 gives an if-and-only-if rule for equality of the resulting vertices, including all residual boundary motion. In particular, the parameters of that covering family are not declared distinct vertices merely because the parameters differ.

## 2. Inputs and versions

The [normalisation volume](parallel-satellites-normalisation.md), §§3–7, proves essential cut pieces, simultaneous pattern straightening, reverse assembly and efficient torus comparison. The [cone proof](parallel-satellites.md), §§3–5, gives the two-parallel boundary model and whole-block separation; the [distance-two example](parallel-satellites-obstruction.md), §8, supplies the genus-six case. HT means Hatcher–Thurston 1985, pp. 225–246; Banks means arXiv:1109.0965v1, 5 September 2011. Their exact editions and page references are in the bibliography. HT's coefficient condition is $`|b_i|\ge2`$. The union classification uses Theorem 1(b),(c),(e), p. 228; the geometric equality test uses Banks Proposition 4.10, p. 7, and its explicit all-incompressible extension, §10, p. 22. PS §§2–3 are retained; its projection and general contraction are not inputs.

## 3. The two zero-slope carriers and all their parameter values

HT use minus continued fractions:

```math
[b_1,\ldots,b_s]
=\frac{1}{b_1-\dfrac{1}{b_2-\cdots-\dfrac{1}{b_s}}},
\qquad p/q=r+[b_1,\ldots,b_s],\qquad |b_i|\ge2.
```

The exhaustive list for $`7/19`$ is:

| $`r`$ | Coefficients | Signed coefficient count | Boundary slope |
|---:|---|---:|---:|
| 0 | $`[2,-2,-2,-3]`$ | -2 | 0 |
| 0 | $`[3,3,-2]`$ | 1 | 6 |
| 0 | $`[3,4,2]`$ | 3 | 10 |
| 1 | $`[-2,-3,-2,-3]`$ | -4 | -4 |
| 1 | $`[-2,-2,2,-2]`$ | -2 | 0 |
| 1 | $`[-2,-2,3,2]`$ | 0 | 4 |

For exhaustion, every nonempty admissible tail has absolute value strictly between zero and one. At a tail $`x`$ the next coefficient must satisfy $`|b|\ge2`$ and $`|b-1/x|<1`$; the next tail is $`b-1/x`$. Its reduced denominator is strictly smaller than that of $`x`$, unless it is zero and the expansion terminates. The initial integer part is therefore zero or one, and this recursion exhausts all six rows with no cutoff. The same exhaustive arithmetic is given in [the two-bridge criterion](parallel-satellites-two-bridge.md), §7.

HT Proposition 2, printed p.230, gives slope

```math
2\left(\sum_i\mathrm{sgn}(b_i)
-\sum_i\mathrm{sgn}(b_i^0)\right),
```

where $`b^0`$ is the unique all-even expansion. Here its signed count is $`-2`$. Thus only the following carriers can occur:

```math
\mathcal E=\Sigma[-2,-2,2,-2],\qquad
\mathcal O=\Sigma[2,-2,-2,-3].
```

We write their carried surfaces as $`E_N(x,y,z)`$ and $`O_N(x,y,z)`$, with $`0\le x,y,z\le N`$ integers.

**Lemma 3.1 (all parameter values).** For each fixed $`N\ge1`$, every $`E_N(x,y,z)`$ is isotopic to $`E_N(0,0,0)`$, and every $`O_N(x,y,z)`$ is isotopic to $`O_N(0,0,0)`$.

**Proof.** Both carriers have first three coefficients of absolute value two. HT Theorem 1(e), printed p.228, supplies the reversible moves

```math
(x,y,z)\longleftrightarrow(x\pm1,y,z),\qquad
(x,y,z)\longleftrightarrow(x\pm1,y\pm1,z),\qquad
(x,y,z)\longleftrightarrow(x,y\pm1,z\pm1),
```

with the two signs in each double move the same, and with all intermediate coordinates in $`[0,N]`$. Here is a bounded normalization, so lattice generation alone is not being used as a proof. First set $`x=0`$ using the first move. While $`z>0`$, if $`y=0`$, increase $`(x,y)`$ from $`(0,0)`$ to $`(1,1)`$, then reset $`x`$ to zero. Decrease $`(y,z)`$ by $`(1,1)`$. This eventually makes $`z=0`$. While $`y>0`$, raise $`x`$ from zero to one and decrease $`(x,y)`$ by $`(1,1)`$. The endpoint is $`(0,0,0)`$. Every auxiliary coordinate is at most $`N`$ since $`N\ge1`$. No move at the last, odd coefficient of $`\mathcal O`$ was used. ∎

## 4. Connected types and the simultaneous companion theorem

Let

```math
R=E_1(0,0,0),\qquad B_*=O_1(0,0,0),\qquad S=O_2(0,0,0).
```

The notation $`B_*`$ is for a nonorientable surface and is distinct from the pair-of-pants base $`B`$.

**Lemma 4.1 (the zero-parameter systems).**

1. $`E_N(0,0,0)`$ is a simultaneous stack of $`N`$ parallel copies of $`R`$.
2. $`O_{2k}(0,0,0)`$ is a simultaneous stack of $`k`$ parallel copies of $`S`$.
3. $`O_{2k+1}(0,0,0)`$ is $`B_*`$ together with $`k`$ nested copies of its horizontal neighbourhood frontier $`S`$.

**Proof.** At zero parameters all sheets use the same plumbing square at each plumbing. They consequently form the ordered-sheet neighbourhood model of the one-sheeted plumbed surface (HT construction, printed p.227 and Fig.3). For $`R`$ the normal line bundle is trivial; the ordered sheets are its distinct product levels.

For $`B_*`$ it is nontrivial. In an orientable ambient manifold its nontrivial holonomy reverses the normal coordinate. A symmetric finite set of normal levels therefore splits into pairs $`\{t,-t\}`$, and, for an odd number of levels, the middle level zero. Each paired level is the connected orientation double of $`B_*`$, namely the horizontal frontier of a regular neighbourhood. HT identify that frontier as $`O_2(0,0,0)`$; more generally doubling all weights gives the neighbourhood frontier, printed p.240. Varying the positive radius gives parallel copies of the same two-sided frontier. The zero level is $`B_*`$. This is a simultaneous embedded model, not a collection of separately chosen component isotopies. ∎

HT Proposition 1 and its proof give a useful independent check: for all-even coefficients there are exactly $`N`$ components; with just one odd coefficient the cycle of sheets is folded once, and no component has more than two sheets (printed p.245, Figs.30-31). On $`\mathcal O`$ the only odd coefficient is $`-3`$. Proposition 1(3), printed p.230, therefore excludes every connected $`N>2`$ surface on this carrier, for **all** plumbing parameters.

Each boundary has longitudinal degree one, and a carried $`N`$-sheet surface has $`N`$ boundary circles (HT pp.242-244 and 914-919). Its Euler characteristic is $`N(1-s)`$; here $`s=4`$.

The complete connected-type table is:

| Underlying type | Orientability | Euler characteristic | Genus | Boundary count | Oriented boundary and integral relative class |
|---|---|---:|---:|---:|---|
| $`R`$ | orientable | -3 | 2 | 1 | $`+\lambda`$, class $`+\eta`$; or $`-\lambda`$, class $`-\eta`$ |
| $`S`$ | orientable | -6 | 3 | 2 | one $`+\lambda`$ and one $`-\lambda`$; class zero, for either orientation |
| $`B_*`$ | nonorientable | -3 | nonorientable genus 4 | 1 | no integral oriented surface class; excluded from the oriented systems considered here |

Here $`H_2(Q,T;\mathbb Z)=\mathbb Z\eta`$, with $`\partial\eta=[\lambda]`$. The boundary homomorphism is injective, since $`H_2(Q)=0`$ and $`H_1(Q)=\mathbb Z[\mu]`$. The two signs on $`S`$ are opposite because it is the relative boundary of a regular neighbourhood; in particular $`[S]=0`$. HT Theorem 1(c) supplies incompressibility and boundary-incompressibility of all the listed carried surfaces. The orientation statements for one sheet are at p.230. The orientability of $`S`$ is the orientation-double construction, not an assumption about arbitrary two-sheet surfaces.

**Theorem 4.2 (joint classification).** Every nonempty oriented longitudinal essential system in $`Q`$, without closed components, has one of exactly two underlying simultaneous normal forms:

- $`N`$ parallel copies of $`R`$, $`N\ge1`$, with independent choices of orientation;
- $`k`$ parallel copies of $`S`$, $`k\ge1`$, with independent choices of orientation.

There is no connected orientable component with three or more boundary circles. A copy of $`R`$ and a copy of $`S`$ cannot occur disjointly in the same system.

**Proof.** Apply HT Theorem 1(b) to the **whole union**, after forgetting its orientations. HT impose no connectedness assumption: their construction explicitly carries disconnected surfaces, p.227, and the proof of Theorem 1(b) uses all arcs of the whole level set at once, pp. 233–239. Componentwise essentiality implies the essentiality needed for that union. There are no closed components to add to the bounded classification. Proposition 2 and Section 3 force the single carrier of the whole system to be $`\mathcal E`$ or $`\mathcal O`$.

Now apply Lemmas 3.1 and 4.1 to that union. The $`\mathcal E`$ case contains only copies of $`R`$. The $`\mathcal O`$ case contains only copies of $`S`$ if $`N`$ is even; if $`N`$ is odd it also contains the nonorientable $`B_*`$, which is forbidden. Both the exclusion of mixed systems and simultaneous parallelism follow. Conversely the stated parallel stacks are carried essential systems and can be oriented independently. ∎

In particular, for $`N\ge3`$ on $`\mathcal O`$, **every** parameter choice gives $`\lfloor N/2\rfloor`$ orientable two-boundary genus-three components, and gives one additional nonorientable one-boundary component exactly when $`N`$ is odd. Even $`N`$ is the precise condition for the entire system to be orientable. No parameter choice produces a larger connected orientable component.

The same argument, **before** restricting to oriented systems, also classifies all the unoriented bounded zero-slope systems: an $`R`$ stack, an $`S`$ stack, or one $`B_*`$ together with an $`S`$ stack. In particular two nonorientable $`B_*`$ components cannot be disjoint. For a two-boundary union the only carried possibilities are $`E_2`$, two orientable $`R`$ components, and $`O_2`$, one orientable $`S`$ component. This additional exclusion will control oriented-stack ambiguity in Section 5.

## 5. Boundary order of the joint normal forms

For the $`R`$ stack label its boundary circles in cyclic meridian order by $`0,\ldots,N-1`$. An oriented stack has boundary word

```math
(\epsilon_0,\ldots,\epsilon_{N-1}),\qquad
\epsilon_i\in\{+1,-1\},\qquad [\Sigma]=\sum_i\epsilon_i\eta.
```

The word is not required to alternate. All coefficients of $`\mathcal E`$ are $`\pm2`$; HT's bracketed statement on p.230 identifies $`R`$ as a fibre. Suspension motion in its mapping torus realizes cyclic rotations of the stack. Conversely boundary motion in an identity isotopy of a torus preserves meridian cyclic order. Thus for the **oriented unmarked companion R stack** the sign word up to cyclic rotation is complete.

For $`k`$ parallel $`S`$ pieces choose a fixed reference stack $`S_1,\ldots,S_k`$. Its boundary order, with transported reference orientations, is

```math
S_1^+,S_2^+,\ldots,S_k^+,S_k^-,\ldots,S_2^-,S_1^-.
```

Write $`n=2k`$ and index these circles by $`\mathbb Z/n`$. The companion pairing is

```math
q(i)=-1-i\pmod n.
```

If $`S_j`$ is assigned sign $`\epsilon_j`$ relative to its reference orientation, the cyclic boundary-sign word is

```math
(\epsilon_1,\ldots,\epsilon_k,-\epsilon_k,\ldots,-\epsilon_1).
```

This order follows from the normal-coordinate reversal at the two oppositely oriented boundaries of a two-sided surface. It is also visible in the nested-neighbourhood model of Lemma 4.1. It retains **which two circles belong to the same component**, not just the unlabelled sign word. Independent signs do not change the underlying pairing. The whole $`S`$ stack has relative class zero for every choice of signs.

**Lemma 5.1 (oriented S stacks).** Relative to this fixed reference stack, its $`2^k`$ choices $`(\epsilon_1,\ldots,\epsilon_k)`$ are pairwise distinct oriented companion-system classes. An identity isotopy of $`Q`$ returning the underlying stack to itself induces the identity permutation on its boundary circles. This statement permits full meridional boundary circuits and does not compute the subgroup of such circuits.

**Proof.** The induced boundary permutation is a cyclic rotation $`i\mapsto i+r`$: the torus isotopy preserves the meridian cyclic order. It must preserve the companion pairing $`q`$, so $`2r=0\pmod{2k}`$. Thus $`r=0`$ or $`r=k`$.

The reference stack consists of nested frontiers of $`B_*`$. Cutting $`Q`$ along it gives a path of chambers. One end chamber contains $`B_*`$ and has its torus trace in the interval between the two innermost frontier boundaries, indices $`k-1,k`$; the other end chamber has trace in the interval between indices $`2k-1,0`$. A rotation by $`k`$ exchanges these two intervals and therefore exchanges these end chambers. The endpoint homeomorphism would carry the essential one-sided core $`B_*`$ to an essential nonorientable longitudinal surface in the other chamber, disjoint from the original $`B_*`$. Both have one boundary circle. This contradicts the two-nonorientable-component exclusion just proved from HT. Hence $`r=k`$ is impossible.

For $`r=0`$ each component and each of its boundary circles returns to itself. An identity isotopy on the torus preserves the orientation of its longitude, so it preserves the sign at each indexed boundary, and hence each $`\epsilon_j`$. Conversely identical choices are the same reference oriented system. This proves completeness of the stated oriented classification. ∎

In particular, even the one-piece $`S`$ system has two distinct oriented classes; a side-reversing self-isotopy has been excluded by an actual HT union argument. Meridional circuits returning each boundary to itself remain relevant to global twisting and are handled by Section 8's test.

## 6. Global incidence and the exact no-closed-component condition

Use [normalisation](parallel-satellites-normalisation.md), §§3–5, and [the two-parallel cut model](parallel-satellites.md), §3. For a non-annular vertex the two actual boundaries must lie on two inner-outer annuli. All intersection circles with $`T`$ are longitudes, and the pattern side contains $`u`$ essential outer-outer annuli. Its endpoint count is

```math
|F\cap T|=2+2u.
```

There is no inner-inner annulus in this branch: it would already use both actual boundaries and leave only forbidden closed components. In the zero-intersection branch the surface is the unique vertical inner-inner annulus $`A`$.

Collapse each companion component to a vertex, each outer-outer annulus to an edge, and retain the two reaching annuli as terminal edges to the labelled actual boundaries. The degrees of the companion vertices are their boundary counts.

For an $`R`$ system each vertex has degree one. An outer-outer annulus joins two such vertices into a complete closed component. Therefore $`u=0`$ and the only assembly is two oppositely oriented copies of $`R`$ with reaching annuli. It is disconnected, with one actual boundary and genus two on each component.

For an $`S`$ system every vertex has degree two. Consequently the incidence graph is one path between the actual boundaries, possibly together with cycles. There is no branching and no higher-valence tree. A cycle is precisely a closed whole component and is forbidden. Thus a legal assembly must be a **single finite chain** of $`k=u+1`$ copies of $`S`$.

The following computes when the cyclic boundary matching gives such a chain.

**Lemma 6.1 (pattern pairing).** If a vertical pattern system has two reaching annuli and $`k-1`$ essential outer-outer annuli, its reaching endpoints are antipodal in the cyclic list of its $`2k`$ outer endpoints. If the positive reaching endpoint is $`a`$, the negative one is $`a+k`$, and the outer-outer pairing is

```math
p(i)=2a-i\pmod{2k},\qquad i\ne a,a+k.
```

**Proof.** Every essential $`b_0`$-to-$`b_0`$ arc separates the two inner holes; a wave cutting off no inner hole is boundary-parallel. Disjoint essential waves are parallel as unmarked arcs. The two reaching arcs cut the pair of pants to a disk. Every wave crosses between the two portions of the outer boundary of that disk, since the wave separates the holes. The $`k-1`$ endpoints on one portion match the endpoints on the other in reverse order, by disjointness. Thus the cyclic list is a reaching endpoint, $`k-1`$ wave endpoints, the other reaching endpoint, and the reversed list of their partners. This is the stated reflection. ∎

Consider the graph on the $`2k`$ boundary circles with all $`q`$ edges and all $`p`$ edges except at its two fixed points, the reaching endpoints. This is the same incidence graph before collapsing companion edges.

**Theorem 6.2 (closed-component test and orientations).** Put

```math
d=\gcd(2a+1,2k).
```

The graph has one path containing both reaching endpoints and exactly $`(d-1)/2`$ cycles. The path contains $`k/d`$ companion pieces, and each cycle contains $`2k/d`$ companion pieces. Therefore the standard matching is legal exactly when

```math
\gcd(2a+1,2k)=1.
```

For a legal matching its compatible orientation is unique: set $`e(a)=+1`$ and change the sign on crossing every $`q`$ or $`p`$ edge. Then $`e(a+k)=-1`$. Orient $`S_j`$ by $`\epsilon_j=e(j-1)`$ relative to the reference stack.

**Proof.** Completing $`p`$ at its two fixed points gives two reflections satisfying

```math
(p\circ q)(i)=i+2a+1\pmod{2k}.
```

Their translation orbits are the $`d`$ residue classes modulo $`d`$. Since $`d`$ is odd, reflection $`q`$ pairs residues $`r`$ and $`-1-r`$, with exactly one fixed residue, $`r=(d-1)/2`$. The latter contains both fixed points of $`p`$: $`a\equiv(d-1)/2\pmod d`$, and $`d`$ divides $`k`$. Deleting those two fixed-point edges leaves a path in that residue class, with $`2k/d`$ boundary vertices. Each other paired pair of residue classes gives one cycle with $`4k/d`$ boundary vertices. Dividing boundary-vertex counts by two gives the asserted companion counts.

In the legal case the graph is a path with $`2k`$ vertices. It has $`2k-1`$ edges, so assigning opposite signs across each edge takes $`+1`$ at its first anchor to $`-1`$ at its second. A $`q`$ edge then has opposite boundary signs as required on $`S`$; a $`p`$ edge has opposite signs as required for an oriented pattern annulus. At the reaching ends the companion signs equal the prescribed actual signs; the pattern's outer sign is their negative. This specifies and verifies all the orientations. ∎

For $`d>1`$ one can sometimes orient the cycles, but they still violate the no-closed-component condition. Deleting them would change the surface and the data; it is not part of the normal form.

**Corollary 6.3 (topology, existence and minima).** Every legal $`S`$ assembly is connected with the two actual boundaries, and

```math
\chi(F)=-6k,\qquad g(F)=3k,\qquad
u=k-1,\qquad |F\cap T|=2k.
```

Every $`k\ge1`$ occurs, for example $`a=0`$. Any such assembly is incompressible. Its displayed $`T`$-circle count is already minimal. The $`R`$ assembly has minimum two circles; the annulus has minimum zero.

**Proof.** Annuli and circle gluing have zero Euler contribution. A path has two remaining actual boundaries and no closed component. All local pieces are essential. [Normalisation Lemma 5.2](parallel-satellites-normalisation.md), proves reverse assembly: minimize a hypothetical compression disk's intersections with $`T`$, remove circles, and use an outermost arc and local boundary-incompressibility to eliminate the remaining arcs. A disk eventually contained in one piece contradicts local incompressibility. That proof applies to multi-boundary pieces and to this pair of pants.

For minimality take an actual minimum-intersection representative of the assembled vertex. The cut classification already proved applies to it. A connected surface of genus $`3k>0`$ cannot belong to the annulus or disconnected $`R`$ case. In the $`S`$ case its genus forces precisely $`k`$ pieces, hence $`2k`$ circles. This proves minimality without needing to assume that a chosen original isotopy preserves $`T`$. The disconnected genus-two assembly is not an annulus and the smallest positive count is two. ∎

Thus there are vertices of unbounded genus and unbounded minimal $`T`$ intersection; this is proved by actual assemblies, not inferred from a formal parameter range.

## 7. A covering family with the remaining pattern twisting recorded

Fix embedded reference stacks of $`R`$ and $`S`$ in $`Q`$ with straight fibre boundary. For each $`k`$ index the latter boundary by $`0,\ldots,2k-1`$ as in Section 5, and fix corresponding points on $`b_0`$. For each $`a`$ choose one reference pattern arc system $`\alpha_{k,a}`$ realizing Lemma 6.1's endpoint matching. Reference orientations are then fixed by Theorem 6.2. Let $`D_0`$ be a Dehn twist about a curve parallel to $`b_0`$, supported away from $`b_0`$ itself and the inner boundaries.

The reference choice is concrete but arbitrary; it is kept fixed for all comparisons. The following are standard forms:

1. $`A`$, the inner-inner annulus.
2. $`G`$, the disconnected $`+R,-R`$ assembly with two reaching annuli.
3. For $`k\ge1`$, $`0\le a<2k`$, $`t\in\mathbb Z`$ and $`\gcd(2a+1,2k)=1`$,

$`\displaystyle F(k,a,t)=\left(\bigcup_{j=1}^k\epsilon_jS_j\right) \cup_T \left(S^1_\lambda\times D_0^t\alpha_{k,a}\right), \qquad \epsilon_j=e(j-1).`$

The reference boundary positions, the labelled reaching ends, and the pairing are part of this definition. A change of reference diagram changes coordinate conventions and must be accompanied by its actual isotopy; it is not an extra identification of vertices.

**Lemma 7.1 (pattern winding).** With these outer endpoints and their pairing fixed, and with inner endpoints permitted to move on their labelled boundary circles, every essential pattern arc system is isotopic to $`D_0^t\alpha_{k,a}`$ for a unique integer $`t`$.

**Proof.** Cutting along the two reaching arcs gives a disk; the waves split that disk into disks. Corresponding boundary intervals and arc sides let one identify these disk decompositions by an orientation-preserving homeomorphism, gluing to a homeomorphism of the pair of pants that fixes the outer boundary and preserves the two inner labels. It remains to record its relative mapping class.

For a labelled pair of pants with all three boundary circles pointwise fixed, the twists in the three boundary collars generate the mapping classes. One elementary verification is to choose the three seams of a hexagon decomposition, remove their bigons, and compare their ends: the discrepancies are the integral windings in the three collars; after removing them the cut disks have boundary-fixing homeomorphisms, which are isotopic to the identity. Permitting rotations of the two inner circles removes the two inner-collar windings. What remains is precisely the outer-collar integer $`t`$. To check uniqueness without assuming a local winding is invariant under all arc homotopies, use a reaching arc to $`b_+`$. A change by $`m`$ outer twists prefixes its relative path by $`b_0^m`$, whereas moving its inner endpoint can only suffix a power of $`b_+`$. In $`H_1(B;\mathbb Z)`$ the class of $`b_0`$ has coefficient $`\pm1`$ on $`b_-`$, and $`b_+`$ has coefficient zero there. A homotopy between those reaching arcs with outer endpoint fixed therefore forces $`m=0`$. ∎

This is an arc-system classification in the pattern piece, with the outer points fixed. It does not say the same integer remains an invariant after companion boundary motion is allowed.

**Theorem 7.2 (coverage).** Every vertex is represented by $`A`$, $`G`$, or some $`F(k,a,t)`$ above. These represent exactly the following whole-surface topological types:

| Family | Components and actual boundaries | Genus | Minimum $`|F\cap T|`$ |
|---|---|---|---:|
| $`A`$ | one component, both actual boundaries | 0 | 0 |
| $`G`$ | two components, one actual boundary each | 2 on each | 2 |
| $`F(k,a,t)`$ | one component, both actual boundaries | $`3k`$ | $`2k`$ |

**Proof.** Start with a minimum representative. Simultaneously normalize its **whole companion system** by Theorem 4.2. Extend the boundary motion into the pattern collar, carrying the whole assembled surface. Simultaneously verticalize the resulting pattern system relative to its straight fibre boundary ([normalisation, Lemma 5.1](parallel-satellites-normalisation.md)). In the $`S`$ case, Lemma 6.1 determines $`a`$ and the pairing, Theorem 6.2 gives the no-closed-component and orientation conditions, and Lemma 7.1 records the remaining pattern integer. Thus no independent component normalizations or incompatible boundary lifts are used.

In the $`R`$ case both pieces are fibres of the same genus-two fibration, with opposite signs. Suspension motion can rotate the fibre pair and realizes the two choices of positive reaching endpoint. A full circuit in the mapping torus returns the oriented fibre stack to itself while its boundary makes one full meridian circuit. Extending that motion into the pattern collar changes the outer-collar winding by one. Consequently every integer winding is absorbed in this case and all $`R`$ assemblies give $`G`$. The inner-inner seam has one unmarked class on a pair of pants, giving $`A`$.

A longitudinal boundary spin creates no additional parameter: fibre-coordinate rotation on the pattern piece leaves every vertical annulus invariant as a set, and extends that spin across the common torus. Meridional winding is retained as $`t`$ in the $`S`$ family. Section 8 determines any residual identifications of that family. ∎

No assertion that distinct $`(a,t)`$ always yield distinct vertices is part of Theorem 7.2. In particular a permutation or a reversal of a reference $`S`$ stack has not been assumed to extend through an identity isotopy of $`Q`$.

## 8. Exact global isotopy criterion on the covering family

This section gives the required equality criterion directly in $`M`$. It is a geometric criterion using finite cut manifolds, not a claim that genus or a boundary word alone is complete. It also avoids assuming that an unspecified boundary-motion stabilizer is trivial.

**Torus comparison in this model.** [The efficient-representative comparison](parallel-satellites-normalisation.md#7-relative-torus-comparison-not-just-separate-normal-forms) applies here as well. Its proof uses essential longitude traces, incompressible and boundary-incompressible cut pieces, an injected $`\mathbb Z^2`$ torus group, boundary-bearing spanning components and the absence of the spanning-bundle exception. All of these were verified above for this $`M`$. Neither the product-annulus lemmas, [normalisation, §6](parallel-satellites-normalisation.md), nor the product-region argument uses four actual boundary labels or the companion $`5_2`$ classification. Thus any ambient isotopy between two present standard forms can be replaced by one preserving $`T`$ setwise: returning annuli in a product region would give forbidden boundary-parallel cut pieces; spanning annuli straighten to products; each product-region push can then be tangent to $`T`$.

It follows that equal $`S`$ standard forms have the same $`a`$, as well as the same $`k`$. Restrict the resulting $`T`$-preserving isotopy to $`Q`$. Its endpoint returns the fixed underlying $`S`$ stack to itself, so Lemma 5.1 forces the identity permutation of boundary circles. The reaching annulus from the labelled positive torus therefore ends at the same indexed circle. This also excludes a nontrivial companion-piece exchange in a global isotopy of these efficient forms. The remaining full meridional circuits are not erased by this argument.

### 8.1. Put a given pair in simplified intersection

Given two standard forms, realize their actual embedded assemblies in the fixed $`M`$. Retain any coincident whole components and make the other components transverse; make boundary curves disjoint except on already identified components. Apply the following operations on the **whole systems**:

- If a product region in Banks Definition 4.1 is present, push a horizontal face through that region to remove the intersection on its collapsed boundary.
- If the horizontal faces are entire parallel components, use the region to identify them and retain them as coincident components.
- Simplify boundary bigons in the same manner and repeat.

The interior of a permitted region must be disjoint from both full systems, including retained components. The test for such a region is the specified marked-product structure $`(W\times I)/\!\sim`$, with horizontal faces in the two surfaces and remaining vertical boundary in $`\partial M`$; it is a local manifold/product test, not a request to decide the original isotopy class. For transverse boundaries these regions are embedded. Degenerate boundary coincidence is handled by the collapsed-boundary convention, Banks Remark 4.4.

There are finitely many candidate chamber boundaries at each stage. In fact, the interior of a connected empty product region is a whole chamber of the complement: its image is open there, and all its frontier is in the two surfaces or the ambient boundary, so it is also closed relative to that chamber. One examines the chamber's normalized boundary with its marked $`F`$ and $`H`$ faces and the prescribed collapsed corner locus. The required condition is that it have that marked product structure. This states a finite **geometric criterion**; no implementation or arithmetic replacement for marked three-manifold product recognition is asserted.

This process terminates: a non-component push decreases the finite transverse arc/circle intersection count without introducing new intersections, and a component identification decreases the number of unpaired components. The empty region's interior is what ensures that other components are not crossed. This is the product-region simplification in PS Section 3, printed p.1494, whose coincident-component convention is essential here. Banks Proposition 4.2, p.5, has incompressible and boundary-incompressible hypotheses rather than a norm hypothesis.

These hypotheses hold in $`M`$: it is irreducible, boundary-irreducible and Haken by the injections of the two piece groups and the torus groups and the usual sphere-cutting argument ([normalisation, §3](parallel-satellites-normalisation.md)). Every spanning component is boundary-incompressible: the only boundary-compressible incompressible alternative is a boundary-parallel annulus, impossible because it would use two circles on one actual torus, while each actual torus is used once. The whole-manifold surface-bundle exception does not occur, since $`\pi_1(T)=\mathbb Z^2`$ injects into $`\ker\phi`$ while a compact spanning fibre with boundary would have a free kernel group. Here $`\phi`$ is total oriented linking and vanishes on all of $`\pi_1(Q)`$.

Call the resulting almost-transverse, simplified pair $`F',H'`$. No cyclic-distance claim is made before this reduction.

### 8.2. A finite height graph of the entire H' complement

The whole open complement $`M\setminus H'`$ is connected. One proof works for disconnected spanning systems as well: a small meridian at an actual boundary of each component crosses only that component once. Removing the crossing segment joins its two local sides in the complement. In the complement's connected dual graph every component edge is thus a loop; the graph has only one vertex. Every closed loop in this complement has $`\phi=0`$.

Construct a finite graph $`\mathcal W(F',H')`$ as follows:

1. Its vertices are **all** chambers of $`M\setminus(F'\cup H')`$.
2. Its edges are the connected wall pieces of $`F'\setminus H'`$, joining their two local chambers, with direction from the negative to the positive side of $`F'`$.
3. Set the height of one chamber to zero. Across a directed edge increase height by one, and across its reverse decrease it by one.

The graph is connected because it cuts the one whole $`H'`$ complement along finitely many walls. Heights are consistent: any closed walk gives a loop in $`M\setminus H'`$, and its signed crossings of $`F'`$ equal $`\phi`$ of that loop, namely zero. Thus a spanning-tree traversal assigns heights to every chamber and each remaining edge verifies the same values. A different root adds a constant.

Define

```math
w(F',H')=\max_{v\in\mathcal W}h(v)-\min_{v\in\mathcal W}h(v).
```

This uses every companion chamber and its pattern attachments. It is not the graph of the pattern piece alone and does not assign independently chosen levels to disconnected companion components.

**Lemma 8.1 (width interpretation).** The displayed integer is the representative cyclic-cover width of a single lift of the **whole** $`M\setminus H'`$ against the complete open $`F'`$-complement blocks.

**Proof.** Since $`\phi`$ vanishes on the connected $`H'`$ complement, the cyclic cover maps each of its lifts homeomorphically to that complement. Choose one such lift. Away from the $`F'`$ walls its chambers lie in $`F'`$-complement blocks. Crossing an oriented wall changes the block index by one. These indices are exactly $`h`$ up to a common additive constant. Every chamber has interior, and every intersection with an open $`F'`$ block contains points off the walls and hence a chamber. Taking the maximum and minimum therefore gives precisely the whole-block width. ∎

**Theorem 8.2 (isotopy test).** For two legal standard forms $`F,H`$,

```math
[F]=[H]\quad\Longleftrightarrow\quad w(F',H')=0,
```

where $`F',H'`$ are obtained by the whole-system reduction above. Equivalently, in simplified intersection there must be no noncoincident $`F'`$ wall, and all actual boundary-bearing components must coincide with the same orientations.

The preliminary filters are exact: $`A`$ only compares with $`A`$, $`G`$ only with $`G`$, and two $`S`$ standard forms can be equal only when both $`k`$ and $`a`$ agree. For equal $`k,a`$, the height test applies to the actual specified twisting diagrams; equal integers certainly give identical standard forms, and unequal integers must be tested rather than identified by assumption.

**Proof.** Banks Proposition 4.10, p.7, says that simplified representatives realize the minimum cyclic width. Its applicability to incompressible spanning surfaces, including disconnected ones, is explicitly stated in Section 10, p.22. By an ambient isotopy carrying any representative of $`[F]`$ to fixed $`F'`$, while carrying the other representative as well, fixing $`F'`$ does not change the two-class minimum: the isotopy preserves $`\phi`$ and its cover. Hence

```math
\delta([F],[H])=w(F',H').
```

If the classes agree, coincident representatives give width zero, so the simplified width is zero. Conversely zero width permits no directed edge of $`\mathcal W`$, as the heights at that edge's ends would differ by one. Thus $`\mathrm{int}(F')\subset H'`$, and properness gives $`F'\subset H'`$. A proper same-dimensional embedding of a surface component into another, with its boundary on the ambient boundary, makes it a whole component: its image is both open and closed in that component. Every $`F'`$ component therefore is a whole $`H'`$ component. Together they already use both actual boundary tori. Any remaining $`H'`$ component would be closed, forbidden here. Hence the two systems coincide. Their actual boundary orientations fix their component orientations, proving equality of the oriented vertices.

The family and $`k`$ filters follow from the table in Theorem 7.2; the $`a`$ filter is the torus-comparison argument above. ∎

This test is an if-and-only-if criterion on geometric standard forms; its checks are product-region structure, finite chamber incidence, and signed integer differences. It contains no unknown quantifier over global ambient isotopies. Different valid sequences of product reduction give the same width by the checked Banks result.

It handles a torus twist or a pattern slide by building the two specified assemblies and performing that same test. A twist is not erased merely because both sides have the same unmarked HT class. Conversely, a genuine identity isotopy implementing a slide must give test value zero. The companion boundary-permutation ambiguity has been settled by Lemma 5.1 and torus comparison. For the pattern integer $`t`$ and the oriented $`S`$ stack, this volume retains the geometric criterion. The [tree volume](parallel-satellites-k719-tree.md), §§5–6, fixes canonical references, computes the return subgroup as zero, and establishes complete integer coordinates.

## 9. Optional distance and descent: a certified linear subfamily

Fix one pair-of-pants coordinate picture and one nested-neighbourhood model of $`B_*`$. Choose **all** the reference $`\alpha_{k,0}`$ from that picture by adding parallel waves between the two inner holes and reaching arcs in the two end annuli, without an outer-collar turn. Let $`F_k=F(k,0,0)`$ and set $`F_0=A`$. Thus all $`S`$ pieces of $`F_k`$ have their transported reference orientation, and its cyclic boundary word is $`+^k-^k`$. The pattern wave $`\gamma_j`$ joins $`S_j^-`$ to $`S_{j+1}^+`$, for $`1\le j<k`$.

**Proposition 9.1 (explicit lower neighbour).** For every $`k\ge1`$,

```math
\delta([F_k],[F_{k-1}])=1.
```

For $`k\ge2`$ this lowers $`u=k-1`$ by one and lowers the minimum torus-circle count by two.

**Proof.** For $`k=1`$ choose the inner-inner seam of $`A`$ disjoint from the two reaching seams of $`F_1`$.

For $`k\ge2`$, take a simultaneous reference stack of $`2k-1`$ copies of $`S`$ in $`Q`$. Assign them, in radial order, alternately to $`F_k`$ and $`F_{k-1}`$:

```math
F_1^*,H_1^*,F_2^*,H_2^*,\ldots,F_{k-1}^*,H_{k-1}^*,F_k^*,
```

where $`F_j^*`$ are the pieces of the larger assembly and $`H_j^*`$ those of the smaller; all orientations agree with their reference orientation. The combined boundary list is their positive ends in that order followed by the negative ends in reverse order. Join $`(F_j^*)^-`$ to $`(F_{j+1}^*)^+`$ and $`(H_j^*)^-`$ to $`(H_{j+1}^*)^+`$. In the combined outer list these waves are nested in the order

```math
\gamma_1,\zeta_1,\gamma_2,\zeta_2,\ldots,\zeta_{k-2},\gamma_{k-1}.
```

They are disjoint parallel waves. Two reaching arcs to the positive inner hole lie in one end annulus, and two to the negative inner hole in the other, again disjoint. Their outer orders match the two first positive ends and the two last ends of the corresponding assemblies. Hence the two **whole** oriented assemblies are disjoint. On forgetting the other assembly, each is the chosen untwisted linear standard form: the wave ordering and end strips agree with its reference, and no outer-collar winding has been introduced.

Both whole surfaces are connected spanning surfaces with the same relative class. A connected spanning surface disjoint from another separates the other's whole cut complement: otherwise a crossing arc could be closed there to give algebraic intersection one with the first surface, while avoiding the other, contradicting equality of their dual linking homomorphisms. It splits that connected block into two nonempty chambers. The cover therefore gives representative width one. This is the [full-block separation argument](parallel-satellites.md), §4, which does not require (SB). Zero class distance is impossible between the present surfaces of different genera, by Section 8's zero-width containment argument and Banks minimization. The distance is consequently one. ∎

**Proposition 9.2 (full-block radial distance).** For every $`k\ge1`$,

```math
\delta([A],[F_k])=k.
```

**Proof.** Choose the inner-inner seam $`\alpha`$ to miss the reaching seams and cross each parallel wave $`\gamma_j`$ once. The annulus $`A`$ meets $`F_k`$ in $`k-1`$ essential longitude circles. These cut $`A`$ into $`k`$ annuli and $`F_k`$ into $`k`$ genus-three, two-boundary pieces, one containing each $`S_j`$.

Here is the complete complement calculation. Write $`n=2k`$ and $`I_{ij}`$ for the interval of $`T`$ between successive boundary indices $`i,j`$. Cutting $`Q`$ along the $`k`$ parallel frontiers gives connected chambers $`K_0,\ldots,K_k`$, with the middle $`K_j`$ products $`S\times I`$. Their torus intervals are

```math
K_0:I_{n-1,0},\qquad
K_j:I_{j-1,j},I_{n-j-1,n-j}\ (1\le j\lt k),\qquad
K_k:I_{k-1,k}.
```

Cutting the pattern along all its $`F_k`$ arcs gives $`k`$ disks $`D_1,\ldots,D_k`$. Disk $`D_j`$ carries intervals $`I_{j-1,j}`$ and $`I_{n-j,n-j+1}`$ (cyclic subscripts), attaching respectively to $`K_j`$ and $`K_{j-1}`$. Thus the **whole** $`F_k`$ complement is the connected chain of spaces $`K_0,D_1,K_1,\ldots,D_k,K_k`$.

The arc of $`\alpha`$ in each $`D_j`$ separates those two attachment intervals. Cutting the whole complement by the $`k`$ annular pieces of $`A\setminus F_k`$ therefore gives exactly $`k+1`$ nonempty chambers, with wall-incidence graph a path. This includes both end companion chambers and all the $`S\times I`$ chambers.

The level labels do not fold back. In the positive boundary block the waves have the same transported coorientation. The chosen seam crosses all $`k-1`$ waves with the same intersection sign. Consequently one full lift of $`A`$ has its $`k`$ annular segments in $`k`$ consecutive $`F_k`$ blocks, with one segment in each. Translating those segments into one fixed full $`F_k`$ block yields walls from $`k`$ different consecutive full $`A`$ lifts. The chamber between two neighbouring walls lies in their common intermediate open $`A`$ block; the end chambers lie in the two outer blocks. Thus that whole $`F_k`$ block meets exactly $`k+1`$ consecutive open $`A`$ blocks, and its width is $`k`$.

Finally this pair is simplified in Banks Definition 4.1. A connected horizontal face on $`A`$ of a product region has its boundaries among the actual boundaries and these intersection circles; no intersection circle can lie in its interior. It must therefore be one of the annular components just cut off on $`A`$. A corresponding face on $`F_k`$ must be a whole corresponding component of its cut surface, because it can have no additional interior boundary. Every available such component has genus three and two boundaries. It cannot be a matching annulus. Hence no product region exists. The actual boundaries can be taken disjoint, and the pair is transverse. Banks Proposition 4.10 with its Section 10 extension now makes the width calculation the class minimum, proving the formula. ∎

For $`k=2`$ the interval table, three chambers and no-product-region check specialize exactly to the [certified distance-two example](parallel-satellites-obstruction.md). The propositions supply an infinite sequence of vertices with a lower-height neighbour in this **specified** subfamily and with unbounded class distance from $`A`$.

They do not select neighbours for arbitrary $`a,t`$, and they do not prove compatibility with a simplex containing other standard forms. Transporting a construction by one common homeomorphism gives another compatible pair, but different vertices cannot be transported independently and assumed to remain compatible. No global Morse or contraction conclusion follows.

## 10. Relation to the complete calculation

This volume establishes the joint companion classification, the covering assembly family, the geometric equality test and the radial subfamily. The [tree volume](parallel-satellites-k719-tree.md) completes twist equality, all edges, all lower neighbours and the contraction of the entire flag complex. Numerical formulas there use its explicitly fixed pillowcase references. The genus-six distance-two example is retained; failure of the annulus cone is compatible with contractibility.
