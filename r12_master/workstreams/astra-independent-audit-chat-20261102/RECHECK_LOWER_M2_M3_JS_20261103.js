#!/usr/bin/env node
"use strict";

// Independent JavaScript replay of the M2 C5-type quotient and M3
// 23-vertex neighborhood-cost representatives. No imported project code.

const mod = x => ((x % 5) + 5) % 5;
const T = Array.from({length: 5}, (_, i) => new Set([mod(i - 1), mod(i + 1)]));
const compatible = (i, j) => ![...T[i]].some(x => T[j].has(x));
const subsets = [];
for (let mask = 1; mask < 32; mask++) {
  subsets.push(Array.from({length: 5}, (_, i) => i).filter(i => (mask >> i) & 1));
}
const pairs = [];
for (const A of subsets) for (const B of subsets) {
  if (A.every(i => B.every(j => compatible(i, j)))) pairs.push([A, B]);
}
const missing = [];
for (const [A, B] of pairs) for (let u = 0; u < 5; u++) for (let v = 0; v < 5; v++) {
  if (!B.every(j => compatible(u, j))) continue;
  if (!A.every(i => compatible(i, v))) continue;
  if (compatible(u, v)) continue;
  missing.push([A, B, u, v]);
}
let extensionPositions = 0;
let extensionFailures = 0;
for (const [A, B] of pairs) {
  const unionB = new Set(B.flatMap(j => [...T[j]]));
  const available = [0, 1, 2, 3, 4].filter(x => !unionB.has(x));
  for (const p of available) {
    extensionPositions++;
    const qs = available.filter(q =>
      q !== p &&
      T.some(t => t.size === 2 && t.has(p) && t.has(q)) &&
      B.every(j => ![...T[j]].some(x => x === p || x === q))
    );
    if (!qs.length) extensionFailures++;
  }
}

const bitCount = x => {
  let c = 0;
  while (x) { x &= x - 1n; c++; }
  return c;
};
function build(sizes) {
  const groups = [];
  let n = 0;
  for (const size of sizes) {
    groups.push(Array.from({length: size}, (_, i) => n + i));
    n += size;
  }
  const edges = [];
  for (let i = 0; i < 5; i++) {
    for (const u of groups[i]) for (const v of groups[(i + 1) % 5]) edges.push([u, v]);
  }
  return {groups, edges, n};
}
function maximalIndependentSets(n, edges) {
  const all = (1n << BigInt(n)) - 1n;
  const complement = Array.from({length: n}, (_, i) => all ^ (1n << BigInt(i)));
  for (const [u, v] of edges) {
    complement[u] &= (~(1n << BigInt(v))) & all;
    complement[v] &= (~(1n << BigInt(u))) & all;
  }
  const output = [];
  function visit(R, P, X) {
    if ((P | X) === 0n) { output.push(R); return; }
    const candidatesInPX = [];
    for (let i = 0; i < n; i++) if (((P | X) >> BigInt(i)) & 1n) candidatesInPX.push(i);
    let pivot = candidatesInPX[0];
    let best = -1;
    for (const i of candidatesInPX) {
      const score = bitCount(complement[i] & P);
      if (score > best) { best = score; pivot = i; }
    }
    let candidates = P & (all ^ complement[pivot]);
    while (candidates) {
      const bit = candidates & (-candidates);
      const v = bit.toString(2).length - 1;
      visit(R | bit, P & complement[v], X & complement[v]);
      P &= (all ^ bit);
      X |= bit;
      candidates &= (all ^ bit);
    }
  }
  visit(0n, all, 0n);
  return output;
}
function inducedEdges(vertices, edges) {
  let count = 0;
  for (const [u, v] of edges) if (vertices.has(u) && vertices.has(v)) count++;
  return count;
}
const cases = [];
for (let a = 1; a <= 10; a++) {
  const base = build([10, a, 1, 1, 11 - a]);
  const G = base.groups;
  const tests = [
    new Set([...G[0], ...G[2], ...G[3]]),
    new Set([...G[1], ...G[4], ...G[2]]),
    new Set([...G[1], ...G[4], ...G[3]])
  ];
  cases.push({base, tests, deleted: null});
  for (let i = 0; i < 5; i++) cases.push({base, tests, deleted: i});
}
{
  const base = build([9, 9, 2, 1, 2]);
  const G = base.groups;
  const tests = [
    new Set([...G[0], ...G[2], ...G[3]]),
    new Set([...G[1], ...G[3], ...G[4]])
  ];
  cases.push({base, tests, deleted: null});
}
let validRepresentatives = 0;
let discardedAlpha12 = 0;
let maximalIndependentCount = 0;
let maximumMinCost = 0;
let costFailures = 0;
for (const {base, tests, deleted} of cases) {
  let edges = base.edges.slice();
  if (deleted !== null) {
    const u = base.groups[deleted][0];
    const v = base.groups[(deleted + 1) % 5][0];
    edges = edges.filter(([x, y]) => !((x === u && y === v) || (x === v && y === u)));
  }
  const maximal = maximalIndependentSets(base.n, edges);
  if (Math.max(...maximal.map(bitCount)) >= 12) { discardedAlpha12++; continue; }
  validRepresentatives++;
  for (const mask of maximal) {
    const I = new Set(Array.from({length: base.n}, (_, i) => i).filter(i => (mask >> BigInt(i)) & 1n));
    const minCost = Math.min(...tests.map(S => inducedEdges(S, edges) + [...S].filter(v => I.has(v)).length));
    if (minCost > 6) costFailures++;
    maximumMinCost = Math.max(maximumMinCost, minCost);
    maximalIndependentCount++;
  }
}

