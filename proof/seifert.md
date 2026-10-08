# Seifert exteriors: surface dichotomy and classification

[Overview](../README.md) · [Objects](objects.md) · [Sources](../sources/bibliography.md) · [Scope](scope.md)

Merged proof sequence: [objects and elementary interfaces](objects.md) (§§1–2), [Seifert applications](seifert.md) (§3), and [closure and main theorem](main-theorem.md) (§§4–7). References to these numbered sections use this sequence.

## 3. Seifert exteriors: the full surface dichotomy

Fix a Seifert fibering of $`E(L)`$, an oriented regular fibre $`f`$, and $`k=\phi(f)`$. Reversing the fibre orientation reverses $`k`$, not the alternatives below. On each $`T_i`$ a regular fibre is a primitive slope, and regular fibres on different tori are freely homotopic up to orientation. Write its slope in the basis of §2.1 as

```math
f_i=k_i\mu_i+u_i\gamma_i,\qquad k_i=\pm k.
```

Therefore

```math
|\gamma_i\cdot f_i|=|k|.
\qquad\text{(3.1)}
```

For $`k=0`$, primitivity gives $`f_i=\pm\gamma_i`$; for $`k\ne0`$, the boundary slope has nonzero geometric intersection with the fibre slope. These are statements about the actual boundary data, not guessed from a named link classification.

**Theorem 3.1 (Seifert dichotomy).** Let $`E(L)`$ be Seifert fibred.

**Vertical case:** If $`k=0`$, every component of every incompressible spanning surface is isotopic to a vertical annulus. Thus $`n`$ is even, every such surface has $`n/2`$ annulus components, $`\chi_-=0`$, and $`x_E(\alpha)=0`$. In the reduced spanning convention,
  
```math
X(L)=MS(E(L)).
  \qquad\text{(3.2)}
```

**Horizontal case:** If $`k\ne0`$, every incompressible spanning surface is connected and isotopic to a horizontal surface. All spanning surfaces are connected, so D′ applies with its stated geometric inputs. In fact $`L`$ is fibred for $`\phi`$, and $`X(L)`$ is a point by [the fibred-surface proof](connected-sum.md), §6.1, giving an alternative proof with no PS projection or minimal-area input.

**Proof.** The unknot is covered by §2.3. Otherwise apply H Proposition 1.12 (pp. 20–22) to each essential component. A horizontal surface has transverse boundary, so (3.1) excludes it if $`k=0`$. A vertical component with boundary is an annulus: vertical surfaces are circle bundles over one-manifolds, and the closed torus and Klein-bottle alternatives are excluded here (H, p. 22). Its boundary circles lie on different labelled tori. This proves the first component classification, in every genus; simultaneous verticalization of the whole system is not needed for its Euler characteristic.

An incompressible surface exists by §2.2. Its annuli represent $`\alpha`$ with zero norm, so $`x_E(\alpha)=0`$. Conversely a reduced norm-zero spanning surface in this nontrivial boundary-irreducible exterior has only annuli: disks are excluded in §2.3, and any other orientable component with boundary has negative Euler characteristic. An annulus's core is homotopic to its essential boundary in an incompressible boundary torus, so it is nontrivial in $`\pi_1(E)`$ and the annulus is incompressible. Thus both vertex sets in (3.2) agree. Their whole-complement distance definition and flag completion agree as well. This proves equality of complexes. It supplies no contraction in the general vertical case; only the independently treated cases below have a contractibility conclusion here.

If $`k\ne0`$, (3.1) excludes vertical components. Each horizontal connected component projects onto the entire connected base by H's branched-cover description and the explicit surjectivity statement (pp. 22–23). In particular it meets **every** boundary torus: in boundary charts the projection is a finite covering of boundary collars. Two horizontal components would provide at least two boundary curves on every torus, impossible. Hence there is exactly one component. This argument does not assume that separately chosen isotopies of components can be performed simultaneously.

Lemma 2.2 now proves connectedness of all spanning surfaces, including the uncompressed ones required in D′. The whole complement of this connected horizontal surface is connected by §2.1. H's horizontal-surface argument then gives $`E\mathbin{\|}F=F\times I`$ (p. 23), not the separating semi-bundle alternative. Gluing its two horizontal faces makes $`E`$ a surface bundle over $`S^1`$ with fibre $`F`$. Its oriented fibre class is $`\mathrm{PD}(\phi)`$, so this is the required spanning fibration. ∎

**Exceptional fibres and the Euler formula.** If the remaining exceptional fibres have multiplicities $`q_1,\ldots,q_s\ge2`$, a connected horizontal spanning surface has degree

```math
d=|k|,\qquad
\chi(F)=d\left(\chi(B)-\sum_{j=1}^s(1-1/q_j)\right).
\qquad\text{(3.3)}
```

