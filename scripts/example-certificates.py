#!/usr/bin/env python3
"""Offline, exact certificates for closed braids and total-linking Alexander rank.

Requires Python 3 and sympy. Run this file from any directory; its only output
file is example-certificates-results.json next to it. No network, environment secrets or Git.

Words are tuples of signed generator indices (1-based). The Artin convention is
sigma_i(x_i)=x_i*x_{i+1}*x_i^-1, sigma_i(x_{i+1})=x_i.
For beta=g_1...g_k, rho(beta)=rho(g_1) o ... o rho(g_k).
The closure group has relators rho(beta)(x_j)*x_j^-1.
All meridians are sent to t; every computation is exact over Q(t).
"""

from __future__ import annotations

import hashlib
import json
from itertools import combinations
from pathlib import Path

import sympy as sp

t = sp.Symbol("t")


def reduced(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(int(letter))
    return tuple(stack)


def inverse(word):
    return tuple(-letter for letter in reversed(word))


def substitute(word, images):
    result = ()
    for letter in word:
        image = images[abs(letter) - 1]
        result = reduced(result + (image if letter > 0 else inverse(image)))
    return result


def artin_generator(n, signed_index):
    i = abs(signed_index)
    if not 1 <= i < n:
        raise ValueError("Invalid braid generator")
    images = [(j,) for j in range(1, n + 1)]
    if signed_index > 0:
        images[i - 1] = (i, i + 1, -i)
        images[i] = (i,)
    else:
        images[i - 1] = (i + 1,)
        images[i] = (-(i + 1), i, i + 1)
    return tuple(images)


def artin_action(n, braid):
    images = tuple((j,) for j in range(1, n + 1))
    for letter in braid:
        images = tuple(substitute(w, images) for w in artin_generator(n, letter))
    return images


def fox_row(word, n):
    """Abelianized left Fox derivatives, computed directly from a free word."""
    row = [sp.Integer(0)] * n
    prefix_exponent = 0
    for letter in word:
        j = abs(letter) - 1
        if letter > 0:
            row[j] += t ** prefix_exponent
            prefix_exponent += 1
        else:
            row[j] -= t ** (prefix_exponent - 1)
            prefix_exponent -= 1
    return [sp.factor(x) for x in row]


def generator_matrix(n, signed_index):
    """Independent hard-coded unreduced Burau/Fox matrix, no free-word calls."""
    i = abs(signed_index) - 1
    matrix = sp.eye(n)
    block = (sp.Matrix([[1 - t, t], [1, 0]]) if signed_index > 0 else
             sp.Matrix([[0, 1], [1 / t, 1 - 1 / t]]))
    matrix[i:i + 2, i:i + 2] = block
    return matrix


def burau_product(n, braid):
    product = sp.eye(n)
    # Left Fox chain rule: J(alpha o gamma)=J(gamma)*J(alpha).
    # All Artin automorphisms preserve the total-exponent homomorphism.
    for letter in braid:
        product = generator_matrix(n, letter) * product
    return product.applyfunc(sp.factor)


def component_and_linking_data(n, braid):
    # Each entry is the top-strand label currently occupying a bottom position.
    labels = list(range(1, n + 1))
    crossings = []
    for step, signed_index in enumerate(braid, start=1):
        i = abs(signed_index) - 1
        crossings.append({"step": step, "generator": signed_index,
                          "top_labels": [labels[i], labels[i + 1]],
                          "sign": 1 if signed_index > 0 else -1})
        labels[i], labels[i + 1] = labels[i + 1], labels[i]
    # Closing bottom position j to top j makes cycles of this permutation.
    cycles = []
    unseen = set(range(1, n + 1))
    while unseen:
        start = min(unseen)
        cycle = []
        current = start
        while current in unseen:
            unseen.remove(current)
            cycle.append(current)
            current = labels[current - 1]
        cycles.append(cycle)
    owner = {strand: i for i, cycle in enumerate(cycles) for strand in cycle}
    counts = [[0 for _ in cycles] for _ in cycles]
    for crossing in crossings:
        a, b = (owner[label] for label in crossing["top_labels"])
        crossing["components_zero_based"] = [a, b]
        crossing["intercomponent"] = a != b
        if a != b:
            counts[a][b] += crossing["sign"]
            counts[b][a] += crossing["sign"]
    assert all(value % 2 == 0 for row in counts for value in row)
    linking = [[value // 2 for value in row] for row in counts]
    # Test every nontrivial partition up to exchanging the two parts.
    witnesses = []
    m = len(cycles)
    for mask in range(1, (1 << m) - 1):
        if not mask & 1:
            continue
        part = [i for i in range(m) if mask & (1 << i)]
        other = [i for i in range(m) if not mask & (1 << i)]
        sums = [sum(linking[i][j] for j in (other if i in part else part))
                for i in range(m)]
        if all(value == 0 for value in sums):
            witnesses.append({"part_zero_based": part,
                              "complement_zero_based": other,
                              "cross_linking_sums": sums})
    return {"bottom_position_to_top_label": labels, "component_cycles": cycles,
            "component_count": m, "crossings": crossings,
            "linking_matrix": linking,
            "linking_indecomposable": len(witnesses) == 0,
            "decomposable_partition_witnesses": witnesses}


def matrix_strings(matrix):
    return [[str(sp.factor(matrix[i, j])) for j in range(matrix.cols)]
            for i in range(matrix.rows)]


def exact_certificate(name, n, braid, expected_components=None, expected_rank=None):
    images = artin_action(n, braid)
    relators = tuple(reduced(image + (-(j + 1),)) for j, image in enumerate(images))
    jacobian = sp.Matrix([fox_row(image, n) for image in images])
    relation_matrix = sp.Matrix([fox_row(relator, n) for relator in relators])
    independent = burau_product(n, braid)
    assert (jacobian - independent).applyfunc(sp.cancel) == sp.zeros(n)
    assert (relation_matrix - jacobian + sp.eye(n)).applyfunc(sp.cancel) == sp.zeros(n)
    assert (relation_matrix * sp.ones(n, 1)).applyfunc(sp.cancel) == sp.zeros(n, 1)
    # sympy handles rational functions exactly; no floating point specialization.
    rank = relation_matrix.rank(iszerofunc=lambda x: sp.cancel(x) == 0)
    h1_rank = n - 1 - rank
    minors = []
    for rows in combinations(range(n), n - 1):
        for columns in combinations(range(n), n - 1):
            value = sp.factor(relation_matrix.extract(rows, columns).det())
            if value != 0:
                minors.append({"rows_zero_based": list(rows),
                               "columns_zero_based": list(columns),
                               "determinant": str(value)})
    # Since J*1=1, quotient by the invariant line gives a reduced Burau matrix.
    basis = sp.eye(n)
    basis[:, n - 1] = sp.ones(n, 1)
    conjugated = (basis.inv() * independent * basis).applyfunc(sp.factor)
    assert conjugated[:n - 1, n - 1] == sp.zeros(n - 1, 1)
    assert conjugated[n - 1, n - 1] == 1
    reduced_burau = conjugated[:n - 1, :n - 1]
    reduced_determinant = sp.factor((sp.eye(n - 1) - reduced_burau).det())
    closure_polynomial = sp.factor(reduced_determinant / sum(t ** j for j in range(n)))
    data = component_and_linking_data(n, braid)
    ordinary_h1_dimension = n - relation_matrix.subs(t, 1).rank()
    assert ordinary_h1_dimension == data["component_count"]
    if expected_components is not None:
        assert data["component_count"] == expected_components
    if expected_rank is not None:
        assert h1_rank == expected_rank
    if h1_rank == 0:
        assert minors
        assert reduced_determinant != 0
    data.update({"name": name, "strand_count": n, "braid_word": list(braid),
                 "artin_images_signed_words": [list(w) for w in images],
                 "closure_relators_signed_words": [list(w) for w in relators],
                 "fox_jacobian": matrix_strings(jacobian),
                 "alexander_relation_matrix": matrix_strings(relation_matrix),
                 "independent_unreduced_burau_product": matrix_strings(independent),
                 "fox_equals_independent_matrix": True,
                 "relation_matrix_rank_over_Qt": rank,
                 "boundary_d1_rank_over_Qt": 1,
                 "kernel_d1_dimension_over_Qt": n - 1,
                 "ordinary_H1_dimension_at_t1": ordinary_h1_dimension,
                 "r_phi": h1_rank,
                 "nonzero_maximal_minors": minors,
                 "reduced_burau_matrix": matrix_strings(reduced_burau),
                 "det_I_minus_reduced_burau": str(reduced_determinant),
                 "burau_closure_polynomial_up_to_unit": str(closure_polynomial),
                 "non_split_certificate": ("r_phi=0; the proved connectivity lemma excludes a split link" if h1_rank == 0 else "not asserted")})
    return data


def consistency_checks():
    # These checks protect the group-action and Fox conventions, independently
    # of the two examples. They are not a classification by numerical guesses.
    n = 3
    identity = tuple((j,) for j in range(1, n + 1))
    assert artin_action(n, [1, -1, 2, -2]) == identity
    assert artin_action(n, [1, 2, 1]) == artin_action(n, [2, 1, 2])
    assert burau_product(n, [1, -1, 2, -2]) == sp.eye(n)
    assert (burau_product(n, [1, 2, 1]) - burau_product(n, [2, 1, 2])).applyfunc(sp.cancel) == sp.zeros(n)
    unlink = sp.Matrix([fox_row((j, -j), 2) for j in [1, 2]])
    assert unlink.rank() == 0  # r_phi(unlink_2)=1
    hopf_images = artin_action(2, [1, 1])
    hopf_A = sp.Matrix([fox_row(reduced(w + (-(j + 1),)), 2)
                       for j, w in enumerate(hopf_images)])
    assert hopf_A.rank() == 1  # r_phi(Hopf)=0
    assert component_and_linking_data(2, [1, 1])["linking_matrix"] == [[0, 1], [1, 0]]
    return {"inverse_actions": True, "braid_relation_free_words": True,
            "inverse_matrices": True, "braid_relation_matrices": True,
            "two_component_unlink_rank": 1, "positive_Hopf_rank": 0,
            "positive_Hopf_linking_number": 1}


def main():
    checks = consistency_checks()
    examples = [exact_certificate("specified_two_component_braid", 3, [1, -2, 1, -2, 1], 2, 0),
                exact_certificate("three_component_braid", 3, [1, -2, 1, -2, 1, -2], 3, 0)]
    for example in examples:
        assert all(value == 0 for row in example["linking_matrix"] for value in row)
        assert not example["linking_indecomposable"]
    result = {"schema_version": "1.0", "sympy_version": sp.__version__,
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "coefficient_ring": "Q[t,t^-1]", "rank_field": "Q(t)",
              "orientation": "all braid strands oriented from top to bottom, then closed",
              "conventions": {"positive_Artin_action": "xi -> xi*x(i+1)*xi^-1; x(i+1) -> xi",
                              "word_composition": "rho(g1...gk)=rho(g1) o ... o rho(gk)",
                              "Fox_chain_rule_at_total_linking": "J(phi o psi)=J(psi)*J(phi)",
                              "presentation": "<x1,...,xn | rho(beta)(xj)*xj^-1, j=1,...,n>",
                              "rank_formula": "r_phi=(n-1)-rank_Q(t)(J_beta-I)"},
              "consistency_checks": checks, "examples": examples,
              "limitations": ["No standard-link table identification is asserted.",
                              "Matrix product is an independent implementation of the same Alexander invariant, not a different invariant.",
                              "Non-splitness uses the connectivity lemma proved in the accompanying Markdown."]}
    target = Path(__file__).resolve().with_name("example-certificates-results.json")
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    for example in examples:
        print(json.dumps({key: example[key] for key in ["name", "component_count", "linking_matrix", "relation_matrix_rank_over_Qt", "r_phi", "linking_indecomposable", "nonzero_maximal_minors", "burau_closure_polynomial_up_to_unit"]}, ensure_ascii=False))
    print(f"Wrote {target}")


if __name__ == "__main__":
    main()
