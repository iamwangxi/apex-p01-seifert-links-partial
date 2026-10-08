# Two parallels of K_{7/19}: the full complex is a tree

[Overview](../README.md) · [Objects](objects.md) · [Sources](../sources/bibliography.md) · [Scope](scope.md)

## 1. Object and the joint-normal-form inputs

Let $`C=K_{7/19}`$ and let $`L`$ be its two oppositely oriented zero-framed parallels. Write

```math
M=E(L)=Q\cup_T P,\qquad Q=E(C),\qquad P=S^1_\lambda\times B.
```

The pair of pants $`B`$ has boundary circles $`b_0,b_+,b_-`$. The common torus is $`T=S^1_\lambda\times b_0`$. All ambient isotopies start at the identity; actual boundary tori remain labelled, and boundary curves may move. A vertex is an oriented, componentwise incompressible spanning surface, with one prescribed longitude on each actual torus, no closed component, and no genus restriction. Edges use the minimum width of **complete open complement blocks** in the linking-number cyclic cover. The complex $`X(L)`$ is the flag completion of those edges.

We use the following proved statements of the joint normal forms, after reading its proof and its newly available adversarial review:

1. Every essential longitudinal companion system is a simultaneous stack entirely of $`R`$ pieces, or entirely of $`S`$ pieces. The pieces have types $`(g,b)=(2,1)`$ and $`(3,2)`$, respectively; $`S`$ has relative class zero. Mixed disjoint systems are impossible. [Joint normal forms](parallel-satellites-k719-normal-forms.md).
2. An $`S`$ stack has ordered boundary pairing $`q(i)=-1-i\pmod{2k}`$. A returning identity isotopy induces the identity boundary permutation, including when orientations are forgotten initially. The two end chambers cannot be exchanged: an exchange would give two disjoint essential one-sided cores. [Joint normal forms](parallel-satellites-k719-normal-forms.md).
3. Every vertex is $`A`$, $`G`$, or a legal $`F(k,a,t)`$. Here $`A`$ is the annulus, $`G`$ is the single disconnected $`+R,-R`$ vertex, and the last surface is a connected chain of $`k`$ copies of $`S`$. Its legal condition is $`\gcd(2a+1,2k)=1`$, and its genus is $`3k`$. [Joint normal forms](parallel-satellites-k719-normal-forms.md).
4. Efficient globally isotopic assemblies admit a $`T`$-preserving isotopy. In particular equality of two chain vertices preserves $`k,a`$. [Joint normal forms](parallel-satellites-k719-normal-forms.md).
5. Simplified intersection realizes the class minimum width; zero width means equality. [Joint normal forms, §8](parallel-satellites-k719-normal-forms.md), using the explicit Banks extension to all incompressible spanning surfaces.

## 2. Sources and supporting interfaces

The preceding inputs are proved in [joint normal forms](parallel-satellites-k719-normal-forms.md), §§3–8. The [geometric normalisation volume](parallel-satellites-normalisation.md), §§3–7, supplies essentiality, reverse assembly and the product-annulus/torus-comparison proofs. HT Theorem 1 and Propositions 1–2, pp. 228–230, classify longitudinal systems; its pillowcase arc classification is on p. 232. Banks Definition 4.1/Proposition 4.2, p. 5, Proposition 4.10, p. 7, and the all-incompressible extension, §10, p. 22, supply product regions and the class-minimum width. PS §§2–3 supply the complete-block and simplified-intersection conventions. Editions are in the bibliography. No PS §§4–7 projection or contractibility conclusion is used.

## 3. Cyclic adjacency and actual disjointness

The following observation establishes the direction in which disjointness cannot simply be assumed.

**Lemma 3.1 (a transverse crossing costs at least two layers).** If two spanning representatives $`F,H`$ have a transverse interior intersection, their complete-block representative width is at least two.

**Proof.** Every complete complement is connected, by the meridian argument of [the whole-complement argument](parallel-satellites.md), §4. Its lift is a single copy, and all complete lifts are deck translates. Near a transverse intersection choose lifts of the intersecting walls, say $`\widetilde F_i,\widetilde H_j`$. The four local quadrants meet the two consecutive complete $`F`$ blocks $`U_{i-1},U_i`$ and the two consecutive complete $`H`$ blocks $`W_{j-1},W_j`$. Both $`W_{j-1}`$ and $`W_j`$ meet both $`U_{i-1}`$ and $`U_i`$ locally. But $`W_j=\tau W_{j-1}`$, so translating the two intersections of $`W_j`$ back shows that $`W_{j-1}`$ also meets $`U_{i-2}`$. One complete $`H`$ block therefore meets three consecutive complete $`F`$ blocks. Its width is at least two. This uses the deck relation between the **whole** blocks, not separate choices of local chamber levels. ∎

