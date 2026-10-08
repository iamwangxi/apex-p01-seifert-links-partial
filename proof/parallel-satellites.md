# Parallel satellites: an annulus-cone theorem

[Overview](../README.md) · [Objects](objects.md) · [Sources](../sources/bibliography.md) · [Scope](scope.md)

Parallel-satellite proof sequence: [cone theorem and witnesses](parallel-satellites.md) (§§1–5, 9); [two-bridge criterion and examples](parallel-satellites-two-bridge.md) (§§6–7); [distance-two obstruction](parallel-satellites-obstruction.md) (§8). References within this sequence retain these section numbers. The [torus exact-edge proof](parallel-satellites-torus.md) has its own numbering.

## 1. Object, framing, and the precise hypothesis

Let $`C`$ be a nontrivial tame knot, $`V=N(C)`$ its zero-framed neighbourhood, and $`L`$ two parallel cores with orientations $`+C,-C`$. Write

```math
M=E(L)=P\cup_T Q,\qquad P=S^1_\lambda\times B,\qquad Q=E(C),
```

where $`B`$ is a pair of pants with labelled inner boundaries $`b_+,b_-`$ and outer boundary $`b_0`$. On $`T=\partial Q`$, $`\lambda`$ is the **preferred** companion longitude; the other coordinate is its meridian $`\mu`$. On the two actual link tori, the spanning boundaries have orientations $`+\lambda,-\lambda`$. Their linking number is zero.

A spanning surface is oriented, properly embedded, has exactly one prescribed boundary on each labelled actual torus, and has no closed component. It may be disconnected; incompressibility is componentwise. Ambient isotopies start at the identity, preserve actual torus labels, and permit the boundary curves to move. There is no genus or norm restriction.

Let $`\phi:\pi_1(M)\to\mathbb Z`$ be total oriented linking number. In reference companion coordinates it has values $`+1,-1`$ on the two inner meridians, and zero on $`\lambda`$. Its restriction to **all** of $`\pi_1(Q)`$ is zero: the companion meridian links the two oriented parallels with cancelling signs. Every spanning surface represents $`\mathrm{PD}(\phi)`$.

For spanning representatives $`S,F`$, let $`U_j=\tau^jU_0`$ be lifts of the **whole open complement** $`M\setminus S`$, and $`W`$ one lift of the whole open complement $`M\setminus F`$. Define

```math
D(S,F)=\max\{j:W\cap U_j\ne\varnothing\}
       -\min\{j:W\cap U_j\ne\varnothing\},\qquad
\delta([S],[F])=\min_{S',F'}D(S',F').
```

The minimum is over the two ambient-isotopy classes. Independent lift choices for disconnected components are prohibited. The complex $`X(L)=IS_{\mathrm{cyc}}(L)`$ has these incompressible vertices, an edge between distinct classes when $`\delta=1`$, and flag completion. Section 4 proves the required distance bounds directly; no minimum-norm distance theorem is used there.

Choose a seam $`\alpha`$ from $`b_+`$ to $`b_-`$, and set $`A=S^1_\lambda\times\alpha`$, $`a=[A]`$. Its core injects through $`\pi_1(P)\to\pi_1(M)`$, so $`a`$ is a vertex.

The precise companion hypothesis is:

> **(SB).** Every connected, orientable, properly embedded, incompressible and boundary-incompressible surface in $`Q`$, with **nonempty** boundary all of whose circles have preferred-longitude slope, has exactly one boundary circle.

Orientability is the convention of the spanning problem; nonempty boundary is the convention of [the torus proof](parallel-satellites-torus.md), §3. A literal empty-boundary reading would admit a peripheral torus and would not hold even for a torus knot. No such component occurs among the cut pieces below. A hypothesis quantifying over more surfaces than the displayed one also suffices for the conditional theorem.

**Theorem 1.1 (conditional cone theorem).** If $`C`$ satisfies (SB), then

```math
\delta(a,v)=1\quad\text{for every vertex }v\ne a.
```

