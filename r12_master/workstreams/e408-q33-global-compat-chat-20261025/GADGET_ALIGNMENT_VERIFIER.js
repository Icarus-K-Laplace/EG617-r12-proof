#!/usr/bin/env node
"use strict";

/*
Deterministic finite verifier for the exact-129 11-vertex gadget alignment lemmas.

Normal form for each s in {1,2,3,4}:
  A={a0,...,a4}, B={b0,...,b4}, x.
  A and B are cliques.
  a0 is adjacent to b0,...,b_(s-1).
  x is adjacent to a1,...,a4 and b_s,...,b4.
  No other cross-edges.
This is the normal form from Theorem 12.1.

Universal K5 family:
  s=1: {A,B}
  s=2,3: {A,B,A'}
  s=4: {A',B}, where A'={a1,a2,a3,a4,x}.

The script exhausts every subset of each 11-vertex graph, tests clique status
pairwise, builds every disjoint clique pair of the indicated sizes, and checks
all alignment properties used by P49_BOUNDARY_EXCLUSION.md and the R=14
boundary analysis.

IMPORTANT SCOPE:
  * The pair/pair alignment assertion deliberately excludes type (5,3)+(5,3).
    That combination is ruled out by the integer budget in every use below.
  * No claim is made for a high K4 against a low (5,3) pair in isolation; that
    broader assertion has a counterexample for s=2,3.
  * These are fixed-size gadget checks, not a graph-completion certificate.
*/

function fail(message) {
  process.stderr.write("FAIL: " + message + "\n");
  process.exit(1);
}
function assert(condition, message) {
  if (!condition) fail(message);
}
function popcount(mask) {
  let n = 0;
  for (let x = mask; x; x &= x - 1) n++;
  return n;
}
function isClique(mask, adjacency, n) {
  for (let i = 0; i < n; i++) {
    if (((mask >>> i) & 1) === 0) continue;
    for (let j = i + 1; j < n; j++) {
      if (((mask >>> j) & 1) && ((adjacency[i] >>> j) & 1) === 0) return false;
    }
  }
  return true;
}
function enumerateCliques(adjacency, n, size) {
  const result = [];
  for (let mask = 0; mask < (1 << n); mask++) {
    if (popcount(mask) === size && isClique(mask, adjacency, n)) result.push(mask);
  }
  return result;
}
function disjoint(a, b) {
  return (a & b) === 0;
}
function edge(adjacency, u, v) {
  adjacency[u] |= 1 << v;
  adjacency[v] |= 1 << u;
}
function makeGadget(s) {
  const adjacency = Array(11).fill(0);
  for (let i = 0; i < 5; i++) for (let j = i + 1; j < 5; j++) edge(adjacency, i, j);
  for (let i = 5; i < 10; i++) for (let j = i + 1; j < 10; j++) edge(adjacency, i, j);
  for (let j = 5; j < 5 + s; j++) edge(adjacency, 0, j);
  for (let i = 1; i < 5; i++) edge(adjacency, 10, i);
  for (let j = 5 + s; j < 10; j++) edge(adjacency, 10, j);
  return adjacency;
}
function maskOf(vertices) {
  return vertices.reduce((m, v) => m | (1 << v), 0);
}
function disjointPairs(bySize, type) {
  const a = Number(type[0]), b = Number(type[1]), out = [];
  if (a === b) {
    const xs = bySize[a];
    for (let i = 0; i < xs.length; i++) {
      for (let j = i + 1; j < xs.length; j++) {
        if (disjoint(xs[i], xs[j])) out.push({ E: xs[i], F: xs[j], type });
      }
    }
  } else {
    for (const E of bySize[a]) {
      for (const F of bySize[b]) {
        if (disjoint(E, F)) out.push({ E, F, type });
      }
    }
  }
  return out;
}
function pairHasMemberDisjoint(D, pair, minSize = 0) {
  return [pair.E, pair.F].some(E => popcount(E) >= minSize && disjoint(D, E));
}
function findD(families, predicate) {
  return families.some(D => predicate(D));
}