**Corollary 3.2.** Distinct vertices joined by an edge have disjoint representatives in the present model. Conversely, disjoint representatives give an edge whenever at least one of the two whole spanning surfaces is connected.

**Proof.** First take almost-transverse simplified representatives, so their width is the class minimum by Banks Proposition 4.10 and Section 10. Lemma 3.1 excludes transverse intersections at width one. Distinct connected chain vertices cannot have a coincident whole component. Nor can a component of $`G`$ coincide with $`A`$ or a chain, because it has one actual boundary rather than both. Hence these pairs are genuinely disjoint. There is only one disconnected vertex, $`G`$.

For the converse let the connected surface be $`F`$. It lies as one complete proper wall in the connected cut block of $`H`$. It separates that block: otherwise a once-crossing arc closes in the block to give a loop with $`F`$ intersection $`\pm1`$ and $`H`$ intersection zero, contrary to both being dual to the same linking homomorphism. A connected separating wall gives exactly two nonempty chambers. In a complete lifted $`H`$ block there is one complete lift of $`F`$, and the chambers lie in its two consecutive open $`F`$ blocks. Representative width is one. Zero class width would mean equality, so distinct classes have minimum width one. ∎

This corollary applies because the only disconnected vertex has already been classified. It does not assert that arbitrary disjoint disconnected spanning systems have width one.

## 4. Simultaneous minimisation of a disjoint pair

**Lemma 4.1.** A disjoint pair of the present spanning surfaces has representatives which remain disjoint and whose entire cut systems at $`T`$ are essential. Their pattern annuli can then be verticalised simultaneously.

**Proof.** Among transverse representatives of the disjoint **union**, minimise the total number of $`T`$ circles. All components of the union are incompressible and have actual boundary. The innermost-circle and ball argument removes an inessential trace while keeping the other surface disjoint: its component cannot be wholly trapped in a ball, because it has boundary outside that ball. Cutting along the remaining essential circles gives injective cut-piece groups.

If a cut piece is a boundary-parallel annulus, it has both boundaries on $`T`$. It cannot have two boundaries on one actual torus, since it belongs to one of the original spanning surfaces, which uses that torus once. In its annular parallelism solid torus the other cut pieces of the **union** have cyclic injective groups and hence are primitive annuli. [Normalisation Lemma 3.3](parallel-satellites-normalisation.md) works on this finite union. Pushing the innermost annulus through an empty domain reduces the total count without crossing the other surface. Thus no such piece remains. Boundary-incompressibility follows as in the normalisation and cone proofs.

The individual surfaces still have their prescribed actual boundaries and no closed components. the longitudinal cut argument in the joint normal forms therefore applies to each; all traces have longitude slope. Straighten all actual and common-torus boundary curves in disjoint collars, carrying the whole union. [Normalisation Lemma 5.1](parallel-satellites-normalisation.md) now verticalises its full finite pattern annulus system relative to those straight boundaries. None of these operations independently chooses conflicting representatives. ∎

**Corollary 4.2 (the disconnected vertex is a leaf).** The only neighbour of $`G`$ is $`A`$.

**Proof.** A chain cannot be disjoint from $`G`$. Apply Lemma 4.1 to a hypothetical disjoint pair. The essential-cut classification in the joint normal forms applies even if its representatives were obtained by minimising the union rather than each separately. A connected positive-genus spanning surface must have $`S`$ chain pieces; a disconnected surface with one actual boundary on each component must have $`R`$ pieces. Thus their companion union is an essential mixed $`R,S`$ system, forbidden by [Joint normal forms, Theorem 4.2](parallel-satellites-k719-normal-forms.md). Corollary 3.2 excludes an edge. The $`u=0`$ pattern construction of [the cone volume](parallel-satellites.md), §3, supplies disjoint $`A,G`$, hence their distance is one. ∎

## 5. A marked two-dimensional comparison surface

