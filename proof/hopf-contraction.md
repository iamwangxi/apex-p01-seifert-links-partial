# All balanced Hopf fibre links: finite-input nullhomotopies

[Overview](../README.md) · [Matching model](hopf-model.md) · [Main theorem](main-theorem.md) · [Sources](../sources/bibliography.md)

Every balanced Hopf fibre link has contractible $`X(H_{2m})`$. The fixed-graph theorem below covers disconnected embedded bipartite multiarcs, bridges, common matching arcs and complementary regions that are not disks. Its region-potential decoder converts a perfect-matching flow into a point of the true cyclic-distance complex. Combining it with one finite height family gives a finite nullhomotopy of every finite inclusion.

Circle-valued maps, regular fibres and averaging follow the second proof in Hatcher, *The cyclic cycle complex of a surface*, arXiv:0806.0326v1 (2008), pp.5–6. Planar bipartite face heights and matching lattices are classical; see Propp, *Lattice structure for orientations of graphs*, arXiv:math/0209005v3 (2021), §3, Theorem 2, pp.21–22. The potential and rounding facts used here are proved below, including the noncellular cases, and do not invoke Propp’s theorem.

The matching model and class-minimum calculation retain PS Definition 2.1 and Proposition 3.2 in §§2–3, including its stated Sakuma interface. No projection, order, dismantling or contractibility result from PS §§4–7 is used. Geometric disjointness alone never declares two different matchings adjacent.

## 1. Objects, conventions and the fixed-graph theorem

Let $`P=P_{2m}`$ be an oriented sphere with $`m`$ positive and $`m`$ negative labelled boundary circles. A matching consists of $`m`$ disjoint proper arcs, one end on every labelled circle, with each arc joining opposite signs. Endpoints may slide on their own circles. Write $`[A]`$ for the corresponding vertex of $`X=X(H_{2m})`$.

We use the vertex bijection, normalisation and arbitrary-hole complete-block formula proved in [the matching model](hopf-model.md), Theorem 1.1 and §§2–5. Successive cutting joins two previously unused boundary circles, so remains connected. Its special six-hole converse from disjointness to adjacency is not used here. For $`m\ge2`$, choose one hyperbolic metric with geodesic boundary and use each proper arc class's unique orthogeodesic. The case $`m=1`$ has one endpoint-free arc class on an annulus and one vertex.

An allowed graph $`G`$ is a finite collection of pairwise disjoint, pairwise nonisotopic positive-negative proper arcs containing a matching on **all prescribed boundary circles**. Different edges may have the same labelled ends. The embedded collection, rather than just its abstract adjacency matrix, is retained. Its joint isotopy class is determined by its individual proper arc classes, by the simultaneous multiarc straightening in [the model](hopf-model.md), §3.1. This lets all subgraphs use the same canonical representatives.

Cap each boundary circle by a disk, extend its incident arc ends by nonintersecting radial spokes to the centre, and regard that centre as a vertex. This gives an embedded bipartite multigraph $`\widehat G\subset S^2`$. Direct every edge from its negative end to its positive end. Let $`\mathcal R_G`$ be the **connected open regions** of $`S^2\setminus\widehat G`$. These are not individual boundary walks of a ribbon graph. In particular, an annular region bounded by two different graph components is a single region. Let $`\ell(e),r(e)`$ be the regions to the left and right of the directed edge, possibly the same region.

For a region function $`u`$, set

```math
(D_Gu)_e=u_{\ell(e)}-u_{r(e)}.
```

Write $`\chi_A`$ for a matching's edge-indicator vector and

```math
P_G=\left\{w\in\mathbb R^{E(G)}:w_e\ge0,\quad
\sum_{e\ni v}w_e=1\text{ for every prescribed vertex }v\right\}.
```

Every $`w\in P_G`$ satisfies $`0\le w_e\le1`$. Fix a reference matching $`M`$, write $`m=\chi_M`$, and fix one root region $`f_0`$. Lemma 2.1 gives a unique $`u`$ satisfying

```math
w=m+D_Gu,\qquad u_{f_0}=0.
```

For **every** $`0\le\theta\lt1`$, define

```math
q_f^\theta=\lfloor u_f+\theta\rfloor,\qquad
m_e^\theta=m_e+(D_Gq^\theta)_e.
```

Section 4 below proves that $`m^\theta=\chi_{M_\theta}`$ for a matching. Define

```math
\mathcal S_G(w)=\int_0^1[M_\theta]\,d\theta.
```

This notation means a finite barycentric sum: cut the interval at the finitely many numbers $`\{-u_f\}`$, use the constant matching on each open interval, and combine repeated matching vertices. Threshold values themselves have measure zero.

