# D′: inherited inputs, topology and fixed output classes

[Overview](../README.md) · [Objects](objects.md) · [Sources](../sources/bibliography.md) · [Scope](scope.md)

D′ proof sequence: [statement, connectivity and examples](connected-surfaces.md) (§§1–4); [exchange topology and fixed classes](connected-surfaces-exchange.md) (§§5.1–5.3); [collars and area gain](connected-surfaces-collars.md) (§§5.4–5.6); [contractibility and truncations](connected-surfaces-contractibility.md) (§§5.7–6). Section references in this sequence retain this numbering.

### 5.1 Precisely what is inherited

The competition paper §3, pp. 7–8, and its Theorem D proof, pp. 21–22, use the following geometric interface for **connected incompressible surfaces having exactly one boundary curve on each boundary torus**:

- $`(U)`$: universal disjointness of relative area minimizers in classes admitting disjoint representatives, with the whole-surface coincidence alternative.
- $`(E)(i)`$: attainment for piecewise smooth representatives with the entire prescribed boundary fixed.
- $`(E)(ii)`$: attainment while the prescribed boundary curves slide in their boundary foliations.
- $`(Fin)`$: for each fixed connected topological type and area bound, compactness and finitely many proper-isotopy classes among the stable minimal surfaces.
- $`(\mathrm{Reg1})`$, $`(\mathrm{Reg2})`$: smooth proper boundary regularity and transversality (the paper calls these (R1), (R2)), in the multiple-boundary form recorded after Theorem A.6, pp. 27–28. These names distinguish the analytic inputs from repairs R1 and R2.

We retain the original strictly convex boundary collars and their foliations; the foliation parameter space is the finite product of the individual longitude-leaf families. The local geometric interface includes the pointwise rounding-gain and admissibility bounds of competition Lemma 5.4, the positive push-off and finite area cost in competition Lemma 5.5, the tangency structure of competition Proposition 5.7, the disc-exchange inequality (14) of competition Lemma 5.6, and the local angle/tube estimates on the buffered good region in competition Corollary B.4(2),(3). Source lemma numbers in this paragraph refer to the competition paper, not the new lemmas below. Their independent analytic certification is outside this conditional statement. **We do not assume** the no-disc-patch conclusion, the multi-torus length conclusion, fixed smooth output classes, universal common-neighbor adjacency, or the final strict area inequality: §§5.3–5.7 derive those conclusions with the stated corrections. In particular the faulty deductions identified in R1–R3 are not part of the inherited interface.

The source's declared connectedness/one-curve-per-torus hypotheses are indeed met under $`(C)`$. As an additional direct check of the hypothesis interface, K17's specified preprint p. 18, explicitly assumes a compact connected source and one source boundary component on each ambient boundary component. p. 20 permit a union of boundary tori. This verifies the stated interface, not every analytic step in its proofs. No claim is made that an existing single-boundary compactness repair independently establishes this multiple-boundary package.

The author's v2 proof uses its own fixed-boundary attainment and sliding-boundary implementation (p. 65). Its four topological uses of connectedness agree with the competition version. We use its explicit local positive-parameter, collar, and classification repairs only as cross-checks for the proofs written below; we do **not** substitute its attainment or compactness implementation into the competition paper.

### 5.2 Four uses of the old hypothesis

The four uses are listed explicitly in v2, p. 67. Their competition-paper counterparts and replacements are as follows.

| Use | Competition-paper location | Replacement under (C) |
|---|---|---|
| (i) Disjointness versus coincidence | Lemma 4.3, p. 9 | Every representative is connected. Thus the coincidence alternative of (U) identifies the whole surface and hence the vertex; distinct adjacent vertices have disjoint minimizers. This supplies simultaneous flagness and the three-surface disjointness configuration. |
| (ii) A frontier has one boundary-bearing component carrying every prescribed boundary curve | Lemma 4.9, pp. 11–12; torus-by-torus count, p. 22 | Each frontier has one longitude on each torus. Discard its closed components. The remainder is a spanning surface, so (C) makes it connected, with all $`n`$ boundary curves. The condition applies before compression and before any least-area replacement. |
| (iii) A separating compression cannot split the prescribed boundary curves between two surfaces | Lemma 6.2, p. 21 | If both compressed sides had boundary, their union would be a disconnected spanning surface, contradicting (C). Exactly one side carries all the boundary; the other is closed and is discarded. |
| (iv) Vertex-set and edge-convention alignment | p. 21; original K definition, p. 225 | Every spanning surface permitted by K is already connected, and componentwise incompressibility is consequently the connected condition. There is no remaining disconnected-vertex discrepancy. The distance-one/disjoint discrepancy identified by PV concerns disconnected surfaces; the connected surface argument remains the original one. In the actual contractibility proof we keep geometric adjacency and do not need to redefine an edge using the PS convention. |