const B = (n, k) => 2*k + 1 + k*(n - 2*k - 1) + Math.floor((n - 2*k - 1)**2 / 4);
const D = n => {
  const q = Math.floor(n / 12), r = n % 12;
  const p = 12*q*(q - 1)/2 + q*r;
  return n*(n - 1)/2 - 11*p;
};
const result = {
  status: "PASS",
  type_quotient: {
    compatible_nonempty_type_set_pairs: pairs.length,
    side_size_patterns: [...new Set(pairs.map(([A, B]) => [Math.min(A.length, B.length), Math.max(A.length, B.length)].join("x")))],
    incompatible_missing_cross_edge_cases: missing.length,
    all_missing_cases_have_singleton_sides: missing.every(([A, B]) => A.length === 1 && B.length === 1)
  },
  m2b_singleton_extension: {
    positions_checked: extensionPositions,
    failures: extensionFailures
  },
  m3_neighborhood_costs: {
    family_representatives: cases.length,
    valid_alpha_at_most_11: validRepresentatives,
    discarded_alpha_at_least_12: discardedAlpha12,
    maximal_independent_sets_checked: maximalIndependentCount,
    maximum_minimum_cost: maximumMinCost,
    cost_failures: costFailures,
    forced_14_set_edges: 78 - maximumMinCost
  },
  arithmetic: {
    B23: Array.from({length: 10}, (_, i) => [i + 2, B(23, i + 2)]),
    B18: Array.from({length: 7}, (_, i) => [i + 2, B(18, i + 2)]),
    D14: D(14), D23: D(23), D24: D(24), D37: D(37), D38: D(38)
  },
  scope: "Independent finite recheck of the C5 type quotient, M2b extension positions, explicit M3 blow-up/deletion representatives and displayed integer bounds; not a formal proof of the analytic reductions."
};
if (pairs.length !== 20 || missing.length !== 10 || extensionPositions !== 55 || extensionFailures !== 0 ||
    cases.length !== 61 || validRepresentatives !== 49 || discardedAlpha12 !== 12 ||
    maximalIndependentCount !== 263 || maximumMinCost !== 6 || costFailures !== 0) {
  throw new Error("Independent lower-order replay mismatch: " + JSON.stringify(result));
}
console.log(JSON.stringify(result, null, 2));