Take a second labelled pair of pants $`B_c`$, with boundary circles $`b_0,c_0,c_1`$, and glue it to $`B`$ along $`b_0`$. The result $`\Sigma`$ is a four-holed sphere with actual holes $`b_+,b_-`$ and auxiliary holes $`c_0,c_1`$. Keep the two auxiliary labels distinct: $`c_1`$ models the chamber containing the one-sided core $`B_*`$, and $`c_0`$ the other end chamber.

Consider essential simple arcs from $`b_+`$ to $`b_-`$, with endpoints free on their labelled boundary circles. At minimum intersection with $`b_0`$, an arc either avoids $`B_c`$, or cuts $`B_c`$ in $`k`$ parallel essential outer-outer waves and $`B`$ in two reaching arcs and $`k-1`$ waves. The cap waves separate $`c_0,c_1`$. Their boundary pairing, in a fixed nested reference position, is $`q(i)=-1-i`$, exactly the $`S`$ pairing. The complementary pattern pairing is the reflection in the joint normal forms with two reaching endpoints. An illegal matching would form closed components, and so cannot be one simple arc.

Replace the $`k`$ cap waves by $`k`$ copies of $`S`$, preserving their boundary pairing and their radial order, and replace the $`B`$ arcs by their $`S^1_\lambda`$ products. Orient the resulting chain from its positive actual boundary, using the sign rule in the joint normal forms along the path. This gives an actual incompressible spanning surface. The zero-wave arc gives $`A`$. This is a construction of assemblies; it is not a homeomorphism from $`Q`$ to a Seifert piece.

### 5.1. Explicit pillowcase coordinates

Fill the four boundary holes temporarily by marked points. Use

```math
\Sigma^\circ=(\mathbb R^2/\mathbb Z^2)/(x\sim-x)
```

with marked points $`P_+=(0,0)`$, $`P_-=(1/2,0)`$, $`C_0=(0,1/2)`$, $`C_1=(1/2,1/2)`$. The arc from $`P_+`$ to $`P_-`$ is the projection of the half of a primitive straight torus circle of vector $`(p,q)`$. Its endpoint condition is precisely $`p`$ odd and $`q`$ even. HT, printed p.232, gives the complete rational classification of these pillowcase arcs. The two marked-point parity conditions are also immediate from $`(p,q)/2`$ modulo $`\mathbb Z^2`$.

Choose $`q=2k>0`$; changing the sign of both coordinates changes no underlying arc. When $`q=0`$, primitivity leaves the one class $`(1,0)`$, called $`\infty`$. In these coordinates $`b_0`$ encloses $`C_0,C_1`$; its two torus lifts are horizontal circles. Minimum intersection with $`b_0`$ is $`2k`$.

The reference diagrams $`\alpha_{k,a}`$ in the joint-normal-form volume may be chosen arbitrarily, except that its linear $`a=0`$ family is chosen compatibly. Here we fix those reference choices explicitly: use the pattern restriction of the straight arc of vector $`(2a+1,2k)`$, and use the fixed nested cap waves as its companion model. These are permitted reference choices for that volume. For a different preselected pattern reference, its $`t`$ is translated by a fixed integer depending on $`k,a`$. Statements about the difference of two $`t`$ values at fixed $`k,a`$ are independent of that change.

To check the anchor formula, put the lifts of $`b_0`$ at $`y=\pm c`$ and let $`c\to1/2`$ from below. The cap endpoints of the straight half-circle tend to

```math
x_j=\frac{p(j+1/2)}{2k},\qquad -x_j,
\qquad 0\le j\lt k.
```

Because $`\gcd(p,2k)=1`$, these are the $`2k`$ points $`(2i+1)/(4k)`$, in cyclic order. Their reflection is $`i\mapsto-1-i`$. The positive reaching endpoint tends to $`p/(4k)`$, so its index satisfies $`p\equiv2a+1\pmod{4k}`$; the other endpoint is antipodal. Each cap wave can be straightened to the fixed nested wave system, with this order retained. The auxiliary labels distinguish the two end gaps.

A positive twist about $`b_0`$ lifts to twists about **both** horizontal torus circles, so it sends $`(p,2k)`$ to $`(p+4k,2k)`$. Fix the sign of $`D_0`$ accordingly. Therefore the marked arc coordinate of the canonical standard form is

```math
p=2a+1+4kt,\qquad \gcd(p,k)=1,
\qquad 0\le a\lt2k.
```

