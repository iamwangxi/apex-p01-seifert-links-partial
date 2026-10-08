# Counterexamples to Lemmas 6.1, 6.5 and Theorem 7.2 of Przytycki–Schultens

[Overview](../README.md) · [Objects](objects.md) · [Sources](../sources/bibliography.md) · [Scope](scope.md)

The certificate, both class-distance verifications and the finite twelve-dimensional filling are specified in this note. The statement of PS Theorem 1.1 is not refuted.

## 1. Abstract and precise conclusions

We construct an oriented, non-split eight-component link and five minimum-Thurston-norm spanning systems. Four of their vertices, denoted by $`A,B,S,P_-`$, satisfy

```math
\pi_A(B)=P_-,\qquad
\delta(A,B)=\delta(S,P_-)=2,
\qquad
\delta(A,S)=\delta(B,S)=\delta(A,P_-)=\delta(B,P_-)=1.
```

Here $`\pi`$ is precisely the torus-deleted operation in Definition 4.1 of the **published** paper of Przytycki and Schultens [PSJ], and $`\delta`$ is their cyclic-cover distance minimized over ordinary ambient isotopy classes. The actual input representatives satisfy that definition's position requirements. The independent distance-direction statement, Lemma 5.4 of [PSJ], gives $`B<_A S`$. Consequently Lemma 6.1 is false, and the radius-one instance of the vertex conclusion of Lemma 6.5 is false.

Moreover, direct applications of Definition 4.1 give $`\pi_A(S)=\pi_A(P_-)=A`$. The induced flag subcomplex on these four vertices is therefore finite and $`A`$-convex in the published sense. It is a four-cycle, with no triangles, and its graph is not dismantlable. This is a counterexample to Theorem 7.2 of [PSJ], rather than merely a defect in that theorem's proposed dismantling order.

Theorem 1.1 of [PSJ], which asserts contractibility of the **whole** complex, is not disproved. Its published proof through Theorem 7.2 does not establish the generality allowing disconnected minimum-norm spanning systems. In fact, the four-cycle in this example is contained in an explicitly specified finite contractible subcomplex with realization homeomorphic to $`[0,1]^{12}`$. No conclusion about noncontractibility of the whole complex follows. This counterexample does not affect the knot case.

The example concerns the unweighted, prescribed-boundary setting of [PSJ]. The weighted, free-boundary complexes introduced in [SchS] and used in [SchF] are different objects. We discuss those texts in §8 without asserting a two-dimensional counterexample or a general repair in the weighted setting.

## 2. Setting, distance and the published projection

### 2.1. The complex being tested

In [PSJ, pp.1489–1490], the ambient manifold is compact, connected, oriented, irreducible and boundary-irreducible. A prescribed union $`\gamma`$ of oriented curves does not separate any boundary component, and $`\alpha\in H_2(E,\partial E;\mathbb Z)`$ satisfies $`\partial\alpha=[\gamma]`$. The map from absolute to relative second homology is assumed to be zero. A spanning surface is unweighted, has **no torus components**, represents $`\alpha`$, and has boundary homotopic to $`\gamma`$. The vertices of $`MS(E,\gamma,\alpha)`$ are its minimum-Thurston-norm isotopy classes. Isotopy allows the boundary curves to move in their prescribed homotopy classes; it is not isotopy relative to fixed boundary points.

For our link $`L`$, take $`E=E(L)`$, and let

```math
\phi_L:\pi_1(E)\longrightarrow\mathbb Z,
\qquad \phi_L(\mu_i)=1,
```

where the meridians carry the orientations of the link components. The class $`\alpha`$ is dual to $`\phi_L`$. The curve on each boundary torus is the spanning longitude of the **whole oriented link**. It need not be the preferred longitude of that component considered as an isolated knot. On the ungrafted Hopf exterior these curves are regular-fibre slopes with the inherited signs.

All systems used below have one boundary curve on each labelled torus and no closed components at all. Their complements are connected. One way to see the latter is to consider the chamber graph of a cut system: the complement of the single essential boundary curve in a boundary torus connects the two normal sides of its incident surface component. Every component has boundary, so every edge in the chamber graph is a loop. Connectedness of the exterior leaves just one chamber.

Let $`p:\widetilde E\to E`$ be the cover associated with $`\ker\phi_L`$, and let $`\tau`$ denote its positive deck generator. For a specified surface $`F`$, use a connected lift $`E^F`$ of its **entire** complement. Its translates exhaust the lifted complement. For two specified representatives define

```math
D(F,G)=\max I(F,G)-\min I(F,G),\qquad
I(F,G)=\{i:\tau^i E^F\cap E^G\ne\varnothing\},
```

and define $`\delta([F],[G])`$ by minimizing over their ambient isotopy classes. Thus $`D`$ is a representative width and $`\delta`$ is a class distance. An edge means class distance one. The complex is flag. These are [PSJ, Definition 2.1, pp.1492–1493].

We use the cyclic-distance triangle inequality, not a general identification with the graph metric. For example, if a complete $`G`$ domain meets $`F`$ domains in an interval $`[a,b]`$, and a complete $`H`$ domain meets translates of that $`G`$ domain in $`[c,d]`$, its $`F`$ indices lie in $`[a+c,b+d]`$. This proves the width inequality. Aligning the middle representative by ambient isotopy proves the class-distance inequality. Proposition 2.2 of [PSJ] also supplies this metric fact. We do not use Proposition 2.3's reverse graph-distance inequality, whose proof invokes §4.

### 2.2. Position and order

The meanings of almost transverse, almost disjoint and simplified intersection are those of [PSJ, p.1494]. Coincident whole components are allowed. Simplified intersection excludes the product regions specified there, including boundary product regions. Crucially,

```math
F,G\text{ almost transverse with simplified intersection}
\quad\Longrightarrow\quad
D(F,G)=\delta([F],[G])
```

for minimum-norm surfaces, by Proposition 3.2 [PSJ, pp.1494–1495]. This result precedes the projection construction and does not use its observer properties.

For adjacent vertices, the relation $`<_\sigma`$ is the geometric relation of [PSJ, Definition 5.1, p.1497]. It is not an arbitrary total order. Equality is included in $`\le_\sigma`$, and distinct nonadjacent vertices are not comparable by this relation. We will use the following direction rule from Lemma 5.4 [PSJ, p.1498]: an adjacent vertex farther from $`\sigma`$ is below the nearer vertex. This rule uses complete domains and §3, not a projection.

### 2.3. The projection and the version distinction

For base representative $`F\in\sigma`$ and input representative $`G\in\rho`$, Definition 4.1 requires distinct minimum-norm vertices and an almost-transverse pair with simplified intersection and almost-disjoint boundaries. Choose $`E^G`$, let $`r`$ be its largest $`F`$ overlap index, and put

```math
X=\overline{E^G}\setminus E_r^F,
\qquad
Y=\tau(\overline{E^G})\cup\overline{E_r^F},
\qquad
\widetilde P^*=\partial X\cap\partial Y.
```

