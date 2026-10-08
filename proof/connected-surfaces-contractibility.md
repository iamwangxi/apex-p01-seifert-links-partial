# D′: the exchange conclusion and downward-closed truncations

[Overview](../README.md) · [Objects](objects.md) · [Sources](../sources/bibliography.md) · [Scope](scope.md)

D′ proof sequence: [statement, connectivity and examples](connected-surfaces.md) (§§1–4); [exchange topology and fixed classes](connected-surfaces-exchange.md) (§§5.1–5.3); [collars and area gain](connected-surfaces-collars.md) (§§5.4–5.6); [contractibility and truncations](connected-surfaces-contractibility.md) (§§5.7–6). Section references in this sequence retain this numbering.

### 5.7 Proof of Theorem D′

There is a spanning surface by the Seifert construction. Under (C), the compression argument in §5.2 gives an incompressible connected spanning surface, so $`IS(L)`$ is nonempty. Kakimizu's Theorem A, K10 p. 226, gives connectedness for a non-split link. The exterior is irreducible.

By (E), choose a relative area minimizer for each vertex independently of later neighbors. By (U) and §5.2(i), minimizers of distinct adjacent classes are disjoint. Every finite clique therefore has simultaneously disjoint representatives: $`IS(L)`$ is flag. This also supplies $`S\cap(A\cup B)=\varnothing`$ for a distance-two pair with a common neighbor.

Put $`c(v)=(g(v),A(v))`$, lexicographically ordered. At fixed genus $`h`$, all representatives have connected type $`(h,n)`$. By (E) and (Fin), only finitely many vertices of this type have area at most any given bound. Competition Lemma 4.8, p. 11, applies: each genus fiber of attained areas is well ordered, and so is their ordered sum over $`h\in\mathbb N`$. The attained value set, not all of $`\mathbb N\times\mathbb R_{>0}`$, is used.

For a distance-two pair $`u,w`$, §§5.4–5.6 give a transverse configuration with no disc patches and fixed positive gain, or use (T0) directly. The slope, primitivity, boundary count and Euler calculations in §5.2 produce two connected boundary-bearing outputs. Fix their coarse smooth classes and compression sequences, obtaining $`w_\uparrow,w_\downarrow`$. Lemmas 5.3–5.4 show these fixed vertices are equal or adjacent to **every** common neighbor; compression robustness also gives equality or adjacency to the input vertices and initial common neighbor. The genus budget is

```math
g(w_\uparrow)+g(w_\downarrow)\le g(u)+g(w).
```

In equality, §5.6 gives strict decrease in the sum of vertex area infima. Some output has complexity below $`\max\{c(u),c(w)\}`$: if input genera differ, an output genus is below their maximum; if they agree, either an output genus is smaller or both output genera equal the common genus, when strict area-sum decrease forces an output area below the maximum input area. This supplies (N2); fixed universal-neighbor adjacency supplies (N1).

Thus $`(IS(L),c)`$ is an exchange complex. The competition paper's combinatorial Theorem B gives contractibility. Closed frontier components were discarded topologically before least-area replacement; all surfaces supplied to inherited minimization/compactness are connected with one boundary curve per torus. This proves the first assertion of Theorem D′; §6 proves the truncation assertion. $`\square`$

## 6. Truncations

Let $`D`$ be a nonempty vertex set with the following precise downward-closed property:

```math
v\in D,\quad c(u)\le c(v)\quad\Longrightarrow\quad u\in D.
```

In particular $`D`$ is a union of complete complexity fibers. Break ties as in competition Lemma 2.2, p. 4. The refined well-order compares original complexity first, so $`D`$ remains downward closed. Corollary 2.3, p. 4, gives isometric embedding and connectedness of the full subcomplex. Lemma 2.4(1), pp. 4–5, makes it an exchange complex, and Theorem B makes it contractible.

The genus set $`D_\ell=\{g\le\ell\}`$ has this property, and is nonempty exactly when $`\ell\ge g(L)`$, where $`g(L)`$ is the minimum genus of the connected spanning surfaces. A least-genus surface is incompressible by the compression result above. The lexicographic set $`D_{\ell,a}`$ in §1 also has the property. It is nonempty if $`\ell>g(L)`$, or if $`\ell=g(L)`$ and $`a`$ is at least the least attained area at that genus.

This is the truncation actually used in the competition proof, p. 20. The introductory Theorem C, p. 2, uses a rectangle $`\{g\le\ell,A\le a\}`$; such a rectangle need not be downward closed for the lexicographic order. **We do not transfer that broader wording.** No claim is made for empty truncations or arbitrary rectangular genus/area caps.