A search of both specified source texts for the old linking hypothesis and its connectivity-lemma references found no additional use of a nonzero linking number after that connectivity implication. Connectedness also supplies the analytic source hypothesis in §5.1 and the no-disc-patch argument; neither is a new consequence of linking arithmetic.

Here are the potentially hidden points explicitly, including the cover and slopes.

**Compression.** In case (iii), if the discarded closed side $`F_2`$ were a sphere, the original separating circle would bound a disk in $`F`$, contradicting essentiality. Hence $`\chi(F_2)\le0`$. Euler characteristic after compression gives

```math
\chi(F_1)=\chi(F)+2-\chi(F_2)\ge\chi(F)+2.
```

Since both $`F`$ and $`F_1`$ have $`n`$ boundary curves and are connected, $`\chi=2-2g-n`$ implies a genus decrease of at least one. A nonseparating compression also decreases genus by one. Iteration terminates and always retains a connected spanning surface. The robustness-of-neighbors argument, Lemma 4.5 and Corollary 4.6, p. 10, only needs this connected boundary-bearing surface, incompressibility of the neighbor, and irreducibility of the exterior. Its ball-isotopy argument does not invoke linking arithmetic.

**Boundary slopes.** Let $`\ell_i`$ be the preferred longitude and $`\mu_i`$ the oriented meridian of $`T_i`$. The surface-framed curve has slope

```math
\lambda_i=\ell_i-\Bigl(\sum_{j\ne i}\mathrm{lk}(L_i,L_j)\Bigr)\mu_i.
```

Indeed the oriented sum $`\partial F`$ bounds in $`S^3\setminus L_i`$, so its total linking number with $`L_i`$ is zero. Also
$`[\ell_i]=\sum_{j\ne i}\mathrm{lk}(L_i,L_j)[\mu_j]`$ in $`H_1(E)`$. Thus $`\phi(\lambda_i)=0`$, whether those linking numbers vanish or not. This is equation (26), competition p. 20, and v2 equation (46), pp. 63–64. The restriction $`\phi|\pi_1(T_i)`$ is onto because $`\phi(\mu_i)=1`$; its primitive kernel is generated by $`\lambda_i`$. The lifted torus is therefore an annulus with longitudinal core curves, exactly as required for the frontier boundary count. No nonzero linking number is used.

**Primitivity and separating lifts.** A spanning surface is dual to $`\phi`$, and $`\phi`$ is primitive since it is onto. We never claim it generates $`H_2(E,\partial E)\cong\mathbb Z^n`$. This is exactly the correction in competition p. 22 and v2 p. 67. For a connected spanning surface $`S`$, the connected cut-open domain and the stacking construction of Lemma 2.1 show that each full lift of $`S`$ separates the cover into the connected unions of levels below and above it. An entire connected input disjoint from $`S`$ lifts into one cut-open domain. Thus the upper/lower whole-surface separation required in Lemma 4.9 is valid here. We do not infer it from a claim about separate components of a disconnected surface.

**Euler-characteristic budget.** After closed frontier components of nonpositive Euler characteristic are discarded, the original normal-exchange identity gives

```math
\chi(P_\uparrow)+\chi(P_\downarrow)\ge\chi(A)+\chi(B).
```

All four boundary-bearing surfaces are connected with $`n`$ boundary curves. Substitution of $`\chi=2-2g-n`$, instead of the knot formula $`1-2g`$, cancels the fixed $`4-2n`$ terms and gives

```math
g(P_\uparrow)+g(P_\downarrow)\le g(A)+g(B).
```

Subsequent compressions only decrease genus. Consequently the genus budget in Theorem 5.1(c), competition p. 17, is unchanged, rather than requiring a new disconnected-surface complexity.

### 5.3 R1: fixed smooth classes before a later neighbor