The closures matter: the first subtraction is a **closed** $`G`$ domain minus an **open** $`F`$ domain. Boundaries and closures are relative to the cover, including its ambient boundary. The published definition then removes the torus components of $`\widetilde P^*`$ and defines $`\pi_\sigma(\rho)`$ to be the isotopy class of its projected proper remainder [PSJ, pp.1495–1496]. The formula, its bars, and the torus-removal sentence have been checked on the PDF.

The locally available arXiv v2 has a broader preliminary spanning-surface definition and no torus-removal step in Definition 4.1 [PSV, p.2; p.10]. We test the **published** operation, not an operation retaining the closed torus allowed by that preprint's wording.

## 3. The link, qualifying representatives and nine distances

### 3.1. A marked Hopf exterior

Let $`H_8`$ be eight regular fibres of the positive Hopf fibration, four positively and four negatively oriented, with labels

```math
1+,\ 1-,\ 2+,\ 2-,\ 3+,\ 3-,\ 4+,\ 4-.
```

Its exterior is $`E(H_8)=S^1\times F_0`$, where $`F_0`$ is an eight-holed sphere. We specify a cut-open model so that the surfaces and all sheet calculations are reproducible.

Let $`\Sigma`$ be $`[0,48]\times[0,40]`$ with the interiors of the rectangles

```math
[36,40]\times[18,22],\qquad
[18,22]\times[18,22],\qquad
[18,22]\times[3,7]
```

removed. Call its outer boundary $`B_1`$ and these inner boundaries $`B_2,B_3,B_4`$. On $`B_1`$ the minus face is the left interval from height 16 to height 24, and the plus face is the complementary outer path from height 32 around the other three sides to height 8. On each inner boundary the minus and plus faces are the middle unit intervals of its bottom and top sides. Pair each minus face with its plus face by an orientation-reversing boundary identification. The result is $`F_0`$. The two remaining intervals on $`B_j`$ become its two labelled link-boundary circles $`j+,j-`$. Let $`s=s_1\sqcup\cdots\sqcup s_4`$ be the four identified seams. Cutting $`S_0=S^1\times s`$ gives $`S^1\times\Sigma`$.

For $`Q(x_0,x_1;y_0,y_1)=[x_0,x_1]\times[y_0,y_1]`$, define

```math
\begin{aligned}
M_A={}&Q(0,4;14,28)\cup Q(4,39;26,28)
 \cup Q(37,39;22,27)\cup Q(33,44;15,27),\\ 
M_B={}&Q(0,6;12,27)\cup Q(6,38;12,14)
 \cup Q(35,38;13,20)\cup Q(34,43;17,25),\\ 
U_2={}&Q(37,39;22,24),\qquad
L_3=Q(19,21;16,18),\qquad L_4=Q(19,21;1,3),\\ 
V_A={}&\mathrm{cl}_{\Sigma}
 \bigl(((M_A\setminus U_2)\cup L_3\cup L_4)\cap\Sigma\bigr),\\ 
V_B={}&\mathrm{cl}_{\Sigma}
 \bigl(((M_B\setminus U_2)\cup L_3\cup L_4)\cap\Sigma\bigr).
\end{aligned}
```

Here closure is taken after removing the hole interiors. The noncommon proper frontier arcs are

```math
\begin{aligned}
a_1={}&(0,14),(4,14),(4,26),(33,26),(33,15),
 (44,15),(44,27),(39,27),(39,28),(0,28),\\ 
b_1={}&(0,12),(38,12),(38,17),(43,17),(43,25),
 (34,25),(34,17),(35,17),(35,14),(6,14),(6,27),(0,27).
\end{aligned}
```

Successive points specify polygonal segments. The three common proper arcs are

```math
\begin{aligned}
p_2={}&(37,22),(37,24),(39,24),(39,22),\\ 
p_3={}&(19,18),(19,16),(21,16),(21,18),\\ 
p_4={}&(19,3),(19,1),(21,1),(21,3).
\end{aligned}
```

Write $`a=a_1\sqcup p_2\sqcup p_3\sqcup p_4`$ and similarly $`b`$. Each component joins the appropriate positive and negative boundary circles. Give the vertical annuli the coorientations for which $`V_A,V_B`$ belong to their lower regions. The initial systems are $`A_0=S^1\times a`$ and $`B_0^{\mathrm{surf}}=S^1\times b`$; the superscript distinguishes this surface from the base path used in §6.

Set $`W=V_A\cap V_B`$ and $`U=V_A\cup V_B`$. The proper intersection and union frontier systems have first arcs

```math
\begin{aligned}
p_1={}&(0,14),(4,14),(4,26),(6,26),(6,27),(0,27),\\ 
q_1={}&(0,12),(38,12),(38,15),(44,15),
 (44,27),(39,27),(39,28),(0,28),
\end{aligned}
```

and the same $`p_2,p_3,p_4`$. Write these systems as $`p,q`$. Their closed frontier components are $`c_2,c_3`$, respectively, where

```math
\begin{aligned}
c_2={}&(34,17),(35,17),(35,15),(38,15),
 (38,17),(43,17),(43,25),(34,25),\\ 
c_3={}&(6,14),(6,26),(33,26),(33,15),(35,15),(35,14).
\end{aligned}
```

The first encloses $`B_2`$, and the second encloses $`B_3`$. Close the polygonal paths at their final points. Let $`D_2,D_3`$ be the corresponding inside regions in $`\Sigma`$, excluding the hole interiors, and let $`C_j=S^1\times c_j`$.

The disjoint disks

```math
Q(0,4;14,27)\cup Q(4,6;26,27),\quad U_2,\quad L_3,\quad L_4
```

give simultaneous oriented product isotopies from $`p`$ to $`s`$. Thus the proper intersection output has base vertex $`s`$. The union output has base vertex $`q`$, which is different. The base distances needed below are

```math
\delta(s,a)=\delta(s,b)=\delta(s,q)
=\delta(q,a)=\delta(q,b)=1,
\qquad \delta(a,b)=2.
```

For distinctness, the first-annulus differences $`a_1-p_1`$ and $`b_1-p_1`$, closed by endpoint-torus intervals, wind around boundary pair 2. The differences $`q_1-a_1`$ and $`q_1-b_1`$ wind around pair 3, and $`q_1-p_1`$ around both pairs. These give nonzero sums of boundary-torus classes modulo the two endpoint tori. Boundary motion changes only the endpoint-torus terms. The widths are computed in §§3.5 and 3.8; the product-region check for $`a,b`$ is the ungrafted version of §3.4. In particular the path $`a-s-b`$ has no diagonal edge.

### 3.2. The local knot and grafting

