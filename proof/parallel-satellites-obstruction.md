# A two-bridge obstruction to the annulus cone

[Overview](../README.md) · [Objects](objects.md) · [Sources](../sources/bibliography.md) · [Scope](scope.md)

Parallel-satellite proof sequence: [cone theorem and witnesses](parallel-satellites.md) (§§1–5, 9); [two-bridge criterion and examples](parallel-satellites-two-bridge.md) (§§6–7); [distance-two obstruction](parallel-satellites-obstruction.md) (§8). References within this sequence retain these section numbers. The [torus exact-edge proof](parallel-satellites-torus.md) has its own numbering.

## 8. Removing (SB): the failure point and a distance-two vertex

### 8.1. What continues to hold

For arbitrary nontrivial $`C`$, the cut essentiality and longitudinal pattern arguments of §3.1–3.2 still apply. A minimum representative other than $`a`$ has $`r=2`$ and may have $`u>0`$. If it has $`u=0`$, §3.3 constructs a disjoint representative of $`a`$ and §4 proves distance one, even if its companion part is a **connected** two-boundary surface. Thus failure of (SB) does not, by itself, force outer–outer annuli in every vertex, or prove that $`a`$ fails to be a cone.

For example the connected genus-three $`S`$ of §6.1, attached to two reaching annuli, gives a connected genus-three spanning vertex for the $`K_{7/19}`$ parallels with $`u=0`$ and distance one from $`a`$.

On the other hand, every essential $`b_0`$–$`b_0`$ arc in a pair of pants separates the two inner holes; otherwise it cuts off an empty disk and is boundary-parallel. Any inner–inner seam must meet it. Consequently a surviving outer–outer pattern annulus prevents the disjoint **pattern-side** annulus construction. Multi-boundary companion components allow such annuli to lead onward to actual boundaries instead of forming closed components. If global disjointness can be established by another argument, the separation and width-one proof of §4 remains valid: that part does not use (SB).

### 8.2. An actual spanning vertex with a necessary outer–outer annulus

Continue with $`C=K_{7/19}`$ and the separating essential genus-three surface $`S`$ from §6.1. Take two nearby parallel copies $`S_1,S_2`$, with the **same** transported orientation. They each have relative class zero. Straighten their four boundaries on $`T`$ and label them in positive meridional order as

```math
1=S_1^+,\quad 2=S_2^+,\quad 3=S_2^-,\quad 4=S_1^-.
```

This order follows from taking parallel levels of a two-sided surface whose two boundary orientations are opposite: at one boundary the normal displacement goes forward in the meridian coordinate, and at the other it goes backward.

Choose a pattern outer–outer seam $`\gamma`$ with endpoints 2 and 4, separating the holes, a reaching seam $`\beta_+`$ with outer endpoint 1, and a reaching seam $`\beta_-`$ with outer endpoint 3. All three seams are disjoint: cut first along $`\gamma`$, obtaining two annuli with the respective inner holes; choose the reaching seam in each annulus. The annulus on $`\gamma`$ joins $`S_2^+`$ to $`S_1^-`$. The other two attach the remaining boundaries to the actual $`+, -`$ components. Opposite cut-side orientations match on each gluing circle.

The resulting $`F`$ is connected, has the two actual boundaries, and no closed component. Every pattern annulus is essential, and both companion components are essential. The reverse-assembly compression-disk argument applies: minimize a compression disk's intersections with the incompressible gluing torus; remove circles, and use an outermost arc and local boundary-incompressibility to eliminate it; a disk remaining in one piece contradicts local incompressibility. Thus $`F`$ is an actual vertex. Euler characteristic gives

```math
\chi(F)=\chi(S_1)+\chi(S_2)=-12,\qquad |\partial F|=2,\qquad g(F)=6.
```

Its displayed intersection with $`T`$ has four circles. This number is minimal by the following topology argument. A zero-circle representative would be the annulus. A two-circle essential minimum representative has $`r=2,u=0`$. Its companion part has two boundaries and lies on one of the only two zero carriers in §6.1. On the all-even four-band carrier it has two genus-two components; on the other it is a connected genus-three surface. Adding boundary annuli does not change genus or component count. Neither gives a connected genus-six surface. Positive counts are $`2+2u`$, so the minimum is exactly four. In particular this vertex cannot eliminate its outer–outer annulus by changing to a minimum representative.

There are no globally disjoint representatives of $`a`$ and this vertex either. Cutting $`M`$ along the canonical $`A`$ turns the pattern piece into $`S^1`$ times an annulus, a boundary collar on $`Q`$. Thus $`M\mathbin{\|}A`$ is homeomorphic to $`Q`$, with the remaining actual boundaries mapping to preferred longitudes on its reconstructed torus. If a genus-six $`F'`$ were disjoint from $`A`$, it would be a connected incompressible two-longitude surface there; incompressibility in $`M`$ implies incompressibility in the cut manifold. H Lemma 1.11 supplies boundary-incompressibility, since it is not an annulus. The same two-carrier classification allows only genus three for a connected two-boundary surface, a contradiction. Any disjoint pair with another representative $`A'\in a`$ can be moved to this situation by carrying the whole pair through an ambient isotopy from $`A'`$ to $`A`$.

