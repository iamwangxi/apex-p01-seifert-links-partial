# Parallel satellites: geometric normalisation and torus comparison

[Overview](../README.md) · [Objects](objects.md) · [Sources](../sources/bibliography.md) · [Scope](scope.md)

## 1. Two-parallel model and comparison statement

Let $`C=K_{7/19}`$, a nontrivial companion, $`Q=E(C)`$, and $`P=S^1_\lambda\times B`$ for a pair of pants with outer boundary $`b_0`$ and two labelled inner boundaries. Glue $`P`$ to $`Q`$ along $`T=S^1_\lambda\times b_0`$, where $`\lambda`$ is the preferred companion longitude. The actual boundary signs are $`+\lambda,-\lambda`$. Surfaces have no closed components and one prescribed boundary per actual torus. Isotopies may move boundaries.

The arguments below are the essential-cut, joint-straightening, reverse-assembly and product-annulus interfaces used in the [joint longitudinal classification](parallel-satellites-k719-normal-forms.md) and [tree calculation](parallel-satellites-k719-tree.md). Their application to the two-parallel model retains exactly the hypotheses used in those proofs.

**Theorem 1.2 (efficient isotopy comparison).** Two efficient representatives which are ambient isotopic admit an ambient isotopy preserving $`T`$ setwise. Here efficiency is defined in §7. This is an existence assertion for a comparison isotopy, not a claim that a given isotopy is continuously normalised.

## 2. Literature inputs

Hatcher's 3-manifold notes supply the Loop Theorem consequence, irreducibility gluing and Lemma 1.11/Proposition 1.12, pp. 13–15, 20–22, 59. Banks arXiv:1109.0965v1 supplies Definition 4.1 and Proposition 4.2, p. 5, and the empty-product-region comparison, Lemma 7.3, p. 15. PS §3, pp. 1494–1495, supplies simplification with coincident whole components. No projection or contractibility conclusion of PS §§4–7 is used. The product-annulus arguments needed for preservation of $`T`$ are proved in §6.

## 3. Essential intersection and cut pieces

The pattern $`P`$ is irreducible: cutting it along a base-cutting system of incompressible vertical annuli gives a solid torus, and Hatcher's cutting fact, printed pp.14–15, transfers irreducibility back. All its boundary tori are incompressible: their groups are $`\langle f,c_i\rangle\cong\mathbb Z^2`$ in $`\mathbb Z\times\pi_1(B)`$, and each peripheral $`c_i`$ has infinite order. The companion $`Q`$ is irreducible and boundary-incompressible because $`C`$ is nontrivial. Gluing along these incompressible torus boundaries makes $`M`$ irreducible and preserves the injections of the two piece groups and all the displayed torus groups. This is the usual amalgam normal form and the sphere-cutting argument in Hatcher pp.13–15. In particular $`T`$ is incompressible and $`M`$ is boundary-irreducible and Haken.

There are no disk spanning components, since their prescribed longitudes are nontrivial in the injected actual boundary-torus groups. Each component of $`F`$ is boundary-incompressible by Hatcher Lemma 1.11: a boundary-parallel annulus would use two curves on a single actual boundary torus, whereas $`F`$ uses that torus once. Thus the product-region theorem applies to the entire system, independently of genus.

The surface-bundle exception to product-region simplification cannot occur. The total linking homomorphism $`\phi`$ vanishes on $`\pi_1(T)`$, while that subgroup injects as $`\mathbb Z^2`$. A spanning fibration would have a compact fibre with boundary and hence a free kernel group, which cannot contain this $`\mathbb Z^2`$. A spanning component with only some actual boundary labels cannot itself be a fibre of all of $`M`$, since a fibre meets every boundary torus.

**Lemma 3.1.** At minimum intersection every intersection circle is essential both in $`F`$ and in $`T`$. Every cut surface component is incompressible in its ambient piece and has nonempty boundary. No cut component is a disk.

**Proof.** An inessential circle on either incompressible surface is inessential on the other. Choose an innermost disk on $`T`$, and the disk it bounds on $`F`$. Their sphere bounds a ball. No whole component of $`F`$ can lie in this interior ball, since each has boundary on $`\partial M`$; the rest of the component carrying the disk is also outside it. The usual disk-push removes this intersection, contradicting the minimum. This is the innermost-disk argument of Hatcher pp.13–15, with the no-closed-component condition supplying the stated safeguard.

