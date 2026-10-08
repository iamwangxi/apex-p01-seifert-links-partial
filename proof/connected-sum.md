# Banks connected sums: an audit for all incompressible spanning surfaces

[Overview](../README.md) · [Objects](objects.md) · [Sources](../sources/bibliography.md) · [Scope](scope.md)

## 1. Statement and conventions

Work with tame, oriented, properly embedded surfaces in compact link exteriors, and ambient isotopies starting at the identity. Boundary tori retain their labels, but boundary curves may move. A spanning surface has one oriented spanning boundary on every link torus and no closed component. It may be disconnected; incompressibility is componentwise.

For an oriented link $`J`$, let $`\phi_J:\pi_1(E(J))\to\mathbb Z`$ send every oriented meridian to $`1`$. Write $`\alpha_J`$ for its dual relative class. For spanning surfaces $`S,R`$, choose a connected lift $`V_R`$ of the **entire** complement $`E(J)\setminus R`$, and translates $`V_{S,n}=\tau^nV_{S,0}`$. Put

```math
\delta(S,R)=\max\{n:V_R\cap V_{S,n}\ne\varnothing\}
             -\min\{n:V_R\cap V_{S,n}\ne\varnothing\},
\qquad
\delta([S],[R])=\min_{S',R'}\delta(S',R').
```

The minimum is over representatives of the two specified isotopy classes. The sets here are open complement blocks; closures are used only when taking frontiers. Each overlap-index set is a finite interval: a path in a connected complement block cannot skip an intermediate cut block. Thus “exactly two lifts” is equivalent to width one. Define $`X(J)=IS_{\mathrm{cyc}}(J)`$ to have all the above incompressible isotopy classes as vertices, an edge on distinct vertices with $`\delta=1`$, and all simplices prescribed by flag completion. Realizations have the usual weak simplicial topology.

**Theorem A (audited Banks 10.3).** Let $`J_1,J_2`$ be oriented non-split links, neither fibred for $`\alpha_{J_i}`$. Specify a component in each link and take their oriented connected sum. There is a choice-dependent vertex bijection

```math
V(X(J_1\#J_2))\longleftrightarrow
 V(X(J_1))\times V(X(J_2))\times\mathbb Z.
```

It identifies the complex on the left with the ordered product triangulation constructed in Banks §§5–9, and induces a homeomorphism

```math
|X(J_1\#J_2)|\cong |X(J_1)|\times|X(J_2)|\times\mathbb R.
```

The integer records the winding of the connecting rectangle **after relative representatives in the factors have been chosen**. This statement covers every genus and disconnected spanning systems. It does not assert a categorical simplicial product with independent arbitrary edge choices.

**Theorem B (four-fibre consequence, including fibre knots).** Let $`H_4`$ consist of four regular fibres of the positive Hopf fibration, with orientation signs $`(+,+,-,-)`$. Insert arbitrary oriented knots $`K_i`$ into four disjoint local balls, one on each labelled component. Set

```math
L=H_4\#_1K_1\#_2K_2\#_3K_3\#_4K_4,
\qquad
I=\{i:K_i\text{ is non-fibred}\},\qquad m=|I|.
```

Then

```math
|X(L)|\cong |X(H_4)|\times\prod_{i\in I}|X(K_i)|\times\mathbb R^m.
```

Every fibre-knot factor has a one-vertex $`X(K_i)`$. Thus equivalently the product may include all four $`X(K_i)`$ factors, while the Euclidean exponent remains $`m`$. In particular, **if all four knots are non-fibred**, the formula specialises to

```math
|X(L)|\cong |X(H_4)|\times\prod_{i=1}^4|X(K_i)|\times\mathbb R^4.
```

An unknot is allowed and contributes neither a factor nor a winding coordinate. No assumption about uniqueness or minimal genus of a non-fibred knot's incompressible surfaces is imposed.

## 2. Sources and audited conventions

The source codes B, PJ (journal PS), PV (PS preprint), K, H and HA are defined in the [bibliography](../sources/bibliography.md). Banks Definitions 2.1 and 10.1 agree with the spanning conventions above. In particular ordinary ambient isotopy allows boundary movement, all closed components are excluded, disconnected surfaces are allowed, and edges and flag completion are the cyclic ones. The source actually checked is arXiv:1109.0965v1 (5 September 2011), including Theorem 10.3 on p. 22.