### 8.3. Whole-complement width and its minimum

Choose the inner–inner seam $`\alpha`$ to miss both reaching seams and cross $`\gamma`$ once. Then $`A\cap F`$ is one essential longitude circle $`c`$, lying in the joining annulus. On $`A`$, it separates two annuli. On $`F`$, it separates two genus-three surfaces, each with one actual boundary and the boundary $`c`$.

Here is a full-block calculation. Cutting the pattern along $`\beta_+,\beta_-,\gamma`$ gives two disks $`D_+,D_-`$. Put $`I_{ij}`$ for the outer interval between successive boundary labels. Cutting $`Q`$ along $`S_1,S_2`$ gives three connected blocks $`K_0,K_1,K_2`$, where $`K_1\cong S\times I`$ is the parallelism between them. The attachment intervals are

```math
K_0:I_{41},\qquad K_1:I_{12},I_{34},\qquad K_2:I_{23};
```

$`D_+`$ carries $`I_{41},I_{12}`$, and $`D_-`$ carries $`I_{23},I_{34}`$. In particular $`K_1`$ connects the two pattern blocks, so this is one whole connected $`N_F`$.

The two pieces of $`\alpha\setminus\gamma`$ cut $`D_+`$ between $`I_{41},I_{12}`$ and $`D_-`$ between $`I_{23},I_{34}`$. Consequently removing the two annular pieces of $`A\setminus F`$ from the whole block gives exactly three nonempty chambers: the one containing $`K_0`$, the middle one containing $`K_1`$ and a piece of each pattern disk, and the one containing $`K_2`$. Their wall-incidence graph is a path with two edges.

In a complete lifted $`F`$-block the two annular walls are parts of **different consecutive** full $`A`$ lifts. To check the level assertion, each full connected $`A`$ lift intersects exactly one full $`F`$ lift in its one lift of $`c`$. Its two annular halves lie in the two consecutive $`F`$-blocks on opposite sides of that $`F`$ lift. Translating by one deck unit supplies the other half lying in a fixed $`F`$-block. Thus that fixed block contains halves of consecutive $`A`$ lifts, not two pieces of a single lift. The three chambers meet exactly three consecutive open $`A`$-blocks, and

```math
D(A,F)=2.
```

Both global surfaces are boundary-incompressible by H Lemma 1.11: $`A`$ uses different actual tori and cannot be boundary-parallel, and $`F`$ is not an annulus. This representative pair also has simplified intersection in Banks Definition 4.1, p. 5. Indeed the horizontal face on $`A`$ of any product region has boundary among $`c`$ and the actual boundary circles; an interior boundary of that face must be a collapsed intersection boundary, since the remaining vertical boundary lies in $`\partial M`$. There are no intersection arcs, and the available circles are all essential on $`A`$. A connected such face can only be one of the two annuli cut off by $`c`$: a disk cannot have that boundary, and a face containing $`c`$ in its interior is inconsistent with a product region's boundary intersections. Its matching face on $`F`$, bounded by the same $`c`$ and the corresponding actual boundary, would have to be the entire corresponding component of $`F\mathbin{\|}c`$, which has genus three and is not an annulus. No product region exists. The pair is transverse and has disjoint actual boundary curves, hence is almost transverse. The whole exterior cannot be fibred for its spanning class: its injected $`\pi_1(T)=\mathbb Z^2`$ lies in $`\ker\phi`$, whereas a compact fibre with nonempty boundary has free fundamental group. Thus no surface-bundle exception enters this simplification argument.

Banks Proposition 4.10, p. 7, says a pair in this position minimizes representative width. Its validity for the full incompressible complex is explicitly stated in §10, p. 22. This is the local simplified-intersection criterion, not a PS projection claim. Fixing $`A`$ causes no loss in the class minimum: an ambient isotopy carrying any $`A'\in a`$ to $`A`$ carries the other representative too, preserves the linking cover, and preserves widths. Therefore

```math
\delta(a,[F])=2.
```

In particular the annulus is **not** a cone vertex for the two parallels of $`K_{7/19}`$. This does not refute contractibility of their entire $`X`$. It refutes a universal annulus-cone extension to all two-bridge companions. The conditional theorem and its torus/twist applications remain unaffected.

The [complete tree calculation](parallel-satellites-k719-tree.md) proves that the entire complex in this example is nevertheless contractible. The genus-six surface here is its untwisted linear chain with two companion pieces.