Consequently $`X(L)`$ is the simplicial cone with vertex $`a`$, and its realization is contractible. This theorem does not classify the other vertices or their gluing twists.

## 2. Inputs and independence

H, HT and B denote the exact editions in the [bibliography](../sources/bibliography.md): Hatcher's 3-manifold notes, Hatcher–Thurston 1985, and Banks arXiv:1109.0965v1. The cone proof uses H Lemma 1.11 and Proposition 1.12, pp. 20–22, the explicit elementary pattern arguments below, and covering-space theory. It uses neither Competition Theorem A nor D′ nor PS's projection or contractibility theorem. The [two-bridge applications](parallel-satellites-two-bridge.md) use HT Theorem 1, p. 228, Propositions 1–2, p. 230, the neighbourhood double, p. 240, and component, boundary and Euler counts, pp. 243–245. Only the [distance-two obstruction](parallel-satellites-obstruction.md) additionally invokes B Proposition 4.10, p. 7, as explicitly extended to incompressible surfaces in §10, p. 22.

## 3. Minimum intersection and the same spanning representative

### 3.1. Essential cut pieces

The groups of all three boundary tori of $`P`$ inject into $`\mathbb Z\times\pi_1(B)`$. The nontrivial companion exterior $`Q`$ is irreducible and boundary-incompressible. Amalgam normal form gives injections of both piece groups and all the displayed torus groups into $`\pi_1(M)`$. The usual sphere-cutting argument gives irreducibility of $`M`$; hence $`L`$ is non-split. H's cutting argument is on pp. 14–15.

Fix an arbitrary vertex $`v=[F]`$. Choose a transverse representative minimizing the integer $`|F\cap T|`$ over its full ambient-isotopy class. This is an intersection minimum, not a genus, area or norm minimum.

Every intersection circle is essential on both surfaces. Indeed, incompressibility makes a circle trivial on one trivial on the other. An innermost disk on $`T`$, the corresponding disk on $`F`$, and irreducibility give a disk push reducing intersection. No entire spanning component can be trapped in the ball, since each has actual boundary. Cut-piece groups inject into the original surface group after cutting along essential circles, and hence into their own ambient piece. The cut pieces are therefore incompressible. There are no disk cut pieces and no closed cut pieces.

There is also no boundary-parallel annular cut piece. Such a piece must have both ends on $`T`$: one actual torus is used only once by $`F`$, and different boundary tori cannot support a boundary parallelism. Its parallelism with a $`T`$-subannulus is a solid torus. Other cut pieces inside that solid torus have groups injecting into its cyclic group. They have boundary and are not disks, so they are annuli with primitive longitudinal boundary in that solid torus. A meridian disk cuts each into one disk. Relative disk isotopy in the resulting ball straightens this finite system and supplies an innermost empty annular parallelism. Pushing that annulus across $`T`$ removes two circles, contradicting the minimum. This is the elementary nested-annulus argument also written in [the torus proof](parallel-satellites-torus.md), §4.1; it does not delete closed components.

H Lemma 1.11, p. 20, now makes every cut component boundary-incompressible. Thus H Proposition 1.12 applies on the pattern side with its full essentiality hypothesis.

### 3.2. Longitudes and the exclusion of outer–outer annuli

A pattern component meeting an actual torus has fibre-slope boundary there. It cannot be horizontal, so it is a verticalisable annulus. If the two actual boundaries are paired by an inner–inner annulus, it is a whole component of $`F`$. Any remaining component would have no actual boundary and would be closed. Consequently there is no remaining component, $`F\cap T=\varnothing`$, and $`F`$ represents $`a`$.

Otherwise each actual boundary is on an inner–outer annulus. In particular there is a longitude on $`T`$. All essential disjoint circles on a torus have the same unoriented slope, so **all** of $`F\cap T`$ is longitudinal. Every remaining pattern component has only fibre-slope boundary, excludes the horizontal case, and is an annulus.

Let $`t,r,u`$ be the numbers of inner–inner, inner–outer and outer–outer pattern annuli. Endpoint counting gives