The degree is determined on any boundary torus: its single transverse boundary meets a regular fibre in exactly $`|k|`$ points. At an exceptional fibre of multiplicity $`q_j`$, a horizontal disk patch projects with local degree $`q_j`$, so $`q_j\mid d`$, and the surface has $`d/q_j`$ points over that cone point. Triangulating the base with these points as vertices gives (3.3). This is exactly H, p. 22. The exceptional fibres were included in Proposition 1.12's proof, pp. 20–21; no argument assuming a product exterior has replaced that proposition. The formula is a check on horizontal topology, not a license to assert that an arbitrary orientation or slope produces such a surface. Here existence came from compressing a genuine spanning surface.

The base of an exterior in $`S^3`$ is planar and orientable, as proved next, so $`\chi(B)=2-n`$. With the solid-torus exception separated, there are no boundary-parallel annuli, hidden closed components, or one-sided surfaces in this proof. The dichotomy is relative to the chosen Seifert fibering; exteriors such as $`T^2\times I`$ can have more than one fibering, which causes no inconsistency.

### 3.1. Which links in $`S^3`$ have Seifert exteriors?

For completeness the following classification is derived from meridional filling; it is not attributed to the surface-classification proposition. Up to homeomorphism of oriented pairs, allowing the component orientations to be assigned arbitrarily, they are precisely the union of these two constructions:

1. A finite nonempty collection of fibres in a Seifert fibering of $`S^3`$. Equivalently, choose coprime nonzero integers $`p,q`$; take finitely many regular orbits of
   
$`\displaystyle (z_1,z_2)\longmapsto(e^{ipt}z_1,e^{iqt}z_2),\qquad (z_1,z_2)\in S^3\subset\mathbb C^2,`$

   and optionally either or both coordinate-core circles. Regular orbits are parallel $`(p,q)`$ torus curves; the core circles may be exceptional or regular. This includes torus knots/links, their core-axis additions, and the elementary unknot/Hopf cases.
2. A **keychain**: one unknotted central component together with $`n-1`$ mutually unlinked meridian circles, each linked once with the central component, in the standard product arrangement. Its exterior is $`S^1\times\Sigma_{0,n}`$. For $`n=1`$ this is the unknot and for $`n=2`$ a Hopf link. The two constructions need not be disjoint.

In particular “a union of fibres of a fibering of $`S^3`$” alone is not a complete classification: the meridian-equals-fibre filling case must be included.

**Derivation.** An orientation-reversing simple base loop, avoiding cone points, would lift to an embedded Klein bottle (H, p. 32). No closed nonorientable surface embeds in $`S^3`$: a one-sided loop would intersect it once modulo two, contradicting $`H_1(S^3;\mathbb Z/2)=0`$. Thus the base is orientable. A nonseparating base loop would lift to a torus whose complement in $`E`$ is connected, whereas every embedded torus in $`S^3`$ separates (also H, p. 14). The base therefore has genus zero and $`n`$ boundary circles.

Remove the exceptional-fibre neighborhoods and choose a section of the resulting product circle bundle. With $`h=f`$, exceptional loops $`x_j`$, and oriented boundary section loops $`d_i`$, van Kampen gives

```math
\pi_1(E)=\left\langle h,x_1,\ldots,x_s,d_1,\ldots,d_n\,\middle|\,
 h\text{ central},\quad x_j^{q_j}h^{c_j}=1,\quad
 x_1\cdots x_s d_1\cdots d_n=1\right\rangle.
\qquad\text{(3.4)}
```

Any section integer in the last relation can be absorbed into a $`d_i`$, since the base has boundary. Here $`q_j\ge2`$ and $`\gcd(c_j,q_j)=1`$. The meridian slope on $`T_i`$ is

```math
\mu_i=d_i^{a_i}h^{b_i},\qquad \gcd(a_i,b_i)=1.
\qquad\text{(3.5)}
```

These coordinates follow directly from H's model and section construction, pp. 32–35. The exponent $`|a_i|`$ is the meridian's intersection with the regular fibre, not its intersection with the spanning longitude.

**No fibre-meridian.** If every $`a_i\ne0`$, the fibering extends across every original meridional solid-torus filling, with core multiplicity $`|a_i|`$ (H, p. 33). The filled manifold is the original $`S^3`$, and its base is $`S^2`$. Its orbifold group is the quotient of $`\pi_1(S^3)`$ by the fibre, and hence trivial. A sphere with three or more cone points has nontrivial orbifold group: killing all but three cone generators surjects onto

```math
\langle u,v,w\mid u^a=v^b=w^c=uvw=1\rangle,
\qquad a,b,c\ge2.
```