All primitive odd $`p`$ occur, including negative $`p`$. This also checks legality: the matching has one arc and no closed loop exactly when $`\gcd(p,2k)=1`$, equivalently the gcd condition in the joint normal forms. For $`a=0,t=0`$ the straight half-circle gives successive cap waves joined in radial order; it is the linear $`F_k`$ reference of [joint normal forms, §9](parallel-satellites-k719-normal-forms.md).

### 5.2. The marked arc graph is a tree

Two distinct pillowcase arcs with the same two endpoints have disjoint interiors exactly when the determinant of their primitive torus vectors has absolute value two. Their two torus circles necessarily meet at the two common branch points. In straight minimal position they meet $`|\det|`$ times; every additional intersection is away from the branch points and descends to an interior arc intersection. Thus the marked arc edge rule, after writing $`q=2k`$, is

```math
\left|pk'-p'k\right|=1.
```

This includes $`\infty=(1,0)`$: its neighbours have $`k=1`$. The graph $`\mathcal T`$ consequently has vertex $`\infty`$ and all reduced $`p/k`$ with $`k>0`$ and $`p`$ odd; its edges use the displayed determinant. It is the odd-numerator induced subgraph of the Farey graph, not the entire Farey graph.

**Lemma 5.1 (unique parent).** Each $`p/k`$, $`k>0`$, has exactly one neighbour of smaller denominator. There are no edges between equal denominators. Consequently $`\mathcal T`$ is a tree rooted at $`\infty`$.

**Proof.** For $`k=1`$, the unique smaller-denominator vertex is $`\infty`$. For $`k>1`$ let $`r`$ be the inverse of $`p`$ modulo $`k`$, with $`1\le r\lt k`$, and put

```math
(p_1,k_1)=\left(\frac{pr-1}{k},r\right),\qquad
(p_2,k_2)=(p-p_1,k-r).
```

These are the two reduced smaller-denominator Farey neighbours, with determinants $`+1,-1`$. Uniqueness for each sign follows by reducing the determinant equation modulo $`k`$ and then solving for its numerator. Since $`p_1+p_2=p`$ is odd, exactly one numerator is odd. That is the unique parent $`P(p/k)`$ in $`\mathcal T`$. If denominators agree, the determinant is $`k(p-p')`$, an even integer, and cannot be $`\pm1`$.

Following parents strictly decreases nonnegative denominators, and reaches $`\infty`$, so the graph is connected. A finite cycle would have a vertex with largest denominator and two distinct lower neighbours, contradicting uniqueness. Therefore it is a tree. ∎

In particular, genus need not drop by exactly three along an edge. For example, $`3/4`$ has odd-numerator parent $`1/1`$. Thus canonical $`F(4,1,0)`$ is adjacent to $`F(1,0,0)`$, although their $`k`$ values differ by three.

## 6. What three-dimensional boundary motion identifies

We first isolate the full boundary-motion subgroup, and then compute it. No boundary circuit is erased merely from the unmarked HT classification.

Choose the oriented reference $`S`$ in $`Q`$. Let $`H\subseteq\mathbb Z`$ consist of full meridional winding numbers of ambient isotopies of $`Q`$, beginning at the identity and returning this $`S`$ to itself with its orientation. The endpoint preserves both boundary circles individually by [Joint normal forms, Lemma 5.1](parallel-satellites-k719-normal-forms.md). Their winding numbers agree, because a torus isotopy carries their ordered longitude pair without crossings. Longitudinal displacement has no effect on vertical pattern annuli. Concatenation and reversal prove that $`H`$ is a subgroup, so $`H=d\mathbb Z`$ for a unique $`d\ge0`$, with $`d=0`$ meaning the zero subgroup.

**Lemma 6.1 (one common subgroup).** Every oriented reference stack of $`k\ge1`$ copies of $`S`$, with any independent choices of their orientations, has the same meridional return subgroup $`H`$.

**Proof.** A stack-return isotopy preserves each component and each boundary by [Joint normal forms, Lemma 5.1](parallel-satellites-k719-normal-forms.md). Restrict it to one component, then conjugate by a fixed radial identification with the chosen one-piece reference. All boundary windings are the same, so its winding belongs to $`H`$.

