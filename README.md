# Partial link extensions: Hopf fibre links, annular satellites, and connected sums

Every nonempty oriented union of Hopf fibres has contractible cyclic incompressible-surface complex $`X`$. For every balanced $`H_{2m}`$, the proof nullhomotopes arbitrary finite input by equivariant height interpolation, regular-fibre arc-flow averaging and region-potential common rounding in a perfect-matching polytope. The decoder preserves true cyclic simplices and glues along zero-weight faces. Unbalanced Hopf fibre links are fibred in their prescribed spanning class and have one vertex.

Annular satellites have three complete calculations: a cone under (SB), exactly one edge for torus companions, and a tree for the two oppositely oriented zero-framed parallels of $`K_{7/19}`$. The four-fibre Farey tree, the connected-surface extension under its stated inputs and Banks’s audited closure organise these results. The complex includes all incompressible genera, disconnected and non-minimal systems; the extension to general links remains partial.

## Target and object

The target is *Contractibility of the Complex of Incompressible Seifert Surfaces: The Knot Case of Kakimizu's Problem*, attributed to Apex Intelligence, the official competition version dated **11 September 2026**, 48 pages. Its Introduction, p. 2, leaves general links untreated; Theorem D uses linking-indecomposability. PDF SHA-256:

```text
34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f
```

Spanning surfaces are oriented, componentwise incompressible, have no closed components and one prescribed oriented boundary on each labelled link torus. Boundaries may move during ambient isotopy. Vertices include all genera. Distinct classes are adjacent when the **minimum whole-complement cyclic-cover width** is one; simplices are the flag completion. A whole complement has one common deck choice. For connected surfaces this agrees with the original geometric-disjointness complex. No general comparison for disconnected surfaces is asserted.

## Principal calculations

**All Hopf fibre links.** For $`H_{2m}`$, every vertex is an $`m`$-arc positive-negative perfect matching on a sphere with $`2m`$ labelled holes. A normalised signed region graph inside one complete cut block gives

```math
\delta([F_a],[F_b])=\max H-\min H.
```

This formula holds for every hole number. A true simplex has simultaneous disjoint normal arc representatives; the converse from disjointness to adjacency is needed and proved only in the six-hole structural calculation. The six-hole complex contains a tetrahedron, while the four-hole complex is a Farey tree.

For every finite input $`K`$ and matching $`M_*`$, the contraction constructs finite $`Y\supset K\cup\{M_*\}`$ and a nullhomotopy of the inclusion inside $`Y`$. All band functions have common equivariant real lifts. Convex interpolation preserves monotone degree $`\pm1`$ boundary restrictions, so each regular fibre has one endpoint per hole and its retained intervals form a legal matching. Averaging these intervals in arc coordinates gives $`w\in P_G`$ on the actual embedded support graph.

A reference matching gives region potentials $`w=m+D_Gu`$. The common rule $`m+D_G\lfloor u+\theta\rfloor`$ gives legal perfect matchings whose pairwise difference potential has oscillation at most one, hence a true cyclic simplex. Its threshold average is continuous, agrees after zero-edge deletion, and recovers every input simplex’s exact barycentric coordinates. The fixed-graph induced complex triangulates $`P_G`$; it need not be a single simplex. Uniform finite templates and these zero-face rules handle phase collisions and changing graphs. The finite image itself need not be contractible.

Circle maps, regular fibres and averaging follow Hatcher 2008, second proof, pp.5–6. Planar bipartite matching face heights are classical background: Propp, arXiv:math/0209005v3, §3, Theorem 2 and the height description, pp.21–22. All needed potential and rounding facts are proved explicitly here. PS Theorem 1.1 already states a conclusion covering the balanced family; this is an independent family proof avoiding PS §§4–7 and retaining §3. For an unbalanced orientation, $`\phi(f)=\sum_i\epsilon_i\ne0`$ and the Seifert horizontal argument proves fibration and a point.

**Satellite cone and edge.** (SB) means that every connected orientable essential companion surface with nonempty boundary entirely of preferred-longitude slope has one boundary circle. Essential means incompressible and boundary-incompressible. Under (SB), the canonical annulus $`A`$ is adjacent to every other vertex, so the full complex is a cone. Torus-knot companions give exactly two vertices, $`A`$ and two oppositely oriented companion fibres with reaching collars, hence one edge. Joint fibre normalisation and compatible gluing eliminate all residual twists.