## 3. The PS inputs extend without using a projection

### 3.1. Boundary-incompressibility and complete complement blocks

For a non-split link other than the unknot, the exterior is irreducible and boundary-irreducible, as required in B Remark 4.3, p. 6. Every component of an incompressible spanning system is boundary-incompressible. Indeed H Lemma 1.11 leaves only the boundary-parallel-annulus exception, whose two boundaries lie on the same torus. Our whole system has only one boundary on each torus, so the exception is impossible. This is independent of Euler characteristic. There are no sphere components because all closed components have already been excluded.

The complement of the entire spanning system is connected, also without a norm assumption. On a torus the complement of its one essential boundary curve is connected and joins the two normal sides. Each surface component has nonempty boundary, so its two sides belong to the same complement chamber. The dual chamber graph consequently has no edge joining distinct chambers; connectedness of the exterior leaves one chamber. Every loop in this complement has $`\phi_J=0`$, by intersection with the surface system. Its connected lifts therefore form the translates of a complete cut block. No separate deck shift for an individual component is allowed.

The metric facts used below are elementary block facts, not path-metric equalities. For three fixed systems, if $`V_R`$ overlaps the $`S`$ blocks in indices $`[a,b]`$, and $`V_T`$ overlaps the translates of $`V_R`$ in indices $`[p,q]`$, every overlap of $`V_T`$ with an $`S`$ block has index in $`[a+p,b+q]`$. Choose a point of the overlap off the middle surface to see this. Hence

```math
\delta(S,T)\le (b-a)+(q-p)=\delta(S,R)+\delta(R,T).
```

For isotopy classes, fix a minimizing middle representative and minimize the two pairs in turn; an ambient isotopy can always carry a selected representative of that middle class to the fixed one. The inequality therefore survives minimization. Symmetry follows by reversing the overlap index differences. A width-zero pair has one complement block contained in the other; its translates exhaust the cover and force the blocks to agree, so their whole surface frontiers agree. Thus zero class-distance occurs only on an identical isotopy class. In particular an adjacent pair has differences of its distances to any basepoint bounded by one. Nothing here constructs an edge path.

### 3.2. The “minimal genus” in B 4.8–4.10 is removable

PJ Proposition 3.3, p. 1495, is stated for possibly noncompact submanifolds with **incompressible and boundary-incompressible** frontiers, almost transverse with simplified intersection. It has no Thurston-norm or genus hypothesis. Lifts of the surfaces in §3.1 meet those hypotheses; the cyclic cover is irreducible and boundary-irreducible. Applying Proposition 3.3 directly gives the all-incompressible version of PJ Corollary 3.4, hence B Proposition 4.8. The word “minimal” in the latter two corollaries is a restriction of the application, not a restriction of the underlying theorem.

Here is the full distance consequence needed for B Proposition 4.10. Fix $`S`$ and choose $`R'\in[R]`$ minimizing the overlap width. Write its extreme indices as $`m',r'`$. Lift an isotopy from $`R'`$ to an almost-transverse, simplified representative $`R`$, carrying its complete complement block to $`V_R`$. For every $`j\notin[m',r']`$, the original block is disjoint from $`V_{S,j}`$. The generalized submanifold theorem forces the new block to remain disjoint from each such block. Thus $`r\le r'`$ and $`m\ge m'`$, and minimality gives

```math
\delta(S,R)=\delta([S],[R]).
```

This is exactly PJ Proposition 3.2's proof, p. 1495, with Proposition 3.3 replacing its specialized corollary. No cut-and-paste output or projection occurs.

PJ Lemma 3.5, p. 1495, and PV p. 9, already state the triple-positioning assertion for arbitrary orientable incompressible and boundary-incompressible surfaces. Therefore B Lemma 4.9, despite its narrower wording at p. 7, is valid in the required generality. As usual, the fibre-bundle degeneracy is excluded by the non-fibred hypotheses; coincident components are retained, not perturbed into an artificial transverse configuration.

