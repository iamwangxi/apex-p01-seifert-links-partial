# Balanced Hopf fibre links: matching model and complete-block distances

[Overview](../README.md) · [Contraction](hopf-contraction.md) · [Four-fibre tree](hopf-four.md) · [Sources](../sources/bibliography.md)

For every $`m\ge1`$, let $`H_{2m}`$ consist of $`2m`$ fibres of the positive Hopf fibration, with $`m`$ signs of each kind. Put $`P=P_{2m}`$, an oriented sphere with labelled boundary circles $`C_1,\ldots,C_{2m}`$, where $`\epsilon_i=1`$ for $`1\le i\le m`$ and $`\epsilon_i=-1`$ otherwise. Its exterior is $`E=S^1_h\times P`$. The total oriented linking homomorphism satisfies $`\phi(\mu_i^H)=\epsilon_i`$ and $`\phi(h)=0`$; its restriction to the base is the primitive peripheral homomorphism $`\psi(c_i)=\epsilon_i`$.

An allowed system consists of $`m`$ disjoint embedded proper arcs, each joining a positive circle to a negative circle and using every labelled circle once. Endpoints may slide on their circles. The arc coorientations, equivalently the orientations of the vertical annuli, are forced by the prescribed spanning boundary. Vertices of $`X(H_{2m})`$ have all incompressible genera, no closed components, and unrestricted identity ambient isotopy respecting the labelled tori. Edges use the minimum cyclic width of the whole open complement, as in [objects](objects.md).

**Theorem 1.1 (all balanced hole numbers).** The assignment $`a\mapsto[F_a]`$, $`F_a=S^1_h\times a`$, is a bijection from allowed joint arc-isotopy classes to $`V(X(H_{2m}))`$. Valid rational PL codes have decidable equality. For normalised representatives $`a,b`$, the signed region graph inside the complete complement $`P\setminus b`$ has an integer potential $`H`$, unique up to one common constant, and


```math
\delta([F_a],[F_b])=\max H-\min H.
```


Distinct classes are adjacent exactly when this range is one; all simplices are determined by the flag completion. A transverse crossing in normal position forces range at least two, for every $`m`$. Thus every true finite simplex has simultaneous disjoint-interior normal representatives, with common arc classes represented once. The reverse implication from disjointness to adjacency is proved below only for six holes.

For $`m=1`$, $`P`$ is an annulus, its endpoint-free spanning arc has one class, and $`X(H_2)`$ is a point. The arguments involving a hyperbolic metric below are for $`m\ge2`$. The contraction for every $`m`$ is proved in [the companion proof](hopf-contraction.md), independently of PS §§4–7. The class-minimum interface here remains PS Proposition 3.2 and its stated §3/Sakuma interface.

## 2. Verticalisation of the complete system

### 2.1. Boundary slope and essentiality

In reference Hopf coordinates write the total boundary as


```math
\partial F=\sum_{i=1}^{2m}\epsilon_i(\lambda_i^H+b_i\mu_i^H).
```


Since $`[\lambda_i^H]=\sum_{j\ne i}[\mu_j^H]`$ and $`\sum_i\epsilon_i=0`$, its $`\mu_i^H`$ coefficient in $`H_1(E)`$ is $`\epsilon_i(b_i-1)`$. A spanning boundary is null-homologous, hence $`b_i=1`$ for every $`i`$. Thus the actual spanning boundary is the fibre slope $`h=\lambda_i^H+\mu_i^H`$, oriented $`\epsilon_i h`$. The individual preferred longitude must not be substituted here.

The link is non-split: a splitting sphere would give zero linking numbers across its partition, whereas all such numbers are $`\epsilon_i\epsilon_j=\pm1`$. Thus its exterior is irreducible. Its boundary tori are incompressible also directly: $`\langle h,c_i\rangle\cong\mathbb Z^2`$ injects into $`\mathbb Z\times\pi_1(P)`$, since $`c_i`$ has infinite order.