Conversely start with a return isotopy of one $`S`$. Take the reference stack in a small two-sided collar of that surface; a radial isotopy places any prescribed parallel stack there. Carry all its levels by the same ambient isotopy. The endpoint preserves the orientation and hence the normal direction of $`S`$. By collar straightening relative to $`S`$, adjust that endpoint in a smaller collar so that it preserves the chosen levels. The adjustment is confined to small normal intervals and adds no full meridional circuit. Every level now returns, with the same winding as the original one-piece surface. It also preserves every independent orientation sign. Conjugate back to the original reference stack. This proves both inclusions, simultaneously for the full stack. ∎

**Lemma 6.2 (the complete equality relation).** In the canonical reference convention,

```math
[F(k,a,t)]=[F(k',a',t')]
\quad\Longleftrightarrow\quad
k=k',\ a=a',\ t'-t\in H.
```

**Proof.** Equality preserves $`k,a`$ by the efficient torus comparison in the joint normal forms and boundary-permutation exclusion. The resulting $`T`$-preserving isotopy restricts to a return isotopy of the full companion stack, with winding $`m\in H`$ by Lemma 6.1. Extend its boundary path into a pattern collar. A full meridional circuit contributes one outer-boundary twist, up to the fixed overall sign convention; longitudinal motion leaves the vertical annuli invariant. After removing this collar transport, the remaining pattern comparison has fixed outer endpoints. [Joint normal forms, Lemma 7.1](parallel-satellites-k719-normal-forms.md) then forces equality of its relative winding integers. Thus $`t'-t\in H`$; the sign convention is immaterial because $`H=-H`$.

Conversely a return motion realizing $`m\in H`$ carries the whole oriented companion stack by Lemma 6.1. Extend the common boundary motion through the pattern collar and retain the actual inner labels. Its endpoint adds the corresponding $`m`$ outer twists. Relative isotopy extension in both pieces gives an ambient isotopy of the whole assembly. Thus all differences in $`H`$ really identify vertices. No independent component motion is used. ∎

Equivalently, $`H`$ acts on the marked arc tree by

```math
T_m(p/k)=(p+4km)/k,\qquad T_m(\infty)=\infty.
```

The action preserves denominator and the determinant edge rule. The following local product argument determines the subgroup, without a normaliser theorem or an unverified surface-bundle assertion.

**Lemma 6.3 (confinement for the one-piece chain).** If two $`k=1`$ standard forms with the same anchor are isotopic in $`M`$, their twisting integers are equal. Consequently $`H=\{0\}`$.

**Proof.** Fix a small two-sided collar $`U=S\times[-\varepsilon,\varepsilon]`$ of the reference companion surface, with its two boundary annuli contained in disjoint proper meridional strips $`J_+,J_-`$ on $`T`$. Represent the two isotopic whole surfaces $`F,H_0`$ with companion pieces at distinct parallel levels of $`U`$. This small radial displacement is extended into the pattern collar; it introduces no full meridional turn. Their common-torus traces are disjoint, and their actual boundaries are chosen disjoint. Each surface remains efficient, with one genus-three companion piece and two reaching annuli.

Apply the finite empty-product-region simplification used in [normalisation, §7](parallel-satellites-normalisation.md), and [joint normal forms, §8](parallel-satellites-k719-normal-forms.md). We check that every move can keep all companion boundary motion inside $`J_+\cup J_-`$. Suppose $`N`$ is one such product region. By the [product-annulus argument](parallel-satellites-normalisation.md), §§6–7 its intersection with $`T`$ has no returning annulus, and all spanning annuli can be straightened to $`\Gamma\times I`$ in its horizontal product coordinates. Thus cutting $`N`$ by $`T`$ gives products of the components of its horizontal face cut by $`\Gamma`$; each lies in $`Q`$ or $`P`$.

If the horizontal face has any portion in $`Q`$, that portion is the **entire** companion piece of that surface. Indeed a face boundary inside $`Q`$ would have to be a collapsed intersection curve, or lie on the actual manifold boundary. The two companion pieces are disjoint, and $`Q`$ contains no actual link boundary, so neither possibility occurs. The product component in $`Q`$ therefore has these two distinct whole $`S`$ pieces as its horizontal faces, and has its remaining boundary on $`T`$. Its interior is disjoint from both pieces. Its frontier is entirely in those pieces or $`T`$, so its interior is a full chamber of their complement in $`Q`$ (the open-and-closed chamber argument).

