# Bibliography, editions and verification status

[Overview](../README.md) · [Scope](../proof/scope.md)

Printed page numbers refer to the specified edition. The checks below report the supplied proof and source-audit records; assembling this package did not independently re-prove every cited theorem or newly inspect every source page. Materials were already available offline. Public links are bibliographic or recorded author-copy destinations, not pages revisited during packaging. No third-party full text or PDF is bundled.

## C — Target competition paper

**Apex Intelligence.** *Contractibility of the Complex of Incompressible Seifert Surfaces: The Knot Case of Kakimizu's Problem*. Official competition version, 11 September 2026, 48 pages.

Acquisition: supplied official competition PDF. No exact public download URL was supplied in the permitted records, so none is invented. PDF SHA-256, checked again during packaging: `34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f`. Text SHA-256: `54f60d38dd61a7ad2eaef2c376f17422cacd2a734c63d4cdad531d4b0ff34d91`.

Theorem A, Theorem D and the untreated general-link extension: Introduction, p. 2. Exchange results: §2, pp. 3–6, including Theorem B, Lemma 2.2, Corollary 2.3 and Lemma 2.4. Geometric interface: §3, pp. 6–8. Lemmas 4.3, 4.5, Corollary 4.6, Lemmas 4.8–4.9: §4, pp. 9–12. Theorem 5.1 and proof: §5, pp. 13–19. Link slopes, compression and multiple tori: §6.3, pp. 20–22. The corrected case split is on p. 22. Positive-width rounding and push-offs: Appendix B, pp. 28–32; collar perturbation, noncollapsing, length and gain: pp. 33–38.

The geometric and combinatorial results are inherited where stated. The package supplies the local deductions and connectedness replacement, not independent certification of the full analytic package.

## V2 — Subsequent author version