There is no disk component, since a fibre boundary is nontrivial in $`\pi_1(E)`$. Hatcher Lemma 1.11 makes every remaining incompressible component boundary-incompressible unless it is a boundary-parallel annulus. That exception would put two boundaries on the same torus, contrary to the spanning convention. We can therefore use Hatcher Proposition 1.12 with its actual **essential** hypothesis.

A horizontal component has boundary transverse to the fibres, hence nonzero intersection with the fibre slope. Our boundary slope excludes it. Every component is consequently isotopic to a vertical annulus. $`2m`$ boundaries give precisely $`m`$ annuli. An oriented annulus has opposite fibre orientations at its two ends, so each pairs a positive label with a negative one.

Source: Hatcher, *Notes on Basic 3-Manifold Topology*, Lemma 1.11 and Proposition 1.12, printed pp.20–22.

### 2.2. Simultaneous verticalisation

Verticalise one annulus. Its base arc joins two distinct boundary components, so cutting along it leaves a connected planar surface with $`2m-1`$ boundary components, and cutting the product leaves the corresponding circle product. Carry the other annuli by ambient isotopy extension.

Each remaining component is incompressible in this cut product and has fibre boundaries on two distinct **untouched** original tori. It is again essential by Lemma 1.11, and Proposition 1.12 again excludes horizontality. Use the boundary-fixed verticalisation in Hatcher's proof, printed p.22. Relative isotopy extension fixes the cut product's boundary, in particular both faces of the first annulus. The isotopy thus glues back fixing that annulus.

Repeat for all $`m`$ annuli. The successive base surfaces have $`2m,2m-1,\ldots,m`$ boundary circles. This proves simultaneous verticalisation of the whole system, not just separate verticalisability of its components. Conversely every $`F_a`$ is incompressible: each annulus core maps to the infinite-order fibre $`h`$. Its boundary and orientation are exactly those required.

Every such surface has Thurston norm zero. Hence all these representatives are norm-minimising. Conversely a reduced norm-zero spanning surface here can only have annuli: disks are excluded, and every other oriented component with nonempty boundary has negative Euler characteristic. Its essential fibre boundary makes its core nontrivial and the annulus incompressible. Thus $`X(H_{2m})`$ equals the reduced norm-minimising cyclic complex at the level of vertices, edges and flag completion. No contractibility consequence of this equality is taken.

## 3. Genuine ambient isotopy and effective vertex data

### 3.1. Relative paths and the whole system

Fix a basepoint $`x`$, paths $`u_i`$ to $`C_i`$, and based peripheral loops $`c_i`$. Then


```math
F=\pi_1(P,x)\cong F_{2m-1},\qquad K_i=\langle c_i\rangle,\qquad c_1\cdots c_{2m}=1.
```


For an arc from $`C_i`$ to $`C_j`$, close its endpoints along their boundary circles and record the based word $`w`$ of $`u_i a u_j^{-1}`$. Endpoint choices change exactly $`w\mapsto c_i^rwc_j^s`$. Its endpoint-free proper homotopy class is therefore the double coset $`K_iwK_j`$: in the universal cover, the two peripheral cosets specify the boundary lifts at its ends. An allowed system is recorded by a permutation $`\pi\in S_m`$ and


```math
\left(K_iw_iK_{m+\pi(i)}\right)_{i=1}^{m}.
```


Only data realised by disjoint embedded arcs are admissible; arbitrary free-group word tuples are not declared vertices.

For a vertical annulus choose a path between its two boundary circles and project it to $`P`$. Changing that path winds around the annulus core, whose projection is trivial. If an unrestricted ambient isotopy of $`E`$ takes $`F_a`$ to $`F_b`$, it preserves each labelled torus and the endpoint pairing. Projecting the tracks of these paths gives proper homotopies in $`P`$, with endpoint tracks on the specified circles. Thus all corresponding double cosets agree, without requiring the isotopy to remain vertical.