### 3.3. Order inputs and a PDF-confirmed subscript slip

PJ §5 uses only complete complement blocks, the preceding simplified-position result, and the submanifold theorem. Its order is defined for adjacent classes. Remark 5.2 gives representative independence; Lemma 5.3 gives a direction; Lemma 5.5 excludes directed cycles. They use no projection. Their statements and proofs transfer with “vertex of $`MS`$” replaced by “incompressible vertex” and the distance replaced by $`\delta`$.

There is a literal subscript slip worth recording instead of silently quoting a wrong sentence. In PJ p. 1499, the proof says $`V_{R^*}`$ and $`V_{R^1}`$ are in the same isotopy class. But $`R^*\in\rho_k`$ was just chosen (p. 1498), not in $`\rho_1`$. The corresponding error appears in PV p. 13. The correct comparison is with **$`V_{R^k}`$**, and likewise the second frontier in the following product is that of $`R^k`$.

The repair is forced by the construction and gives the claimed conclusion. Choose the adjacent lifts successively, all with rightmost overlap index $`r`$. If $`U_i`$ is the closed negative half of the cover bounded by the selected upper frontier of $`R^i`$, the adjacent containment in PJ Definition 5.1 gives

```math
U_*\subseteq U_1\subseteq\cdots\subseteq U_k.
```

The first and last frontiers represent the same class $`\rho_k`$. Their complement lifts are isotopic with zero deck displacement: the generalized Corollary 3.4 preserves their common rightmost index $`r`$. They are almost disjoint and bound the parallelism product used in PS's argument. Each intermediate complete spanning system lies between them. In a product, an incompressible system with the same single boundary on each labelled vertical boundary annulus and no closed component is a parallel copy of the horizontal system. This can be seen by cutting the horizontal components into disks with vertical rectangles, the disk argument given in §6.1. Hence all $`\rho_i=\rho_k`$, contradicting a directed cycle of distinct adjacent vertices. This repairs the comparison without invoking genus minimization or a projection.

For the distance-direction statement, PJ Lemma 5.4 also works with $`\delta`$: the adjacent block containment bounds the extreme indices by $`m'-1,r'`$, and if $`\delta`$ increases it increases by exactly one. The elementary triangle inequality for overlap widths gives this last assertion. This lemma is not needed for the ordered-product axioms; B Corollary 5.8 uses just B Lemmas 5.2 and 5.4, corresponding to PJ Lemmas 5.3 and 5.5.

### 3.4. The hidden path-metric dependency and its removal

B Proposition 2.4 is phrased using a graph distance, and B §10 says that it also holds for $`IS`$ (p. 22). A blanket certification of that claim would require more work: PJ Proposition 2.3 proves path-metric equality by the projection construction in §4, as PJ p. 1493 and p. 1495 expressly say. The original geometric-edge argument of K cannot simply be reused for disconnected cyclic-edge systems.

**No such equality is used here.** All relevant occurrences of graph distance in B's product proof are values labeling overlap intervals, not lengths of edge paths. In B Proposition 6.4, p. 13, set $`k=\delta([S_1],[R])`$; the generalized Proposition 4.10 directly gives

```math
\{n:V_R\cap V_n\ne\varnothing\}=\{0,-1,\ldots,-k\}.
```

The no-deck-displacement contradiction, the construction of boundary-fixed representatives, and the adjacent ordering then proceed unchanged. B §5 can likewise be read using $`\delta`$. Edges are always tested by the width-one definition. The proof never requests an edge path of length $`k`$.

Consequently the dependency chain for Theorem A is PJ **Proposition 3.3, Lemma 3.5, and the proofs in §5**, together with B's product-region and gluing arguments. It excludes PJ/PV Definition 4.1, Remark 4.2, projection well-definedness, and every lemma about projection outputs. This is a precise bypass of the potential hidden dependence, not a claim that §10's entire path-metric assertion has been verified.

## 4. Audit of the rest of Banks's proof

The following table covers the places where tautness occurs in §§4–9 and the replacements needed for §10.