const expected = {
  1: { k3: 32, k4: 18, k5: 4, p55: 3, p54: 28, p53: 52, p44: 65 },
  2: { k3: 30, k4: 15, k5: 3, p55: 2, p54: 20, p53: 40, p44: 50 },
  3: { k3: 30, k4: 15, k5: 3, p55: 2, p54: 20, p53: 40, p44: 50 },
  4: { k3: 32, k4: 18, k5: 4, p55: 3, p54: 28, p53: 52, p44: 65 }
};
const A = maskOf([0, 1, 2, 3, 4]);
const B = maskOf([5, 6, 7, 8, 9]);
const Aprime = maskOf([1, 2, 3, 4, 10]);
const universal = {
  1: [A, B],
  2: [A, B, Aprime],
  3: [A, B, Aprime],
  4: [Aprime, B]
};

const summary = [];
const totals = {
  baseHighK5: 0, baseHighK4: 0, highK3Low55: 0,
  highK5Low53or44: 0, highK5TwoLowPairs: 0,
  pairPairExcept53_53: 0, tripleHighPairTwoLowPairs: 0
};
let totalFailures = 0;

for (let s = 1; s <= 4; s++) {
  const adjacency = makeGadget(s);
  const bySize = {
    3: enumerateCliques(adjacency, 11, 3),
    4: enumerateCliques(adjacency, 11, 4),
    5: enumerateCliques(adjacency, 11, 5)
  };
  const p55 = disjointPairs(bySize, "55");
  const p54 = disjointPairs(bySize, "54");
  const p53 = disjointPairs(bySize, "53");
  const p44 = disjointPairs(bySize, "44");
  const low = [...p55, ...p54];
  const highPairs = [...p55, ...p54, ...p53, ...p44];
  const exp = expected[s];

  assert(bySize[3].length === exp.k3, "s=" + s + ": K3 count mismatch");
  assert(bySize[4].length === exp.k4, "s=" + s + ": K4 count mismatch");
  assert(bySize[5].length === exp.k5, "s=" + s + ": K5 count mismatch");
  assert(p55.length === exp.p55, "s=" + s + ": disjoint K5/K5 pair count mismatch");
  assert(p54.length === exp.p54, "s=" + s + ": disjoint K5/K4 pair count mismatch");
  assert(p53.length === exp.p53, "s=" + s + ": disjoint K5/K3 pair count mismatch");
  assert(p44.length === exp.p44, "s=" + s + ": disjoint K4/K4 pair count mismatch");

  for (const D of universal[s]) {
    assert(bySize[5].includes(D), "s=" + s + ": universal set is not a K5");
    for (const pair of p55) {
      assert(pairHasMemberDisjoint(D, pair),
        "s=" + s + ": a universal D misses both members of a disjoint K5/K5 pair");
    }
  }

  let baseHighK5 = 0, baseHighK4 = 0, highK3Low55 = 0;
  let highK5Low53or44 = 0, highK5TwoLowPairs = 0;
  let pairPairExcept53_53 = 0, tripleHighPairTwoLowPairs = 0;
  let failures = 0;

  // Original lemma: high omitted E of size 5 or 4, low pair of type 55 or 54.
  for (const E of bySize[5]) {
    for (const pair of low) {
      baseHighK5++;
      if (!findD(universal[s], D => disjoint(D, E) && pairHasMemberDisjoint(D, pair, 4))) {
        failures++;
      }
    }
  }
  for (const E of bySize[4]) {
    for (const pair of low) {
      baseHighK4++;
      if (!findD(universal[s], D => disjoint(D, E) && pairHasMemberDisjoint(D, pair, 4))) {
        failures++;
      }
    }
  }

  // R=14 r=7/8 terminal: high omitted K3 against six r=1 blocks (type 55).
  for (const E of bySize[3]) {
    for (const pair of p55) {
      highK3Low55++;
      if (!findD(universal[s], D => disjoint(D, E) && pairHasMemberDisjoint(D, pair, 5))) {
        failures++;
      }
    }
  }

  // r=6 with r=3: a high gadget-only row has omitted K5; low pair is 53 or 44.
  for (const E of bySize[5]) {
    for (const pair of [...p53, ...p44]) {
      highK5Low53or44++;
      if (!findD(universal[s], D => disjoint(D, E) && pairHasMemberDisjoint(D, pair, 4))) {
        failures++;
      }
    }
  }

  // r=6 Case A/B with two r=2 blocks: one fixed high omitted K5 and two low pairs 55/54.
  for (const E of bySize[5]) {
    for (const p of low) {
      for (const q of low) {
        highK5TwoLowPairs++;
        if (!findD(universal[s], D =>
          disjoint(D, E) && pairHasMemberDisjoint(D, p, 4) && pairHasMemberDisjoint(D, q, 4))) {
          failures++;
        }
      }
    }
  }

  // Two omitted pairs: select a member of size >=4 from each.
  // Exclude 53+53, which is ruled out by the R<=14 missing-edge budget.
  for (const p of highPairs) {
    for (const q of highPairs) {
      if (p.type === "53" && q.type === "53") continue;
      pairPairExcept53_53++;
      if (!findD(universal[s], D =>
        pairHasMemberDisjoint(D, p, 4) && pairHasMemberDisjoint(D, q, 4))) {
        failures++;
      }
    }
  }

  // One high omitted pair and two low pairs of type 55/54.
  for (const p of highPairs) {
    for (const q of low) {
      for (const z of low) {
        tripleHighPairTwoLowPairs++;
        if (!findD(universal[s], D =>
          pairHasMemberDisjoint(D, p, 4) &&
          pairHasMemberDisjoint(D, q, 4) &&
          pairHasMemberDisjoint(D, z, 4))) {
          failures++;
        }
      }
    }
  }

  totals.baseHighK5 += baseHighK5;
  totals.baseHighK4 += baseHighK4;
  totals.highK3Low55 += highK3Low55;
  totals.highK5Low53or44 += highK5Low53or44;
  totals.highK5TwoLowPairs += highK5TwoLowPairs;
  totals.pairPairExcept53_53 += pairPairExcept53_53;
  totals.tripleHighPairTwoLowPairs += tripleHighPairTwoLowPairs;
  totalFailures += failures;
  summary.push({
    s,
    cliqueCounts: { K3: bySize[3].length, K4: bySize[4].length, K5: bySize[5].length },
    pairCounts: { "55": p55.length, "54": p54.length, "53": p53.length, "44": p44.length },
    alignmentChecks: {
      highK5Low55or54: baseHighK5,
      highK4Low55or54: baseHighK4,
      highK3Low55: highK3Low55,
      highK5Low53or44: highK5Low53or44,
      highK5TwoLowPairs: highK5TwoLowPairs,
      pairPairExcept53_53: pairPairExcept53_53,
      tripleHighPairTwoLowPairs: tripleHighPairTwoLowPairs
    },
    failures
  });
}