Cutting a surface along essential circles makes each resulting subsurface $`\pi_1`$-injective in that surface. The Loop Theorem turns incompressibility of $`F`$ into $`\pi_1(F)`$-injectivity in $`M`$. Hence a cut component injects into $`M`$, and therefore into its own ambient piece. A closed cut component would already be a closed component of $`F`$. A disk cut component would have boundary either an essential intersection circle or a nontrivial actual longitude, both impossible. $`\square`$

We give the elementary annulus facts used in eliminating the boundary-parallel alternative.

**Lemma 3.2 (primitive annuli in a solid torus).** In $`S^1\times D^2`$, a finite disjoint system of incompressible annuli whose boundary curves have longitudinal degree one can be simultaneously straightened to $`S^1`$ times disjoint proper disk arcs, after first straightening its boundary. The subsequent isotopy fixes that boundary. A subcollection having all its boundary on a fixed boundary annulus therefore has an innermost annulus parallel to a subannulus of that boundary annulus, with empty parallelism interior.

**Proof.** Straighten the primitive boundary curves to the circle-fibre slope by a solid-torus coordinate change. A meridian disk meets each of the two boundary circles of each annulus once. Remove closed intersections with the annulus system by the innermost-disk/ball argument; no such circle can be essential in an incompressible annulus, since it bounds a disk in the solid torus. What remains on each annulus is exactly one spanning arc, because it has just those two boundary endpoints. Cut the solid torus along the meridian disk. Each annulus becomes a disk in a ball. Its boundary is the same as that of the product rectangle on its trace arc in the meridian disk. The relative disk isotopy theorem in a ball (Hatcher, printed p.20) straightens the disjoint disk system, successively taking outermost disks. This glues to the claimed simultaneous isotopy. In the disk model a finite collection of disjoint arcs with ends on a fixed boundary interval has an innermost arc and an empty disk between it and that interval. Taking its circle product proves the last assertion. $`\square`$

**Lemma 3.3.** Minimum-intersection cut pieces contain no boundary-parallel annulus. Thus all cut components are boundary-incompressible.

**Proof.** By Hatcher Lemma 1.11, a boundary-compressible cut component could only be a boundary-parallel annulus. Its two boundary circles cannot lie on an actual link torus, since that torus is used once. They must lie on $`T`$.

Suppose such a cut annulus bounds an annular parallelism solid torus $`R`$ with a subannulus of $`T`$. Other parts of the cut surface inside $`R`$ have boundary on that $`T`$-subannulus. Their groups inject into $`M`$ by Lemma 3.1 and hence into $`R`$; as $`\pi_1(R)=\mathbb Z`$, they are annuli. Their boundary curves are the generator slope of this annular product. Lemma 3.2 supplies an innermost annulus with empty parallelism interior. Push it through that product and slightly across $`T`$. There is a thin empty collar beyond the open $`T`$-subannulus, so this is an ambient isotopy of the whole surface removing two intersection circles. This contradicts minimality. Apply Lemma 1.11 again to the remaining alternatives. $`\square`$

## 4. Why no non-longitudinal boundary can occur

The two prescribed actual boundary slopes are $`\epsilon_i f`$: the chosen zero framing makes pairwise linking numbers zero, so the spanning longitude of the oriented whole link is its individual preferred longitude. On $`T`$, the same $`f`$ is $`\lambda_C`$.

**Lemma 4.1.** Every pattern component meeting an actual link torus is a vertical annulus, and either connects two actual link tori or connects one actual link torus to $`T`$.

**Proof.** Lemmas 3.1 and 3.3 make the component essential in Hatcher's precise sense. By Proposition 1.12 it is vertical or horizontal. A horizontal component has boundary of nonzero geometric intersection with the fibre slope on every boundary torus it meets. Its prescribed actual fibre boundary excludes that case. A vertical component with boundary is an annulus. $`\square`$

Suppose $`F\cap T\ne\varnothing`$. At least one of the two actual-boundary components of $`F\cap P`$ must reach $`T`$. Otherwise these pattern components form the inner-to-inner annulus, already complete components of $`F`$; every remaining component of $`F`$ would have no actual boundary, contrary to the hypothesis. The reaching annulus has longitude slope on its outer end.