Use the twisted Whitehead double of the trefoil called $`K_\alpha`$ in [BL, Theorem 2.3, Figure 1, p.3]. The subscript here is Banks's knot name. That paper constructs genus-one Seifert surfaces $`R,R_0`$ which can be made disjoint and are not ambient isotopic [BL, pp.3–4]. The distinction is certified by the companion torus: $`R`$ avoids it, whereas $`R_0`$ cannot be isotoped to avoid it. Let $`r=[R]`$ and $`r_0=[R_0]`$. These distinct knot vertices are adjacent, and their rooted order is $`r_0<_r r`$.

Tie this knot into each of the eight labelled Hopf components in disjoint balls, in the displayed order of §3.1. For a negative label reverse both the local surface orientation and its meridional convention, so that its positive local deck transformation agrees with the global one. Choose a small common trivial boundary-arc ball for the pair $`R,R_0`$, away from the detecting companion torus. The inserted pieces have identical single-arc traces on the decomposing annulus.

Call the resulting link $`L`$. For $`S`$ use $`R`$ at all eight insertions, starting with the base system $`s`$. For $`A,B`$ use $`R_0`$ at every insertion, starting with $`a,b`$. At the noncommon endpoint component take appropriately nested parallel copies of $`R_0`$; on the other three components keep the endpoint copies coincident. Intersection and union select one such copy at each insertion, without a new seam or a closed local frontier. Denote the resulting proper frontier systems by $`P_-,P_+`$. Their base systems are $`p,q`$ and their local knot pieces are all $`R_0`$.

These are actual simultaneous assemblies of embedded surfaces. They are not independently selected points in a putative coordinate product. Each final system consists of four genus-two components with two boundary curves each.

### 3.3. Non-splitness, non-fibredness and minimal norm

Every two Hopf components have oriented linking number $`\pm1`$. A splitting sphere would force the linking numbers across its nonempty partition to vanish. Local knot insertion preserves these numbers. Thus the base, every intermediate link and $`L`$ are non-split; their exteriors meet the irreducibility and boundary-irreducibility assumptions of [PSJ]. In a link exterior, absolute second homology is generated by the boundary tori with the sole total-boundary relation, and its map to relative second homology is zero. Our one primitive curve on each torus does not separate that torus.

The base is not fibred in the spanning class. Indeed

```math
\pi_1(E(H_8))=\mathbb Z\langle f\rangle\times F_7,
\qquad \phi_L(f)=4-4=0.
```

The restriction to $`F_7`$ is onto. With a basis $`x,y_1,\ldots,y_6`$ having values 1 and 0, its kernel has free basis

```math
\{x^n y_i x^{-n}:n\in\mathbb Z,\ 1\le i\le6\}.
```

It is not finitely generated. A fibration in this primitive class would have a compact connected fibre, whose group is finitely generated. At each insertion the group is a meridional amalgam. Sending a local knot-group element $`g`$ to $`\mu^{\phi_K(g)}`$ and fixing the old group is a retraction respecting the spanning class. Every intermediate kernel therefore surjects onto the base kernel and remains non-finitely generated.

The local knot is also non-fibred. For completeness, a fibred knot's fibre has no distinct disjoint incompressible spanning neighbour. Cut along the fibre to obtain a surface product. Straighten a disjoint spanning surface's single boundary curve in the vertical annulus, and cut the product by vertical rectangles from a disk-cutting arc system of the fibre. Incompressibility removes circular traces; each rectangle has one spanning trace. The remaining surface in the ball is the horizontal disk, so gluing back makes it parallel to the fibre. The geometric-disjointness incompressible complex is connected by [K92, Theorem A, p.226]. Hence a fibred knot has just that vertex. Banks's two distinct vertices exclude fibredness. This uses neither PS contractibility nor a cyclic/graph metric identification.

We also need minimal norm, not just incompressibility. After $`t`$ insertions any spanning system with maximum Euler characteristic can be put into single-arc position at the $`t`$ decomposing annuli. To justify this normal form, a loop on a spanning system has $`\phi=0`$, whereas an essential circle in a decomposing annulus is a meridian with $`\phi=\pm1`$. Inessential circles are removed by incompressibility and irreducibility. The normalized boundary trace leaves one spanning arc on each annulus. This is the cutting argument used in [BC, §7 and §10].

Cutting gives a base spanning system and $`t`$ single-boundary knot surfaces. Each cut part retains original boundary: a part incident to a cut arc contains a nonempty original boundary interval, and other parts already had boundary. The base has $`\chi\le0`$. A connected base part with just one Hopf boundary would contradict a nonzero linking number with the remaining components; a part with at least two boundaries has nonpositive characteristic. Each knot part has $`\chi\le-1`$. Gluing $`t`$ arcs subtracts $`t`$, so

```math
\chi\le -2t.
```

All five specified systems attain equality. At $`t=8`$ they have characteristic $`-16`$ and norm 16. There are no disk spanning components, by nonzero linking numbers (and by nontriviality of the final component knots). Thus their Euler-characteristic maximality gives Thurston-norm minimality. A competitor in the broader PS convention can first have its closed components removed: the absolute-to-relative map is zero and removal cannot increase norm. It cannot beat the same bound.

Compression of a boundary-bearing component would improve the maximum characteristic after retaining its boundary-bearing descendants. Hence these systems are incompressible. Boundary-incompressibility follows from [H3, Lemma 1.11, p.20]: its only exception is a boundary-parallel annulus with two curves on the same ambient torus, which our one-curve-per-torus condition excludes. These arguments apply at every insertion stage.

### 3.4. Qualification of the actual projection inputs

The actual $`A,B`$ meet in three noncommon fibre circles, over

```math
x_1=(6,26),\qquad x_2=(35,15),\qquad x_3=(38,15).
```

Their orders on the first components are $`x_1,x_2,x_3`$ and $`x_3,x_2,x_1`$. These circles are transverse and essential; the other three whole components coincide. The grafts add no intersections. Their boundary curves are disjoint or coincident. Thus they are almost transverse with almost-disjoint boundaries.

Here is the product-region check needed for simplified intersection. A transverse seam cannot run through the interior of a horizontal product end: the other surface would then enter the product's interior. An end on a noncommon component must therefore use an entire cut patch. The possible ends are its two interior annular patches and its two terminal patches, the latter acquiring the local genus-one pieces.

| Possible product ends | Exclusion |
|---|---|
| Matching interior annular patches | Their doubled boundaries are $`C_2,C_3`$. In the final exterior, $`[C_j]=\pm([T_{j+}]+[T_{j-}])\ne0`$ for $`j=2,3`$. A complete boundary of such an interior product would have zero absolute class. |
| Matching terminal patches at a seam | The reversed seam order places their original boundaries on different labelled tori. The corresponding vertical boundary cannot lie in a single ambient boundary component. |
| A terminal patch and an interior annulus | Their topology and boundary patterns differ. |
| Distinct labelled whole components | Their boundary-torus labels differ. |

