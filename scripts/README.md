# Exact braid certificates

[Overview](../README.md) · [Mathematical derivation](../proof/connected-surfaces.md#4-exact-new-examples)

`example-certificates.py` requires Python 3 and Sympy. The supplied certificate and repeated packaging run use **Sympy 1.14.0**. With that dependency already installed, run from the repository root:

```sh
python3 -B scripts/example-certificates.py
```

The program writes `example-certificates-results.json` alongside itself. It uses exact rational functions over $`\mathbb Q(t)`$, without floating-point evaluations or numerical rank estimates. It records expanded Artin words and relators, Fox matrices, all nonzero maximal minors, component permutations, crossing ownership, linking numbers and its own SHA-256. It checks against a separately implemented generator-matrix product, inverses, the braid relation, the two-component unlink and the positive Hopf link.

For the specified examples the component counts are 2 and 3. Every linking number is zero, the relation-matrix rank is 2, and $`r_\phi=0`$. The first maximal minors are $`(t-1)^3`$ and $`(t-1)^4/t`$. The accompanying topology proves all-surface connectedness and non-splitness; these are not guesses from a link table.

The published program has only a filename/docstring adaptation from the reviewed computation. Recomputing its fingerprint explains the different `script_sha256`; its mathematical certificate fields agree with the original. The two routes compute the same Alexander invariant, not unrelated invariants.

Code uses [MIT](LICENSE); this documentation uses CC BY 4.0 as specified in [the repository licence](../LICENSE).
