# Four balanced Hopf fibres: the full cyclic complex is an infinite Farey tree

Let $`H_4`$ consist of four regular positive Hopf fibres with orientation signs $`(+,+,-,-)`$. Write $`E(H_4)=S^1_h\times P`$, where $`P`$ is a sphere with four labelled boundary circles. Vertices and cyclic edges are those in [objects](objects.md). Boundary curves may move on their labelled tori.

The total-meridian homomorphism satisfies $`\phi(\mu_i^H)=\epsilon_i`$ and $`\phi(h)=0`$. Its cover is $`S^1_h\times\widetilde P`$, with peripheral values $`\epsilon_i`$ on $`P`$. Source codes H, J, B and O refer to [the specified editions](../sources/bibliography.md).

The classification and distance calculation below use Hatcher's essential-surface theorem and PS §3's distance-realisation result. They do not use the PS projection or PS Theorem 1.1. The pillowcase slope classification is included in full.

[Overview](../README.md) · [Objects](objects.md) · [Sources](../sources/bibliography.md) · [Scope](scope.md)

## 2. All incompressible spanning surfaces are two vertical annuli

**Proposition 2.1.** Every vertex has a representative

```math
F_a=S^1_h\times(a_1\cup a_2),
```

where $`a_1,a_2`$ are disjoint proper arcs in $`P`$, use each labelled boundary once, and each join a positive label to a negative label. Conversely, every such oriented annulus system is an admissible incompressible spanning surface.

**Proof.** First establish the boundary slopes, without assuming connectedness or minimal genus. In the reference Hopf coordinates write

```math
\partial F=\sum_i\epsilon_i(\lambda_i^H+b_i\mu_i^H).
```

Each boundary has longitudinal degree one. In the exterior $`[\lambda_i^H]=\sum_{j\ne i}[\mu_j^H]`$, and $`\sum_i\epsilon_i=0`$. The coefficient of $`[\mu_i^H]`$ in the null-homologous total boundary is therefore

```math
\epsilon_i b_i+\sum_{j\ne i}\epsilon_j=\epsilon_i(b_i-1).
```

Hence all $`b_i=1`$, so all boundary curves have fibre slope $`h=\lambda_i^H+\mu_i^H`$, oriented $`\epsilon_i h`$. These are the spanning-surface boundary slopes, not the individually zero-framed preferred longitudes $`\lambda_i^H`$.

The link is non-split: all pairwise linking numbers are $`\epsilon_i\epsilon_j=\pm1`$, whereas a splitting sphere would make every linking number across its partition zero. Its exterior is irreducible. Its boundary tori are also incompressible: the maps

```math
\langle h,c_i\rangle\cong\mathbb Z^2\longrightarrow \mathbb Z\times\pi_1(P)
```

are injective, since the peripheral element $`c_i`$ has infinite order.

Every component of $`F`$ has nonempty boundary. None is a disk, because a fibre boundary represents the nontrivial central element $`h`$. Hatcher Lemma 1.11 says that an incompressible component is boundary-incompressible or a boundary-parallel annulus. The latter has two boundaries on the same torus, impossible here. Thus every component is essential in the precise sense required by Hatcher Proposition 1.12.

That proposition makes each component vertical or horizontal up to isotopy. A horizontal component with boundary has boundary transverse to the fibres, and its boundary has nonzero intersection with fibre slope. Fibre boundaries exclude this alternative. Thus every component is an annulus, and four total boundaries give exactly two annuli.

The two annuli can be verticalised simultaneously as follows. Verticalise the first, using the boundary-fixed clause in Hatcher's proof on p. 22. Ambient isotopy extension carries the second annulus along and preserves disjointness. The first annulus's base arc joins distinct holes. Cutting along it gives $`S^1`$ times a pair of pants. The second annulus is incompressible in that cut product and has its two boundary circles on two distinct untouched tori. Lemma 1.11 and Proposition 1.12 apply again, and fibre boundary excludes horizontality. This isotopy can fix the other boundary torus of the cut product, since the entire track of the second annulus misses it; relative isotopy extension gives an ambient extension fixing that torus. In particular it fixes both cut faces, so glues back while leaving the first annulus fixed.

