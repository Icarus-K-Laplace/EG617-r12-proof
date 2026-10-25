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
status by all internal pairs, then checks:
  (i) every K5 E is disjoint from some D in G_s;
  (ii) every D in G_s has a disjoint member in every disjoint K5/K5 pair;
  (iii) for every K5 E and every disjoint low-block omitted pair (F,G),
       where |F|=5 and |G| is 4 or 5, some D in G_s is disjoint from E
       and from at least one of F,G.
A row whose omitted set is disjoint from D has a C-neighborhood containing D.
All such omitted sets lie in U\\D, a 6-set; since they have size at least 4,
they pairwise intersect. The blocker lemma then forces the corresponding
outer vertices to be C-adjacent.

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
  1: { k5: 4, k4: 18, p55: 3, p54: 28, tests55: 12, tests54: 112 },
  2: { k5: 3, k4: 15, p55: 2, p54: 20, tests55: 6, tests54: 60 },
  3: { k5: 3, k4: 15, p55: 2, p54: 20, tests55: 6, tests54: 60 },
  4: { k5: 4, k4: 18, p55: 3, p54: 28, tests55: 12, tests54: 112 }
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
let totalTests55 = 0;
let totalTests54 = 0;
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
  for (const E of K5) {
    assert(universal[s].some(D => disjoint(D, E)),
      "s=" + s + ": some K5 E is disjoint from no universal D");
  }

  let tests55 = 0;
  let tests54 = 0;
  for (const E of K5) {
    for (const [F, G] of p55) {
      tests55++;
      assert(universal[s].some(D =>
        disjoint(D, E) && (disjoint(D, F) || disjoint(D, G))),
      "s=" + s + ": no alignment for high E and low K5/K5 pair");
    }
    for (const [F, G] of p54) {
      tests54++;
      assert(universal[s].some(D =>
        disjoint(D, E) && (disjoint(D, F) || disjoint(D, G))),
      "s=" + s + ": no alignment for high E and low K5/K4 pair");
    }
  }
  assert(tests55 === exp.tests55, "s=" + s + ": incomplete K5/K5 alignment sweep");
  assert(tests54 === exp.tests54, "s=" + s + ": incomplete K5/K4 alignment sweep");
  totalTests55 += tests55;
  totalTests54 += tests54;
  summary.push({ s, K5: K5.length, K4: K4.length,
    disjointK5Pairs: p55.length, disjointK5K4Pairs: p54.length,
    alignmentChecks55: tests55, alignmentChecks54: tests54, failures: 0 });
}
assert(totalTests55 === 36, "global K5/K5 test count mismatch");
assert(totalTests54 === 344, "global K5/K4 test count mismatch");
process.stdout.write(JSON.stringify({
  contract: "exact 11-vertex normal form; s=1,2,3,4",
  universalCliqueSets: {
    1: ["A", "B"],
    2: ["A", "B", "A'"],
    3: ["A", "B", "A'"],
    4: ["A'", "B"]
  },
  summary,
  totalAlignmentChecks55: totalTests55,
  totalAlignmentChecks54: totalTests54,
  totalFailures: 0,
  result: "PASS"
}, null, 2) + "\n");