This triangle group has a nontrivial rotation representation from reflections in a triangle of angles $`\pi/a,\pi/b,\pi/c`$, on the sphere, Euclidean plane, or hyperbolic plane according as the angle sum is greater than, equal to, or less than $`\pi`$. The product of two adjacent reflections has the indicated order and is not the identity; the three rotation generators multiply to one. Thus there are at most two genuine cone points. With two orders their orbifold group is $`\mathbb Z/\gcd(a,b)`$, so the orders are coprime.

Split the base sphere into two disks containing at most one cone point each. Their preimages are model-fibred solid tori, by the same model construction (H, p. 41). In their common torus the meridians intersect once: van Kampen, or its first-homology matrix, gives intersection magnitude one because the union is $`S^3`$. Choose them as the standard Heegaard basis. The common regular-fibre slope is primitive and is nonmeridional on both sides, so it has coprime nonzero coordinates $`p,q`$. The solid-torus model on either side is determined by this slope; it is the weighted fibering displayed above. Original filling cores are fibres, proving construction 1 in this case. The reduction to the standard $`S^3`$ gluing is the elementary lens-space calculation in H, pp. 40–41.

**At least one fibre-meridian.** Let $`z`$ be the number of $`a_i=0`$. Primitivity makes the corresponding meridian $`h^{\pm1}`$, so the filled group kills $`h`$. Solve the final relation of (3.4) for one such unrestricted $`d_i`$. The filled fundamental group is then the free product

```math
\left(\mathop{*}_{j=1}^s\mathbb Z/q_j\right)
 *\left(\mathop{*}_{a_i\ne0}\mathbb Z/|a_i|\right)
 * F_{z-1}.
\qquad\text{(3.6)}
```

Triviality of $`\pi_1(S^3)`$ forces $`z=1`$, $`s=0`$, and $`|a_i|=1`$ on every other boundary. Thus $`E=S^1\times\Sigma_{0,n}`$. Change the section along arcs from the distinguished boundary to the others to remove their integers $`b_i`$; the compensating change on the distinguished boundary does not change its fibre meridian. This is the explicit section-twist move of H, p. 34. Filling all other boundaries along the resulting $`d_i`$ gives $`S^1\times D^2`$, with $`n-1`$ standard parallel product cores. Filling its remaining boundary along $`h`$ makes $`S^3`$. The final core is an unknot, and those product cores are its standard mutually unlinked meridians. This is precisely construction 2. Also $`\phi(h)=\pm1`$ on its distinguished meridian, so this fibering is in the $`k\ne0`$ branch.

Conversely deleting fibre neighborhoods in construction 1 preserves a Seifert fibering. In construction 2, the complement of the central unknot is $`D^2\times S^1`$, and deleting neighborhoods of the standard product cores leaves $`\Sigma_{0,n}\times S^1`$. This proves both directions of the classification. It includes the solid-torus case rather than assuming boundary-irreducibility there. No classification of arbitrary graph-link exteriors or multiple Seifert JSJ pieces is asserted. ∎

### 3.2. Balanced Hopf fibres

Let $`H_{2m}`$, $`m\ge1`$, be $`2m`$ regular positive Hopf fibres, $`m`$ with each orientation. Then $`E(H_{2m})=S^1\times\Sigma_{0,2m}`$. In common Hopf coordinates,

```math
[f]=\sum_{i=1}^{2m}[\mu_i^H],\qquad
\phi(\mu_i^H)=\epsilon_i,\qquad
k=\sum_i\epsilon_i=0.
```

The homology formula follows equally from $`f=\ell_i^H+\mu_i^H`$ on a component torus and the linking number one between distinct reference-oriented fibres. All pairwise actual linking numbers are $`\epsilon_i\epsilon_j\ne0`$, so the link is non-split. Theorem 3.1 proves that every incompressible spanning surface consists of exactly $`m`$ annuli and

```math
X(H_{2m})=MS(E(H_{2m})).
\qquad\text{(3.7)}
```

For every $`m\ge1`$, [the matching model](hopf-model.md) and [the finite-input contraction](hopf-contraction.md), Theorem 9.1, prove that $`X(H_{2m})`$ is contractible. For $`m=1`$ it is a point with annular spanning fibre; for $`m=2`$ the [Hopf-four calculation](hopf-four.md) retains the stronger Farey-tree description. Every $`m\ge2`$ is nonfibred in this balanced class, as proved in [the main theorem](main-theorem.md), §6.3.

For any nonempty oriented union of Hopf fibres, $`k=\sum_i\epsilon_i`$. If it is balanced, the preceding proof applies; otherwise $`k\ne0`$ and Theorem 3.1 gives the prescribed fibration and a one-vertex complex. This includes a single fibre, the unknot. Hence all Hopf fibre links are covered. The $`k=0`$ cases with exceptional fibres remain outside the contraction claim. Equality (3.7) alone does not prove that broader vertical case; see [scope](scope.md).