Conversely, individual proper arc classes determine the joint class of an embedded system. For $`m\ge2`$, choose a hyperbolic metric with totally geodesic boundary. Each proper class joining different boundary circles has a unique orthogeodesic, the common perpendicular between its specified lifts. The bigon and boundary half-bigon criterion makes simple classes embedded and disjoint classes disjoint. An embedded multiarc straightens simultaneously: remove innermost bigons and half-bigons for the entire collection and extend the arc motions by isotopy extension. Equivalently straighten its disjoint lifts between the specified boundary lifts; their compatible endpoint order is preserved. Thus two systems with the same individual classes straighten to the same canonical union, retaining boundary cyclic order. The annulus case $`m=1`$ was handled separately. A base isotopy extends by the identity on $`S^1_h`$. This proves the vertex bijection together with §2.

The endpoint-free arc and simultaneous-straightening interfaces are in Farb–Margalit, §1.2.7, printed pp.35–36. Epstein Theorem 3.1, printed p.89, provides the fixed-endpoint version; endpoint movement is handled by the boundary-circle convention just described.

### 3.2. A fully effective encoding, without an admissibility oracle

Choose once and for all a rational polygonal planar model of $`P`$: one outer polygon and $`(2m-1)`$ disjoint inner polygons, labelled by the $`2m`$ circles $`C_i`$, together with a finite triangulation and a free-group marking. A code consists of $`m`$ finite rational PL polygonal arcs, their endpoint labels, and their coorientations. Exact segment-intersection and point-in-polygon tests decide whether the code is an allowed system. Every allowed system has such a code up to isotopy, by PL approximation and a small perturbation of vertices. An arc's word is obtained by pushing to the marked one-skeleton, or by recording crossings of fixed cuts reducing $`P`$ to a disk. The triangulation and marking are fixed background data, not a mapping-class-group quotient.

Two valid codes define the same vertex exactly when their pairings agree and all $`m`$ double cosets agree. The latter is decidable by the following finite automaton construction.

For $`K_iwK_j`$, make an NFA with a left state bearing directed word loops $`c_i,c_i^{-1}`$, a directed stem spelling $`w`$ to a right state, and right loops $`c_j,c_j^{-1}`$. Add an epsilon edge for every path known to freely reduce to the empty word. Obtain all such edges by taking transitive closure and repeatedly adding


```math
p\longrightarrow_\varepsilon q
\quad\text{if}\quad
p\longrightarrow_z r\longrightarrow_\varepsilon s\longrightarrow_{z^{-1}}q.
```


There are finitely many state pairs, so saturation terminates. Every added edge has a freely trivial witness path. Conversely every freely trivial word admits nested inverse-pair cancellation, so induction on its length proves it is captured. A reduced candidate word $`v`$ is accepted by the saturated NFA exactly when some original accepted word reduces to $`v`$, i.e. exactly when $`v\in K_iwK_j`$. Testing the other representative word decides equality. This argument applies also to the final peripheral word $`c_{2m}=(c_1\cdots c_{2m-1})^{-1}`$.

If canonical data are desired, enumerate reduced words in length-lexicographic order and choose the first accepted word for each coset. There is at least one, so this also terminates. Efficiency is not asserted. The vertex domain remains valid PL codes modulo this decidable equality, so deciding whether an arbitrary unrealised word tuple admits an embedding is unnecessary. This gives a countable, effective domain for the complete model.

## 4. Representatives realising the class minimum

### 4.1. Normal position, including common components

Put any hyperbolic metric with totally geodesic boundary on $`P`$, for example by gluing hyperbolic pairs of pants. Each proper class joining distinct boundary components has a unique orthogeodesic representative. In the universal cover, it is the unique common perpendicular between the specified two boundary lifts. Simple classes give embedded representatives, and disjoint classes give disjoint representatives, by the arc bigon criterion. Thus each entire allowed system is ambient isotopic to its orthogeodesic system. Homotopic arcs of different systems now coincide; different ones are transverse in the interior and have distinct endpoints on any common boundary circle. Equality of an endpoint and perpendicular tangent would force the two whole geodesics to coincide.

Call a PL pair **normalised** if common relative arc classes coincide, all other intersections are transverse, distinct boundary endpoints are disjoint, and there is no ordinary bigon or boundary half-bigon between its component arcs. The orthogeodesic pair has these properties. A sufficiently small simultaneous PL approximation, copying each common arc once, gives a rational normalised pair.