All essential disjoint curves on a torus have one common unoriented slope. Therefore **every** circle of $`F\cap T`$ is longitudinal. This argument covers all minimum representatives and every genus. It does not infer a slope from the vanishing of $`\phi|_T`$.

Now every pattern component, including one having only outer boundary, has fibre boundary. Lemma 3.3 and Proposition 1.12 again exclude horizontal components. A closed pattern component is impossible by Lemma 3.1. Hence the entire pattern surface consists of verticalisable annuli.

The oriented total boundary of the pattern surface is zero in $`H_1(P)`$. Since its boundary circles are all copies of the nonzero class $`f`$, and the inner signed sum is $`1-1=0`$, its outer signed sum is also zero. Thus the $`2n`$ outer circles consist of $`n`$ in each orientation.

Equivalently, the meridian-total homomorphism is zero on all of $`\pi_1(Q)`$, not just on $`\pi_1(T)`$: a companion meridian has total linking $`\sum\epsilon_i=0`$, and $`H_1(Q)`$ is meridionally generated. The restriction of the dual surface class is therefore $`[S]=0\in H_2(Q,T)`$. The injective boundary map of this knot-relative group identifies this with the zero oriented longitude sum.
## 5. Simultaneous pattern normal form and the local objects

For clarity, separate verticalisability of individual annuli from simultaneous verticalisation.

**Lemma 5.1.** The whole pattern annulus system can be verticalised, keeping its already straightened fibre boundary fixed.

**Proof.** Choose disjoint base arcs cutting $`B`$ to a disk, with endpoints avoiding all the finitely many pattern-boundary endpoints. Their circle products are cutting annuli. Boundaries of these cutting annuli miss the boundary of the pattern system, so intersection consists only of circles. Remove inessential circles by innermost-disk isotopies of the whole system. The replacement disk can be chosen close to the innermost disk on one cutting annulus and disjoint from all the other cutting annuli; its boundary already misses them. Thus the replacement removes, rather than creates, any intersections on the replaced surface disk with the other cutting annuli, and the total finite circle count decreases. A remaining circle is essential on each of the two annuli: otherwise injectivity of their fibre cores would contradict its being essential on the other.

Straighten these intersection circles to fibres in the cutting annuli and extend over collars. Cut along the cutting annuli. The ambient product is now a solid torus. Cutting the pattern annuli along their essential core circles produces annuli, with fibre boundary, whose groups inject into this solid torus (they inject into their original annulus and hence into $`P`$). Lemma 3.2 straightens them all relative to the cut boundary. The straightened traces match on the cut faces, so the isotopies glue back to a simultaneous vertical annulus system $`S^1_f\times a`$. All boundary-parallel base arcs are excluded by Lemma 3.3. $`\square`$

**Lemma 5.2 (reverse assembly).** Any compatible essential pattern-annulus and longitudinal companion pair $`A,S`$, with opposite gluing orientations and the prescribed actual boundaries, glues to an incompressible spanning surface, provided the no-closed-component condition after gluing holds.

**Proof.** For a hypothetical compression disk minimise its intersections with $`T`$. Closed disk intersections can be removed using incompressibility of $`T`$ and irreducibility. An outermost remaining disk arc gives a boundary-compression of a cut surface component. Boundary-incompressibility makes its surface arc boundary-parallel; the resulting surface disk permits the usual disk replacement eliminating that intersection arc, contrary to minimality. Eventually the compression disk lies entirely in one piece and contradicts incompressibility there. This argument applies to each glued component, including a companion component with many boundary circles. The prescribed orientations and boundary labels give exactly the spanning boundary. $`\square`$

## 6. The product-annulus facts needed for global isotopy

We now verify the additional ingredient which is automatic for Banks's single product disk but is not automatic for a torus.

**Lemma 6.1 (returning and spanning annuli in a horizontal product).** Let $`N=W\times I`$, where $`W`$ is a compact orientable surface with nonempty boundary. Let $`\mathcal A`$ be a disjoint system of incompressible proper annuli in $`N`$, with boundary in the interiors of $`W\times\{0,1\}`$ and disjoint from the vertical boundary.