```math
2t+r=2,\qquad |F\cap T|=r+2u.
```

For $`v\ne a`$ we have $`t=0,r=2`$. Under (SB), each connected companion piece has exactly one boundary. An outer–outer annulus would join the sole boundaries of two distinct companion pieces; their union with it would already be a closed whole component of $`F`$. It cannot continue to an actual torus. This contradicts the object definition. Hence $`u=0`$.

It follows that this same minimum representative has precisely two inner–outer annuli and two distinct companion components, each with one boundary. Their orientations are positive and negative. The complete spanning system is disconnected with one actual boundary on each component. No companion isotopy classification or fibration has been used.

### 3.3. Simultaneous straightening and the annulus next to this $`F`$

First straighten all fibre-slope boundary curves on $`T,T_+,T_-`$. Extend the $`T`$ motion into collars on **both** sides, carrying the entire $`F`$; extend the actual-boundary motions in their $`P`$-side collars. These collars miss $`T`$ and do not change the minimum intersection count. Straighten the pattern annuli simultaneously, relative to their resulting outer boundary. One elementary proof chooses a system of base arcs cutting $`B`$ to a disk, with endpoints missing the existing boundary endpoints. Their product cutting annuli meet the pattern system only in circles. Remove trivial circles by disk/ball moves decreasing the total count. Straighten essential intersection circles to fibre cores on the cutting faces before cutting. After cutting, the ambient space is a solid torus with a primitive longitudinal annulus system. A meridian disk and relative disk isotopies in a ball straighten the entire system; matching traces on the cut faces make the isotopies glue. This proves the relative system statement rather than separately choosing incompatible isotopies. See also [the torus proof](parallel-satellites-torus.md), §4.2.

Thus, for the **one resulting representative** still called $`F`$, the pattern part is $`S^1\times(\beta_+\cup\beta_-)`$, where the two disjoint seams join the respective inner boundaries to $`b_0`$. Cutting the pair of pants along these seams gives a disk. In that disk choose a proper arc joining the original inner boundary segments and missing the cut seam faces. Its image $`\alpha_F`$ is a seam from $`b_+`$ to $`b_-`$ disjoint from both $`\beta`$'s, with distinct boundary endpoints. Set

```math
A_F=S^1_\lambda\times\alpha_F.
```

Every inner–inner seam in a pair of pants is isotopic to the fixed $`\alpha`$ when endpoints may move on the labelled boundaries. For example, complete the seams to hexagon decompositions; their possible discrepancies are boundary twists, removed by boundary rotations. Therefore $`[A_F]=a`$. By construction $`A_F\cap F=\varnothing`$.

This is a compatible pair of actual representatives. We do not alter the companion pieces independently, identify their unmarked classes, or choose separate lifts for them. We subsequently hold this $`F`$ fixed throughout the block calculation.

## 4. Complete blocks, separation, and the distance lower bound

### 4.1. Two elementary facts about every spanning system

**Connected-complement fact.** The whole complement $`M\setminus F`$ is connected, even when $`F`$ is disconnected. At the boundary of each component, a meridian intersects that component once and misses all others. Removing its crossing segment joins the two local sides of that component in the complement. In the connected dual graph of complement regions every component-edge is consequently a loop. A connected graph having only loop edges has one vertex.

Every loop in this complement has intersection zero with $`F`$, and hence $`\phi=0`$. The cyclic cover therefore restricts to a homeomorphism on each lift of the **whole** open complement. Equivalently, copies of the connected cut block are stacked at a common integer level. The same facts apply to $`A_F`$ and to all other representatives.

**Connected-wall fact.** A connected two-sided proper surface in a connected manifold either is nonseparating or separates into exactly two chambers. Its complement dual graph has one edge. If it is nonseparating, a short crossing arc can be closed up through its complement to give a loop of algebraic intersection one.

### 4.2. Separation in the full $`F`$ block