Opposite orientations at the two ends of an oriented vertical annulus pair a positive boundary with a negative one. This proves the forward statement in every genus, and establishes the surface classification directly for the pure product.

Conversely, each annulus core maps to $`h`$, so its group injects into $`\pi_1(E)`$. The annuli are incompressible, have exactly the required boundary, and have no closed components. The orientation on each annulus is forced by those boundaries. $`\square`$

In particular, all representatives in Proposition 2.1 have Thurston norm zero. Zero is the minimum possible norm, so they are in the minimal-norm class to which PS Proposition 3.2 applies. This is the only minimal-norm input needed in the distance computation.

## 3. Ambient isotopy classes really are unmarked arc-system classes

Endpoints of base arcs are allowed to slide on their labelled boundary circles.

**Proposition 3.1.** $`a\mapsto[F_a]`$ is a bijection between allowed unmarked arc-system classes and vertices of $`X`$.

**Proof.** Surjectivity is Proposition 2.1; a base arc-system isotopy lifts to an ambient isotopy in the circle product.

For injectivity, cutting $`P`$ along both arcs leaves an annulus $`B_a`$. Let $`\beta_a`$ be its core, viewed in $`P`$. It is an essential curve separating the two labels of one paired annulus from the other two. The image of the complete cut complement's group in the exterior is

```math
J_a=\langle h\rangle\times\langle\beta_a\rangle\subset \mathbb Z\times\pi_1(P).
```

An ambient isotopy of the whole surface system gives an isotopy of its complete cut complement, so sends this subgroup to the subgroup for the final system, up to basepoint conjugacy. Quotienting by the central $`\langle h\rangle`$ shows that $`\langle\beta_a\rangle`$ and $`\langle\beta_b\rangle`$ are conjugate in $`\pi_1(P)`$. The essential simple curve $`\beta_a`$ is not a proper power: its homology is the sum of the two corresponding peripheral classes, a primitive nonzero element of $`H_1(P;\mathbb Z)`$. The same holds for $`\beta_b`$. Consequently their generators are conjugate up to inversion. Essential simple curves freely homotopic up to inversion are isotopic.

Finally, $`\beta`$ determines the entire arc system. Each side of $`\beta`$ is a pair of pants, with two original labelled holes and the new boundary $`\beta`$. The arc joining those two original holes is unique up to isotopy with endpoints free. Choose these two arcs on the two sides. This construction inverts $`a\mapsto\beta_a`$ and respects isotopy. Therefore $`a`$ and $`b`$ agree. $`\square`$

This argument permits the ambient isotopy to leave the vertical category. It is not a claim that a path of surfaces can be verticalised continuously. In particular there is no unresolved relative-decomposition assumption hidden in the bijection.

## 4. Accurate slope and parity classification

Fill the four boundary circles by four marked points, and use the pillowcase model

```math
P^\bullet=(\mathbb R^2/\mathbb Z^2)/\iota,
\qquad \iota(x,y)=(-x,-y).
```

The marked points are the images of $`(0,0),(1/2,0),(0,1/2),(1/2,1/2)`$. Choose the marking so that the first two are positive and the last two negative. Removing small disks restores $`P`$. This is just a choice of coordinates on the labelled surface; it does not identify vertices under label permutations.

For a primitive integer vector $`v=(p,q)`$, considered up to sign, put

```math
\ell_v(x,y)=-qx+py\pmod1.
```

The two invariant torus circles $`\ell_v=0`$ and $`\ell_v=1/2`$ pass through all four marked points. Their images are two disjoint arcs, denoted $`a_v`$, after drilling the points. The two circles $`\ell_v=1/4,3/4`$ are exchanged by $`\iota`$; their common image is the associated separating curve $`\beta_v`$.

**Lemma 4.1 (pillowcase slope lemma).** Essential unoriented curve classes in the four-marked sphere, and hence the two-arc-system classes of §3, are in bijection with primitive vectors $`(p,q)`$ modulo sign. The vector is the homology class, up to sign, of either of the two lifts of $`\beta`$ to the branched torus. The standard representatives are $`\beta_v`$ and $`a_v`$ above.

Here is a justification of the uniqueness statement, which is essential: one cannot simply forget the four marked points and invoke unpunctured-torus curve classification.