For two-bridge companions, (SB) holds exactly when every zero-slope admissible minus-continued-fraction carrier is all-even. This includes $`K_{(2m-1)/(4m-1)}`$, $`m\ge1`$, and mirrors, with $`5_2=K_{3/7}`$ at $`m=2`$ up to handedness. No infinitude assertion is made for the $`5_2`$ parallel complex.

**The satellite tree beyond (SB).** For $`K_{7/19}`$, (SB) fails. The full parallel-link vertex set consists of $`A`$, one disconnected vertex $`G`$, and connected chain vertices with canonical coordinates

```math
k\ge1,\qquad 0\le a\lt2k,\qquad \gcd(2a+1,2k)=1,\qquad t\in\mathbb Z.
```

The chain genus is $`3k`$. There is no further twist identification. Put $`p=2a+1+4kt`$ and identify $`A=1/0`$. Chains correspond bijectively to reduced $`p/k`$ with odd numerator and positive denominator. Chain edges satisfy

```math
|pk'-p'k|=1.
```

The annulus is adjacent to all $`k=1`$ chains and to $`G`$; $`G`$ is a leaf. Unique smaller-denominator neighbours prove the complete graph is a tree; flag completion adds no higher simplices. The canonical linear family satisfies $`\delta(A,F_k)=k`$, so the annulus is not a cone vertex. The zero-return-subgroup proof and both directions of the three-dimensional/marked-arc edge correspondence are included. Reflection gives the mirror calculation.

## Organising results and exact closure

The permitted factors are knots (Competition Theorem A and the unknot argument), links with all incompressible spanning surfaces connected under the connected multiple-boundary inputs, all balanced $`H_{2m}`$, $`m\ge1`$ (unbalanced Hopf fibre links are fibred factors), prescribed-class fibred links, the (SB) parallel links, and the $`K_{7/19}`$ parallel link and its mirror.

Every finite binary specified-component connected sum of these factors has contractible $`X`$. If $`r`$ counts original factors nonfibred in their prescribed spanning class, then

```math
r=0\Longrightarrow X(L)=\{*\},\qquad
r\ge1\Longrightarrow
|X(L)|\cong\prod_{J_i\ \mathrm{nonfibred}}|X(J_i)|\times\mathbb R^{r-1}.
```

The product has Banks’s ordered triangulation. Intermediate non-splitness, the exact fibredness rule and all-incompressible fibred absorption are proved. For $`m\ge2`$, the base $`H_{2m}`$ is nonfibred: $`\ker(F_{2m-1}\to\mathbb Z)`$ has infinite Schreier basis with $`2m-2`$ families of generators. The balanced $`H_2`$ has an annular spanning fibre. The satellite torus group $`\mathbb Z^2\subset\ker\phi`$ prevents the $`K_{7/19}`$ parallel factor from being fibred.

For local knots inserted on all $`2m`$ fibres, put $`I=\{i:K_i\text{ is nonfibred}\}`$. If $`m\ge2`$,

```math
|X(H_{2m}\#_1K_1\cdots\#_{2m}K_{2m})|
\cong |X(H_{2m})|\times\prod_{i\in I}|X(K_i)|\times\mathbb R^{|I|}.
```

Here $`r=1+|I|`$. For $`m=1`$, $`r=|I|`$: no nonfibred insertion gives a point, and otherwise the product of the knot factors has Euclidean exponent $`|I|-1`$. Fibred knots contribute no winding coordinate; no negative exponent is used.

The independent connectedness bound is $`b_0(F)-1\le r_\phi(L)`$, where $`r_\phi`$ is the rational Alexander rank. Rank zero forces every spanning surface connected and the link non-split. Under the inherited geometric and combinatorial inputs, the connected-surface complex and its nonempty full subcomplexes downward closed in complete lexicographic complexity are contractible. Exact braid examples have all pairwise linking numbers zero. The proof includes the target's §6.3 length-classification correction, p. 22.

The four-fibre calculation retains its infinite Farey tree. The Seifert structure theorem gives vertical annuli and $`X=MS`$ when $`\phi(f)=0`$, and a prescribed fibration with one vertex when $`\phi(f)\ne0`$. The Hopf-family contraction covers all balanced links, and the horizontal branch covers the unbalanced ones. General $`k=0`$ cases with exceptional fibres remain outside the contraction claim.

## PS certificate, dependencies and literature scope