Let $`N_F=M\mathbin{\|}F`$ be the whole cut block, with corners rounded. It is connected. The compact $`A_F`$ lies properly in it, away from the cut $`F`$ faces; its boundaries are on the original boundary annuli. All loops of $`N_F`$, pushed off the cut faces, have $`\phi=0`$.

Suppose $`A_F`$ were nonseparating in $`N_F`$. The connected-wall fact would supply an interior closed loop $`\gamma`$ with

```math
\gamma\cdot A_F=\pm1.
```

Its image in $`M`$ misses $`F`$. Since both surfaces represent the same class,

```math
\pm1=\gamma\cdot A_F=\phi(\gamma)=\gamma\cdot F=0,
```

a contradiction. Thus $`A_F`$ separates the full block into exactly two connected chambers with nonempty interiors. This includes **all** companion complementary regions and attachments, whatever their topology. No replacement by a pattern-side block or by a companion knot cover is involved.

Choose one complete open $`F`$-block $`W`$ upstairs. It maps homeomorphically onto $`M\setminus F`$ and contains exactly one full lift of $`A_F`$, because $`A_F`$ is connected and disjoint from $`F`$. All other lifts of $`A_F`$ lie in the other $`F`$-blocks. The two chambers lie on the opposite sides of this one wall, namely in consecutive complete $`A_F`$-blocks $`U_k,U_{k+1}`$. There is no further wall in $`W`$ and neither chamber is empty. Therefore

```math
D(A_F,F)=1,\qquad \delta(a,[F])\le1.
```

More generally, this argument proves that a connected spanning surface disjoint from a distinct spanning surface has representative width one. The annulus supplies the connected wall in the present problem; disconnected–disconnected disjointness alone would not supply it.

### 4.3. Width zero forces the annulus class

Take arbitrary representatives $`A'\in a`$ and $`F'\in v`$, without requiring transversality. Suppose a complete open $`F'`$-block has width zero against the $`A'`$ blocks. It cannot contain an interior point of an $`A'`$ wall: a sufficiently small ball at that point, contained in the open $`F'`$-block, meets two adjacent open $`A'`$-blocks.

The block maps homeomorphically onto $`M\setminus F'`$. Hence every interior point of $`A'\setminus F'`$ would produce that contradiction, and

```math
\mathop{\rm int}A'\subset F',\qquad A'\subset F'
```

by properness and closure. Such containment makes $`A'`$ an entire component of $`F'`$: its interior is open in that surface component by the local manifold theorem, and its boundary, lying on $`\partial M`$, is on the corresponding boundary of $`F'`$. The image is closed and also open as a submanifold with boundary. It uses both actual tori. Any other component would have no actual boundary and would be closed, which is forbidden. Thus $`F'=A'`$ as underlying embedded surfaces. The prescribed boundary orientations also determine the same orientation, so $`v=a`$.

For $`v\ne a`$ width zero is therefore impossible, and $`\delta(a,v)\ge1`$. Under (SB), §§3–4.2 attain the upper bound for every such vertex. This proves Theorem 1.1.

If $`\sigma`$ is any simplex of the flag complex, its vertices form a clique. Adding $`a`$ still gives a clique, hence a simplex. The barycentric homotopy $`x\mapsto(1-t)x+ta`$ contracts its realization to $`a`$. It is the ordinary simplicial-cone contraction and is continuous in the weak simplicial topology, including for an infinite complex. Pairwise cone adjacency does not require one simultaneous geometric configuration of all vertices.

## 5. Torus knots satisfy (SB)

Let $`C=T(p,q)`$, with $`p,q\ge2`$ coprime. Its exterior is Seifert fibred over a disk with exceptional orders $`p,q`$. Its regular fibre slope is

```math
h=\lambda+pq\,\mu.
```

For verification, the usual group $`\langle x,y\mid x^p=y^q\rangle`$ sends $`x,y`$ in abelianization to $`q\mu,p\mu`$. The regular fibre $`x^p=y^q`$ has homology $`pq\mu`$ and longitudinal degree one, giving the displayed slope. See [the torus proof](parallel-satellites-torus.md), §3.1.