The connected two-sided $`S`$ separates $`Q`$: otherwise a once-crossing loop would pair its zero relative class by one. Two distinct parallel copies therefore cut $`Q`$ into exactly three connected chambers. Only the **middle** one has both companion pieces in its frontier; the two end chambers have just one apiece. Hence every product component in $`Q`$ is precisely the empty middle parallelism slab, contained in the fixed collar $`U`$. In particular its two vertical annuli on $`T`$ lie inside $`J_+,J_-`$. There is no additional $`Q`$ product component with an empty horizontal face, since after cutting $`\Gamma\times I`$ every component is $`W_i\times I`$ with a nonempty horizontal face. A move whose product region misses $`Q`$ fixes $`T`$.

Perform a $`T`$-tangent product push, supported in this slab and its small collars on the $`Q`$ side. When a non-final push passes one companion level through the other, place its endpoint at a nearby parallel level in $`U`$; this is the usual small push beyond the horizontal face. It leaves the companion pieces distinct and disjoint and introduces no new transverse intersections. All intersections involved in the collapsed boundary of this move lie on the pattern side; choosing the companion endpoint at a small normal level changes none of their usual removal. The fixed surface can remain at its original collar level throughout. Every other part of the move is on the pattern side. Thus after the move the same confinement statement applies again. Product pushes decrease the finite intersection count, or identify the final whole parallel component, exactly as in the normalisation and joint-normal-form proofs. They do not require an intervening independent renormalisation of the pair.

The finite process finishes with the two whole isotopic surfaces coincident. Along the resulting $`T`$-preserving isotopy, both companion longitude traces have remained in their original proper annular strips. Close the initial and final small radial displacements within those same strips. The companion return winding is zero. Remove this zero-winding boundary transport from the pattern comparison; [Joint normal forms, Lemma 7.1](parallel-satellites-k719-normal-forms.md), with fixed outer endpoints and free labelled inner endpoints, forces the two integers $`t,t'`$ to agree.

Finally any $`m\in H`$ identifies $`F(1,0,0)`$ with $`F(1,0,m)`$ by the converse direction of Lemma 6.2. Confinement forces $`m=0`$. Conversely zero is realised by the constant isotopy. Thus $`H=\{0\}`$. ∎

Combining Lemmas 6.1-6.3 gives the requested closed formula, including all actual full meridional motions:

```math
[F(k,a,t)]=[F(k',a',t')]
\quad\Longleftrightarrow\quad
(k,a,t)=(k',a',t').
```

At fixed $`k,a`$, the only twist equivalence is $`t=t'`$. Longitudinal rotations are realised by extending the longitude boundary vector field to a field tangent to each companion piece and to $`T`$; its flow preserves the whole stack as a set. Their pattern extension preserves every vertical annulus as a set. They therefore act trivially on $`t`$. Half rotations and component exchanges are excluded by the joint normal forms; full meridional return circuits have now been excluded by the confinement proof, for every oriented stack via Lemma 6.1.

## 7. Lifting and descending every actual edge

**Theorem 7.1 (the complete graph isomorphism).** The marked arc assembly is a graph isomorphism from $`\mathcal T`$ onto the full subgraph on $`A`$ and the chain vertices. In particular an actual edge is present if and only if the corresponding marked arcs have disjoint representatives.

**Proof.** The marked-arc assembly construction is onto by the [covering theorem](parallel-satellites-k719-normal-forms.md), Theorem 7.2 and Section 5's coordinate calculation. Its vertex fibres are singletons by Lemmas 6.2-6.3.

First take two distinct actual adjacent vertices. By Corollary 3.2 they have disjoint representatives. Lemma 4.1 essentialises their joint cut system and verticalises their entire pattern annulus system. For a pair of chains, the joint HT classification puts their **whole companion union** into one parallel $`S`$ stack. Keep the assignment of pieces to each surface, their radial order, signs and common boundary matching. Replace every member of this joint stack by the corresponding nested cap wave in $`B_c`$. The two complete components become two disjoint $`b_+`$-to-$`b_-`$ arcs in $`\Sigma`$. Each has no closed component, since its original whole assembly had none. Forgetting one arc, its cap waves can be radially normalised to the fixed cap model; doing the corresponding radial motion of its companion pieces gives the canonical assembly of that arc. The original joint normalisation and this radial motion are genuine compatible piece isotopies. Consequently the arc maps to the original vertex, rather than merely to a surface with the same genus. Thus the actual edge lifts to a marked arc edge.