Fix the marked point $`(0,0)`$. The orientation-preserving mapping-class group of the sphere fixing this point and permuting the other three is

```math
G=B_3/\langle(st)^3\rangle,
\qquad B_3=\langle s,t\mid sts=tst\rangle.
```

Indeed, remove a small disk about the fixed point. Mapping classes of the remaining disk with three marked points are the three-strand braid group. Capping the boundary by the fixed point kills the boundary full twist. Conversely, an isotopy after capping can be made into an isotopy of the disk after recording its integral rotation about that point; this rotation is exactly a power of the boundary full twist. This proves the stated quotient.

The two elementary half twists lift to Dehn twists on torus curves intersecting once. In a chosen basis their actions are

```math
A=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad B=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
```

Thus the lift gives $`G\to PSL(2,\mathbb Z)`$. It is an isomorphism. Algebraically, with $`u=sts`$ and $`z=st`$, the braid relation is $`u^2=z^3`$, and quotienting the full twist gives $`C_2*C_3`$. The displayed matrices have $`(ABA)^2=(AB)^3=-I`$, generate $`PSL(2,\mathbb Z)`$ by the Euclidean algorithm, and give the same free-product presentation. Faithfulness of the last presentation can also be seen by ping-pong: $`ABA`$ acts by $`x\mapsto-1/x`$, whereas $`AB`$ acts by $`x\mapsto1/(1-x)`$; the nonidentity element of the order-two subgroup sends the positive half-line into the negative half-line, and both nonidentity elements of the order-three subgroup send the negative half-line into the positive half-line. The reduced-word ping-pong argument proves $`C_2*C_3`$ injects.

$`G`$ acts transitively on essential curves: every such curve cuts the sphere into two disks each containing two marked points, and a homeomorphism of these disks can take it to a chosen reference curve. The reference curve can be chosen with lift slope $`(1,0)`$, separating the two positive points from the two negative points.

Its stabiliser in $`G`$ is infinite cyclic, generated by the half twist of the two marked points on the side not containing the fixed point. To verify this, cutting along the reference curve leaves two twice-marked disks. On the side with a fixed marked point only full twists are allowed; on the other side half twists are allowed. Full twists on the two sides represent the same boundary Dehn twist after gluing, so the latter half twist generates the whole stabiliser. Side interchange is impossible because the distinguished point is fixed. On torus homology its image is $`\langle A\rangle`$, exactly the stabiliser in $`PSL(2,\mathbb Z)`$ of the unoriented primitive line $`(1,0)`$.

Consequently the orbit-stabiliser quotient for curves is the same as that for primitive unoriented vectors. This proves both injectivity and surjectivity of the slope assignment. The explicit straight representatives realise it. $`\square`$

The endpoints paired by $`a_v`$ differ by $`v/2`$ in the torus. Thus the three nonzero vectors modulo two give the three labelled pairings. With our signs:

| Vector modulo two | Pairing | Allowed? |
|---|---|---|
| $`(1,0)`$ | same-sign pairs, one positive-positive and one negative-negative | no |
| $`(0,1)`$ | opposite-sign pairs | yes |
| $`(1,1)`$ | the other opposite-sign pairing | yes |

Therefore, with the slope denoted $`p/q`$ and the sign chosen so $`q>0`$,

```math
V(X)=\{p/q:\gcd(p,q)=1,\ q>0\text{ odd}\}.
```

In this marking $`\infty=1/0`$ is in the deleted class. The invariant statement is “two of the three parity classes of $`\mathbb Q\cup\{\infty\}`$”, rather than a marking-independent rule about denominators.

## 5. Why the straight vertical representatives realise the minimum

**Lemma 5.1.** For distinct slopes $`v,w`$, the straight representatives $`F_{a_v},F_{a_w}`$ are almost transverse and have simplified intersection in the sense of PS §3.

**Proof.** Choose the drilled disks sufficiently small for this fixed pair. At each marked point the two distinct straight directions meet its circle in different endpoint positions. Thus boundaries are disjoint. Interior intersections of the annuli are transverse fibre circles. There are no common annulus components: a component's proper base-arc class already determines the other arc by the pair-of-pants argument in §3, so a shared class would make the complete slopes equal.

