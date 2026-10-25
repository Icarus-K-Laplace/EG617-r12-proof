#!/usr/bin/env node
"use strict";

/*
Deterministic finite verifier for the 11-vertex exact-129 gadget alignment lemma.

Input contract:
  A = {a0,...,a4}, B = {b0,...,b4}, and x.
  A and B are cliques. For a parameter s in {1,2,3,4}, a0 is adjacent
  to b0,...,b_(s-1); x is adjacent to a1,...,a4 and b_s,...,b4.
  There are no other cross-edges.
This is exactly the normal form derived from alpha(U)=2, omega(U)=5,
e(U)=29 after swapping A and B so that |A_0|=1.

For each s, G_s is the following list of "universal" K5 cliques:
  s=1: {A,B}
  s=2,3: {A,B,A'}
  s=4: {A',B}
where A'={a1,a2,a3,a4,x}.

The verifier exhaustively enumerates all 2^11 vertex subsets, checks clique
status by all internal pairs, then checks every omitted set E of size four or
five that is a clique, every disjoint K5/K5 pair, and every disjoint K5/K4
pair. It certifies:
  (i) every such E is disjoint from some D in G_s;
  (ii) every D in G_s has a disjoint member in every disjoint K5/K5 pair;
  (iii) for every E and every disjoint low-block omitted pair (F,G),
       where (|F|,|G|)=(5,5) or (5,4), some D in G_s is disjoint from E
       and from at least one of F,G.
A row whose omitted set is disjoint from D has a C-neighborhood containing D.
All such omitted sets lie in U\\D, a 6-set; since they have size at least four,
they pairwise intersect. The blocker compatibility theorem then forces the
corresponding outer vertices to be C-adjacent.

No external packages or randomness are used.
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
      if (((mask >>> j) & 1) && ((adjacency[i] >>> j) & 1) === 0) {
        return false;
      }
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
  const n = 11;
  const adjacency = Array(n).fill(0);
  // A={0,...,4}, B={5,...,9}, x=10.
  for (let i = 0; i < 5; i++) {
    for (let j = i + 1; j < 5; j++) edge(adjacency, i, j);
  }
  for (let i = 5; i < 10; i++) {
    for (let j = i + 1; j < 10; j++) edge(adjacency, i, j);
  }
  for (let j = 5; j < 5 + s; j++) edge(adjacency, 0, j);
  for (let i = 1; i < 5; i++) edge(adjacency, 10, i);
  for (let j = 5 + s; j < 10; j++) edge(adjacency, 10, j);
  return adjacency;
}
function maskOf(vertices) {
  return vertices.reduce((m, v) => m | (1 << v), 0);
}

const expected = {
  1: { k5: 4, k4: 18, p55: 3, p54: 28, tests55K5: 12, tests54K5: 112, tests55K4: 54, tests54K4: 504 },
  2: { k5: 3, k4: 15, p55: 2, p54: 20, tests55K5: 6, tests54K5: 60, tests55K4: 30, tests54K4: 300 },
  3: { k5: 3, k4: 15, p55: 2, p54: 20, tests55K5: 6, tests54K5: 60, tests55K4: 30, tests54K4: 300 },
  4: { k5: 4, k4: 18, p55: 3, p54: 28, tests55K5: 12, tests54K5: 112, tests55K4: 54, tests54K4: 504 }
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
let total55K5 = 0, total54K5 = 0, total55K4 = 0, total54K4 = 0;
for (let s = 1; s <= 4; s++) {
  const adjacency = makeGadget(s);
  const K5 = enumerateCliques(adjacency, 11, 5);
  const K4 = enumerateCliques(adjacency, 11, 4);
  const p55 = [];
  for (let i = 0; i < K5.length; i++) {
    for (let j = i + 1; j < K5.length; j++) {
      if (disjoint(K5[i], K5[j])) p55.push([K5[i], K5[j]]);
    }
  }
  const p54 = [];
  for (const F of K5) {
    for (const G of K4) {
      if (disjoint(F, G)) p54.push([F, G]);
    }
  }
  const exp = expected[s];
  assert(K5.length === exp.k5, "s=" + s + ": unexpected K5 count " + K5.length);
  assert(K4.length === exp.k4, "s=" + s + ": unexpected K4 count " + K4.length);
  assert(p55.length === exp.p55, "s=" + s + ": unexpected disjoint K5-pair count");
  assert(p54.length === exp.p54, "s=" + s + ": unexpected disjoint K5/K4-pair count");

  for (const D of universal[s]) {
    assert(K5.includes(D), "s=" + s + ": universal D is not a K5");
    for (const [F, G] of p55) {
      assert(disjoint(D, F) || disjoint(D, G),
        "s=" + s + ": D fails to align with a disjoint K5/K5 pair");
    }
  }

  // Every high omitted clique E of size 4 or 5 must align with a universal D.
  for (const E of [...K5, ...K4]) {
    assert(universal[s].some(D => disjoint(D, E)),
      "s=" + s + ": some size-4/5 clique E is disjoint from no universal D");
  }

  let tests55K5 = 0, tests54K5 = 0, tests55K4 = 0, tests54K4 = 0;
  for (const E of K5) {
    for (const [F, G] of p55) {
      tests55K5++;
      assert(universal[s].some(D =>
        disjoint(D, E) && (disjoint(D, F) || disjoint(D, G))),
      "s=" + s + ": no K5/K5 alignment for high K5 E");
    }
    for (const [F, G] of p54) {
      tests54K5++;
      assert(universal[s].some(D =>
        disjoint(D, E) && (disjoint(D, F) || disjoint(D, G))),
      "s=" + s + ": no K5/K4 alignment for high K5 E");
    }
  }
  for (const E of K4) {
    for (const [F, G] of p55) {
      tests55K4++;
      assert(universal[s].some(D =>
        disjoint(D, E) && (disjoint(D, F) || disjoint(D, G))),
      "s=" + s + ": no K5/K5 alignment for high K4 E");
    }
    for (const [F, G] of p54) {
      tests54K4++;
      assert(universal[s].some(D =>
        disjoint(D, E) && (disjoint(D, F) || disjoint(D, G))),
      "s=" + s + ": no K5/K4 alignment for high K4 E");
    }
  }
  assert(tests55K5 === exp.tests55K5, "s=" + s + ": incomplete K5-high/K5-pair sweep");
  assert(tests54K5 === exp.tests54K5, "s=" + s + ": incomplete K5-high/K5-K4-pair sweep");
  assert(tests55K4 === exp.tests55K4, "s=" + s + ": incomplete K4-high/K5-pair sweep");
  assert(tests54K4 === exp.tests54K4, "s=" + s + ": incomplete K4-high/K5-K4-pair sweep");
  total55K5 += tests55K5; total54K5 += tests54K5;
  total55K4 += tests55K4; total54K4 += tests54K4;
  summary.push({ s, K5: K5.length, K4: K4.length,
    disjointK5Pairs: p55.length, disjointK5K4Pairs: p54.length,
    highK5Checks55: tests55K5, highK5Checks54: tests54K5,
    highK4Checks55: tests55K4, highK4Checks54: tests54K4, failures: 0 });
}
assert(total55K5 === 36, "global K5-high/K5-pair test count mismatch");
assert(total54K5 === 344, "global K5-high/K5-K4-pair test count mismatch");
assert(total55K4 === 168, "global K4-high/K5-pair test count mismatch");
assert(total54K4 === 1608, "global K4-high/K5-K4-pair test count mismatch");
process.stdout.write(JSON.stringify({
  contract: "exact 11-vertex normal form; s=1,2,3,4",
  universalCliqueSets: {
    1: ["A", "B"],
    2: ["A", "B", "A'"],
    3: ["A", "B", "A'"],
    4: ["A'", "B"]
  },
  summary,
  alignmentChecks: {
    highK5_vs_K5Pair: total55K5,
    highK5_vs_K5K4Pair: total54K5,
    highK4_vs_K5Pair: total55K4,
    highK4_vs_K5K4Pair: total54K4
  },
  totalAlignmentChecks: total55K5 + total54K5 + total55K4 + total54K4,
  totalFailures: 0,
  result: "PASS"
}, null, 2) + "\n");