1. An annulus with both boundary circles on the same horizontal face is parallel to a subannulus of that face. Among returning annuli in that parallelism region there is one with empty parallelism interior and no other annulus boundary in the face subannulus.
2. If no annulus returns to the same face, $`\mathcal A`$ can be simultaneously straightened to $`\Gamma\times I`$. The straightening keeps the horizontal faces setwise and is supported away from the vertical boundary.

**Proof of (1).** Projection to $`W`$ makes the two boundary curves freely homotopic up to reversal. They are essential simple curves, hence cobound a subannulus $`R`$ of that face. Slightly push $`R`$ inside $`N`$ and join it to the returning annulus to form a torus $`U`$.

The product $`N`$ is an irreducible handlebody and $`\pi_1(N)=\pi_1(W)`$ is free. Thus $`U`$ cannot be incompressible, by the Loop Theorem; Hatcher's compressible-torus fact, printed p.14, says it bounds a solid torus or lies in a ball. The latter is excluded by the nontrivial core represented by its horizontal curve. The annular slope has longitudinal degree one in the resulting solid torus: if its degree were $`|d|>1`$, that essential simple curve would be a proper $`d`$th power in $`\pi_1(W)`$; if $`d=0`$, it would be trivial there. An essential simple curve in a surface with boundary is not a proper power. For a separating curve this also follows from an adapted surface presentation: its cyclically reduced boundary word is a product of distinct boundary letters and commutators, with a participating oriented letter occurring once, so it cannot be a repeated word. The nonseparating case is primitive in an adapted basis.

Degree one identifies the solid torus as the collapsed annular product between the two annular faces. Move its face $`R`$ back to the horizontal boundary. The product then meets that horizontal boundary exactly in $`R`$ and misses the opposite horizontal face and the vertical boundary. Other annuli inside it therefore have both their boundaries on $`R`$; none can exit through the returning face or the ambient boundary. Their boundary curves have this same primitive slope. Lemma 3.2, applied inside this solid torus, gives an innermost empty annular product with a subannulus of $`R`$. Its face subannulus contains no other annulus boundary. This proves the required innermost version as well.

**Proof of (2).** A spanning annulus gives a homotopy between its lower and upper essential simple boundary curves. Thus the two horizontal curve **systems**, including multiplicities, are isotopic as unlabelled curve systems in $`W`$. Isotope the horizontal faces to make both systems the same $`\Gamma`$, without assuming a matching permutation between parallel copies. The annulus straightening below will supply the compatible matching.

Choose proper arcs cutting $`W`$ into disks and put $`\Gamma`$ in minimal position with them. Consider their product disks. Remove circle intersections with $`\mathcal A`$ by the disk/ball argument. An intersection arc with both ends on one horizontal edge of a product disk has both ends on the one boundary circle of its annulus on that face; it is boundary-parallel in that annulus. An outermost such product-disk arc, together with this annular disk, would make a bigon between $`\Gamma`$ and a cutting arc in the horizontal surface. The bigon loop is null-homotopic in $`W`$, since that face is a homotopy equivalence of $`N`$. This contradicts the chosen surface minimal position. Therefore all remaining product-disk arcs span between horizontal faces.

On a product disk a disjoint family of spanning arcs pairs lower and upper endpoints in their order; it can be straightened to vertical arcs. The annuli cut along these arcs are disks in the remaining balls. An annulus missing every cutting disk would have trivial core in such a ball, which is impossible. The disk boundaries are now precisely those of the rectangles on the cut $`\Gamma`$-arcs. Simultaneous relative disk isotopy in each ball makes these rectangles standard. Glue the balls and disks back. This proves $`\mathcal A=\Gamma\times I`$ after ambient isotopy and also proves compatibility for parallel-copy matching. $`\square`$

The same lemma applies to a product region $`(W\times I)/{\sim}`$ with collapsed vertical boundary as in Banks Definition 4.1. All annuli under consideration miss that collapsed locus and the remaining vertical boundary. Trim a boundary collar of $`W`$ away from their compact traces, apply the product lemma there, and extend by the identity; the horizontal faces remain setwise preserved.

## 7. Relative torus comparison, not just separate normal forms