**G. Pan, C. You, J. Zhou and Y. Chen.** *Exchange complexes and contractibility of the complex of incompressible Seifert surfaces*. [arXiv:2609.09224v2](https://arxiv.org/abs/2609.09224v2), 12 September 2026.

Acquisition: supplied arXiv PDF. PDF SHA-256: `f3e9b5f1364886c3d88081c5082caffdd4fce5cd7ec8c529ab96fbeeb8becf64`. Text SHA-256: `15db25866ab18d1ed15aa956dd65d86ef727f5a64ce43e7a4785c5e7c7c4bdae`.

Local comparisons: positive-parameter isotopy and two scales, pp. 33–34; actual collar functions and noncollapsing, pp. 46–47; positive-width perturbation tracks and gains, pp. 49–51; multiple-torus classification and boundary clearance, §8.3, pp. 66–67; connectedness-use list, p. 67. Its different attainment and compactness implementation is not substituted for that of the competition version.

## K — Kakimizu

**Osamu Kakimizu.** *Finding disjoint incompressible spanning surfaces for a link*. *Hiroshima Mathematical Journal* **22** (1992), no. 2, 225–236. [DOI 10.32917/hmj/1206392900](https://doi.org/10.32917/hmj/1206392900).

Acquisition: supplied journal PDF. PDF SHA-256: `eb195635ce7ddb1c74caccae36d4493e875773f29de0f013eb91f5471c10b36c`.

Checked spanning and geometric-complex conventions, p. 225; Theorem A (geometric connectivity) and whole cut-complement construction, p. 226; incompressible-surface arguments, pp. 228–230. The disconnected metric equivalence criticised by PS is not an input. No unverified Kakimizu 2005 fibre-absorption source is invoked.

## B — Banks

**Jessica E. Banks.** *The Kakimizu complex of a connected sum of links*. **Checked edition:** [arXiv:1109.0965v1](https://arxiv.org/abs/1109.0965v1), 5 September 2011, 23 pages. The later journal typesetting has not been compared.

Acquisition: supplied arXiv PDF. PDF SHA-256: `e50c6e9020d8d4cc8bafa470c0c4ab2728e064df6c701570415723875fae068f`.

The supplied audit read the full preprint. Definitions 2.1 and 2.5, pp. 2–3; Definition 4.1 (product regions), p. 5; simplified position and width, §§4–5, pp. 5–11; relative representatives, §6, pp. 12–14; gluing and unrestricted isotopy, §7, pp. 14–15; edges and inverse-edge analysis, §8, pp. 15–20; ordered realization, §9, pp. 20–21; Definition 10.1, Lemma 10.2 and Theorem 10.3, p. 22. The satellite distance-two proof also uses Proposition 4.10, p. 7, and its explicit extension to all incompressible surfaces in §10, p. 22.

Theorem 10.3 belongs to Banks. This package audits its all-incompressible use, replaces path-metric labels by cyclic widths and supplies fibred-factor absorption at that level. Banks's reference [5] is the PS 2010 preprint below, not the journal edition.

## J / PJ — Przytycki–Schultens, journal edition

**Piotr Przytycki and Jennifer Schultens.** *Contractibility of the Kakimizu complex and symmetric Seifert surfaces*. *Transactions of the American Mathematical Society* **364** (2012), no. 3, 1489–1508. [DOI 10.1090/S0002-9947-2011-05465-6](https://doi.org/10.1090/S0002-9947-2011-05465-6).

Acquisition: supplied journal PDF. PDF SHA-256: `f00eba68abe0dfcab5cd4297e80c0cd454c7433112f7a373a72a609cce25157e`.

Definitions and Theorem 1.1, pp. 1489–1490; distance and minimisation, §§2–3, pp. 1492–1495; Proposition 3.2, p. 1494, proved on p. 1495; Proposition 3.3 and Lemma 3.5, p. 1495. The Banks audit also uses §5, pp. 1497–1499, including the recorded Lemma 5.5 subscript correction on p. 1499. The Hopf matching models use §3, not the projection.

The checked counterexample refutes Lemma 6.1's ordered and adjacent-or-equal conclusions, p. 1499; Lemma 6.5's radius-one vertex conclusion, p. 1501; and Theorem 7.2's dismantlability assertion for finite rooted-convex subcomplexes, p. 1503 (proof through p. 1504). The four taut classes satisfy $`\pi_A(B)=P_-`$, $`\delta(A,B)=\delta(S,P_-)=2`$, with all four cross distances equal to one. The remaining projections make the induced flag four-cycle rooted-convex. The complete certificate, both distance verifications and the finite twelve-dimensional filling are in [the counterexample note](../proof/ps-counterexample.md).

Theorem 1.1's statement is not refuted by that finite subcomplex. Its cited §7 general proof cannot be used to certify the removed disconnected all-minimal factor class. The positive factor and closure proofs use neither PS's projection (§4) nor its general contractibility theorem (§7). The Hopf matching models and Banks audit retain the §3 and §5 inputs recorded above. The counterexample note evaluates Definition 4.1 to test the disputed claims. See [scope](../proof/scope.md).

## PV — Przytycki–Schultens, preprint edition

Same authors and title, [arXiv:1004.4168v2](https://arxiv.org/abs/1004.4168v2), 2010. Acquisition: supplied arXiv PDF. PDF SHA-256: `fd27c311f7cc937d54bb7c8e2530a172eeafa6f7e26a1cb0fe98f6aaeb755cb2`.

Checked §3, pp. 7–9, and §5, pp. 11–13, against the journal counterpart for Banks's inputs. The same Lemma 5.5 subscript slip occurs on p. 13. The disconnected-surface warning and complement conventions are on pp. 2 and 6. Preprint pages are not journal pages.

## H — Hatcher, 3-manifold notes

**Allen Hatcher.** *Notes on Basic 3-Manifold Topology*. Supplied author notes, using that copy's internal printed pagination. [Author PDF](https://pi.math.cornell.edu/~hatcher/3M/3M.pdf).

Acquisition: supplied author copy; the author's page is the public route. Text SHA-256: `9e88372d9e10aba5739de2e650e7dd4331312dd20349b7919ca647189744fd1a`. No unverified revision date is assigned.

Incompressibility conventions and gluing, pp. 13–15; Lemma 1.10, pp. 19–20; Lemma 1.11, p. 20; Proposition 1.12, pp. 20–22; horizontal branched covering and Euler formula, p. 22; horizontal product complement, p. 23; Proposition 1.13, pp. 23–24; Corollary 1.15, p. 25; nonorientable bases and section moves, pp. 32–35; genus-one gluing and model solid tori, pp. 40–41. The supplied audits visually checked the essential-surface and filling-model pages. These support the explicit filling derivation, not an unquoted general graph-link classification.

## HA — Hatcher, algebraic topology

**Allen Hatcher.** *Algebraic Topology*. Cambridge University Press, 2002. [Author book page](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html).

Acquisition: supplied author PDF. Checked Theorem A.6 and its countable-CW product argument, p. 524, to identify the compactly generated product from ordered triangulations with the ordinary product. The Hopf finite-input proofs and their independent reviews also checked Proposition A.1, p. 520 (compact images in finite subcomplexes), and Whitehead Theorem 4.5, p. 346, including the subcomplex deformation-retraction conclusion.

## O — Oertel

**Ulrich Oertel.** *Sums of incompressible surfaces*. *Proceedings of the American Mathematical Society* **102** (1988), no. 3, 711–719. [AMS volume](https://www.ams.org/journals/proc/1988-102-03/).

Acquisition: supplied journal PDF. Checked relative product regions, p. 712, especially the requirement that the uncollapsed vertical boundary lie in the ambient boundary; compared Banks Definition 4.1, p. 5. The Hopf-four proof does not treat an arbitrary solid-torus chamber as a product region.

## K17 — Schultens and Kapovich's appendix

**Jennifer Schultens.** *The Kakimizu complex is simply connected*, with an appendix by Michael Kapovich. *Journal of Topology* **3** (2010), no. 4, 883–900. **Checked edition:** [arXiv:0707.3926v4](https://arxiv.org/abs/0707.3926v4).

Acquisition: supplied author preprint. Text SHA-256: `0551e173a34d142294490f8027ecf72d013e3a925517305cdf2a7dcf4f7b002c`. Checked connected source and one source boundary per ambient boundary, preprint p. 18, and allowance of several boundary tori, preprint p. 20. This checks the hypothesis interface, not its complete analytic proof. Preprint pagination is not attributed to the journal.

## HT — Hatcher–Thurston

**A. Hatcher and W. Thurston.** *Incompressible surfaces in 2-bridge knot complements*. *Inventiones Mathematicae* **79** (1985), 225–246.

Acquisition: supplied public author copy, available through [Hatcher's papers page](https://pi.math.cornell.edu/~hatcher/). The supplied satellite proofs and independent reviews checked Theorem 1(b),(c),(e), p. 228 (classification and essentiality); Proposition 1, p. 230 (components and orientability); Proposition 2, p. 230 (boundary slopes); the example table, p. 231; the regular-neighbourhood double, p. 240; boundary and Euler counts, pp. 243–244; and the exact all-even component count, p. 245.

These inputs support the exact (SB) criterion, the infinite family, and the joint normal forms and complete tree for the $`K_{7/19}`$ parallel link. The tree proof also checks the pillowcase arc classification, p. 232, and the whole disconnected-system argument, pp. 233–239. Zero slope is not the same as an all-even carrier. The two-bridge proof uses the original minus continued-fraction convention; no link-table name is needed except the stated $`K_{3/7}=5_2`$ identification up to handedness.

## W — Banks, local infinitude

**Jessica E. Banks.** *On links with locally infinite Kakimizu complexes*. **Checked edition:** [arXiv:1010.3831v2](https://arxiv.org/abs/1010.3831v2), 12 April 2011.

Acquisition: supplied author preprint. Theorem 2.3 and its proof, pp. 3–4, supply the two distinct genus-one spanning surfaces used in the local insertions of [the PS counterexample](../proof/ps-counterexample.md). This package does not use a local-infinitude theorem to infer infinitely many vertices for the parallel links. The exact title, identifier and date above are taken from the supplied preprint's first page.


## HC — Hatcher, cyclic cycle complex

**Allen Hatcher.** *The cyclic cycle complex of a surface*. [arXiv:0806.0326v1](https://arxiv.org/abs/0806.0326v1), 2 June 2008, 7 pages.

Acquisition: public arXiv copy. The second proof, pp.5–6, uses bicollars to give circle maps, extends a family, combines regular-value preimages with a partition of unity, and reduces the oriented metric dual graph by eliminating sinks and sources. It is the method source for [the all-hole Hopf proof](../proof/hopf-contraction.md#13-method-sources-and-precise-scope). Monotone prescribed boundary, arc-flow averaging, fixed-graph decoding and finite parameter gluing are proved there; Hatcher’s closed-surface contraction theorem is not automatically transferred to this object.

## PR — Propp, planar orientations and matchings

**James Propp.** *Lattice structure for orientations of graphs*. **Checked edition:** [arXiv:math/0209005v3](https://arxiv.org/abs/math/0209005v3), 19 March 2021, 38 pages. Published in *Electronic Journal of Combinatorics* **32**(4) (2025), #P4.26. Page citations here refer to the checked arXiv v3, not to journal pagination.

Acquisition: public arXiv PDF. Checked §3, “Matchings of Bipartite Graphs”, Theorem 2 on p.21 and its proof and explicit face-height description on p.22. The section works with connected bipartite plane graphs, after the stated forced-edge restrictions, and derives the matching distributive lattice from orientations of the dual. This is background attribution for the classical planar matching-height structure. [The fixed-graph proof](../proof/hopf-contraction.md) independently proves all circulation, common-rounding, complete-block distance and zero-face facts it uses, including disconnected graphs, bridges and non-disk regions; Propp’s theorem is not a proof input.

## FM — Farb and Margalit

**Benson Farb and Dan Margalit.** *A Primer on Mapping Class Groups*. Princeton University Press, 2012.

Acquisition: supplied book PDF. The model and contraction proofs and their independent reviews checked pp. 33–36, particularly §1.2.7, pp. 35–36: proper arcs, endpoint-free isotopy, bigons and boundary half-bigons, simultaneous straightening and isotopy extension. These are surface-topology interfaces, rather than a contraction theorem for the matching complex.

## EP — Epstein

**D. B. A. Epstein.** *Curves on 2-manifolds and isotopies*. *Acta Mathematica* **115** (1966), 83–107.

Acquisition: supplied journal PDF. The Hopf matching model and its review checked Theorem 3.1, p. 89, for fixed-endpoint proper arcs. Free-endpoint motion is handled separately with the boundary-circle convention and the Farb–Margalit interface. No fixed-endpoint theorem is substituted without that step.

## HTri — Hatcher, ordinary arc complexes

**Allen Hatcher.** *On triangulations of surfaces*. *Topology and its Applications* **40** (1991), 189–194; checked revised and expanded author version, titled *Triangulations of Surfaces*. [Revised author PDF](https://pi.math.cornell.edu/~hatcher/Papers/TriangSurf.pdf).

Acquisition: supplied revised author copy. Its pp. 4–5 were checked in the matching construction and review. Ordinary arc surgery redirects endpoints and need not preserve one endpoint per labelled hole or positive-negative pairing; its contraction is not an input to the fixed-boundary matching theorem. This comparison is distinct from the cyclic-cycle method HC.

## S17 — Schultens, surface and 3-manifold complexes

**Jennifer Schultens.** *Kakimizu complexes of surfaces and 3-manifolds*. *Topology Proceedings* **50** (2017), 111–139. [arXiv:1401.2111v4](https://arxiv.org/abs/1401.2111v4).

Acquisition: the arXiv v4 PDF, whose banner is dated 26 April 2016; the date 13 October 2018 on its title page is the compilation date of arXiv's regenerated PDF. The checked copy is identified by PDF SHA-256 `73846865166a28de21f03a554aca6d0651af754852815db17b7985a58eab15fd`. The preprint-page references below refer to that checked copy, rather than to the journal typesetting.

Checked Definition 1 and weighted Seifert curves, pp. 3–4; deletion and transfer of weights, pp. 10, 13; Lemma 7, p. 14; Lemma 9 and Theorem 5, pp. 17–18; proposed 3-manifold framework, §8, p. 26. Vertices have weights and connected complement, and arc endpoints move freely, rather than using the prescribed unweighted boundary system here. The note records the analogous complete-frontier issue without deciding the truth of the two-dimensional statements. Its theorem is not a contraction input for our fixed-boundary complex.

## S14 — Schultens, earlier surface preprint

Same author and title, [arXiv:1401.2111v3](https://arxiv.org/abs/1401.2111v3), 24 July 2014.

Acquisition: supplied earlier preprint. The counterexample source comparison checked §§1, 3–4 against v4, including deletion of a null-homologous frontier and transfer of the smallest weight. Those operations were already present in v3; the comparison does not identify v4 as a published PS erratum.

## S18 — Schultens, Seifert-fibred spaces

**Jennifer Schultens.** *Kakimizu complexes of Seifert fibered spaces*. *Algebraic & Geometric Topology* **18** (2018), 2897–2918.

Acquisition: supplied full journal article, 22 pages. Checked the introductory applicability claim and scope, p. 2898; weighted definitions and connected-complement convention, pp. 2899–2900; §7 and Theorem 37, pp. 2912–2914. The vertical-complex identification is proved for closed orientable Seifert-fibred spaces. The Hopf-link exteriors here have boundary, and the prescribed-boundary, unweighted vertices are different objects. No automatic extension to our $`k=0`$ branch is inferred.

## Search status and citation conventions

As of 7 October 2026, the recorded literature search had located no PS 2012 erratum. No stronger priority or absence claim is made. [The counterexample](../proof/ps-counterexample.md) uses PSJ=J/PJ, PSV=PV, BC=B, BL=W, K92=K, H3=H, SchS=S17, SchSv3=S14 and SchF=S18. Its mathematical conclusions rest on the specified definitions and examples.