The bigon criterion for endpoint-free arcs includes half-bigons, not merely interior bigons; see Farb–Margalit §1.2.7, printed pp.35–36. For two internally disjoint systems, innermost bigon/half-bigon removal is compatible with their internal disjointness. In a half-bigon, the relevant boundary interval has no other endpoints of either colour: each system uses that circle only once.

### 4.2. No three-dimensional product regions

**Lemma 4.1.** For the orthogeodesic pair, and for any normalised PL pair, $`F_a,F_b`$ are almost transverse and have simplified intersection as required by PS Proposition 3.2.

**Proof.** All transverse intersections are complete interior fibre circles. Common components coincide. Distinct surface boundaries are disjoint essential fibres, so they cannot bound a boundary product disk. Coincident fibre boundaries likewise cannot be the two distinct sides of such an embedded disk.

First isolate a common annulus $`A`$. It is disjoint from every other component of both systems, and those other components use neither of its boundary tori. A product with one face in $`A`$ and the other in a noncommon component has no collapsed intersection sides. Its face in $`A`$ must therefore be the whole annulus, with both face boundary circles on the two tori of $`A`$. Its other face would have to use those same tori, which is impossible. If both faces lie in $`A`$, every collapsed side gives the same boundary curve in $`A`$ on both faces. An uncollapsed side would join two boundary circles on the same ambient torus, but $`A`$ has only one actual boundary circle there: both horizontal ends would be that very same circle, impossible for an embedded uncollapsed product side. Thus all face boundary curves are collapsed and the two faces have the same boundary in $`A`$, including the same use of any original boundary circle. Compare their characteristic functions modulo two: the symmetric difference has no jump across an interior boundary curve, so is locally constant on $`A`$. It is zero near each original boundary circle, since either both faces include its inward collar or both omit it. As $`A`$ is connected, the two faces coincide, again impossible for an embedded product. This handles common components without treating their two-dimensional coincidence as a finite collection of intersection circles.

Now consider a connected product region with both faces in noncommon annuli. The boundary of either horizontal face lies on intersection fibres (collapsed sides) or on surface boundary fibres (uncollapsed sides in $`\partial E`$). Its frontier in a vertical annulus is therefore a union of complete fibre circles. A connected face is a fibre subannulus, not a disk or a higher-complexity surface. Intervals of an interior intersection circle cannot end part way around that circle: an uncollapsed end would have to enter $`\partial E`$. The same conclusion follows by viewing the face as a compact subsurface whose frontier is contained in the finite union of these disjoint circles.

A spanning section of the annular face, followed through the product, yields a homotopy of a subarc of an $`a`$-arc to a subarc of a $`b`$-arc. An end on a collapsed intersection fibre is fixed after projection to $`P`$. An uncollapsed end moves only on its prescribed $`C_i`$. There are three possibilities.

* Two fixed interior ends: the two lifted geodesic segments have the same two distinct endpoints, so coincide. For a normalised PL pair, the equivalent universal-cover argument gives a bigon if two distinct lifts meet twice; an innermost such bigon projects to a bigon downstairs.
* One interior end and one boundary end: a fixed lifted point has a unique perpendicular to the specified boundary geodesic, so the two orthogeodesic subsegments coincide. For PL arcs the same configuration is a boundary half-bigon, after taking an innermost one.
* Two boundary ends: the full arcs have the same relative homotopy class. They have already been identified as a common component. Such an annulus cannot supply two distinct horizontal faces of an embedded product region.

For the PL statements these are precisely the universal-cover cases in the arc bigon criterion; the innermost disk has no other lifts in its interior and projects embedded, as in the proof of that criterion. All cases contradict normalisation or distinctness of the two faces. Thus no product region exists. ∎

The relative condition that uncollapsed vertical boundary lies in the ambient boundary is essential here. It is explicit in Oertel, printed p.712, and in Banks Definition 4.1, preprint p.5. An arbitrary solid torus chamber bounded partly by the surfaces is not a product region in this definition.

All hypotheses of PS Proposition 3.2 now hold: the ambient manifold is orientable, irreducible and boundary-irreducible; the surfaces are oriented, incompressible and boundary-incompressible, norm-minimising, almost transverse, and have simplified intersection. Therefore