const totalChecks = Object.values(totals).reduce((a, b) => a + b, 0);
assert(totals.baseHighK5 === 380, "global high-K5 base count mismatch");
assert(totals.baseHighK4 === 1776, "global high-K4 base count mismatch");
assert(totals.highK3Low55 === 312, "global high-K3/low-55 count mismatch");
assert(totals.highK5Low53or44 === 1476, "global high-K5/low-53-or-44 count mismatch");
assert(totals.highK5TwoLowPairs === 10592, "global high-K5/two-low-pair count mismatch");
assert(totals.pairPairExcept53_53 === 60288, "global pair-pair count mismatch");
assert(totals.tripleHighPairTwoLowPairs === 392872, "global triple-alignment count mismatch");
assert(totalChecks === 467696, "global alignment test total mismatch");
assert(totalFailures === 0, "one or more alignment checks failed");

process.stdout.write(JSON.stringify({
  contract: "four exact 11-vertex normal forms; all 2^11 subsets per form",
  universalCliqueSets: {
    1: ["A", "B"],
    2: ["A", "B", "A'"],
    3: ["A", "B", "A'"],
    4: ["A'", "B"]
  },
  summary,
  totals,
  totalChecks,
  totalFailures,
  result: "PASS"
}, null, 2) + "\n");