Coincident whole components are retained. A product using two different pieces of one such component would have to match original boundary curves on the same labelled torus; there is only one such curve. If every side were collapsed instead, its double would be a closed whole component, which is absent. Parallel essential boundary curves have no boundary bigon; coincident primitive curves do not bound a boundary disk. This also excludes the boundary products of [PSJ, p.1494].

The classes of $`C_2,C_3`$ remain nonzero after grafting: the insertion balls avoid them and their enclosed boundary labels do not change. In particular one cannot compress them away in an irreducible exterior: compression of such a torus would give a sphere homologous to it, contradicting its nonzero absolute class.

Thus the **specified** representatives $`A,B`$ meet every input condition of Definition 4.1. This verification was not inferred from their eventual class distance.

### 3.5. The closed-region expansion and the actual projection value

In the $`S`$-cut exterior, use the common lower tail and the closed binary regions at its top to define complete lower regions $`H_A,H_B`$. The local region labelling exists as follows. The $`R`$-cut knot block is connected, and every loop in it has algebraic intersection zero with $`R_0`$, since both surfaces represent the same meridional class. The connected two-sided $`R_0`$ separates this block. Its boundary is a core in the cut boundary annulus, with the entire lower and upper $`R`$ faces on opposite sides. Label these sides 1 and 0. The decomposing annulus cut by $`R`$ is a disk, and its $`R_0`$ trace has exactly the matching binary base trace. Glue the labelled blocks along all eight disks.

The resulting lower regions have entire frontiers $`A,B`$ and satisfy

```math
H_S\subset H_A,H_B\subset\tau H_S.
```

Their one-period strips project to the whole connected complements. No independent componentwise deck translations have been made. Write

```math
E_i^A=\mathrm{int}(\tau^{i+1}H_A\setminus\tau^iH_A),
\qquad
E^B=\mathrm{int}(\tau H_B\setminus H_B).
```

In the base open cells the $`A`$ indices on $`E^B`$ are $`\mathbf1_{V_B}-\mathbf1_{V_A}`$, with all three values $`-1,0,1`$. The local parallel endpoint pieces add no larger index. Thus $`m=-1`$ and $`r=1`$.

Substituting these **complete** domains in Definition 4.1, and retaining its closures, gives this period-interior table. The circle factor and the attached local blocks are implicit.

| $`S`$ period | $`\mathrm{int}X`$ | $`\mathrm{int}Y`$ |
|---|---|---|
| 0 | $`\Sigma\setminus V_B`$ | empty |
| 1 | $`W`$ | $`\Sigma\setminus W`$ |
| 2 | empty | $`U`$ |
| Other periods | empty | empty |

Across each 0/1 or 1/2 glued face the two sides of each region have matching labels, so there is no extra $`S`$ wall. A common input component is counted once because of the closed domains. At each transverse seam the quadrant calculation gives the oriented intersection smoothing. It follows that

```math
\widetilde P^*=\tau\,\mathrm{fr}(H_A\cap H_B),
\qquad p(\widetilde P^*)=P_-\sqcup C_2.
```

The same calculation extends over each graft disk, where the two local $`R_0`$ copies are nested. There is exactly this one closed torus. The published removal step leaves precisely $`P_-`$. Consequently

```math
\pi_A(B)=[P_-].
```

The proper union frontier is $`P_+`$, with raw union $`P_+\sqcup C_3`$. It is an additional tested output, **not** another value assigned to $`\pi_A(B)`$ by Definition 4.1.

### 3.6. Complete heights and normalized Banks coordinates

After removing the closed frontiers the open-cell heights are

```math
\begin{aligned}
h_A&=1-\mathbf1_{V_A},&h_B&=1-\mathbf1_{V_B},\\ 
h_-&=1-\mathbf1_W+\mathbf1_{D_2},&
h_+&=1-\mathbf1_U-\mathbf1_{D_3}.
\end{aligned}
```

The last terms cancel the jumps of the deleted closed walls. The single integer potential and complete domains are

```math
n_F(k,x)=k+h_F(x)-1,
\qquad E^F=\{n_F=0\}.
```

The upper-face height is always the lower-face height plus one; this makes the potential well-defined across the period identifications. Its zero set contains exactly one point of each orbit off the proper surface and maps homeomorphically onto the entire connected complement. The local binary regions extend the same potential.

| System | Lower-face heights $`a_j(F)`$ | Upper-face heights | $`S`$ period indices of its complete domain |
|---|---|---|---|
| $`A,B`$ | $`(0,0,0,0)`$ | $`(1,1,1,1)`$ | $`\{0,1\}`$ |
| $`P_-`$ | $`(0,1,0,0)`$ | $`(1,2,1,1)`$ | $`\{-1,0,1\}`$ |
| $`P_+`$ | $`(0,0,-1,0)`$ | $`(1,1,0,1)`$ | $`\{0,1,2\}`$ |

The base output $`p`$ is isotopic to $`s`$, but its **relative-boundary** motion must be retained when computing the connecting-rectangle winding. Banks's coordinates record local classes and integer winding after choosing the relative sections of Proposition 6.4, not independent lifts of surface components [BC, pp.13–15].

Let $`L_t`$ be the link after $`t`$ insertions, and $`S_t,F_t`$ the corresponding prefix assemblies. At every stage use the rooted basepoint $`S_t`$. Simplify any still-ungrafted output annuli parallel to $`S_t`$ by the four disjoint product disks of §3.1. Transport the whole domain without an additional common deck shift. Denote its largest $`S_t`$ index by $`r_F(t)`$. The result is

| $`t`$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $`r_A(t)=r_B(t)`$ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| $`r_-(t)`$ | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| $`r_+(t)`$ | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 |

Geometrically a local $`R_0`$ insertion at block $`j`$ contributes the two nonempty sheets $`\{-a_j,1-a_j\}`$. The minus system first retains a two-sided chamber at insertion $`1+`$ and first retains sheet $`-1`$ at $`2+`$. The plus system already has a nonparallel base first arc, and first acquires sheet 2 at $`3+`$. Collapsing the other, still-parallel annuli creates no further sheet. The ordered product relation of Banks §9 must not be substituted for these prefix rooted geometric orders.

At insertion $`i`$ in block $`j`$, normalization of the preceding factor shifts its domain by $`-r_F(i-1)`$. Its selected complete upper wall at the joining boundary is then at period

```math
\ell_i=1-a_j(F)-r_F(i-1).
```

The local $`R_0`$ domain originally meets sheets 0 and 1; its own Banks normalization shifts by $`-1`$, putting its selected upper wall at period 0. The original compatible connecting rectangle is flat. To read its winding explicitly, use a positive real lifted meridional coordinate with reference upper boundary at 1. If the common original fractional phase is $`\eta\in(0,1)`$, the two normalized boundary phases are $`\ell_i+\eta`$ and $`\eta`$. Moving them to the reference curves gives displacements $`1-\ell_i-\eta`$ and $`1-\eta`$. In the positive convention of Banks Definition 7.1, the rectangle acquires the difference of these displacements. Hence

