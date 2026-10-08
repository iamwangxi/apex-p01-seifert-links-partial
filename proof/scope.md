# Scope, dependencies and contribution limits

[Overview](../README.md) · [Main theorem](main-theorem.md) · [Sources](../sources/bibliography.md)

The principal results are the [finite-input nullhomotopy mechanism for all balanced Hopf fibre links](hopf-contraction.md) and the satellite calculations as an [annulus cone](parallel-satellites.md), [one edge](parallel-satellites-torus.md), and a [complete tree](parallel-satellites-k719-tree.md). The connected-surface extension and Banks closure organise these cases. This package proves partial results for the whole-complement cyclic flag complex $`X=IS_{\mathrm{cyc}}(L)`$, allowing disconnected and non-minimal incompressible spanning surfaces. It supplies no all-link contraction or general disconnected cyclic/geometric comparison.

The [main theorem](main-theorem.md), Theorem 5.2, closes knots, the all-connected class under its declared inputs, all balanced $`H_{2m}`$, $`m\ge1`$, prescribed-class fibred links, (SB) parallel links and the $`K_{7/19}`$ parallel link and its mirror under finite specified-component connected sums. Banks's existing product theorem gives the non-fibred original-factor count $`r`$ and exponent $`r-1`$ when $`r\ge1`$; all-fibred sums are points. Local insertions on $`H_{2m}`$ with $`m\ge2`$ have exponent $`|I|`$, since the base itself is nonfibred. For the fibred base $`H_2`$, $`I=\varnothing`$ gives a point and $`|I|\ge1`$ gives exponent $`|I|-1`$.

## Method attribution and novelty boundary

The Hopf-family proof adapts Hatcher, *The cyclic cycle complex of a surface*, arXiv:0806.0326v1 (2008), second proof, pp.5–6. Circle maps, regular fibres and averaging have that precedent. The fixed-boundary adaptations are monotone degree-one boundary restrictions, legal retained matching arcs, finite arc-flow coordinates, region-potential common rounding and zero-face gluing. The decoder’s initial recovery is exact on every true input simplex, and finite templates prove continuity across collisions and graph changes. Every finite inclusion is nullhomotoped in a finite subcomplex; that finite image need not itself be contractible.

Planar bipartite matching face heights and distributive lattices are classical: Propp, *Lattice structure for orientations of graphs*, arXiv:math/0209005v3 (2021), §3, Theorem 2 and the face-height description, pp.21–22. The proof here establishes its needed circulation, rounding, distance and gluing facts self-containedly, including disconnected graphs and non-disk regions, rather than invoking Propp’s theorem.

PS Theorem 1.1 already states a result covering the balanced norm-zero Hopf family. The contribution is this independent family proof with its explicit finite-input mechanism, avoiding PS §§4–7. Banks’s product theorem belongs to Banks. No priority claim is made for circle-map averaging or planar matching heights.

A literature search on 7 October 2026 located no erratum to PS 2012; this cannot exclude missed or unpublished material. Schultens's *Topology Proceedings* 50 (2017) and *AGT* 18 (2018) use weighted curves/surfaces with connected complement and freely moving boundary, rather than the prescribed-boundary, unweighted object here. The Seifert-space proof in the latter is restricted to closed spaces. These are related frameworks, not automatic replacement proofs for the complexes in this package.

## External inputs and retained PS results