If one vertex is $`A`$, the same argument uses no cap waves for that component. Alternatively cutting along the actual annulus leaves $`Q`$ with a collar; HT permits a disjoint connected two-longitude surface only of genus three. The [cone volume](parallel-satellites.md), §3, constructs disjoint annuli for every $`k=1`$ chain. This is exactly the root-edge rule of $`\mathcal T`$.

For the converse take disjoint marked arcs. Minimise the total intersection of their disjoint union with $`b_0`$ by empty innermost bigon removal, keeping both arcs disjoint. Their cap-wave union is a simultaneous nested system. Replace that system by one actual parallel $`S`$ stack, keeping the two assignments, and use the simultaneous vertical pattern annuli. This builds two disjoint whole spanning surfaces whose vertices are those of the two arcs. Both chain surfaces, or the annulus if present, are connected. Corollary 3.2 gives representative width one and class distance one for distinct vertices. This also proves that the use of a marked arc edge is sufficient for cyclic adjacency, rather than only geometric disjointness. ∎

The full cyclic criterion can now be stated for all vertex pairs:

- $`A,G`$ are adjacent.
- $`A,F(k,a,t)`$ are adjacent exactly when $`k=1`$.
- $`G`$ and any chain are not adjacent.

For two distinct chain vertices, put $`p=2a+1+4kt`$, $`p'=2a'+1+4k't'`$. They are adjacent exactly when

```math
\left|pk'-p'k\right|=1.
```

The chain criterion can equivalently be written without $`p,p'`$:

```math
\delta(F(k,a,t),F(k',a',t'))=1
\quad\Longleftrightarrow\quad
 t=t',\qquad
\left|k'(2a+1)-k(2a'+1)\right|=1.
```

Indeed put $`b=k'(2a+1)-k(2a'+1)`$. The chosen residue ranges give $`|b|\le4kk'-(k+k')`$. If $`t-t'\ne0`$, then $`|b+4kk'(t-t')|\ge k+k'\ge2`$. Thus an edge cannot change $`t`$. It also cannot cross $`a=k`$: when one $`a`$ is below its $`k`$ and the other is at least its $`k'`$, the base fractions lie on opposite sides of the even integer two, and their determinant has absolute value at least $`k+k'`$.

These are pure integer criteria in the explicitly fixed canonical reference convention. Removing $`A`$ leaves separate chain branches indexed by $`t\in\mathbb Z`$ and the two ranges $`a<k`$, $`a\ge k`$. Their roots are $`F(1,0,t)`$ and $`F(1,1,t)`$, respectively. The following section supplies each lower neighbour and proves its uniqueness.

## 8. A concrete unique lower neighbour and the descending links

For a canonical representative $`F(k,a,t)`$ compute $`p=2a+1+4kt`$ and its odd-numerator Farey parent $`p_*/k_*`$ by Lemma 5.1. If $`k_*=0`$, set $`D(F)=A`$. Otherwise define

```math
a_*\equiv\frac{p_*-1}{2}\pmod{2k_*},\qquad
0\le a_*\lt2k_*,\qquad
t_*=\frac{p_*-(2a_*+1)}{4k_*},
\qquad D(F)=[F(k_*,a_*,t_*)].
```

Set $`D(G)=A`$. The integer $`t_*`$ exists by the chosen residue, and legality follows from the determinant-one parent equation. This is an explicit assembled surface, not a statement that an unspecified neighbour exists.

**Theorem 8.1 (well-defined descent and complete adjacency test).** The displayed lower neighbour depends only on the actual vertex. Every vertex other than $`A`$ has exactly one lower neighbour for the nonnegative height $`h(A)=0`$, $`h(G)=1`$, $`h(F)=k`$. There are no edges between chain vertices of the same height. For two chain vertices of different heights, the lower one is adjacent to the higher one exactly when it equals the computed $`D`$ of the higher one. Equality is the coordinate equality of Section 6; [Joint normal forms, Theorem 8.2](parallel-satellites-k719-normal-forms.md) remains an independent geometric test.

**Proof.** Every $`T_m`$ is a denominator-preserving automorphism of the marked tree fixing its root. It therefore preserves the unique-parent rule:

```math
P(T_m v)=T_m P(v).
```

Lemma 6.3 gives $`H=\{0\}`$, so the canonical coordinates already specify a unique vertex. Parent equivariance also shows that the descent would be well-defined on any common return subgroup quotient; no arbitrary choice on a simplex is hidden here.

