# Two-bridge companions: the exact (SB) criterion

[Overview](../README.md) · [Objects](objects.md) · [Sources](../sources/bibliography.md) · [Scope](scope.md)

Parallel-satellite proof sequence: [cone theorem and witnesses](parallel-satellites.md) (§§1–5, 9); [two-bridge criterion and examples](parallel-satellites-two-bridge.md) (§§6–7); [distance-two obstruction](parallel-satellites-obstruction.md) (§8). References within this sequence retain these section numbers. The [torus exact-edge proof](parallel-satellites-torus.md) has its own numbering.

## 6. The exact two-bridge criterion and a counterexample

Use HT's minus continued-fraction convention

```math
[b_1,\ldots,b_k]=\frac1{b_1-\dfrac1{b_2-\cdots-\dfrac1{b_k}}},\qquad
\frac pq=r+[b_1,\ldots,b_k],\qquad |b_i|\ge2.
```

HT Theorem 1(b),(c), p. 228, classifies all nonclosed essential surfaces by these carriers and proves their essentiality. HT Proposition 2, p. 230, gives

```math
m(b)=2\bigl(s(b)-s(b^0)\bigr),\qquad
s(b)=\sum_i\mathrm{sign}(b_i),
```

where $`b^0`$ is the unique all-even expansion. The coefficient counts in this formula are not the sheet number $`N`$. Each boundary circle wraps once longitudinally, and there are exactly $`N`$ boundary circles: see HT pp. 243–244.

For an all-even carrier the **whole** $`N`$-sheeted surface has exactly $`N`$ components, not just “is disconnected for $`N>1`$”: HT Proposition 1(1), p. 230, with proof on p. 245. This assertion applies only after one has established that the carrier is all-even.

**Theorem 6.1 (two-bridge (SB) criterion).** A nontrivial two-bridge knot $`K_{p/q}`$ satisfies (SB) if and only if every admissible expansion with $`s(b)=s(b^0)`$ is all-even. Equivalently, its only zero-slope carrier is its unique all-even carrier.

**Proof.** If every zero-slope carrier is all-even, HT classifies a connected surface in (SB) on one of them. Its $`N`$ components force $`N=1`$, hence one boundary.

Conversely suppose there is a zero-slope carrier containing an odd coefficient. Its one-sheeted plumbing $`R=S_1(0,\ldots,0)`$ is connected and nonorientable (HT p. 230). Take the horizontal frontier of a small regular neighbourhood of $`R`$ in the orientable exterior. It is its orientation double, hence connected and orientable. HT explicitly identify this double as

```math
\widehat R=S_2(0,\ldots,0)
```

on the same carrier: more generally the regular-neighbourhood boundary of $`S_N(n_i)`$ is $`S_{2N}(2n_i)`$, HT p. 240. The vertical annulus lying on $`\partial Q`$ is omitted in the proper-surface frontier and its corners are rounded. Theorem 1(c) makes the frontier incompressible and boundary-incompressible. Proposition 1(2) independently confirms its connectedness. Proposition 2 gives two preferred-longitude boundaries, so it violates (SB). ∎

This also settles the orientation issue: merely discarding the nonorientable one-sheeted ancestor would wrongly discard its orientable two-sheeted frontier.

### 6.1. Explicit rational certificate for $`K_{7/19}`$

The two expansions

```math
\frac7{19}=1+[-2,-2,2,-2]=[2,-2,-2,-3]
```

are admissible. In the first, successive tails from the end are $`-1/2,2/5,-5/12,-12/19`$. In the second they are $`-1/3,-3/5,-5/7,7/19`$. The first is all-even and has signed coefficient count $`-2`$; the second also has signed count $`-2`$. The latter therefore has **zero** slope although its last coefficient is odd.

Let $`R=S_1(0,0,0)`$ on the second carrier. Its connected orientable frontier $`S=S_2(0,0,0)`$ is essential, has two preferred-longitude boundaries, and

```math
\chi(S)=2(1-4)=-6,\qquad 2-2g(S)-2=-6,\qquad g(S)=3.
```

Here the Euler formula is HT p. 244. The two boundary orientations are opposite: $`S`$ is a relative boundary of the regular neighbourhood, so $`[S]=0`$ and its oriented longitude sum vanishes. Thus the example also satisfies the zero-relative-class companion condition relevant to the parallel-link problem. This is an actual embedded essential surface, not just a boundary-slope entry.

For use in §8, the complete expansion list is

| $`r`$ | $`b`$ | $`s(b)`$ | Slope |
|---:|---|---:|---:|
| 0 | $`[2,-2,-2,-3]`$ | -2 | 0 |
| 0 | $`[3,3,-2]`$ | 1 | 6 |
| 0 | $`[3,4,2]`$ | 3 | 10 |
| 1 | $`[-2,-3,-2,-3]`$ | -4 | -4 |
| 1 | $`[-2,-2,2,-2]`$ | -2 | 0 |
| 1 | $`[-2,-2,3,2]`$ | 0 | 4 |