Call a representative **efficient** here if its intersection circles are essential, all have longitude slope, and all cut surface components are incompressible and boundary-incompressible and are not boundary-parallel annuli. Minimum representatives are efficient by §§3–4. Compatible assemblies in Lemma 5.2 are efficient as well: a cut boundary circle is essential in its local surface and nontrivial in $`M`$, so remains essential in the glued surface.

**Lemma 7.1.** A parallelism/product region between two efficient representatives can be used for a surface simplification while preserving $`T`$ setwise.

**Proof.** First move the longitude multicurves slightly on $`T`$ so the two traces are disjoint, and choose disjoint boundary curves on the actual link tori. These are $`T`$-preserving collar isotopies. Make the surfaces transverse elsewhere, allowing already common components to remain common. Take one of the embedded product regions of the usual product-region simplification, with horizontal surface $`W`$. Its interior is disjoint from the full two surface systems, as required in Banks Definition 4.1. The possible collapsed locus misses $`T`$, because the two traces on $`T`$ are disjoint.

Cutting $`T`$ by its two parallel longitude traces gives annuli. Consequently its intersection with this product region is a finite system of proper annuli, unless a whole component $`T`$ lies inside the region. The latter is impossible: $`W`$ has boundary, since it is a subsurface of a spanning component with boundary, and the product-region group is free, whereas $`\pi_1(T)=\mathbb Z^2`$ injects into $`M`$ and would therefore inject into that free group. The annulus cores are nontrivial in the product region, for the same injectivity reason.

No annulus can return to one horizontal face. Otherwise Lemma 6.1(1) supplies an innermost product to a face subannulus $`R`$, with interior free of $`T`$ and with no extra $`T`$-trace in $`R`$. The interior is also free of both surface systems. Hence $`R`$ is a complete annulus cut piece of one of these surfaces, parallel to a subannulus of $`T`$ in a cut piece of $`M`$. This contradicts efficiency. Notice that this eliminates **returning annuli**; merely counting the total circles on the two faces would not do so.

All the annuli therefore span. By Lemma 6.1(2) they are product annuli $`\Gamma\times I`$, after a change of product coordinates which preserves the horizontal faces. The ordinary product-region push can now be performed with a vector field tangent to these product annuli. Extend it over the small end collars tangentially to $`T`$, and over the complement by isotopy extension. Conjugating back by the coordinate change gives a simplification supported near the original region which preserves the original $`T`$ setwise. It has exactly the usual intersection reduction, or identifies a whole pair of parallel components. $`\square`$

**Proof of Theorem 1.2.** Use the finite product-region simplification described in PS §3 and used in Banks Lemma 7.3. Each move decreases the transverse intersection count or identifies a full corresponding component; already identified components are retained as common components. The definition of each simplification region uses the full systems, so its interior is free of these components. Replace every move by the $`T`$-preserving move of Lemma 7.1. Efficiency is preserved, because such a move restricts to an isotopy in each fixed cut piece. Boundary traces can be kept disjoint except on already common components.

The resulting systems have simplified intersection. Corresponding components which are isotopic must then coincide; this is exactly the coincident-component convention of PS §3, printed p.1494. Equivalently, a still unpaired isotopic component supplies another product region by the parallelism theorem. Finite iteration therefore finishes at the given target system. Concatenate the $`T`$-preserving moves. This proves the existence of the required isotopy, without normalising the initially supplied isotopy at all its times. $`\square`$

The same proof compares any two efficient globally isotopic representatives. In particular an efficient assembly from Lemma 5.2 has the same number of $`T`$-circles as a minimum representative, so its number is already the minimum.

**Precise gluing consequence.** Take the actual pairs $`(A,S)`$ with a common boundary multicurve and actual matching, and quotient by paths of pairs having common boundary throughout. A path restricts to compatible piece isotopies and conversely extends ambiently, first extending its common boundary motion in collars and then using relative isotopy extension in each piece. Theorem 1.2 and the preceding observation show that this quotient classifies the global isotopy classes in the model. It is an equality of isotopy equivalence relations, not a computation of the boundary-motion stabilisers.

Thus the number of circles, their balanced cyclic sign word (up to cyclic rotation), and the local **system** classes with their boundary-motion orbit are intrinsic. Individual component classes or arbitrary independent boundary lifts cannot replace that orbit. No assertion that the remaining gluing fibre is $`\mathbb Z^k`$ or a product of ordinary Kakimizu complexes is made.