```math
n_i(F)=(1-\eta)-(1-\ell_i-\eta)
=1-a_j(F)-r_F(i-1).
```

This also fixes the sign. The endpoints have zero winding. At the first minus insertion the preceding base is $`s`$, so the pocket's move to the lower $`s_1`$ face contributes one positive turn; the first integer is 1. At $`2+`$ the lower-face offset is 1, giving $`-1`$. Orientation conventions at negative labels were fixed in §3.2 and introduce no further sign change. The observer uses its reference sections and zero winding throughout. This is a geometric section calculation, rather than an inference from an arithmetic table.

Banks's injectivity result makes these records invariant under unrestricted ambient isotopy. All preceding factors and all local factors are non-fibred, as checked above, so there is no integer absorption. With the recursive notation $`(v_0;(v_1,n_1),\ldots,(v_8,n_8))`$ we obtain

| Vertex | Base vertex | Eight local vertices | Eight integers |
|---|---|---|---|
| $`S`$ | $`s`$ | all $`r`$ | $`(0,0,0,0,0,0,0,0)`$ |
| $`A`$ | $`a`$ | all $`r_0`$ | $`(0,0,0,0,0,0,0,0)`$ |
| $`B`$ | $`b`$ | all $`r_0`$ | $`(0,0,0,0,0,0,0,0)`$ |
| $`P_-`$ | $`s`$ | all $`r_0`$ | $`(1,0,-1,-1,0,0,0,0)`$ |
| $`P_+`$ | $`q`$ | all $`r_0`$ | $`(0,0,0,0,1,0,-1,-1)`$ |

### 3.7. First distance verification: Banks's necessary and sufficient edge rule

For two distinct triples $`(u,k_u,n_u)`$ and $`(v,k_v,n_v)`$, interchange them if needed so that the local vertices satisfy $`k_u\le k_v`$. Corollary 8.2 and Proposition 8.3 of [BC, pp.16–17] give the exact edge condition

```math
(u\le v\text{ and }n_u=n_v)
\quad\text{or}\quad
(v\le u\text{ and }n_u=n_v+1).
```

The preceding-factor comparison is its rooted geometric adjacent-or-equal relation. When the local vertices are equal, **both** choices of their order must be tested. The sign has been checked against the original PDF.

The prefix directions needed here are as follows. The endpoints are below $`S_t`$ at every stage. The minus prefix equals $`S_0`$ at stage 0; at stages 1 and 2 it is below $`S_t`$ and below both endpoints. The plus prefix is below $`S_t`$ through stage 4, and both endpoints are below it during those stages. After its critical insertion, each output is below the distance-one endpoints on their edges, by the independent distance-direction rule.

For the equal-distance comparisons, use the complete-domain indices, not an assumed product ordering. The endpoint indices on the minus domain are $`\{-1,0\}`$ and on the plus domain $`\{0,1\}`$. Combine them with the whole-domain shifts in the table of $`r_F(t)`$. The selected minus lift still meets the endpoints' rightmost rooted block, giving $`P_-<_S A,B`$ before its critical insertion. The selected plus lift must instead be shifted down once when compared to an endpoint and then misses that rightmost block, giving $`A,B<_S P_+`$. The base equality at stage 0 is treated separately. These are the lift tests in [BC, Definition 5.1, pp. 7–8].

There are two decisive class nonedges:

| Insertion | Preceding and local orders | New integers, output versus observer | Failure of the edge rule |
|---|---|---|---|
| Third, $`2+`$, for $`P_-`$ | $`P_{-,2}<_ {S_2}S_2`$, $`r_0<_r r`$ | $`-1,0`$ | They are unequal, and the second alternative requires both a reversed preceding order and $`-1=1`$. |
| Fifth, $`3+`$, for $`P_+`$ | $`P_{+,4}<_ {S_4}S_4`$, $`r_0<_r r`$ | $`1,0`$ | The equal-integer alternative fails; the other requires the false reversed preceding order. |

Proposition 8.3 makes each later factor projection preserve equality or adjacency. Thus neither nonedge can disappear in subsequent assemblies. The final observer and either output also have different local vertex records. Their final distances are at least two, for **all** representatives.

All remaining required edges can be checked stage by stage. For $`S,A`$ and $`S,B`$, both new integers are zero, the preceding endpoint is below the observer, and $`r_0\le r`$, so the first alternative applies at every insertion. For $`P_-,A/B`$, the first insertion uses $`1=0+1`$ with equal local vertices and the reversed allowed comparison; the second has equal integers; the third and fourth use $`0=(-1)+1`$; the remaining four have equal integers. For $`P_+,A/B`$, integers agree for the first four insertions, the fifth uses $`1=0+1`$, the sixth agrees, and the seventh and eighth use $`0=(-1)+1`$. The prefix directions just established are exactly those required in these cases.

The base $`a,b`$ are nonadjacent; Proposition 8.3 prevents final $`A,B`$ from becoming adjacent or equal. Their two edges through $`S`$ bound their cyclic distance by two. The output-observer pairs have two edges through $`A`$, bounding their cyclic distances by two as well. The triangle inequality of §2.1 is sufficient. The final nine values are therefore

| Class pair | $`\delta`$ |
|---|---:|
| $`S,A`$ | 1 |
| $`S,B`$ | 1 |
| $`A,B`$ | 2 |
| $`P_-,S`$ | 2 |
| $`P_+,S`$ | 2 |
| $`P_-,A`$ | 1 |
| $`P_-,B`$ | 1 |
| $`P_+,A`$ | 1 |
| $`P_+,B`$ | 1 |

The necessary edge rule and the ordinary-isotopy vertex bijection are what make the lower bounds class-level statements. A raw lift meeting three periods would not by itself do so.

### 3.8. Second distance verification: nonparallelism and full domains

This verification does **not** use the eight winding integers or Banks's edge inequalities. It does use the first, factor-class invariance part of Banks Lemma 7.3, as a topological nonparallelism test. The two verifications are independent of the coordinate arithmetic, rather than having disjoint sets of foundational inputs.

Suppose a matching component of $`S`$ and an output were parallel. Its product region misses the other components of $`S`$: an incompressible component entering that product while missing both ends would be parallel to an end by [BC, Proposition 4.7], contrary to its different boundary labels. A product isotopy could therefore replace just that component of $`S`$, keeping its other components fixed. Both complete systems are in single-arc normal form. The first part of Banks Lemma 7.3 [BC] says an unrestricted ambient isotopy preserves each cut factor vertex. At a graft on the replaced component it would change $`r`$ to $`r_0`$, a contradiction. Thus every matching component of $`S`$ and $`A,B,P_-,P_+`$ is nonparallel.