Let $`S`$ be any surface quantified in (SB). H Proposition 1.12 excludes the vertical case: a bounded vertical surface is an annulus with regular-fibre slope, different from $`\lambda`$. Thus $`S`$ is horizontal. Orient the fibre vector field. On a connected oriented horizontal surface its transverse sign is constant. Projection to the oriented base has constant orientation sign, and all boundary circles cover the one base boundary with that sign. Consequently all $`b=|\partial S|`$ longitudinal boundaries have the same orientation.

The boundary homomorphism identifies $`H_2(Q,\partial Q)`$ with the longitude kernel, since $`H_2(Q)=0`$ and $`H_1(Q)=\mathbb Z[\mu]`$. If $`\eta`$ is a Seifert generator, then

```math
[S]=\pm b\eta\ne0.
```

A separating proper oriented surface has relative class zero. Therefore $`S`$ is nonseparating, and a crossing arc closed in its complement gives a loop pairing with $`[S]`$ by one. Its class is primitive. The displayed formula forces $`b=1`$. This proves (SB) for every nontrivial torus knot, with no genus restriction. Reflection handles mirrors. The fibre-uniqueness argument in the torus proof is not required here.

## 9. Disconnected, non-minimal witnesses and a smaller factor closure

This section holds for every nontrivial companion $`C`$, independently of (SB) and independently of the number of vertices.

Choose a minimum-genus Seifert surface $`R\subset Q`$, of genus $`g\ge1`$. A genuine compression, retaining its one-boundary descendant, would lower its genus; thus it is incompressible. Take disjoint parallel copies $`R,-R`$ and attach two reaching pattern annuli. Call the resulting disconnected spanning system $`G`$. Each component's group is unchanged by the annular boundary collar, injects into $`\pi_1(Q)`$, and then injects into $`\pi_1(M)`$. Thus $`G`$ is an incompressible vertex, with

```math
\chi_-(G)=2(2g-1)>0,\qquad
x_M(\mathrm{PD}(\phi))=\chi_-(A)=0.
```

It supplies both a disconnected and a non-norm-minimal vertex. These facts hold in particular for the nonfibred $`5_2`$ companion. Finiteness or infinitude of the vertex set is irrelevant to these witnesses.

For a structural comparison, consider the smaller factor class of nonempty non-split links satisfying at least one of: being a knot; every incompressible spanning surface connected; every incompressible spanning surface norm-minimal. Suppose the two-component $`L`$ were a finite specified-component sum of such factors $`J_i`$. Component counting gives

```math
1=|L|-1=\sum_i(|J_i|-1).
```

Exactly one original factor has two components; all others are knots. Thus only local knot insertions into that two-component factor are possible, including arbitrary further knot-sum bracketings.

Normalize the incompressible spanning annulus $`A`$ against each meridional decomposing annulus to one trace arc. An essential intersection circle would have $`\phi=\pm1`$, while every loop on $`A`$ has $`\phi=0`$; trivial circles are removed by incompressibility and irreducibility. The prescribed boundary meets each meridional boundary once, so one spanning trace remains. Banks §10, p. 22, explicitly supplies this interface for incompressible surfaces, not merely norm-minimal ones. Sequential cutting preserves the earlier traces, as in [the torus proof](parallel-satellites-torus.md), §7.2.

At a node separating a knot block from a two-component block, the genus-zero annulus cuts into a one-boundary genus-zero knot piece and a two-boundary genus-zero central piece. The knot piece is a disk, so that knot block is an unknot. Recursively cutting this disk gives disks for each of its original knot leaves, and repeating on the central annulus treats every remaining node. Thus every original knot factor is an unknot. The sole two-component factor is isotopic to $`L`$ itself. The vertex $`G`$ shows that $`L`$ satisfies neither of the other two factor conditions, and it is not a knot. It cannot be an allowed original factor. This contradicts membership in the stated closure.

This is a structural exclusion and assumes no contractibility theorem for the all-minimal factors. The enlarged factor class in [the merged theorem](main-theorem.md) explicitly includes the parallel links satisfying (SB).