```math
\delta([F_a],[F_b])=d(F_a,F_b).
```


Source: PS journal version, printed pp.1494–1495. This remains a cited §3 result, including its stated Proposition 3.3/Sakuma interface; it is not presented as an independent reproof of Sakuma's theorem.

### 4.3. Terminating normalisation as a decision algorithm

Here is a deliberately inefficient algorithm that avoids requiring an exact numerical geodesic solver. Enumerate pairs of valid rational PL codes. Retain only pairs equivalent to the two input vertex codes by §3.2. Test that common arc classes coincide, the finite overlay is almost transverse with disjoint other boundary endpoints, and it has no bigons or half-bigons.

These are finite tests: enumerate subarcs between overlay intersections or endpoints; check whether their two-sided or boundary-three-sided union is an embedded Jordan curve bounding a disk in $`P`$. Polygon tests determine whether its disk contains a deleted hole. Common full-arc rectangles are handled by the double-coset test. A small rational approximation of the orthogeodesic pair supplies a successful code pair, so the enumeration terminates. Lemma 4.1 applies to every successful output. This is an actual algorithm, although no efficient or implemented preprocessing is claimed. Ordinary innermost-disk simplification can replace the search in implementations.

## 5. The complete-block height formula

### 5.1. The single block

Cutting $`P`$ along the $`m`$ arcs of $`b`$ merges $`m`$ disjoint pairs of boundary circles. The complete cut surface $`B_b`$ is a sphere with $`m`$ holes: it is connected, has $`m`$ boundary components, and has


```math
\chi(B_b)=\chi(P)+m=(2-2m)+m=2-m.
```


Every loop in $`P\setminus b`$ has zero intersection with $`b`$, so $`\psi`$ vanishes on its fundamental group. Hence each connected lift of $`P\setminus b`$ projects homeomorphically to that **entire** complement. There is one lift choice, up to one common deck translate. Taking its product with $`S^1_h`$ gives a complete lift of $`E\setminus F_b`$.

The oriented relative one-cycle of $`a`$ is dual to the same $`\psi`$: a small peripheral loop crosses its single incident arc with the prescribed sign, and peripheral loops generate $`H_1(P)`$. Thus the signed intersection count with $`a`$ is also zero on every loop in $`P\setminus b`$. This is the integrability used below.

### 5.2. Finite signed graph

Let $`\mathcal C(a,b)`$ be the finite set of connected regions of $`P\setminus(a\cup b)`$, with nonempty interior. Form a graph whose vertices are these regions. For every open segment of $`a\setminus b`$, subdivided at its intersections with $`b`$, join its two incident regions. Direct this edge in the positive coorientation of $`a`$ and assign step $`+1`$; reversing traversal gives $`-1`$. A common $`a=b`$ arc is on the frontier of $`B_b`$ and gives **no** graph edge. Graph edges do not cross $`b`$.

This graph is connected: a path in the complete connected complement $`P\setminus b`$, transverse to $`a`$, joins any two regions and crosses only the listed edges. Choose a root region and set $`H=0`$ there. For any path in the graph define $`H`$ by summing its signed steps. Differences between two paths are signed intersections of a loop in $`P\setminus b`$ with $`a`$, hence zero. Therefore $`H`$ is a well-defined integer potential. In particular, a nonzero-step self-loop cannot occur in a valid overlay.

If one prefers an ordinary cellulation, add finitely many auxiliary edges and triangulate the regions. Give crossings of every auxiliary edge step zero and never join across a $`b`$-edge. This yields the same range. It also handles regions which are not disks without treating their boundary cycles as separate cells.

### 5.3. Why the range is the actual minimum

Take a single connected lift $`\widetilde B_b`$. The complete $`a`$-complement blocks are indexed $`\widetilde B_{a,k}=\tau^k\widetilde B_{a,0}`$. Each lifted region lies in precisely one open $`a`$-block, and crossing a directed $`a`$-segment changes its block index by $`1`$. Thus these indices are exactly the $`H`$ values, up to one additive constant and possibly a common reversal of signs. Every region is nonempty, so every recorded index is actually attained. Conversely any open-block intersection with $`\widetilde B_b`$ contains a point avoiding both arc systems and therefore contains a point of a listed region. Frontier contact alone contributes no index.