For an endpoint and a proper output, push the first output component slightly into the intersection or union side, and retain the three common whole components. A product between their first components would likewise change the base factor from $`a`$ or $`b`$ to $`s`$ or $`q`$. Those distinct base classes were certified in §3.1. Different boundary labels exclude other products. Hence these endpoint-output representatives are almost disjoint and simplified. The actual endpoint pair is simplified by §3.4.

The complete-domain calculation now applies Proposition 3.2 directly to all nine pairs. The exact index sets, with a suitable single common normalization for each pair, are

| Target domain | Source domains met | Index set | Width |
|---|---|---|---:|
| $`E^A,E^B`$ | $`S`$ domains | $`\{0,1\}`$ | 1 |
| $`E^B`$ | $`A`$ domains | $`\{-1,0,1\}`$ | 2 |
| $`E^{P_-}`$ | $`S`$ domains | $`\{-1,0,1\}`$ | 2 |
| $`E^{P_+}`$ | $`S`$ domains | $`\{0,1,2\}`$ | 2 |
| $`E^{P_-}`$ | $`A`$ or $`B`$ domains | $`\{-1,0\}`$ | 1 |
| $`E^{P_+}`$ | $`A`$ or $`B`$ domains | $`\{0,1\}`$ | 1 |

On the base cells these sets are just differences of the height functions. The parallel local endpoint/output pieces add only the already displayed neighbouring indices. Against the observer, the two local $`R_0`$ sides retain $`\{-a_j,1-a_j\}`$ at each graft. Their unions supply the third sheet for either output; no local block supplies a fourth. All displayed extreme indices have nonempty open witnesses. Small rounding into the chosen side adds only an already allowed adjacent index. Common components remain coincident.

Nonparallelism and simplified position turn these representative widths into the nine class distances by [PSJ, Proposition 3.2]. In particular this method separately proves $`\delta(S,P_\pm)=2`$ without trusting the relative-boundary winding calculation.

## 4. How the three published statements fail

Throughout this section the surface symbols also denote their vertices when no representative is needed.

### 4.1. Lemma 6.1

Set $`\sigma=A`$, $`\rho=B`$ and $`\rho'=S`$ in [PSJ, Lemma 6.1, p.1499]. Its assumptions hold separately: all three are minimum-norm vertices; $`B\ne A`$; $`B,S`$ are adjacent; and $`\delta(A,B)=2>1=\delta(A,S)`$. By **Lemma 5.4**, independent of the projection, the direction is $`B<_A S`$, as required, rather than its reverse.

The prescribed output is $`\pi_A(B)=P_-`$. The conclusion would make $`S\le_A P_-`$, in particular equal or adjacent. But $`\delta(S,P_-)=2`$. Both the ordered conclusion and the equal-or-adjacent conclusion fail.

### 4.2. The radius-one vertex conclusion of Lemma 6.5

Set $`\sigma=A`$, $`\rho=B`$, $`\sigma'=S`$ and radius $`d=1`$ in [PSJ, Lemma 6.5, p.1501]. The vertices are legal, $`A\ne B`$, and both assumed observer distances are one. The actual representatives $`S,A,B`$ can be used pairwise in the stated position: the endpoint pair was checked in §3.4, and the disjoint observer pairs are nonparallel and simplified by §3.8. The conclusion $`\delta(S,\pi_A(B))\le1`$ is false. This refutes the **vertex statement**, not only the domain choice in its proof.

### 4.3. Theorem 7.2

Let $`C`$ be the induced flag subcomplex on $`\{A,B,S,P_-\}`$. We check its $`A`$-convexity directly rather than using an unexamined general projection property.

The complete lower regions satisfy

```math
H_S\subset H_A\subset\tau H_S\subset\tau H_A,
\qquad
H_-\subset H_A\subset\tau H_-\subset\tau H_A.
```

Here $`H_-`$ is bounded by the **reconstructed complete** $`P_-`$ wall, not by the proper pieces left at their old periods after torus deletion. The second nesting follows from $`0\le h_--h_A\le1`$ and persists through the nested local pieces. Push the first output component into the intersection side when comparing it to $`A`$; the nesting persists, and the actual pairs are simplified as checked in §3.8.

For $`F=S`$ or $`P_-`$, its domain has $`A`$ indices $`\{-1,0\}`$, hence $`r=0`$. Put $`K=H_A`$. The nesting is $`H_F\subset K\subset\tau H_F\subset\tau K`$. In Definition 4.1, the lower part of $`X`$ is $`K\setminus H_F`$ and $`Y`$ starts on the upper side of $`K`$. Their common frontier is precisely $`\mathrm{fr}K`$. The closures retain a shared component once, and any residual points at a higher shared wall are interior to $`Y`$, not extra frontier. Thus the raw output is $`A`$, with no torus to remove:

```math
\pi_A(S)=A,\qquad \pi_A(P_-)=A.
```

Together with $`\pi_A(B)=P_-`$, this checks every non-root vertex in the definition of $`A`$-convexity [PSJ, p.1503].

The nine distances show that the edges of $`C`$ are exactly

```math
A-S,\qquad S-B,\qquad B-P_-,\qquad P_--A.
```

Neither diagonal is present. There are no triangles, so $`|C|`$ is a circle. Its graph is not dismantlable in Definition 7.1: whichever vertex is removed first, neither of its two neighbours is adjacent to the other neighbour. No first vertex has the domination required by condition (ii). This contradicts [PSJ, Theorem 7.2, pp.1503–1504], as well as its asserted contractibility of every finite rooted-convex flag subcomplex.

## 5. Why deleting a torus changes the complete wall

The ungrafted model isolates the mechanism. Its raw intersection projection is $`P\sqcup C_2`$, where $`P=S^1\times p`$. Let $`\Psi`$ be the proper lift retained at its original position after deleting $`C_2`$. Its four components all lie in period 1. But the potential

```math
h_P=1-\mathbf1_W+\mathbf1_{D_2},
\qquad n_P(k,x)=k+h_P(x)-1
```

gives the actual complete domain $`E^P=\{n_P=0\}`$. Its complete upper wall $`\Lambda=\overline{E^P}\cap\overline{\tau E^P}`$ has component periods

```math
(1,0,1,1),
```

whereas $`\Psi`$ has periods $`(1,1,1,1)`$. No common deck translation equates them. These periods are forced by one globally defined potential; they are not four independently adjustable lifts. Erasing the closed wall merges complementary chambers, so the old proper lift need no longer be a complete wall.

The precise domain selection in the proof of Lemma 6.5 [PSJ, p.1501] therefore cannot be carried out with its stated two walls. Even replacing them by the correct walls does not give the subsequently asserted containment. At $`x=(38.5,23.5)`$, inside $`U_2`$ and $`D_2`$ but outside $`V_A,V_B`$, we have $`h_A=h_B=1`$ and $`h_P=2`$. Thus $`z=(-1,x)\in E^P`$ but its two endpoint indices are both $`-1`$. Since $`r=1`$,