Fix transverse connected inputs $`A,B`$, with disjoint boundary tuples and a fixed connected surface $`S`$ disjoint from both. The cover/frontier construction of §5.2 gives two labelled corner frontiers, in opposite regions of the strip between lifts of $`S`$. Fix their corner charts and sector labels. Write $`\eta_\uparrow,\eta_\downarrow`$ for smooth positive admissible widths, and $`\sigma>0`$ for a sufficiently small positive push-off time. Closed components will be discarded after these operations.

**Lemma 5.3 (positive widths and push-offs determine representatives, not classes).** With those charts and labels fixed, all sufficiently small admissible positive-width roundings and positive push-offs give the same two smooth ambient-isotopy classes, separately labelled $`\uparrow,\downarrow`$. The isotopies can fix $`S`$, preserve each boundary torus, and retain a longitude leaf on each torus throughout. In particular the classes have representatives inside every neighborhood of $`A\cup B`$ disjoint from $`S`$.

**Proof.** For either frontier, compare widths $`\eta^0,\eta^1>0`$ by

```math
\eta^u=(1-u)\eta^0+u\eta^1,\qquad 0\le u\le1.
```

The constraints $`0<\eta\le\eta_{\max}`$ and $`|\partial_s\eta|\le\kappa`$ are convex, since the charts and bounds are fixed. Compactness gives $`\min_{\Gamma\times[0,1]}\eta^u>0`$. In the source's straightened coordinates the profile is

```math
\xi_1=m(s)\eta^u(s)\Theta\!\left(\xi_2/\eta^u(s)\right)
\quad\text{for }|\xi_2|\le\eta^u(s),
```

and is $`m(s)|\xi_2|`$ outside. Infinite-order matching at the edges makes this a smooth embedding family in $`u`$; see the explicit profile and seam calculation at competition p. 29 and p. 30. The labelled roundings remain separated in opposite sectors, agree with their respective unmodified patches off the seams, and are unchanged near the ambient boundary. Smooth isotopy extension with a cutoff in the prescribed neighborhood gives an ambient isotopy of the pair fixing $`S`$. Only **positive** widths occur; no smooth diffeomorphism taking a genuine corner to a smooth sheet is asserted.

Along this compact family choose smooth inward push-off fields. Near each boundary torus use a fixed field tangent to that torus and carrying its longitude leaves to leaves; the roundings there are unchanged. Extend by inward normals in the interior and a nonnegative partition of unity. Positivity of the inward normal component is retained. Compactness gives one small positive flow time valid throughout the family. On a fixed rounding, admissible fields can likewise be compared by convex interpolation after reducing flow time, keeping their boundary fields fixed. First reduce the initial push-off to a common small time, then vary widths and fields, then adjust to the final small time. This gives a smooth isotopy of the outputs. The push-off construction is competition p. 31; its class independence at fixed width alone does not prove the width comparison.

Finally replace both widths by $`\lambda\eta_\bullet`$, $`0<\lambda\le1`$. All constraints persist. For this fixed compact transverse pair, slopes and chart distortion are bounded, so the actual geometric support and displacement of rounding tend uniformly to zero as $`\lambda\downarrow0`$. Coordinate width is not being identified with metric radius. The roundings eventually lie in any prescribed neighborhood of the input union. Choose positive push-offs still smaller so they stay there, in their own open regions. The preceding comparisons retain the already fixed classes. Discarding closed components retains the same labelled boundary-bearing classes by (C). $`\square`$

**Lemma 5.4 (fixed descendants and the universal-neighbor quantifier).** Fix the coarse classes using one positive-width, positive-push-off choice, and fix a terminating compression sequence for each, hence two final vertices $`w_\uparrow,w_\downarrow`$. For every later common neighbor $`z`$ of the two input vertices, these **same** vertices are equal or adjacent to $`z`$. This also holds for the perturbation families used when the original inputs have interior tangencies or common boundary leaves.

**Proof in the transverse case.** Choose a minimizer $`Z\in z`$. Universal disjointness and whole-surface connectedness make $`Z`$ disjoint from both fixed input minimizers when its class is distinct from them. Set $`d_Z=\mathrm{dist}(Z,A\cup B)>0`$, and choose a neighborhood of $`A\cup B`$ whose closure misses $`Z\cup S`$. By Lemma 5.3 first shrink both positive widths, and then shrink the positive push-offs, to put both coarse representatives in that neighborhood. Their classes remain the ones chosen before $`z`$. Keeping width fixed and only letting $`\sigma\downarrow0`$ would approach the rounded surface and would not justify this step.