**Theorem 1.1 (fixed-graph carrier).** The following hold.

1. The region potential exists and is unique up to one common constant, without connectedness or cellularity assumptions on $`G`$.
2. Every $`M_\theta`$ is a legal matching vertex, including at a threshold.
3. Any two threshold outputs have cyclic class distance at most one. Thus the positive-weight vertices of $`\mathcal S_G(w)`$ span a simplex.
4. $`\mathcal S_G:P_G\to|X|`$ is continuous and piecewise affine on a finite polyhedral subdivision. It is independent of the reference matching, root region and isotopic choice of embedded representatives.
5. Removing zero-weight edges commutes with decoding. Rules for two different allowed graphs agree on their common coordinate face, even if their remaining edges cross each other.
6. If $`\sigma`$ is a true simplex of $`X`$ whose matchings are contained in $`G`$, then

```math
\mathcal S_G\left(\sum_{A\in\sigma}\lambda_A\chi_A\right)
=\sum_{A\in\sigma}\lambda_A[A].
```

In particular, the subcomplex induced by all matchings of $`G`$ triangulates $`P_G`$ under the affine edge-coordinate map. It need not be one simplex.

## 2. Circulations and potentials on noncellular spherical graphs

**Lemma 2.1.** For a finite graph embedded in the oriented sphere, every real edge circulation $`c`$ is $`D_Gu`$ for a region function $`u`$. The kernel of $`D_G`$ consists of the common constants. If $`c`$ is integral, the root-normalised $`u`$ is integral.

**Proof.** Choose a spanning tree in each graph component. Each non-tree edge, together with the unique tree path between its ends, gives an oriented simple cycle. Parallel edges can give a simple two-edge cycle. These fundamental cycles span all circulations: subtract the multiple of each fundamental cycle needed to kill its non-tree edge, leaving a circulation supported on a forest. A forest circulation is zero, by successively removing leaves. This argument also shows directly that a bridge carries zero circulation.

By the Jordan curve theorem, an oriented simple cycle separates $`S^2`$ into two disks. Assign value one to every $`G`$ region on its left side and zero to every region on its right side. Every connected $`G`$ region lies wholly on one side. The resulting potential has difference one along a cycle edge traversed in its cycle direction, minus one if traversed oppositely, and zero along every other edge. Thus its difference vector is the cycle circulation. Taking the same linear combination as the cycle decomposition produces $`u`$. Subtract its root value. No region has been filled by a separate disk in this argument; a region with several boundary curves is assigned just one value.

For uniqueness, the region adjacency graph across **all** edges is connected. Indeed, a path on the sphere between two interior region points can be chosen to avoid finitely many vertices and cross edges transversely finitely often. If $`D_Gu=0`$, its value is unchanged at every such crossing, so it is constant on all regions. This is one global constant even when $`G`$ is disconnected. If $`c`$ is integral, following a path in this connected dual graph from the root shows every $`u_f`$ is an integer. ∎

For $`c=w-m`$, the vertex circulation equations hold because all incident edges point out at a negative vertex and in at a positive vertex, and the incident sums of both $`w`$ and $`m`$ equal one. Hence Lemma 2.1 proves assertion (a).

Conversely, $`D_Gu`$ is a circulation for any $`u`$. The successive sector values around a vertex telescope. A sector can reappear, and the left and right sectors of a bridge can agree; neither changes this telescoping identity. We will use this converse for rounded potentials.

**Capping convention, including unused holes.** A capped disk minus its incident radial star has one sector attached to each interval between successive arc ends. Each such sector attaches to only that interval, so adding the disk does not join formerly different complementary regions. With one incident arc, the single sector attaches to the connected boundary circle minus that endpoint. With no incident arcs, the disk simply fills a hole of the existing region. Every sector meets the original surface along a nonempty interval. Consequently capping induces a bijection of complementary components, with every capped region represented by a nonempty region in the original surface.

The circulation lemma therefore still applies if some auxiliary holes of a planar surface are not used by $`G`$: their filling introduces no extra choice of potential and no region merger. For $`X(H_{2m})`$ itself all $`2m`$ prescribed holes must be used by a matching; an isolated prescribed vertex would make $`P_G`$ empty and cannot be silently omitted from the matching condition. Non-disk regions arise already for graphs using every prescribed hole.

## 3. Identification with the complete complementary block

**Proposition 3.1.** Let $`A,B`$ be matching subgraphs of an allowed $`G`$, and let $`v`$ satisfy

```math
\chi_A-\chi_B=D_Gv.
```

Then