Consequently the maximum and minimum intersected **open** block indices are $`\max H`$ and $`\min H`$. Multiplication by $`S^1_h`$ changes neither. Definition 2.1 gives $`d(F_a,F_b)=\max H-\min H`$, and Lemma 4.1/Proposition 3.2 makes this the class minimum. This proves the boxed formula.

If $`a=b`$, the graph has one vertex and no nonzero-step edge, hence width zero. Conversely a noncommon $`a`$-arc has an internal segment in $`P\setminus b`$ and yields a unit height difference. Thus width zero is equivalent to equality of the normalised whole systems; no separate appeal to distance/path-distance equality is needed.

Sources for the open-block convention and class minimisation: PS Definition 2.1, printed p.1492; class minimisation, printed p.1493. This construction uses no deletion of a closed frontier and no independent component shifts.

### 5.4. Exact distance-one certificate

For different vertex codes, normalise the pair, build this graph, and propagate heights by a spanning tree. Check the remaining edge equations. The pair is an edge exactly when the maximum minus minimum is one. Equivalently there is a surjective $`H:V(G)\to\{0,1\}`$ with


```math
H(v)-H(u)=1
```


on each positively directed $`a`$-crossing, and zero on auxiliary edges. Computing the full range also computes every pairwise class distance. Failure of graph integrability is a bad-input certificate, not a putative new distance.

## 6. A special simplification for six holes

### 6.1. A crossing obstruction valid for every hole number

**Lemma 6.1.** If a normalised pair has an interior transverse arc crossing, its whole-block width is at least two.

**Proof.** Work in a small base disk about a crossing, and its evenly covered lift. The local $`a`$-wall divides it into two consecutive open $`a`$-block indices, say $`k,k+1`$. On each side of the local $`b`$-wall both of these indices occur, in its two nonempty quadrants. The two local $`b`$-sides belong to consecutive translates of the complete $`b`$-block. To bring both sides into the chosen single $`\widetilde B_b`$, one side must be deck-translated by exactly one relative to the other. Deck translation also translates all $`a`$-block indices by one. The chosen complete $`b`$-block therefore meets indices either $`\{k-1,k,k+1\}`$ or $`\{k,k+1,k+2\}`$. Its width is at least two. This uses both sides of the same complete block, rather than choosing separate annulus lifts. ∎

Together with §4, this proves for every $`m`$ that a distance-one pair has disjoint-interior normalised representatives. One fixed metric supplies these representatives simultaneously for every finite clique. The next two subsections concern only $`m=3`$.

### 6.2. At most one alternating circle

**Lemma 6.2.** Suppose two different allowed systems on $`P`$ are in disjoint-interior normal position, with every common arc class identified. After filling the six boundary circles by labelled points and deleting isolated common edges, their union has exactly one alternating circle.

**Proof.** At any label not incident to a common arc, there are exactly two different edges, one of each colour. At the other labels, the common edge is isolated from all noncommon edges. Thus the noncommon union is a disjoint collection of embedded even alternating circles. A circle has length $`2`$, $`4`$ or $`6`$, and different circles use disjoint labels. A length-two circle consists of two arcs joining the same labelled holes. If one side contains no other labelled point, drilling the two corner points leaves an empty rectangle between the arcs. They are then the same endpoint-free arc class, excluded by normalisation.

If there is more than one circle, the only possible length lists are $`(4,2)`$, $`(2,2)`$ with one remaining common edge, or $`(2,2,2)`$. For $`(4,2)`$, the whole four-circle lies on one side of the two-circle, leaving the other side empty of labels. For $`(2,2)`$, the complement of the two disjoint circles has two disk end-regions and an annular middle region. The isolated remaining common edge, and both its labels, lie in one region. At least one disk end-region is therefore empty of other labels. In the $`(2,2,2)`$ case, the complementary-region dual graph is a tree; an end-region is a disk bounded by one two-circle, with no other label inside. Each possibility makes some two-circle an empty rectangle, a contradiction. Different systems must have a noncommon arc, so the number of circles is one, not zero. ∎