| Banks passage | Input actually used | All-incompressible justification |
|---|---|---|
| 4.2–4.7, pp. 5–7 | Product regions, isotopy/parallelism; incompressibility and boundary-incompressibility | §3.1 supplies the latter. No norm computation occurs. Non-fibred excludes a product winding around the entire exterior. |
| 4.8–4.10, p. 7 | Rigidity of complete lifted blocks, triple positioning, width minimization | §3.2; use the general PS theorem, not the restricted wording alone. |
| 4.11, pp. 7–8 | A path from a positive side to a negative side has algebraic intersection one with the other system | Both spanning systems are dual to the same $`\phi`$; their complements are connected. Its proof contains no genus argument. |
| 4.12, p. 8 | Product parallelism avoiding a third incompressible system | The general product-region criterion and 4.7 apply componentwise. |
| 4.13, p. 9 | Width-one blocks and the forced push-off side for common components | A transverse crossing would make a block and its translate both overlap a forbidden third block. Thus simplified width-one representatives are almost disjoint. The path test forces the side of each common component; no complexity assumption. |
| 5.1–5.4/5.8, pp. 9–11 | Representative-independent adjacent order, no directed cycles | §3.3, with its explicit correction of the PS subscript slip. |
| 5.6, p. 11 | Cut a base spanning surface into spanning surfaces of the factors | We may still choose a taut basepoint; alternatively use any incompressible one. The cut pieces are incompressible by the single-arc argument below. No restriction is imposed on other vertices. |
| 6.1–6.3, pp. 12–13 | Relative boundary ordering and its antisymmetry | Only product regions and incompressibility; no Euler-characteristic comparison. |
| 6.4–6.5, pp. 13–14 | Canonical relative representatives; no ambiguity in boundary winding; direction for pushing common components | §3.2 and §3.4 give the full block-isotopy argument with $`k=\delta`$. The second half uses triple positioning and the adjacent order. |
| 7.1, p. 14 | Gluing factor surfaces with a winding rectangle gives an allowed vertex | Replace “taut” by B Lemma 10.2; see also the group proof below. |
| 7.2, p. 14 | Surjectivity by cutting a spanning surface in one arc and extending factor isotopies into the band | B §10 explicitly supplies the incompressible cutting statement, p. 22; no minimality of Euler characteristic. |
| 7.3 first half, p. 15 | Unrestricted global isotopy determines both local vertex classes | Isotopic essential surfaces give product regions; the decomposing annulus cuts the relevant product into products. Uses no tautness. |
| 7.3 second half, p. 15 | A nonzero winding identification forces a factor complement to be a product | Hence that **oriented factor** is fibred, contradicting the hypothesis; no genus bound. |
| 8.1/8.2, pp. 15–17 | Glue width-one factor configurations with compatible rectangles | The path criterion 4.11 proves global width one; repeated/equal factor vertices are covered by the push-off cases. |
| 8.3, pp. 17–20 | Normalize a second adjacent surface in the first surface's complement; restrict to factors; read the band winding | The cut annulus minus its first trace is a disk. Incompressibility and the product-region arguments suffice. The cases of common components use 4.12/4.13, not a genus computation. |
| §9, pp. 20–21 | Vertex bijection, exact graph isomorphism, flag completion, ordered-product realization | These are combinatorial/topological statements. The optional geometric interpretation in Remark 9.1 is not needed. |
| §10, p. 22 | Single-arc normal form; incompressibility of the reverse assembly | Explicitly stated and Lemma 10.2 proved in the original; the argument below makes the all-genus interface transparent. |

Here are the important geometric interfaces in more detail.

**Single-arc cutting.** The decomposing sphere punctures to a meridional annulus $`A`$. Its core has $`\phi=\pm1`$, whereas every loop on a spanning surface has $`\phi=0`$ (push the loop slightly off the entire system). There is therefore no essential circle of intersection in $`A`$. Inessential circles are removed using incompressibility and irreducibility. The longitudinal coefficient one puts one boundary endpoint on each boundary circle of $`A`$, so the remaining trace is one spanning arc. Cutting along that arc makes each cut-piece surface group a free factor of the original surface-component group; the factor surfaces are incompressible. No closed cut component is created: a component meeting the cut trace has boundary, and a component not meeting it already had original spanning boundary. This is B §10's cutting assertion.