We check product regions, including boundary product regions, with the **relative** convention used by the original definition: for $`J=(W\times I)/{\sim}`$ the uncollapsed vertical boundary lies in $`\partial E`$. This condition is explicit in Oertel, p. 712 (p. 2), and Banks Definition 4.1, p. 5. In the latter restatement the horizontal faces are exactly $`J\cap F_{a_v}`$ and $`J\cap F_{a_w}`$. It is this relative convention, rather than an arbitrary solid torus chamber, that is meant by a product region.

For such a region, the boundaries of a horizontal face lie on intersection circles (collapsed sides) or on surface boundary circles (uncollapsed sides in $`\partial E`$). These are all complete fibre circles. There can be no collapsed boundary interval ending in the interior of an intersection circle, because its endpoint would have to reach the uncollapsed side in $`\partial E`$, whereas the intersection circles are interior and the surface boundaries are disjoint. A connected face in an annulus is therefore a subannulus, since cutting an annulus by essential fibre circles leaves only annuli. In particular it is not a disk. The case of the whole annulus is included.

Take a spanning section of such an annular face and follow it across the product. Project to $`P`$. This gives a homotopy between a subarc of an $`a_v`$-arc and a subarc of an $`a_w`$-arc. An end on an intersection fibre stays at its intersection point. An end on $`\partial E`$ travels in its labelled boundary circle. The sections can be straightened within their faces, so their projections are the corresponding straight arc segments.

Lift this disk homotopy first to the unbranched torus cover of the drilled pillowcase and then to the planar cover of the torus. Cap the drilled disks only for this endpoint argument: a boundary end becomes its marked point. The two lifted segments lie on straight lines of directions $`v`$ and $`w`$ and have the same two distinct endpoints. The endpoints are distinct because a nontrivial subarc of either embedded base arc has distinct endpoints. Two lines of different slopes cannot share two points. This excludes the product region. It also covers a face equal to a whole annulus, where both endpoints are marked points.

A boundary product region would be a disk between boundary subarcs. The boundary curves here are disjoint essential parallel fibres, so such a disk cannot occur. Hence neither type of PS product region exists. $`\square`$

The ambient manifold is orientable, irreducible and boundary-irreducible; the annuli are incompressible and boundary-incompressible; and each is norm-minimising as part of the whole spanning system (§2). PS Proposition 3.2, p. 1494 and proved on p. 1495, therefore gives

```math
\delta([F_{a_v}],[F_{a_w}])=d(F_{a_v},F_{a_w}).
```

In particular the forthcoming cut-block calculation is a calculation of the **isotopy-class minimum**, not merely an upper bound from convenient representatives.

## 6. The full cyclic-cover distance formula

Take two allowed primitive vectors $`v_s=(p_s,q_s)`$ and $`v_t=(p_t,q_t)`$, with positive odd denominators. Choose integers $`c,d`$ satisfying

```math
cp_s+dq_s=1,\qquad c\equiv0\pmod2,
```

and set

```math
M=\begin{pmatrix}q_s&-p_s\\c&d\end{pmatrix}\in SL(2,\mathbb Z).
```

Such a choice exists: the solutions for $`c`$ differ by the odd number $`q_s`$. Moreover $`d`$ is odd. Thus $`M`$ preserves the two rows of marked points, and hence the signs and $`\phi`$. It descends to a sign-preserving homeomorphism of $`P`$, after adjusting the drilling collars. Applying it to both surfaces computes the same distance; any within-row label permutation here is a coordinate change, not a vertex identification. It takes $`v_s`$ to $`(0,1)`$ and $`v_t`$ to

```math
D_0=q_sp_t-p_sq_t,\qquad Q_0=cp_t+dq_t.
```

If $`D_0=0`$, the two primitive unoriented slopes coincide and their distance is zero. Otherwise choose the sign of this second vector so that

```math
D=|D_0|>0,\qquad Q=\mathrm{sgn}(D_0)Q_0.
```

$`Q`$ is odd and $`\gcd(D,Q)=1`$. Replacing $`Q`$ by $`Q+2Dk`$ is permitted and leaves the following formula unchanged.

Define integers

```math
H_0=0,\qquad H_{j+1}=H_j+(-1)^{\lfloor Qj/D\rfloor}
\quad(0\le j<2D).
```