Here is an exhaustive arithmetic method, used with exact rational arithmetic. Every nonempty admissible tail $`x`$ has $`0\lt|x|\lt1`$. This follows inductively from $`|b|\ge2`$ and $`|x_{\rm next}|\lt1`$. Thus for $`0\lt p/q\lt1`$ the integer part is $`r=0`$ or $`1`$. At each subsequent step $`x=1/(b-y)`$ the only options have $`|b|\ge2`$ and $`|b-1/x|\lt1`$; take $`y=b-1/x`$, terminating at zero. If $`x=a/d`$ is reduced and $`|a|\lt d`$, the reduced denominator of nonzero $`y`$ is $`|a|\lt d`$. Hence the recursion terminates and exhausts all expansions; there is no search cutoff. Applying it at $`7/19`$ gives exactly the six rows above. In particular the only zero carriers have four bands.

For reproducibility, this is the exact finite computation used for the table. The denominator argument just given is its termination and exhaustion proof.

```python
from fractions import Fraction
from functools import lru_cache

@lru_cache(None)
def tails(x):
    if x == 0:
        return [()]
    z = 1 / x
    k = z.numerator // z.denominator
    return [(b,) + t
            for b in range(k - 1, k + 3)
            if abs(b) >= 2 and abs(b - z) < 1
            for t in tails(b - z)]

def expansions(x):
    return [(r, b) for r in (0, 1) for b in tails(x - r)]

def value(b):
    x = Fraction(0)
    for c in reversed(b):
        x = 1 / (c - x)
    return x

x = Fraction(7, 19)
rows = expansions(x)
assert len(rows) == 6
assert all(r + value(b) == x for r, b in rows)
baseline = [b for r, b in rows if all(c % 2 == 0 for c in b)]
assert baseline == [(-2, -2, 2, -2)]
s0 = sum(1 if c > 0 else -1 for c in baseline[0])
for r, b in rows:
    slope = 2 * (sum(1 if c > 0 else -1 for c in b) - s0)
    print(r, b, slope)
```

**Not every two-bridge knot satisfies (SB).** Proposition 1(1) cannot be applied to a zero-slope branch merely from its slope. The missing implication “zero slope implies all coefficients even” is false.

## 7. A valid infinite two-bridge family, including $`5_2`$

**Theorem 7.1.** For every integer $`m\ge1`$, the nontrivial two-bridge knot

```math
C_m=K_{(2m-1)/(4m-1)}
```

satisfies (SB). Its two oppositely oriented zero-framed parallels have $`a`$ as a cone vertex and contractible $`X`$. The same holds for the mirrors. For $`m\ge2`$ this supplies nonfibred companions.

**Proof of (SB).** For $`m\ge2`$ the exhaustive admissible expansion list is

```math
1+[-2,-2m],\qquad [2,-(2m-1)],\qquad
[3,\underbrace{2,\ldots,2}_{2m-2}].
```

All have value $`(2m-1)/(4m-1)`$. Exhaustion follows from the same strict-tail rule as in §6.1. For integer part one, the reciprocal of the negative tail is $`-2+1/(2m)`$; only $`b_1=-2`$ is allowed, and the residual reciprocal $`-2m`$ terminates. For integer part zero, the reciprocal is $`2+1/(2m-1)`$; only $`b_1=2,3`$ are allowed. The former terminates with $`-(2m-1)`$. The latter leaves $`(2m-2)/(2m-1)`$. A tail $`j/(j+1)`$, $`j\ge1`$, permits only the next coefficient two and then leaves $`(j-1)/j`$; induction gives precisely the displayed string of twos.

Their signed counts are respectively $`-2,0,2m-1`$, so their slopes are $`0,4,4m+2`$. Only the first is zero, and it is all-even. Theorem 6.1 proves (SB). At $`m=1`$, the list is just $`1+[-2,-2]`$ and $`[3]`$, with slopes zero and six; the same conclusion follows. Theorem 1.1 then gives the cone and contractibility.

**Nonfibredness when $`m\ge2`$.** The one-sheeted all-even surface is the genus-one plumbing of the two bands with $`-2,-2m`$ half-twists. For their oriented core basis, a choice of plumbing square gives a Seifert matrix

```math
V=\begin{pmatrix}-1&1\\0&-m\end{pmatrix},\qquad
\det(V-tV^T)=m t^2+(1-2m)t+m.
```

The diagonal entries are the full twists $`-1,-m`$; the single plumbing contributes one off-diagonal linking and zero in the other direction. Reversing a core orientation changes both off-diagonal signs and leaves the determinant unchanged. This is the ordinary two-band Seifert calculation in the band convention of HT p.226 and Fig.2, p.227; the determinant is also verified directly from the displayed matrix. A fibred knot has a monic Alexander polynomial, since it is the characteristic polynomial of the integral monodromy on fibre homology, up to a unit. The extreme coefficients here have absolute value $`m>1`$, proving nonfibredness. ∎

At $`m=2`$ this gives $`C_2=K_{3/7}=5_2`$ up to handedness, with polynomial $`2t^2-3t+2`$. Thus a nonfibred example is included without assuming the invalid assertion about all two-bridge knots. No finiteness or infinitude of the parallel link's complete vertex set is asserted.