```math
z\notin\overline{E^B}\cup\overline{E^A_{r-1}},
\qquad
E^P\not\subseteq\overline{E^B}\cup\overline{E^A_{r-1}}.
```

The witness has an open neighbourhood away from all walls, so a closure or a small rounding cannot remove it. A genuinely pairwise-simplified observer for this pure domain test is the proper union output $`S^1\times q`$, pushed into the union side on its first component and kept common on the others.

The pure model nevertheless has $`[P]=[S_0]`$ by the four disjoint product disks of §3.1, hence $`\delta(P,S_0)=0`$. Its specified instances of the observer vertex conclusions hold. Its raw representative width two is not a class-distance lower bound. This is why the domain defect alone is insufficient to refute the lemmas.

Grafting changes that last fact. Each formerly parallel matching component acquires the distinct local classes $`r`$ and $`r_0`$. Factor-class invariance prevents the product isotopies. The extra chambers then survive in a simplified configuration, where Proposition 3.2 converts the width two into a class distance two. Thus the ungrafted model explains the wall error, while the grafted construction supplies the stronger vertex counterexample. Compare.

## 6. A finite contractible extension of the four-cycle

Write $`X(J)`$ for the all-genus cyclic complex of an oriented link: vertices are ordinary ambient isotopy classes of incompressible spanning systems with no closed components, edges use cyclic class distance one, and simplices are given by flag completion. This is [BC, Definition 10.1, p.22], not Kakimizu's original geometric-disjointness complex. Among the minimum-norm vertices of our example, the minimum-norm cyclic complex of [PSJ] and the all-incompressible cyclic complex $`X(L)`$ have the same edges; neither statement concerns the geometric-disjointness complex.

**Lemma.** The four-cycle $`C`$ constructed above is contained in a finite subcomplex $`K\subset X(L)`$ such that

```math
|K|\cong[0,1]^{12}.
```

Indeed, in this example $`K`$ can be chosen inside the minimum-norm subcomplex as well.

**Proof.** Use the recursive Banks sections of §3.6. In the base factor take the induced path

```math
\mathcal B_0=a-s-b.
```

At insertion $`i`$ take the local edge $`\mathcal E_i=[r_0,r]`$ and the integer interval in the integer-line complex $`\mathcal Z`$ given by

```math
J_1=[0,1],\qquad J_3=J_4=[-1,0],
\qquad J_i=\{0\}\quad(i\ne1,3,4).
```

Here nondegenerate intervals have their two integer vertices and their connecting edge. These intervals refer to the **eight recursive integers**, not the four face offsets. The base path is a subcomplex because $`a,b`$ are not adjacent. The local edge exists because $`r_0,r`$ are distinct adjacent knot classes. Every integer of $`A,B,S,P_-`$ lies in its corresponding $`J_i`$, as can be checked directly in the coordinate table.

We justify that this restriction is a triangulated subcomplex, rather than simply taking the inverse image of a box under an unspecified realization homeomorphism. In Banks's ordered product, a set of vertex pairs spans a simplex precisely when its factor projections span simplices and the pairs are linearly ordered on that set [BC, Definition 3.3 and Theorem 3.5, pp.4–5]. First triangulate the preceding complex times $`\mathcal Z`$ by the coordinate order $`\le_1`$. Banks then changes the ordering of this **same** triangulation to

```math
(u,n)\le_2(v,m)
\quad\Longleftrightarrow\quad
(u\le v\text{ and }n=m)
\quad\text{or}\quad
(v\le u\text{ and }m=n-1).
```

Finally take its ordered product with the local knot factor. This is exactly [BC, §9, pp.20–21]. The change from $`\le_1`$ to $`\le_2`$ reorders the existing simplices; it does not replace the underlying triangulation. The resulting product has the edge rule of §3.7 and maps simplicially to the connected-sum complex.

Inductively start with $`K_0=\mathcal B_0`$. At insertion $`i`$, restrict this construction to $`K_{i-1}\times J_i`$, with the inherited rooted order on $`K_{i-1}`$, and then to its ordered product with $`\mathcal E_i`$. A simplex in the ambient ordered product with these factor projections is a simplex in the restricted product. Since the factors are full subcomplexes on their selected vertices, the resulting $`K_i`$ is full on its selected recursive records. In particular the four vertices and all four edges of $`C`$ are retained. The root $`S_{i-1}`$ is included at each stage; the induced order is its actual rooted geometric order, not a presumed equality with a prior stage's auxiliary $`\le_3`$.

The vertex maps are injective by Banks Lemma 7.3. All link hypotheses were verified in §3.3. For the all-genus interpretation one may use [BC, §10, Theorem 10.3] and [the all-incompressible transfer](connected-sum.md), §§3–4. There is also a shorter justification sufficient for this particular $`K`$: every selected base system is four annuli and every local surface is genus one; arbitrary selected band integers preserve their Euler characteristics and create no closed components. All these assemblies therefore have $`\chi=-16`$ and are minimum-norm systems by §3.3. Banks's minimum-layer §§5–9 already give the desired simplicial subcomplex, which then embeds in $`X(L)`$.

No PS observer property or contractibility theorem is used here. In normalizing Banks's sections, the overlap label is the cyclic width obtained from PS Proposition 3.2. The places in Proposition 6.4 phrased in terms of graph distance can be read with this width; no shortest path is used in the section, vertex or edge argument. This bypass is explained in [the connected-sum audit](connected-sum.md), §3.4.

The ordered-product realization map on the restricted **finite** complexes is a homeomorphism. Induction yields

```math
|K_8|\cong |\mathcal B_0|
\times\prod_{i=1}^{8}|\mathcal E_i|
\times\prod_{i=1}^{8}|J_i|
\cong[0,1]^{1+8+3}=[0,1]^{12}.
```

The base path, although it has two edges, realizes as one interval. Only three integer intervals are nondegenerate. The finite vertex count is $`3\cdot2^8\cdot2^3=6144`$. Taking $`K=K_8`$ proves the lemma. $`\square`$

Thus the four-cycle is explicitly null-homotopic in a larger finite subcomplex, including one in the minimum layer. The lemma does not assume contractibility of $`X(H_8)`$ or of an entire knot factor, and does not establish a finite-extension rule for arbitrary links.

## 7. Consequences for the proof of Theorem 1.1 and possible repairs

The proof in [PSJ, §7, pp.1503–1504] first seeks finite contractible carriers for arbitrary finite subcomplexes. It closes a finite vertex set under the rooted projection, and then uses Theorem 7.2 to dismantle the resulting rooted-convex flag complex. Its crucial final stepretracts a vertex $`x_i`$ to $`\pi_\sigma(x_i)`$ and invokes Lemma 6.1 to guarantee adjacency or equality to every later neighbour.