**Reverse assembly.** The exterior group is a meridional amalgam

```math
G_1*_{\langle\mu\rangle}G_2.
```

Each factor surface group injects into its exterior and lies in $`\ker\phi`$, while $`\phi`$ is injective on the meridional edge group. The component formed by the band has free-product group. A reduced alternating word in its two surface groups remains reduced in the amalgam, even after a meridional conjugation accounting for the band twist. All other components remain in individual vertex groups. Thus every assembled surface component is incompressible. The assembly adds no closed component. This also supplies an independent proof of B Lemma 10.2, without relying on a minimum Euler characteristic.

**Global isotopy comparison.** B Lemma 7.3 compares two *already assembled* surfaces under arbitrary ambient isotopy, not only under a splitting-preserving isotopy. With both annular traces single and disjoint, a parallelism product that meets the decomposing annulus is cut by its product disk into parallelism products on the two sides. Its isotopy either reduces intersections or identifies a whole pair of components. Iteration identifies the factor vertex classes. The second half then uses the boundary pattern on the connected-sum torus: if two different band windings represent the same whole surface, one of the factor cut complements must be the whole horizontal product. That makes the factor a fibre for its given orientation. These implications supply the unrestricted global-isotopy comparison under the present hypotheses. There is no assumption that an arbitrary isotopy path was already simultaneously in annular normal form.

For reference the edge rule is explicit. Choose B's adjacent order on the two factor vertex sets, with equality allowed. After interchanging the two triples if needed so that $`b_2\le a_2`$, distinct triples $`(a_1,a_2,n_a)`$ and $`(b_1,b_2,n_b)`$ are adjacent exactly when

```math
\bigl(b_1\le a_1\text{ and }n_b=n_a\bigr)
\quad\text{or}\quad
\bigl(a_1\le b_1\text{ and }n_b=n_a+1\bigr).
```

The comparisons require adjacent or equal factor vertices. This is B Corollary 8.2 together with Proposition 8.3, not just geometric disjointness. It records the common-component boundary order and the single global deck convention correctly.

Lastly, there is no weak-topology loophole in the homeomorphism. Each vertex set is countable: compact tame surface embeddings in a compact triangulated 3-manifold can be isotoped to finite piecewise-linear embeddings with rational coordinates in a fixed finite atlas. There are countably many finite domain triangulations and rational data, and sufficiently close such approximations are isotopic by a tubular neighbourhood. Therefore each flag complex has countably many simplices. Ordered product triangulation gives the usual finite-simplex product identifications, hence a homeomorphism for the compactly generated product; HA Theorem A.6 identifies that topology with the ordinary product for countable CW complexes. The factors $`\mathbb R`$ cause no issue either, being locally compact. This proves Theorem A with the stated realization topology.

## 5. The four-fibre hypotheses and iteration

In the common positive Hopf reference orientation, denote meridians by $`\mu_i^H`$ and signs by $`\epsilon_i`$. Distinct fibres have oriented linking numbers

```math
\mathrm{lk}(H_i,H_j)=\epsilon_i\epsilon_j=\pm1.
```

A splitting sphere would force all cross-linking numbers of its nonempty partition to vanish, which is impossible. Local knot insertions preserve all these numbers. Thus $`H_4`$ and every intermediate four-component link are non-split.

The base exterior is $`E(H_4)\cong S^1\times P`$, where $`P`$ is a sphere with four holes. Let $`f`$ be its regular-fibre loop. In meridional homology $`f=\sum_i\mu_i^H`$; equivalently on torus $`i`$ it is $`\lambda_i^H+\mu_i^H`$. Hence

```math
\phi_H(\mu_i^H)=\epsilon_i,
\qquad \phi_H(f)=\sum_i\epsilon_i=0,
\qquad \pi_1(E(H_4))=\mathbb Z\langle f\rangle\times F_3.
```