Knot factors invoke Competition Theorem A. The connected-surface result invokes the [multiple-boundary geometric interface](connected-surfaces-exchange.md#51-precisely-what-is-inherited) and Competition Theorem B. Attainment, compactness/finiteness, universal disjointness, regularity and the stated local exchange estimates remain inherited inputs.

The positive factor contractions and closure do not use PS's projection (§4), observer assertions (§6), or general contraction (§7). This does not mean independence from all PS results. The Hopf matching models use PS §3 distance minimisation. The Banks transfer uses Proposition 3.3, Lemma 3.5 and §5's order arguments, with its recorded subscript correction in Lemma 5.5. The satellite tree and distance-two proof use Banks Proposition 4.10 and its explicit all-incompressible extension in §10. The [counterexample note](ps-counterexample.md) evaluates the PS projection to test it, rather than invoking its disputed conclusions as premises.

## The PS counterexample and its finite filling

The [self-contained certificate](ps-counterexample.md) constructs eight balanced Hopf fibres with the same nonfibred genus-one knot locally inserted on each component. Four taut classes satisfy

```math
\pi_A(B)=P_-,\qquad \delta(A,B)=\delta(S,P_-)=2,
```

```math
\delta(A,S)=\delta(B,S)=\delta(A,P_-)=\delta(B,P_-)=1.
```

The independent direction rule gives $`B<_A S`$. Lemma 6.1's ordered and adjacent-or-equal conclusions, p. 1499, and the radius-one vertex conclusion of Lemma 6.5, p. 1501, fail. Direct calculation gives $`\pi_A(S)=\pi_A(P_-)=A`$. The four vertices therefore form a finite $`A`$-convex flag four-cycle, whose graph is not dismantlable, contradicting Theorem 7.2, pp. 1503–1504.

The note supplies two class-distance verifications and a finite filling $`|K|\cong[0,1]^{12}`$ with 6,144 vertices, including a filling in the minimum-norm layer. This refutes the cited general disconnected proof through Lemma 6.1 and Theorem 7.2, not the statement of Theorem 1.1 about the whole complex. Lemma 6.5 is used directly in §8 rather than §7. No additional §8 statement is refuted here, and this example does not affect the knot case or the target's connected-surface result.

Consequently the main theorem has no universal all-minimal factor class. PS's retained §3 and §5 inputs are separate from these refuted statements. The weighted surface literature is discussed in the note without asserting a two-dimensional counterexample or a general repair.

## Conditional reduction and remaining cases

If a particular non-split factor has every incompressible spanning surface norm-minimising, its reduced no-closed-component complexes satisfy $`X=MS`$. If that particular $`MS`$ has an independent contraction, the closure theorem can add it. Equality of the objects and the product theorem alone do not supply the contraction.

At $`k=\phi(f)=0`$ in a Seifert exterior, the vertical-annulus classification and $`X=MS`$ remain structural. The finite-input proof covers every balanced $`H_{2m}`$; together with the horizontal branch it covers all Hopf fibre links. It does not establish the general exceptional-fibre vertical case. At $`k\ne0`$, the horizontal product complement proves the prescribed fibration and $`X`$ is a point.

The $`K_{7/19}`$ two-parallel complex is contractible despite its distance-two annulus example: its full complex is a tree with one disconnected leaf and chain genera $`3k`$ unbounded. The tree proof depends on joint pure stacks, exclusion of mixed systems, zero meridional return subgroup, and both directions of the marked-arc edge correspondence. Merely knowing that another companion has one- and two-boundary pieces does not supply these interfaces. No complete inventory or infinitude assertion is made for nonfibred (SB) companions such as $`5_2`$.

A remaining link can have only minimum-norm vertices; non-minimality is not the boundary of the proved list. General satellite/JSJ gluing, all-link contractibility, and a general finite-carrier rule remain outside the results. The connected-surface truncations concern nonempty full subcomplexes downward closed in complete lexicographic complexity; arbitrary rectangular genus/area caps are not included.

## Verification level

The connected-surface argument has two adversarial review rounds. The satellite cone and edge, Hopf matching model and all-hole rounding/composition proof, and joint normal forms and satellite tree have separate fresh-context adversarial reviews. The PS certificate incorporates its construction review and source comparison. The older connected-sum and Seifert calculations have written source interfaces. Assembling this combined revision adds no independent cross-document review or proof-assistant certification.

The distributed example program uses exact arithmetic. Formula checks concern syntax, rather than mathematical truth. Bibliographic editions and checked pages are recorded in the [source register](../sources/bibliography.md); the manifest identifies every distributed file except itself.