In our $`A`$-convex four-cycle, $`B`$ is farther from $`A`$ than either $`S`$ or $`P_-`$. On both edges the independent order rule therefore puts $`B`$ before those vertices. The proposed move $`B\mapsto\pi_A(B)=P_-`$ encounters the later neighbour $`S`$, which is not adjacent to $`P_-`$. Condition (ii) of Definition 7.1 fails precisely at the application in the last paragraph of that proof. In fact no dismantling order works for this graph.

Lemma 6.5 is not directly used in this §7 proof; [PSJ] uses it in §8 through the convex-hull diameter statement. The failure of Theorem 1.1's displayed proof here is through the independently refuted Lemma 6.1 and Theorem 7.2. We do not infer further statement-level counterexamples in §8 without separate examples.

Theorem 1.1's conclusion about the whole complex has not been refuted. A noncontractible subcomplex need not be a retract and need not inject homology into the whole complex. Section 6 explicitly exhibits its filling in this example. We therefore cannot use the four-cycle to assert that the link's minimum complex, or its all-genus complex, is noncontractible.

The knot case is unaffected by this counterexample. With one spanning boundary curve and no closed components, a knot's spanning surface is connected. The mechanism above depends on several boundary-bearing components changing their complete-wall levels after deletion of a torus of nonzero absolute class. A knot exterior has $`H_2(E(K);\mathbb Z)=0`$, so the specific absolute-homology obstruction cannot be copied into it. This is a scope statement about the present example, not a new audit of every line of the knot proof.

Rebuilding a complete domain cannot restore the old observer conclusion for the same output class: $`\delta(S,P_-)=2`$ is already a class invariant. Choosing different representatives or writing different lifts does not change that value. Retaining $`C_2`$ would violate the published no-torus convention; compressing it is unavailable; choosing the union frontier fails the same radius-one test because $`\delta(S,P_+)=2`$. If the same Definition 4.1 and its Proposition 4.4 well-definedness are retained, changing qualifying input representatives cannot be invoked as a cost-free change of the output class. We do not give a counterexample to Proposition 4.4.

Possible further work has to change or add mathematics. One route is a genuinely different operation with proved distance decrease and the required neighbour compatibility. Another is the finite-carrier approach used at the start of §7: extend each finite input to a finite contractible subcomplex without insisting that the old projection-convex closure itself be contractible. Section 6 verifies one such carrier for this example. It supplies neither a general construction nor a finite-termination proof.

Whether a weighted, free-boundary framework can repair an appropriate three-dimensional general statement is also open in this note. It would require a precise comparison of definitions and a proved projection/carrier mechanism; it is not a correction obtained simply by relabelling the present vertices.

## 8. Related literature and the limited novelty claim

### 8.1. Weighted Seifert curves are a different setting

Schultens's *Kakimizu complexes of surfaces and 3-manifolds* [SchS], published in *Topology Proceedings* 50 (2017), 111–139, treats in two dimensions a pair $`(S,\alpha)`$ with a primitive relative first-homology class. A vertex is a weighted Seifert curve $`(w,c)`$, where $`c`$ is an oriented disjoint union of curves and arcs, its complement is connected, and $`w\circ c=\alpha`$. The v4 definition uses natural-number weights [SchS, §1, pp.3–4]. Boundaries of arcs are free to move on $`\partial S`$; there is no prescribed boundary system corresponding to $`\gamma`$ in [PSJ].

In §3, the cut-and-paste curve may have disconnected complement. The construction explicitly deletes a null-homologous complementary frontier, or eliminates a smallest-weight frontier arc and transfers its signed weight to the other frontier components, until the complement is connected. Negative weights are converted by reversing orientations [SchS, pp.10, 13]. These changes are already present in v3 [SchSv3]. They are not a newly added correction to PS's published fixed-boundary projection. Among the v4 changes, the weights become natural numbers, the final $`d_k`$ is placed above $`h(w',c'_{-1})`$ and below $`c_m`$, and Lemma 9's proof treats the root and distance-one cases explicitly [SchS; compare SchSv3].

We checked the v4 construction, Lemma 7, Lemma 9 and the remaining text for a separate argument controlling the complementary lifts after those deletions or weight eliminations. Lemma 7 uses a lift of the complement of the **final** projected curve with frontier in $`e_k\cup\tau(e_k)`$ [SchS, p.14]. Lemma 9 uses the analogous frontier choice for both final outputs to bound their intersections by two domains [SchS, p.18]. We found no separate treatment in that text of the merging of complementary lifts caused by removing components. The two-dimensional analogous steps are written with the same implicit complete-frontier assumption. **This note does not decide whether the two-dimensional statements are true or false.** We give no two-dimensional counterexample. The pure vertical model of §5 is itself a warning against inferring a false vertex conclusion from a false raw-wall interpretation.

The final three-dimensional discussion of [SchS, §8, p.26] proposes weighted essential surfaces representing a relative class and having connected complement, and states an extension of the definitions and arguments to codimension-one submanifolds. These surfaces and operations are not the unweighted, prescribed-boundary vertices and torus-deleted operation tested here. We make no transfer of this counterexample to that framework and no assertion that the framework repairs all three-dimensional arguments.

### 8.2. Seifert-fibred spaces

In *Kakimizu complexes of Seifert fibered spaces* [SchF], the introduction states that the PS argument applies in the generalized setting [SchF, p.2898]. Definition 1 and the following vertex definition use weighted surfaces with connected complement, minimizing Thurston norm, with no specified boundary system [SchF, pp.2899–2900]. These are again different from [PSJ].

Theorem 37 identifies vertical complexes with complexes of a surface obtained from the base orbifold by removing singular-point neighbourhoods. The introduction and §7 expressly restrict the proof to **closed** orientable Seifert-fibred spaces [SchF, pp.2898, 2912–2914]. Thus the published restricted theorem is not a direct theorem about $`E(H_8)`$, which has boundary, or about our fixed-boundary subcomplex. It provides related structure, not a replacement proof for the statement disputed here.

The cited article is the full 22-page publication, pp. 2897–2918.

### 8.3. Search status

A literature search on 7 October 2026 located no erratum to PS 2012 and no public counterexample of this kind. That bounded negative result cannot exclude a missed public item or an unpublished correction. No claim about what either author knew, or any stronger priority claim, is made. The mathematical conclusions depend on the checked definitions and example.

## References and editions

The [bibliography](../sources/bibliography.md) records the public sources, versions and checked pages. In this note PSJ denotes the published Przytycki–Schultens 2012 paper (bibliography J/PJ); PSV its arXiv:1004.4168v2 (PV); BC Banks arXiv:1109.0965v1 (B); BL Banks arXiv:1010.3831v2 (W); K92 Kakimizu 1992 (K); H3 Hatcher's 3-manifold notes (H); SchS Schultens arXiv:1401.2111v4 / Topology Proceedings 50 (2017) (S17); SchSv3 arXiv:1401.2111v3 (S14); and SchF the full AGT 18 (2018) article (S18). PSJ and SchF use printed journal pages; checked arXiv editions use preprint pages. No external full text is bundled.