The restriction $`\chi:F_3\to\mathbb Z`$ is onto. Choose a free basis $`a,b,c`$ with $`\chi(a)=1`$ and $`\chi(b)=\chi(c)=0`$ by elementary Nielsen changes from the peripheral basis. The Reidemeister–Schreier basis for its kernel is

```math
\{a^n b a^{-n},\ a^n c a^{-n}:n\in\mathbb Z\}.
```

Thus

```math
\ker\phi_H=\mathbb Z\langle f\rangle\times\ker\chi
```

is not finitely generated. A fibration in the primitive class $`\phi_H`$ would have this group as the group of its compact connected fibre, which is finitely generated. This proves that $`H_4`$ is **not fibred for the specified $`\alpha`$**, rather than relying on an unoriented assertion about the Hopf exterior. 

This obstruction survives every local knot insertion. At a stage $`G=G_{\mathrm{old}}*_{\langle\mu\rangle}G_K`$, the map which is the identity on $`G_{\mathrm{old}}`$ and sends

```math
g\in G_K\longmapsto\mu^{\phi_K(g)}
```

is a retraction to $`G_{\mathrm{old}}`$. It respects $`\phi`$ and restricts to a surjection of kernels. The composed retraction onto the base has the non-finitely-generated $`\ker\phi_H`$ as its kernel image. None of the intermediate links can therefore be fibred in the spanning class. This argument works for composite, fibred, non-fibred, or trivial local knots.

If all $`K_i`$ are non-fibred, apply Theorem A four times along the four labelled components. At every application both factors are non-split and non-fibred in the required orientation class. Associating the finite products proves the $`\mathbb R^4`$ formula and gives a recursive vertex bijection with four independent integers. The treatment of the other knots follows next.

## 6. Fibred factors: a separate all-genus argument

B Proposition 1.3, p. 1, says only $`MS(J\#K)\cong MS(J)`$ for a fibred factor and cites Kakimizu 2005 Proposition 2.4. It does **not** by its wording prove the required $`IS_{\mathrm{cyc}}`$ assertion. The following proof fills that interface using a source actually read in this audit.

### 6.1. A fibred link has just one incompressible spanning vertex

Let $`K`$ be a non-split fibred oriented link, other than the unknot, with connected spanning fibre $`F`$. First any incompressible spanning surface disjoint from $`F`$ is isotopic to $`F`$. Cut the exterior along $`F`$ to obtain $`F\times I`$. The surface $`R`$ in this product has one boundary curve in each vertical annulus of $`\partial F\times I`$, and no closed component. Its boundary system can be straightened to $`\partial F\times\{1/2\}`$ independently on these annuli. It remains incompressible in the product.

Choose disjoint proper arcs cutting $`F`$ to a disk and use their vertical rectangles as a disk system in the product. Straighten $`\partial R`$ to the middle curve and minimize intersections with these disks, in sequence. Inessential circle intersections can be eliminated by incompressibility and irreducibility. Each rectangle then has exactly two boundary intersections and so one arc of trace. Straighten that arc, keeping its endpoints fixed, to the middle trace. Cutting along the rectangles preserves incompressibility of surface pieces: their groups are free factors of the original surface group, which injects into the product group.

The resulting ambient manifold is a ball. Every remaining surface piece is a disk, since its group injects into the trivial group. On the sphere boundary its total trace is exactly the boundary of the horizontal cut-open fibre disk. There is one such circle, so one disk and no additional components. Disks in a ball with that boundary are isotopic relative to the boundary. Glue back across the rectangles. This gives the asserted isotopy in $`F\times I`$. The same proof works componentwise for a product of a disconnected horizontal system, as used in §3.3.

K Theorem A, p. 226, states that the **geometric-disjointness** incompressible complex of a non-split oriented link is connected. Use this connectivity theorem itself, not its claimed identification of a geometric graph distance with cyclic width. The preceding product argument says its fibre vertex has no distinct adjacent vertex. Connectedness then forces the entire vertex set to be that one vertex. Consequently $`X(K)`$ has one vertex also. In the knot case required for Theorem B, the spanning surfaces are automatically connected, so even the disconnected metric issue does not arise in this use. For the unknot, a spanning incompressible surface is a meridian disk of the solid-torus exterior, giving the same conclusion directly.