```math
\delta([A],[B])=\max_{f\in\mathcal R_G}v_f
-\min_{f\in\mathcal R_G}v_f.
```

**Proof.** First delete from $`G`$ every edge used by neither matching, retaining their common edges once. Across a deleted edge the circulation is zero, so its two incident potential values agree. Deleting an embedded edge merges its incident open regions if they are different; if they are already the same, it changes the topology of that region without creating a new potential value. More generally, any path in the larger complement avoiding the retained graph can be perturbed to avoid all vertices and cross only deleted edges, and therefore has constant potential. This proves that $`v`$ descends to the connected regions of the actual union $`A\cup B`$, including all mergers through deleted edges. Every resulting region contains at least one original $`G`$ region, since the finite original graph has empty interior. Hence the range of $`v`$ is unchanged. The capping observation in §2 identifies these components with the regions of $`P\setminus(A\cup B)`$.

Common proper arc classes coincide; distinct edges are nonisotopic and have disjoint interiors and distinct ends on a shared boundary circle. Thus this is a normalised pair in the sense of [the model](hopf-model.md), §4. There are no transverse intersections to make ordinary bigons or half-bigons, and no unrecognised common arc classes.

Cut $`P`$ along the entire matching $`B`$. Its complement is connected: successively cutting an arc joining two different unused boundary circles preserves connectedness. For $`P_{2m}`$ the completed cut surface has $`m`$ boundary circles and Euler characteristic $`2-m`$. Every loop in this complement has zero intersection with $`B`$, hence zero $`\psi`$. Choose **one** connected lift of this complete complement to the $`\psi`$ cover.

Build the complete-complement graph of [the model](hopf-model.md), §5: its vertices are the connected regions of $`P\setminus(A\cup B)`$, and its edges cross only $`A\setminus B`$, with positive crossing from right to left and height step $`+1`$. Do not cross a $`B`$ edge; a common arc gives no internal crossing edge. This graph is connected since the complete $`B`$ complement is connected.

On an $`A`$-only edge our equation gives $`v_\ell-v_r=1`$. On a $`B`$-only edge it gives $`-1`$, but that edge is not traversed in the complete-complement graph. On a common edge it gives zero; that edge is also not traversed. Thus the descended $`v`$ satisfies **exactly** the graph equations for the whole-block index function of the model’s Theorem 1.1. Connectedness makes the two functions equal up to one common constant (or one common sign reversal if all intersection conventions are reversed).

Each region has nonempty interior and represents an attained open-block index in the chosen complete lift. Every open-block intersection contains a point away from the arcs. No index is discarded and no frontier-only contact is added. The model’s Theorem 1.1, using PS Proposition 3.2 for the normalised annuli, identifies its range with the class minimum. This proves the formula. ∎

This proposition does not compute separate widths of annulus components and then take a maximum. In particular disconnected graph components are not permitted independent height shifts. A common edge has zero **difference-potential** jump while remaining a cut boundary in the complete-block construction; the proof does not replace that boundary by an extra crossing edge.