**Theorem 6.1.** For these distinct vertices,

```math
\boxed{\displaystyle
\delta(v_s,v_t)=\max_{0\le j\le2D}H_j-
\min_{0\le j\le2D}H_j.}
```

**Proof.** We calculate after the coordinate change, with $`S=a_{(0,1)}`$ and $`R=a_{(D,Q)}`$. A lift of $`P\setminus R`$ to the twice-covered drilled pillowcase is the annulus represented by

```math
0<-Qx+Dy<1/2
```

in the torus, with the small drilled half-disks at its boundary corners removed. Its planar model is this strip modulo translation $`(x,y)\mapsto(x+D,y+Q)`$. The double cover of the drilled pillowcase is exactly the mod-two cover of $`\phi`$, since all four peripheral values are odd. The other strip is exchanged with it by $`\iota`$. Each maps homeomorphically to the complete annular cut complement in $`P`$; we use one whole annulus, not independent lifts of its two frontier arcs.

The lift of $`S`$ consists of the segments of the lines $`x=j/2`$. In one period $`0\le x<D`$, precisely $`2D`$ such segments cross the strip. Every segment runs from one boundary of the strip-annulus to the other, including the segments terminating at a drilled corner. There are no marked points in its interior. At $`x=j/2`$, the $`y`$-coordinate ranges between

```math
\frac{Qj}{2D}\quad\text{and}\quad\frac{Qj+1}{2D}.
```

The sign of a cooriented crossing of a vertical $`S`$-arc is constant on this interval. Up to one common reversal it is positive for $`0<y\pmod1<1/2`$, negative for $`1/2<y\pmod1<1`$. The sign at the $`j`$th crossing is therefore

```math
s_j=(-1)^{\lfloor Qj/D\rfloor}.
```

For example a path with $`-Qx+Dy=1/4`$ meets the $`j`$th segment at $`y=(Qj+1/2)/(2D)`$, giving precisely that sign. Small enough drilled disks do not meet this path.

Cut the strip-annulus at these $`2D`$ spanning segments. Its chambers occur in cyclic order. Lifting the whole annulus to $`\widetilde P`$ gives the $`S`$-block indices of successive chambers by cumulative signed crossings. These are exactly $`H_0,\ldots,H_{2D-1}`$ up to an additive constant and a common sign. Since $`Q`$ is odd,

```math
s_{j+D}=-s_j,
```

so $`H_{2D}=H_0=0`$. Thus the lift closes up correctly, as a lift of the **whole** annular cut complement. Every listed chamber is nonempty and all its points lie in its listed open $`S`$-block. Consequently the largest and smallest intersected open-block indices are $`\max H_j`$ and $`\min H_j`$. Taking the product with $`S^1_h`$ does not change them. PS Definition 2.1 gives $`d(S,R)=\max H_j-\min H_j`$, and Lemma 5.1 with Proposition 3.2 makes this the class distance. $`\square`$

The choice of Bezout solution does not affect the answer: another even solution has $`c'=c+2kq_s`$, $`d'=d-2kp_s`$, so $`Q'=Q+2kD`$. In the formula the exponent changes by $`2kj`$, leaving every sign unchanged. Coordinate changes and reversal of deck direction likewise preserve the range.

A few exact examples, with the first vertex $`0/1`$, illustrate that the full distance is not a function of determinant alone:

| Second slope | $`D`$ | Heights $`H_0,\ldots,H_{2D}`$ | Distance |
|---|---:|---|---:|
| $`1/3`$ | 1 | $`0,1,0`$ | 1 |
| $`2/3`$ | 2 | $`0,1,0,-1,0`$ | 2 |
| $`3/5`$ | 3 | $`0,1,0,-1,-2,-1,0`$ | 3 |
| $`4/3`$ | 4 | $`0,1,2,1,2,1,0,1,0`$ | 2 |
| $`4/1`$ | 4 | $`0,1,2,3,4,3,2,1,0`$ | 4 |

## 7. Distance one is exactly Farey adjacency

**Corollary 7.1.** Two distinct allowed slopes are adjacent in $`X`$ precisely when

```math
|p_sq_t-p_tq_s|=1.
```