### 6.2. Absorption of a fibred summand, including edges

**Lemma.** Let $`J`$ be non-split and non-fibred in its spanning class, and let $`K`$ be a non-split fibred oriented link. At specified components take their oriented connected sum. There is a simplicial isomorphism

```math
X(J\#K)\cong X(J).
```

The connected sum is non-split and non-fibred in the spanning class. For the latter decomposition implication, suppose that a whole spanning surface is a fibre. Its cut complement is a product, and the decomposing annulus minus its single trace is a properly embedded disk with one trace arc on each horizontal face and two arcs on the vertical boundary. Projecting this disk to the horizontal fibre gives a homotopy between the horizontal arcs; proper simple arcs with these endpoint conditions are isotopic. Straighten its boundary and use irreducibility to isotope the disk to the corresponding vertical rectangle. Cutting along it gives the two factor products. This is the product-disk mechanism used in B Lemma 7.3. Both factor surfaces would be fibres, contrary to the hypothesis on $`J`$. For every application to Theorem B, non-splitness and non-fibredness of the whole link are also independently proved in §5.

**Proof, vertices.** Put every incompressible surface into single-arc normal form at the decomposing annulus as in §4. Its $`K`$ part is the fibre vertex by §6.1. The first half of B Lemma 7.3 still applies: it uses only essential parallelism and single annular traces, not non-fibredness of each cut factor. Therefore an unrestricted global isotopy cannot change the $`J`$-vertex. This makes the map to $`V(X(J))`$ well-defined.

Conversely assemble a $`J`$-surface with $`F`$ and a band. Moving $`F`$ once through the fibration is a loop of unparameterized embedded surfaces. On every boundary it makes one meridional circuit because $`\phi_K(\mu)=1`$. Extend this motion over the connecting rectangle, as in B Lemma 7.2, keeping the other factor unchanged. Boundary motion at the other components of $`K`$ is permitted. Its end identifies winding $`n`$ with winding $`n+1`$. All integers are absorbed. A fibre representative can be brought to the chosen relative representative allowing boundary motion; at the joining component the resulting difference is precisely a band winding. Hence exactly one global vertex occurs over each $`J`$-vertex, proving bijectivity.

**Proof, edges.** Given adjacent distinct $`J`$-vertices, choose their almost-disjoint, width-one configurations by the extended B 4.10/4.13. On the fibred side use two parallel fibre phases, and choose disjoint connecting rectangles compatible with the prescribed annular traces. The winding can be chosen freely since it has just been absorbed. The algebraic-path proof of B Lemma 8.1 shows the assembled whole complement blocks have width one. That proof also covers the equal factor-vertex case by using parallel copies. Thus the bijection preserves edges.

Conversely start with adjacent global vertices and make their surfaces disjoint while retaining the width-one certificate. The relative normalization at the beginning of B Proposition 8.3, p. 17, cuts the second in a single arc in the complement of the first. It applies with the fibred side as well: no non-fibredness assertion is used in this normalization or restriction step. The cut $`J`$-surfaces have width at most one. Equivalently apply the whole-system path criterion B 4.11 to paths lying in the $`J`$ piece; algebraic intersections are unchanged by restriction. Their classes are distinct by the vertex bijection, so they are adjacent. The bijection is a graph isomorphism, hence a simplicial isomorphism by flagness. $`\square`$

If both oriented factors are fibred, their fibre surfaces join along the band and their monodromies extend over it (choose them to fix the boundary), giving a fibration of the connected sum. Its $`X`$ is a point by §6.1. For an unknot factor the connected sum is simply isotopic to the other factor. Thus all fibred-factor cases have an all-genus treatment here; no invocation of the unavailable Kakimizu 2005 original is hidden in it.

Apply this lemma whenever a fibre knot occurs in the four-fibre construction and Theorem A whenever a non-fibred knot occurs. §5 verifies the non-split/non-fibred hypotheses on every intermediate $`J`$. Each non-fibred insertion contributes one $`\mathbb Z`$ coordinate and one $`\mathbb R`$ realization factor, and every fibre insertion contributes none. This completes Theorem B.