### 6.3. The converse from the whole-block calculation

The single circle separates the capped sphere into two regions. Any remaining common edges lie on one side or the other and join distinct unused holes. Cutting along such an edge merges two boundary components without disconnecting its region. Hence $`P\setminus(a\cup b)`$ has exactly two connected regions. The signed graph in §5 has two vertices and at least one unit edge. Its integrable potential consequently has two values differing by one. By the **whole-block** formula its class distance is exactly one.

We have proved


```math
\boxed{[a]\ne[b]:\quad \delta([F_a],[F_b])=1
\iff a,b\text{ have disjoint-interior representatives, common classes allowed}.}
```


This is a theorem specific to three arcs on six holes. For more arcs several nontrivial alternating circles can survive, and the potential can have more than two values. Even here, parallel pushes of coincident annulus components can give a representative width two for the same vertex; normalisation and class minimisation remain necessary. Thus this equivalence does not reinstate the general disconnected-surface inference criticised by PS.

## 7. All simplices and the six-hole tetrahedron

The effective graph on valid vertex codes modulo §3 equality has an edge exactly when the normalised whole-block range is one. Its flag completion is $`X(H_{2m})`$, determining all incidences. By §6.1 each true finite clique has simultaneous disjoint-interior representatives, but for more than six holes not every family supported in one embedded graph is a clique. Its exact induced triangulation is proved in [the contraction](hopf-contraction.md), §8.

When $`m=3`$, the converse in §6 shows that a finite set of distinct matching classes is a simplex exactly when their canonical geodesic union has no transverse crossings. This complex contains a tetrahedron. Embed $`K_{3,3}`$ minus $`(3,6)`$ with positive labels $`1,2,3`$ and negative labels $`4,5,6`$. The cyclic neighbour orders are $`1:(4,5,6)`$, $`2:(4,6,5)`$, $`3:(4,5)`$, $`4:(1,2,3)`$, $`5:(1,3,2)`$, and $`6:(1,2)`$. They give faces $`(1,4,3,5)`$, $`(1,5,2,6)`$, $`(1,6,2,4)`$ and $`(2,5,3,4)`$, and an orientable capped ribbon surface with Euler characteristic $`6-8+4=2`$, hence a sphere. Drill its six vertices. Its four matchings are


```math
\begin{aligned}
M_0&=\{(1,4),(2,6),(3,5)\},\\ 
M_1&=\{(1,5),(2,6),(3,4)\},\\ 
M_2&=\{(1,6),(2,4),(3,5)\},\\ 
M_3&=\{(1,6),(2,5),(3,4)\}.
\end{aligned}
```


Their pairings are distinct; each pair leaves one alternating four- or six-circle after common edges are removed, so every pair has complete-block width one. Flagness gives the tetrahedron. This proves only $`\dim X(H_6)\ge3`$; contractibility follows from the separate finite-input proof, and the four-fibre tree retains its stronger structural description.

## 8. Sources and scope

The verticalisation uses Hatcher, *Notes on Basic 3-Manifold Topology*, Lemma 1.11 and Proposition 1.12, pp.20–22, including the relative boundary clause on p.22. Proper arc classes and normalisation use Farb–Margalit, pp.33–36, and Epstein Theorem 3.1, p.89. Relative product regions use Oertel, p.712, and Banks Definition 4.1, preprint p.5. Open complete blocks and the class minimum use PS Definition 2.1 and Proposition 3.2, pp.1492–1495, retaining its stated Sakuma interface. Exact editions are in the [bibliography](../sources/bibliography.md).

No PS projection, order, dismantling or contractibility conclusion from §§4–7 is used, nor Proposition 2.3's reverse argument in §4. Rational representative enumeration is proved terminating; a complete software implementation or efficiency bound is not claimed. The general distance formula and matching model hold for the balanced Hopf family, without extending them to orbifold bases or arbitrary Seifert vertical systems.