**Proof.** If $`D=1`$, the two increments in Theorem 6.1 are $`+1,-1`$ because $`Q`$ is odd; the width is one.

Conversely, width one in a closed sequence of unit increments forces its signs to alternate: there are just two integer heights, and every move must switch them. Reduce $`Q`$ modulo $`2D`$ to $`0<Q<2D`$, which preserves every increment. If $`D>1`$, coprimality excludes $`Q=D`$. Alternation starts with $`+`$ and therefore requires $`s_1=-`$, forcing $`Q>D`$. Write $`Q=D+r`$, with $`1\le r<D`$. For $`0\le j<D`$,

```math
s_j=(-1)^j(-1)^{\lfloor rj/D\rfloor}.
```

Alternation requires every $`\lfloor rj/D\rfloor`$ to be even. These floors increase in steps zero or one and attain all integers from $`0`$ to $`r-1`$, so $`r=1`$. But then $`Q=D+1`$ is odd, making $`D`$ even, whereas $`s_D=(-1)^Q=-1`$ contradicts the alternating value $`(-1)^D=+1`$. Thus width one is impossible for $`D>1`$. $`\square`$

At determinant one the straight base arc systems have disjoint interiors: their lifted line intersections occur only at the four marked points, removed by drilling. This gives geometrically disjoint representatives as well. The edge proof, however, is the complete-block calculation and the minimisation argument, not the inference “disjoint implies distance one”.

The distinction remains relevant even in this example. For a fixed system $`S=A\cup B`$, push $`A`$ a little in its positive normal direction and $`B`$ in its negative normal direction, obtaining a geometrically disjoint representative $`R`$ of the **same vertex**. Its whole cut block contains the original block and slivers of the two adjacent blocks, so $`d(S,R)=2`$. Its class distance is zero, realised by taking $`R=S`$. Independent normal pushes of the two components cannot replace the use of a whole cut block, nor replace minimisation. The general disconnected-surface warning is stated explicitly by PS, p. 1493.

## 8. The actual complex is a tree

By §§4 and 7 the graph is

```math
T=\left(\left\{p/q:\gcd(p,q)=1,\ q>0\text{ odd}\right\},
\quad p/q\sim p'/q'\ \Longleftrightarrow\ |pq'-p'q|=1\right).
```

This is exactly the induced subgraph of the Farey graph on the two allowed parity classes.

**Lemma 8.1.** A vertex with denominator $`q>1`$ has exactly one neighbour with smaller positive odd denominator.

**Proof.** The two equations $`pq'-p'q=1`$ and $`pq'-p'q=-1`$, with $`0<q'<q`$, have unique denominator solutions $`r`$ and $`q-r`$, respectively, where $`r`$ is the inverse of $`p`$ modulo $`q`$ in $`\{1,\ldots,q-1\}`$. The resulting numerator is integral and coprime to its denominator. As $`q`$ is odd, exactly one of these denominators is odd. There are no other smaller-denominator neighbours. $`\square`$

Repeatedly following this unique parent strictly decreases positive denominators until one reaches an integer $`n/1`$. The integer vertices have precisely the edges $`n\sim n+1`$ among themselves. Thus every vertex connects to the integer line, and the graph is connected.

There is no cycle. If a finite simple cycle contains a denominator greater than one, take a vertex with maximal denominator on that cycle. Distinct adjacent vertices cannot have the same denominator greater than one, since their determinant would be a multiple of that denominator. Hence both neighbours of the chosen vertex on the cycle have smaller denominators. This contradicts Lemma 8.1. A cycle entirely on the integer line is also impossible. Therefore $`T`$ is a tree.

For completeness, every edge switches the parity of the numerator, since both denominators are odd. In particular there is no triangle. The flag completion consequently adds no simplices: $`X`$ has dimension one and equals $`T`$ as a simplicial complex.

The usual geometric realisation of a tree is contractible. For instance root it at $`0/1`$ and move each point toward the root along its unique finite edge path. The resulting contraction is continuous on every closed edge times the parameter interval, with image in the finite subtree joining that edge to the root; the CW weak topology (and its product with the finite CW interval) gives global continuity. Infinite valence presents no obstruction.

This proves the homotopy conclusion directly, without PS Theorem 1.1 or any claim that deleting a closed torus preserves a projection certificate.