The [counterexample note](proof/ps-counterexample.md) is self-contained. Its four taut vertices refute PS Lemma 6.1, the radius-one vertex conclusion of Lemma 6.5, and Theorem 7.2 for a finite rooted-convex flag four-cycle. Two class-distance verifications and a finite filling homeomorphic to $`[0,1]^{12}`$ are given. The statement of PS Theorem 1.1 is not refuted. The package therefore does not use it to supply a universal all-minimal factor class.

The positive proofs retain PS §3 and the audited §5 order interfaces where specified; they do not use its projection or general contraction. Knot factors and the connected-surface extension retain the competition paper's stated inputs. Banks's product theorem is an existing theorem. A literature search on 7 October 2026 located no erratum to PS 2012. Schultens 2017/2018 use weighted, freely moving-boundary frameworks, and the Seifert-space proof is restricted to closed spaces. No automatic transfer to the fixed-boundary object or general repair is claimed.

## Proof guide

| File | Content |
|---|---|
| [Hopf matching model](proof/hopf-model.md) | All balanced hole numbers: vertex bijection, effective encodings and complete-block distance; six-hole special structure |
| [All-hole Hopf contraction](proof/hopf-contraction.md) | Fixed-graph polytope decoder, exact initial recovery, zero-face gluing and arbitrary finite nullhomotopies |
| [Satellite cone](proof/parallel-satellites.md) | (SB), same-representative disjointness and whole-block separation |
| [Torus exact edge](proof/parallel-satellites-torus.md) | All-genus classification, joint fibre isotopy and compatible gluing |
| [Two-bridge criterion](proof/parallel-satellites-two-bridge.md) | Exact (SB) scope and infinite companion family |
| [Distance-two example](proof/parallel-satellites-obstruction.md) | Genus-six non-cone witness |
| [Geometric normalisation](proof/parallel-satellites-normalisation.md) | Essential cut pieces, product annuli and efficient torus comparison |
| [Joint longitudinal forms](proof/parallel-satellites-k719-normal-forms.md) | HT parameters, pure stacks, closed-component test and geometric equality criterion |
| [Complete satellite tree](proof/parallel-satellites-k719-tree.md) | Zero return subgroup, canonical coordinates, all edges and entire contraction |
| [PS counterexample](proof/ps-counterexample.md) | Published operation, nine distances, three false statements and finite twelve-dimensional filling |
| [Objects](proof/objects.md) | Boundary slopes, whole-complement convention and compression |
| [Connected surfaces](proof/connected-surfaces.md) | Statement, connectivity rank and exact examples |
| [Exchange topology](proof/connected-surfaces-exchange.md) | Inherited inputs and fixed output classes |
| [Collars and area gain](proof/connected-surfaces-collars.md) | Perturbation, length correction and area estimates |
| [Connected-surface contraction](proof/connected-surfaces-contractibility.md) | Exchange conclusion and downward-closed truncations |
| [Four-fibre tree](proof/hopf-four.md) | Vertices, full cyclic distances and tree |
| [Banks transfer](proof/connected-sum.md) | All-incompressible product and fibred absorption |
| [Seifert exteriors](proof/seifert.md) | Surface dichotomy, filling classification and exact limits |
| [Main theorem](proof/main-theorem.md) | Factor list, closure, nonfibredness, all-fibre insertion formulas and dependency table |
| [Scope](proof/scope.md) | Attribution, retained inputs and unproved generalisations |
| [Bibliography](sources/bibliography.md) | Public editions and checked printed/preprint pages |
| [Computation](scripts/README.md) | Distributed exact braid certificates |

## Verification, AI disclosure and licence

The individual model, contraction and satellite proofs have independent fresh-context adversarial reviews. The combined assembly has no new independent cross-document review or proof-assistant certification. The distributed certificate computations use exact arithmetic. Formula checks concern syntax; the precise source and scope statements accompany the proofs. `MANIFEST.sha256` identifies every distributed file except itself.

GPT-6.1 Sol, in OpenAI Codex under human direction, developed the proof, ran the computations where applicable, and drafted this text; a separate GPT-6.1 Sol session in a fresh context performed an adversarial review. Claude planned the work, checked key steps against the sources, and reviewed and edited the final text. No human expert has certified the work.

Original prose uses [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); code in `scripts/` and executable proof examples uses [MIT](scripts/LICENSE). Third-party publications retain their terms and are not redistributed. See [LICENSE](LICENSE).