Transport each originally specified compression sequence along this smooth ambient isotopy. At each step apply the cleaning in competition Lemma 4.5, p. 10, to the transported prescribed disc and the incompressible $`Z`$. A circle of intersection bounds discs in the compressing disc and in $`Z`$. An innermost disc on $`Z`$, together with the disc it bounds on the compressing disc, gives an interior sphere and hence a ball. The connected boundary-bearing surface misses the sphere and reaches the ambient boundary, so lies outside the ball. The remaining annulus of the compressing disc also lies outside: its interior misses the sphere and it attaches to that same outside surface. Sliding across the ball therefore cleans the prescribed disc without changing its compression class. Repeat finitely many times, transporting the next **specified** disc after each adjustment. This preserves every intermediate and final class, rather than choosing a new descendant after $`z`$. Corollary 4.6, p. 10, gives equality or adjacency. Equality or adjacency to the input vertices and the initial common neighbor follows by cleaning against $`S,A,B`$ separately.

**Positive perturbation parameters.** In the non-transverse cases take the fixed smooth family $`A_t\to A`$, $`0<t\le\delta`$, transverse to $`B`$, with disjoint boundary tuples and disjoint from $`S`$. The no-disc conclusion is established in §5.6. We first show that the labelled smooth coarse classes are constant for positive $`t`$, before any later neighbor is specified.

On a compact interval $`J=[t_a,t_b]\subset(0,\delta]`$, transversality, boundary separation, and separation from $`S`$ have positive minima. Correct the embedding velocity of $`A_t`$ along its intersection with $`B`$ by a vector tangent to $`A_t`$, so the corrected velocity is tangent to $`B`$. Transversality supplies the right inverse. Extend to a time-dependent ambient field tangent to $`B`$ and the ambient boundary and vanishing on $`S`$. Its flow $`H_t`$ moves $`A_{t_a}`$ to $`A_t`$, preserves $`B`$ setwise, and fixes $`S`$. Lift from the identity to the cyclic cover. The lift fixes the two $`S`$-walls, commutes with the deck map, and preserves upper/lower labels, so transports the labelled corner frontiers. This is the construction at competition p. 36.

To compare **smooth** outputs, choose corner frames and straightening charts coherently along this compact transverse track. The oriented sheet normals and their labelled bisectors supply the frames. Compactness gives common positive chart radii and admissibility bounds on $`J`$. Use one sufficiently small constant width $`\bar\eta>0`$ along every seam on the track; its arclength derivative is zero. The profile and unchanged moving patches form a compact smooth surface track whose projection to $`J`$, including the boundary track, is a submersion. A horizontal vector field tangent to that boundary track parametrizes it by neat embeddings. At each endpoint compare its quantitative width to $`\bar\eta`$ in those same endpoint charts by Lemma 5.3, and compare positive push-offs using a common small time. Smooth isotopy extension gives the same two labelled smooth classes at both endpoints. This neither assumes $`H_t`$ sends a separately optimized rounding exactly to another nor assumes smooth dependence of optimized widths on $`t`$; neither $`t=0`$ nor zero width is an output endpoint.

Thus the coarse classes are constant on $`(0,\delta]`$. At one $`t_*>0`$, fix both compression sequences and final vertices. Only afterwards choose $`z,Z`$. Since $`Z`$ misses the compact original union $`A\cup B`$, choose $`t_z>0`$ so it also misses $`A_{t_z}\cup B`$. Apply Lemma 5.3 at this fixed $`t_z`$ to shrink **both** widths and push-offs, transport the fixed sequences, and clean them against $`Z`$. The same final vertices result. For adjacency to the original input vertex $`[A]`$, clean against $`A_{t_z}`$, not necessarily against $`A`$ itself: $`[A_{t_z}]=[A]`$. Cleaning against $`S`$ and $`B`$ works as before. The quantifier order is

```math
\forall(x,u,w)\ \exists(w_\uparrow,w_\downarrow)\ \forall z\ \exists
(\text{same-class representatives and transported, cleaned discs}).
```

In the non-transverse cases the last choices include $`t_z,\eta_z,\sigma_z`$. No positive width, input-to-neighbor distance, or area gain uniform over all later neighbors is required. $`\square`$

These repair competition p. 12 and p. 17 and p. 36. Cross-check the positive-width and two-scale arguments against v2 p. 33 and p. 34, and the coherent positive-$`t`$ comparison against v2 p. 49 and pp. 50–51. No v2 existence or compactness theorem is used.