Every actual edge corresponds to a marked edge by Theorem 7.1. Unequal marked endpoints have unequal denominators, and the lower endpoint is exactly the parent's marked vertex. The unique canonical coordinate supplies precisely that parent, and parent equivariance records independence from a common twisting change of reference. Thus there is precisely one actual lower neighbour. Conversely its marked parent edge supplies an actual edge, since different denominators forbid equality. The assertions involving $`G`$ follow from its leaf property. ∎

With the chain height $`u=k-1`$, the same result applies to every $`k\ge2`$ chain: it has one lower neighbour, possibly jumping over several heights. Its full descending link is a single vertex, hence contractible. The height $`h`$ above includes the annulus and the $`k=1`$ base layer in one ordering.

This criterion covers $`|k-k'|\le1`$ and every other difference, every anchor and every twisting value. It does not assume that independently selected normalisations preserve a previously chosen simplex.

## 9. Contractibility of the entire flag complex

**Theorem 9.1.** The entire $`X(L)`$ is a tree and is contractible.

**Proof.** By Theorem 8.1, the graph $`\mathcal T`$ is connected: repeatedly taking the unique lower neighbour strictly decreases positive denominator and reaches $`A`$. A finite cycle in it would have a vertex with largest denominator and two different lower neighbours. Equal-denominator edges are impossible, so this contradicts uniqueness. Hence it is a tree. Add $`G`$ with its unique edge to $`A`$; the full graph remains a tree.

A tree has no clique of three distinct vertices. Its flag completion therefore adds no higher simplex. In particular there is no missing simplex-compatibility issue: the full simplicial complex is exactly this one-dimensional tree.

Its realization has the weak simplicial topology. Contract each point toward $`A`$ along its unique finite edge path, moving its distance to the root from $`s`$ to $`(1-t)s`$. On each closed edge and time interval this map lies in a finite rooted subtree and is continuous. The weak CW topology, with compact interval factor, gives continuity of the resulting map on the full realization times the interval. It fixes $`A`$ and reaches $`A`$ at time one. Thus it is a contraction of the entire complex, including all genera and all twisting values. ∎

The proof does not infer noncontractibility from a failed cone or a local cycle, and does not use any PS projection or contraction theorem. The complete-block argument first establishes precisely the edges; the graph isomorphism with the marked arc tree then establishes the topology.

## 10. What is and is not completed

The closed twist equivalence is $`t=t'`$ at fixed $`k,a`$: the one common return subgroup is zero by Lemma 6.3. Section 7 gives the complete pure integer adjacency table, with the full cyclic-cover upper and lower bounds proved before the arc comparison. The entire-tree contraction includes all parameters and simplices by flag completion. The confinement, joint normalisation, both directions of edge correspondence and infinite-tree contraction have been rechecked against their stated inputs.

The numerical formulas use the explicit pillowcase pattern references fixed in Section 5.1. For an older arbitrary reference choice, determine its relative winding shift $`c_{k,a}`$ from its actual pattern arcs: concatenate its positive reaching arc with the reversed canonical reaching arc, closing their inner endpoints along $`b_+`$, and take the coefficient of $`[b_-]`$ in $`H_1(B)`$. Choose its sign so that one $`D_0`$ contributes $`+1`$. Motion on $`b_+`$ contributes zero to this coefficient. Then $`t_{\mathrm{canonical}}=t_{\mathrm{old}}+c_{k,a}`$ and $`p=2a+1+4k(t_{\mathrm{old}}+c_{k,a})`$. This is a relative-path homology computation for the supplied diagram, not another isotopy equivalence. The joint-normal-form volume left the reference diagrams for general $`a`$ arbitrary; this manuscript fixes them explicitly.

The same marked-tree proof applies to another companion only if the following actual structural inputs hold: all essential longitudinal systems are simultaneous pure stacks of one single-boundary type or one separating two-boundary type; mixed systems are impossible; the two-boundary pairing is the nested reflection with individually fixed boundary circles under return isotopies; efficient isotopy comparison holds; and the single-boundary assemblies give a controlled base subcomplex. Merely knowing that there are two possible boundary counts does not prove these stronger inputs. No unrestricted general-companion theorem is asserted here.

The integer identities admit finite arithmetic checks, but those do not establish three-dimensional edge lifting, the boundary-motion subgroup or contractibility. The geometric and topological proofs are in §§3–9. No proof-assistant formalisation or three-dimensional product-recognition implementation is asserted.