The proof of the model’s class minimum is in [§4](hopf-model.md#4-representatives-realising-the-class-minimum): a relative product region between noncommon vertical annuli would project to an arc homotopy forbidden by normalisation, and the common-annulus cases are treated separately. PS, printed pp.1492–1495, supplies the open-block and minimisation interface; Oertel, printed p.712, supplies the relative vertical-boundary condition. This is a declared literature interface, including PS's Sakuma reference.

## 4. Legal threshold matchings and their common simplex

**Lemma 4.1.** If $`a,b`$ are real and $`L,U`$ integers with $`L\le a-b\le U`$, then for every real $`\theta`$,

```math
L\le\lfloor a+\theta\rfloor-\lfloor b+\theta\rfloor\le U.
```

**Proof.** Apply monotonicity of the floor to $`b+\theta+L\le a+\theta\le b+\theta+U`$ and use its commutation with integer translations. ∎

The bounds $`0\le w_e\le1`$ give

```math
-m_e\le u_{\ell(e)}-u_{r(e)}\le1-m_e.
```

Lemma 4.1 shows that $`m_e^\theta`$ is an integer in $`[0,1]`$. The circulation identity $`\partial D_Gq^\theta=0`$ preserves all incident sums, so

```math
m_e^\theta\in\{0,1\},\qquad \sum_{e\ni v}m_e^\theta=1.
```

Every threshold output is therefore a perfect matching, embedded by the selected edges of $`G`$. It is a legal vertex of $`X`$. This proves (b), even at the finitely many floor discontinuities.

For $`0\le\theta\lt\theta'\lt1`$, let

```math
d_f=q_f^{\theta'}-q_f^\theta\in\{0,1\}.
```

We have $`\chi_{M_{\theta'}}-\chi_{M_\theta}=D_Gd`$. Proposition 3.1 gives

```math
\delta([M_\theta],[M_{\theta'}])=\mathrm{osc}(d)\le1.
```

This proves (c). Reversing the order of two thresholds gives the same bound. Distinct outputs are thus adjacent, and flagness makes all positive-weight outputs one simplex. In particular the barycentric integral defining $`\mathcal S_G`$ is a point of $`|X|`$.

We also have the exact edge-coordinate identity

```math
\int_0^1\lfloor u_f+\theta\rfloor\,d\theta=u_f,
\qquad
\int_0^1\chi_{M_\theta}\,d\theta=w.
```

For the first identity, write $`u_f=k+a`$, $`0\le a\lt1`$: the floor is $`k`$ for length $`1-a`$ and $`k+1`$ for length $`a`$. The second follows by applying $`D_G`$ and adding $`m`$. Thus every $`w\in P_G`$ is a convex combination of perfect matchings, proved here without an external matching-polytope integrality theorem.

## 5. Independence, continuity and finite affine pieces

### 5.1. Reference and root

Let $`m'=m+D_Gk`$ be another matching. By Lemma 2.1, the root-normalised $`k`$ is integral. The potential for $`w-m'`$ with the same root is $`u'=u-k`$. Hence, for every threshold,

```math
m'+D_G\lfloor u'+\theta\rfloor
=m+D_Gk+D_G(\lfloor u+\theta\rfloor-k)
=m+D_G\lfloor u+\theta\rfloor.
```

Reference independence is pointwise, not just after averaging.

Changing the root or adding a common real constant $`c`$ to $`u`$ replaces the threshold by $`\theta+c`$ modulo one. The extra common integer in $`\lfloor u+\theta+c\rfloor`$ vanishes under $`D_G`$. Lebesgue measure on the threshold circle is invariant under this rotation. Thus the barycentric integral is root independent; individual threshold labels may rotate. An isotopy of the multiarc carries its regions, their incidences and matching classes to the corresponding data, so the resulting map also depends only on the embedded arc classes.

### 5.2. Continuous affine formulas on finitely many cells

With root and reference fixed, solving the injective linear system $`D_Gu=w-m`$, $`u_{f_0}=0`$, makes $`u`$ affine in $`w`$. A simple path in the connected region adjacency graph shows

```math
|u_f|\le |\mathcal R_G|-1,
```

since every edge difference is in $`[-1,1]`$. This also covers a one-region forest.

Subdivide $`P_G`$ by the finitely many relevant hyperplanes

```math
u_f=k,\qquad u_f-u_g=k\qquad (k\in\mathbb Z),
```

including all polytope faces. The displayed bound makes the required integer set finite. On a relative open cell, integer parts of all potentials and the cyclic order of their fractional parts are fixed. For each open threshold interval the rounded matching is fixed. Its interval length is affine in $`u`$, hence in $`w`$. Combining intervals with equal matching class preserves affinity.

At a cell boundary, colliding thresholds enclose intervals whose lengths go to zero. For every positive-length limiting interval, choose an interior threshold away from all limiting breakpoints. All floor values, and hence its matching, are unchanged for nearby parameters. A breakpoint passing through zero merely splits or joins intervals with the same matching. Because there are only finitely many matchings in $`G`$, the corresponding barycentric coordinates converge in one finite geometric realisation. Thus the affine formulas extend continuously and agree on all shared faces, also at multiple simultaneous collisions and lower-dimensional cells. Each cell's image is in the simplex from §4. This proves all of (d).

## 6. Zero-weight deletion and common-face gluing

Let $`w\in P_G`$ and let $`H`$ be the subgraph of edges with $`w_e>0`$. If $`w_e=0`$, then

```math
u_{\ell(e)}-u_{r(e)}=-m_e\in\mathbb Z.
```

Integer translation of the floor gives $`m_e^\theta=0`$ for **every** threshold. In particular any $`M_\theta`$ furnishes a reference matching $`M'`$ contained in $`H`$. Switch to that reference using §5.1. Now on each deleted edge $`e`$ both $`w_e`$ and $`m'_e`$ vanish, so its two potential values agree.

Exactly as in Proposition 3.1, deleting these edges merges their incident regions and the potential descends to the actual regions of $`H`$. This remains true when an edge changes a non-disk region's boundary topology without merging two different regions. Choose the image of the old root as the new root. On each merged region the old potentials are identical, so their rounded values are identical too. The edge indicators on retained edges therefore agree **pointwise** with the rule for $`H`$, while all removed indicators are zero. Consequently

```math
\mathcal S_G(w)=\mathcal S_H(w|_{E(H)}).
```

The same holds for deleting any chosen subset of zero-weight edges, including edges that belong to no perfect matching of $`G`$. If a purported face has no feasible point, there is no gluing assertion to check. On every nonempty zero-coordinate face the preceding argument supplies a supported matching, so its associated subgraph is allowed.

Now put two allowed graphs into common arc-class coordinates, using canonical representatives. Their matching polytopes intersect exactly in the flow polytope of their common edge set, with absent coordinates zero. At a point of this intersection, delete all zero edges from either graph. Both reduce to the **same** positive-support embedded graph $`H`$ and the same intrinsic decoder there. Thus their maps agree. It is not necessary to embed the union of the two graphs, and edges outside the common support may cross. This proves (e).

## 7. Exact recovery on every true input simplex

Let $`\sigma=\{A_0,\ldots,A_k\}`$ be a simplex of $`X`$, realised within $`G`$. For each matching write

```math
\chi_{A_i}=m+D_Gn_i,\qquad (n_i)_{f_0}=0.
```

The $`n_i`$ are integral. Proposition 3.1 and the true simplex condition imply $`\mathrm{osc}(n_i-n_j)\le1`$. The root coordinate of this difference is zero. Therefore its coordinates are all in $`\{0,1\}`$, or all in $`\{-1,0\}`$, or all zero. In particular $`n_i,n_j`$ are comparable in coordinatewise order. Order the distinct matchings so that

```math
n_0\le n_1\le\cdots\le n_k.
```

Their potentials are distinct by injectivity of $`D_G`$. Switch reference to $`A_0`$. Then $`n_0=0`$ and, since $`\mathrm{osc}(n_k-n_0)\le1`$, every coordinate of every $`n_i`$ is zero or one. Each coordinate stays zero throughout the chain or first becomes one at a unique index $`j\in\{1,\ldots,k\}`$. Every strict consecutive step changes at least one coordinate.

For $`w=\sum_i\lambda_i\chi_{A_i}`$ its potential is $`u=\sum_i\lambda_i n_i`$. A coordinate first becoming one at $`j`$ has value

```math
u_f=\sum_{i=j}^k\lambda_i=1-\sum_{i=0}^{j-1}\lambda_i.
```

Set $`s_i=\sum_{t=0}^i\lambda_t`$ and $`s_{-1}=0`$. For $`s_{i-1}\lt\theta\lt s_i`$, rounding turns on exactly those coordinates that have become one by index $`i`$. Thus $`\lfloor u+\theta\rfloor=n_i`$ and $`M_\theta=A_i`$ on an interval of length $`\lambda_i`$. Coordinates always equal to zero stay zero. If a coordinate's weighted value is exactly one, it is already on at threshold zero, consistent with preceding zero-length intervals. Zero coefficients cause coincident thresholds and omit zero-length intervals; they do not change the conclusion.

Integrating gives

```math
\mathcal S_G(w)=\sum_i\lambda_i[A_i].
```

This proves (f) for arbitrary-dimensional input simplices, without a hole bound. It is a chain argument for the **true** distance-one complex; geometric disjointness of a whole graph's matchings is insufficient to justify it.

## 8. The triangulation consequence

Let $`X_G`$ be the subcomplex of $`X`$ induced by the finitely many matching subgraphs of $`G`$. Different edge subsets give different matching vertices, since distinct edges have different proper arc classes and the joint matching class retains those classes. Define the affine edge map on each simplex by

```math
T_G:|X_G|\longrightarrow P_G,\qquad
\sum_i\lambda_i[A_i]\longmapsto\sum_i\lambda_i\chi_{A_i}.
```

Section 4 proves $`T_G\mathcal S_G=\mathrm{id}_{P_G}`$. Section 7 proves $`\mathcal S_GT_G=\mathrm{id}_{|X_G|}`$. Hence these are inverse homeomorphisms. In particular every simplex maps affinely and injectively to an actual affine simplex in $`P_G`$. Two image simplices meet only in the image of their common face, since applying $`\mathcal S_G`$ recovers the same point of $`|X_G|`$. These finitely many simplices cover $`P_G`$, giving precisely the proposed triangulation. Section 6 proves its compatibility with zero-coordinate faces.

This supplies a complete proof of the height-rounding facts used here. No unverified appeal to Propp's matching lattice theory or to a matching-polytope integrality result is required. No claim that this construction or lattice structure is new is made.

## 9. The finite height family for arbitrary balanced hole number

We now compose the fixed-graph decoder with a finite family of equivariant heights.

**Theorem 9.1.** For every $`m\ge1`$, $`|X(H_{2m})|`$ is contractible. More precisely, fix a matching $`M_*`$. For every finite subcomplex $`K\subset X(H_{2m})`$ there is a finite subcomplex $`Y`$ and a continuous homotopy

```math
C_K:|K|\times[0,1]\longrightarrow |Y|
```

from the inclusion to the constant map at $`[M_*]`$. It is obtained by averaging regular-fibre **arc indicators**, followed by the decoder of Theorem 1.1. All choices are made once for the whole finite input, so the formulas agree on its faces. There is a finite terminating rational procedure, with no uniform complexity bound claimed.

The height construction uses circle-valued band maps and their real lifts. Choose the finitely many arc classes in the vertices of $`K`$ and $`M_*`$, copying a common class once. A true distance-one pair has no transverse orthogeodesic crossing, by [the model](hopf-model.md), §6.1. Thus the canonical arc representatives are simultaneously disjoint for every input simplex. Make a simultaneous rational PL approximation, retaining this disjointness, and choose thin bands $`B_e`$ whose interiors and boundary-end intervals are disjoint for every noncrossing pair of different arcs. Only incompatible arcs need cross. Use a common rational triangulation $`T`$ for all the bands.

For each matching $`M_j`$ in this finite list, its circle band map is the transverse coordinate $`t_e\pmod1`$ on $`B_e`$ for $`e\in M_j`$, and zero elsewhere. Its induced homomorphism is the same primitive peripheral $`\psi`$. Lift it to $`h_j:\widetilde P_\psi\to\mathbb R`$, normalising every lift to zero at one common lift of a point outside all bands. Then

```math
h_j(\tau x)=h_j(x)+1,\qquad
h_\mu=\sum_j\mu_jh_j,\qquad \sum_j\mu_j=1,\quad\mu_j\ge0.
```

Every boundary lift of $`h_\mu`$ is monotone in its prescribed degree direction, with increment $`+1`$ or $`-1`$ over one boundary period. For a phase $`r`$ avoiding all triangulation-vertex values modulo one, the descended circle map has a finite embedded PL fibre. It has exactly one boundary endpoint at each prescribed hole: monotonicity excludes multiple preimages of a regular value, and all plateau values were excluded. The oriented interval components have opposite endpoint signs. Removing all closed components therefore leaves a legal $`m`$-arc matching $`A_r(h_\mu)`$.

The boundary argument holds for every $`m`$. Deletion is used solely for this endpoint and legality assertion. It is **not** asserted to preserve a complementary lift, an old height potential, or pairwise distance.

## 10. Finite arc-flow coordinates, including critical collisions

Between consecutive vertex phases, the full fibre has a fixed normal PL template and hence a fixed joint isotopy class, including the classes of its interval components. Cut the phase circle additionally at zero and write $`J`$ for its open intervals. Define the flow in arc-class coordinates by

```math
W_e(\mu)=\sum_J |J|\,\mathbf{1}_{\{e\in A_{r_J}(h_\mu)\}},
\qquad r_J\in J.
```

There are only finitely many arc classes needed for the **entire** coefficient simplex; denote this set by $`\mathcal E`$. Here is the detailed finiteness and continuity argument, without assuming that all phase outputs are a cyclic simplex.

Choose a lift of every triangle of $`T`$ and retain all its corner lifts, with their integer deck transition data. Choose an integer $`L`$ bounding the absolute corner heights for all $`h_j`$. Convex combinations have the same bound. Any phase segment in a chosen lifted triangle lies at real level $`r+k`$, with $`-L-1\le k\le L+1`$. There are finitely many triangle-level pairs. Record the sides met by each segment and the order of all intersection points on each edge, along with the fixed gluing translations. There are only finitely many such templates. Preserving these finite incidences and orders gives an ambient PL isotopy by moving edge points in order and extending over triangles. Deleting circle components leaves finitely many possible joint matching classes and thus finitely many component arc classes $`\mathcal E`$. This retains winding data; recording only endpoint pairings would not suffice.

Every selected corner height $`a_v(\mu)`$ is affine. Subdivide coefficient space by

```math
a_v=k,\qquad a_v-a_{v'}=k,
```

for the finite relevant integer ranges, and include all coefficient faces. On a relative open cell, integer parts and the cyclic order of all vertex phases are fixed. Every positive-length interval $`J`$ has a fixed template, and its length is affine. Thus each $`W_e`$ is affine on the cell. At a shared face, intervals squeezed between colliding phases have length tending to zero; every interval still of positive length has a persistent template, found by choosing one interior phase away from all limiting vertex values. Therefore the edge-coordinate formulas agree on the face. The extra phase cut at zero merely splits or rejoins equal templates. This proves

```math
W:\Delta^{N-1}\longrightarrow\mathbb R^{\mathcal E}
```

is continuous and piecewise affine on a finite subdivision, also at coefficient faces, flat triangles and simultaneous critical-phase collisions. Importantly this is a map into a fixed **finite-dimensional** coordinate space. It has not yet been regarded as a barycentric point of $`|X|`$.

For each parameter $`\mu`$, let $`G_\mu`$ consist of the distinct arc classes with $`W_e(\mu)>0`$. Positive-length intervals give representatives of all these classes in mutually disjoint regular fibres of the **same** circle map. After discarding circles, their actual arc representatives remain disjoint; identifying repeated classes and straightening gives an allowed embedded graph. Every phase matching uses every hole, so

```math
W_e(\mu)\ge0,\qquad \sum_{e\ni v}W_e(\mu)=\sum_J|J|=1.
```

Hence $`W(\mu)\in P_{G_\mu}`$. The graph contains at least one of its phase matchings. There are finitely many such support graphs, since their edges lie in $`\mathcal E`$. They can be obtained directly from the relative open parameter cells: on a cell the positive-length interval templates are fixed, their lengths are positive, and all coordinate summands are nonnegative, so its positive-support graph is fixed. On a boundary of that cell, support can only shrink, by continuity.

## 11. Gluing the decoder while support graphs change

Let $`\mathfrak G`$ be this finite collection of embedded support graphs, put their polytopes in the same coordinate space $`\mathbb R^{\mathcal E}`$, and let

```math
\mathcal P=\bigcup_{G\in\mathfrak G}P_G.
```

Each $`P_G`$ is compact, hence closed in $`\mathcal P`$. Their intersections are common zero-coordinate faces, possibly empty. Section 6 shows the decoders agree on each such intersection. The finite closed-set pasting lemma yields one continuous map

```math
\mathcal S:\mathcal P\longrightarrow |Y_0|,
```

where $`Y_0`$ is the finite subcomplex consisting of the finitely many decoder image simplices and all their faces. It is finite because the graph collection is finite and every graph has finitely many matchings. Each individual image is in a simplex by §4. No simplex containing outputs from all neighbouring parameter cells is required; their formulas agree at the actual common face.

This establishes the critical parameter-changing interface. In particular, the whole family does not need one globally embedded graph: incompatible arc classes at different parameters can cross. Only the positive-support graph at each parameter must be embedded. At a change, the common positive-support graph carries both limiting rules.

Set

```math
F(\mu)=\mathcal S(W(\mu)).
```

It is continuous and has finite image subcomplex. Refining each parameter cell by the inverse images of the fixed-graph decoder hyperplanes gives a finite polyhedral subdivision on which $`F`$ is affine. This is an assertion about coefficient/cone coordinates; its expression in product coordinates $`(x,t)`$ can be bilinear before subdivision.

## 12. Exact starting point and the finite nullhomotopy

Let $`x=\sum_{M\in\sigma}\lambda_M[M]`$ lie in a true input simplex $`\sigma\subset K`$. Its input arcs have common disjoint bands. On a chosen lift of $`B_e`$, the convex height has the form

```math
h_\lambda=b_e+c_e t_e,\qquad
c_e=\sum_{M\ni e}\lambda_M\in[0,1].
```

The constant $`b_e`$ includes the actual integer offsets of the globally normalised lifts. It is independent of the longitudinal coordinate. Outside the bands the height is constant on each chamber. The triangulation includes the band boundaries and vertices in these chambers, so their phases are among the excluded values. Consequently every regular fibre has only full parallel band arcs, and no circle components.

As $`r`$ ranges once around the phase circle, a parallel copy of $`e`$ occurs exactly when $`r\pmod1`$ belongs to the projected open interval from $`b_e`$ to $`b_e+c_e`$. Because $`0\le c_e\le1`$, there is at most one such copy at a regular phase, and the total phase measure of occurrence is exactly $`c_e`$. The endpoint phases and any extra triangulation cuts have measure zero. Thus, in the **actual** initial height family,

```math
W(h_\lambda)=\sum_{M\in\sigma}\lambda_M\chi_M.
```

Applying Theorem 1.1(f), with zero-face compatibility if any $`c_e`$ vanish, gives $`F(\lambda)=x`$. The initial identity is obtained from the actual band flow and exact fixed-graph recovery; no auxiliary homotopy from a different initial map is needed.

Now define

```math
C_K(x,t)=F\left((1-t)\sum_{M\in\sigma}\lambda_M\,\mathbf{e}_M
+t\,\mathbf{e}_{M_*}\right),
```

where equal entries in the finite input list are combined. This is continuous by §§10-11. On an input face the zero coefficients disappear from the identical fixed height family, so both the height and the flow are exactly the same on either incident simplex. At $`t=0`$ the preceding calculation gives the inclusion. At $`t=1`$ every regular fibre of the single band map is a copy of $`M_*`$ with no circles, so $`W=\chi_{M_*}`$ and $`F=[M_*]`$. Let $`Y`$ contain $`Y_0`$, $`K`$, $`M_*`$ and their faces. It is finite and carries the entire nullhomotopy.

For every finite PL input this is terminating: the model’s double-coset and rational representative enumeration produces the simultaneous representatives; finite rational band refinements give $`T`$; a finite height bound gives the finite hyperplane arrangement; finite templates identify interval components and their arc classes; each finite graph's potential is solved linearly and its threshold cells are finite. The existence of orthogeodesic representatives and small rational approximations proves termination of the initial enumeration. The procedure need not be efficient. The accompanying diagnostic is not claimed to implement this entire arbitrary-input construction.

**Passage to the full complex.** The geometric realisation of $`X`$ has the usual CW topology. Taking a one-vertex finite input connects every vertex to $`M_*`$, so it is path connected. Every continuous sphere map has compact image, contained in a finite subcomplex by Hatcher Proposition A.1. The finite nullhomotopy above nullhomotopes its inclusion, and hence that sphere map. All homotopy groups vanish. Whitehead's theorem applied to the inclusion of $`[M_*]`$ therefore makes the whole complex contractible (indeed a point subcomplex is a deformation retract). These standard inputs were checked in Hatcher, Algebraic Topology, printed p.520 / PDF p.529 and printed p.346 / PDF p.355. No claim that each finite image $`Y`$ itself is contractible is needed.

This proves Theorem 9.1, including $`X(H_8)`$ and every balanced $`X(H_{2m})`$ in the matching model. The averaging takes place first in arc coordinates; only the decoded finite barycentric combination is regarded as a point of the true cyclic complex.

## 13. Method, sources and precise scope

Hatcher’s second proof, pp.5–6, supplies bicollar circle maps, extension of map families, regular-value fibres and partition-of-unity averaging. The present construction uses equivariant real-height interpolation, monotone prescribed boundary degrees, averaging of retained arc indicators and a face-height decoder. It does not invoke Hatcher’s source/sink reduction or transfer his closed-surface contraction theorem to this fixed-boundary subcomplex.

Propp’s arXiv v3, dated 19 March 2021, §3, Theorem 2 on p.21 and the face-height description on p.22, provide background for the classical planar bipartite matching-height structure. The work is published as *Electronic Journal of Combinatorics* 32(4) (2025), #P4.26. The fixed-graph proof here is self-contained relative to the model’s PS §3 distance interface, and proves the needed rounding and zero-face compatibility without an external lattice theorem or integrality theorem. No priority claim for planar matching heights or circle-map averaging is made.

PS Theorem 1.1 already states a result covering these norm-zero Hopf complexes. The contribution is this independent family proof and explicit arbitrary-finite-input mechanism, avoiding PS §§4–7. The finite image subcomplex need not itself be contractible, and different finite-input choices need not be assembled into one prescribed global formula before the CW conclusion.

Standard topology inputs are Farb–Margalit §1.2.7, pp.35–36 (endpoint-free multiarcs); Hatcher, *Notes on Basic 3-Manifold Topology*, pp.20–22 (the vertical matching model); PS, pp.1492–1495 (open-block class minimisation); Oertel, p.712 (relative product boundaries); and Hatcher, *Algebraic Topology*, Proposition A.1, p.520, and Whitehead Theorem 4.5, p.346. Exact editions and attribution are recorded in the [bibliography](../sources/bibliography.md). Sakuma’s original theorem is retained through the declared PS interface, rather than independently re-certified.

A finite terminating rational procedure is proved in §12. It is not claimed to be implemented in full. This theorem covers all balanced Hopf fibre links. The [Seifert dichotomy](seifert.md#3-seifert-exteriors-the-full-surface-dichotomy) proves that unbalanced Hopf fibre links are fibred and have one vertex. Together these give all oriented nonempty unions of Hopf fibres. General orbifold bases, positive-genus bases, weighted surface-cycle complexes, satellite/JSJ gluing and arbitrary links remain outside this conclusion.
